#!/usr/bin/env python3
"""Checks every skill against template/SPEC.md. Run before opening a pull request:

    python3 tools/check.py

Exits non-zero and prints one line per problem. Standard library only.
Checks structure and obvious defects. It cannot tell you whether a skill is good;
the filled example in examples/sample.md is the test a human applies.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, 'skills')
MANIFEST = os.path.join(ROOT, '.claude-plugin', 'marketplace.json')
README = os.path.join(ROOT, 'README.md')

MAX_LINES = 150
MAX_BYTES = 7500
MAX_DESC = 600
MAX_SAMPLE_LINES = 90

BANNED = {
    '\u2014': 'em dash', '\u2013': 'en dash', '\u2018': 'curly quote',
    '\u2019': 'curly apostrophe', '\u201c': 'curly quote', '\u201d': 'curly quote',
}
# Things that make a skill depend on its author's setup.
PREREQ = ['CLAUDE.md', 'AskUserQuestion', 'voice guide', 'style guide', 'accounts directory',
          'accounts-directory', 'workspace rule', 'Run `account-context` first',
          'Run `book-triage` first']
REQUIRED_HEADINGS = ['## Start here', '## Do this', '## Rules']
EXEMPT_HEADINGS = {'cs-start': ['## Do this']}

problems, warnings = [], []


def rel(p):
    return os.path.relpath(p, ROOT)


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def frontmatter(text):
    m = re.match(r'---\n(.*?)\n---\n', text, re.S)
    if not m:
        return None, None
    block = m.group(1)
    name = re.search(r'^name:[ \t]*(\S+)[ \t]*$', block, re.M)
    d = re.search(r'^description:[ \t]*>[ \t]*\n((?:[ \t]+.*\n?)+)', block + '\n', re.M)
    desc = ' '.join(d.group(1).split()) if d else None
    return (name.group(1) if name else None), desc


def check_text_files():
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in ('.git', 'node_modules')]
        for f in files:
            if not f.endswith(('.md', '.json', '.py', '.yml', '.tsv')):
                continue
            p = os.path.join(base, f)
            text = read(p)
            for ch, nm in BANNED.items():
                n = text.count(ch)
                if n:
                    problems.append(f'{rel(p)}: {n} {nm}(s)')
            if re.search(r'Open\s*AI', text):
                problems.append(f'{rel(p)}: "Open" directly before "AI"')


def main():
    folders = sorted(d for d in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, d)))
    phrases = {}
    for folder in folders:
        sd = os.path.join(SKILLS, folder)
        sp = os.path.join(sd, 'SKILL.md')
        if not os.path.exists(sp):
            problems.append(f'skills/{folder}: no SKILL.md')
            continue
        text = read(sp)
        lines = text.count('\n') + 1
        size = len(text.encode('utf-8'))
        if lines > MAX_LINES:
            problems.append(f'{rel(sp)}: {lines} lines, limit {MAX_LINES}')
        if size > MAX_BYTES:
            problems.append(f'{rel(sp)}: {size} bytes, limit {MAX_BYTES}')
        name, desc = frontmatter(text)
        if name != folder:
            problems.append(f'{rel(sp)}: frontmatter name "{name}" != folder "{folder}"')
        if not desc:
            problems.append(f'{rel(sp)}: no block description')
        else:
            if len(desc) > MAX_DESC:
                problems.append(f'{rel(sp)}: description {len(desc)} chars, limit {MAX_DESC}')
            if not desc.startswith('Use when'):
                problems.append(f'{rel(sp)}: description must start with "Use when"')
            if 'Not for' not in desc and folder != 'cs-start':
                warnings.append(f'{rel(sp)}: description has no "Not for ... (use x)" pointer')
            for ph in re.findall(r'"([^"]{3,60})"', desc):
                phrases.setdefault(ph.lower().strip(), []).append(folder)
        h1 = re.search(r'^# (.+)$', text, re.M)
        if not h1 or h1.group(1).strip().lower() != folder.replace('-', ' '):
            problems.append(f'{rel(sp)}: H1 should be "{folder.replace("-", " ").title()}"')
        for h in REQUIRED_HEADINGS:
            if h in EXEMPT_HEADINGS.get(folder, []):
                continue
            if h not in text:
                problems.append(f'{rel(sp)}: missing section "{h}"')
        if '## Output' not in text and folder != 'cs-start':
            problems.append(f'{rel(sp)}: missing section "## Output"')
        for needle in PREREQ:
            if needle in text:
                problems.append(f'{rel(sp)}: depends on author setup: "{needle}"')
        if re.search(r'\b\d+(\.\d+)?\s?(%|per cent|percent)', text):
            warnings.append(f'{rel(sp)}: contains a percentage; is it sourced or labeled a default?')
        sample = os.path.join(sd, 'examples', 'sample.md')
        if not os.path.exists(sample):
            problems.append(f'skills/{folder}: missing examples/sample.md')
        else:
            n = read(sample).count('\n') + 1
            if n > MAX_SAMPLE_LINES:
                warnings.append(f'{rel(sample)}: {n} lines; keep samples short')
            if 'nvented' not in read(sample) and 'fictional' not in read(sample):
                problems.append(f'{rel(sample)}: must say the company is invented')
        if os.path.exists(os.path.join(sd, 'README.md')):
            problems.append(f'skills/{folder}: remove per-skill README.md (root README is the catalog)')
        for sub in ('references', 'assets', 'examples'):
            b = os.path.join(sd, sub)
            if os.path.isdir(b):
                for e in os.listdir(b):
                    if os.path.isdir(os.path.join(b, e)):
                        problems.append(f'{rel(os.path.join(b, e))}: nested directory')

    for ph, owners in phrases.items():
        if len(set(owners)) > 1:
            problems.append(f'trigger phrase "{ph}" claimed by: {", ".join(sorted(set(owners)))}')

    # manifest
    try:
        data = json.loads(read(MANIFEST))
    except Exception as e:  # noqa: BLE001
        problems.append(f'marketplace.json unreadable: {e}')
        data = {'plugins': []}
    listed_any = set()
    for plugin in data.get('plugins', []):
        for s in plugin.get('skills', []):
            fn = os.path.basename(s.rstrip('/'))
            listed_any.add(fn)
            if fn not in folders:
                problems.append(f'plugin {plugin.get("name")}: lists missing skill "{fn}"')
    for fo in folders:
        if fo not in listed_any:
            problems.append(f'skill "{fo}" is in no plugin')

    # readme
    if os.path.exists(README):
        rd = read(README)
        for fo in folders:
            if f'`{fo}`' not in rd:
                problems.append(f'README.md does not mention `{fo}`')

    check_text_files()

    for w in warnings:
        print('warn:', w)
    for p in problems:
        print('FAIL:', p)
    print(f'{len(folders)} skills, {len(problems)} problems, {len(warnings)} warnings')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
