#!/usr/bin/env python3
"""
Structural checks for every skill in this repository.

Run it before opening a pull request:

    python3 validate-skills.py

It exits non-zero and prints one line per problem. Continuous integration runs
the same script on every pull request, so anything it catches here is anything
that would fail there.

Every check exists because the defect it catches shipped once. Em dashes were
live across four public repositories for four days. A skill description shipped
at 1,096 characters, over the limit, with its trigger phrases sitting in the
part assistants truncate. A heading kept an old name after every other
reference had been renamed.

This checks structure, not judgement. It cannot tell you whether a skill is
worth installing. See CONTRIBUTING.md for the part that needs a person.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SKILLS_DIR = os.path.join(ROOT, 'skills')
MANIFEST = os.path.join(ROOT, '.claude-plugin', 'marketplace.json')
README = os.path.join(ROOT, 'README.md')

LINE_LIMIT = 500
DESC_LIMIT = 1024

PUNCT = {
    '—': 'em dash',
    '–': 'en dash',
    '‘': 'curly quote',
    '’': 'curly apostrophe',
    '“': 'curly quote',
    '”': 'curly quote',
}
OPENAI = re.compile(r'Open\s*AI')


def rel(path):
    return os.path.relpath(path, ROOT)


def check_punctuation(path, text, bad):
    for ch, name in PUNCT.items():
        n = text.count(ch)
        if n:
            bad.append(f'{rel(path)}: {n} {name}{"s" if n > 1 else ""}')
    if OPENAI.search(text):
        bad.append(f'{rel(path)}: "Open" immediately before "AI"')


def check_skill(path, text, bad):
    folder = os.path.basename(os.path.dirname(path))

    lines = text.splitlines()
    if len(lines) > LINE_LIMIT:
        bad.append(f'{rel(path)}: {len(lines)} lines, limit {LINE_LIMIT}')

    m = re.search(r'^name:[ \t]*(.+?)[ \t]*$', text, re.M)
    if not m:
        bad.append(f'{rel(path)}: no name in frontmatter')
    elif m.group(1) != folder:
        bad.append(f'{rel(path)}: frontmatter name "{m.group(1)}" but folder "{folder}"')

    d = re.search(r'^description:[ \t]*>[ \t]*\n(.*?)\n---', text, re.S | re.M)
    if not d:
        bad.append(f'{rel(path)}: no block description in frontmatter')
    else:
        n = len(' '.join(d.group(1).split()))
        if n > DESC_LIMIT:
            bad.append(f'{rel(path)}: description {n} characters, limit {DESC_LIMIT}')

    h1 = re.search(r'^# (.+)$', text, re.M)
    if h1:
        expected = folder.replace('-', ' ')
        if h1.group(1).strip().lower() != expected.lower():
            bad.append(f'{rel(path)}: H1 "{h1.group(1).strip()}" does not match folder "{folder}"')


def check_reference_depth(skill_dir, bad):
    """References are one level deep. A reference pointing at another reference
    gets partially read, which is worse than not shipping it."""
    for sub in ('references', 'assets'):
        base = os.path.join(skill_dir, sub)
        if not os.path.isdir(base):
            continue
        for entry in os.listdir(base):
            if os.path.isdir(os.path.join(base, entry)):
                bad.append(f'{rel(os.path.join(base, entry))}: nested directory, keep {sub}/ one level deep')


def check_manifest(bad):
    if not (os.path.exists(MANIFEST) and os.path.isdir(SKILLS_DIR)):
        bad.append('no marketplace.json or no skills directory')
        return
    try:
        data = json.load(open(MANIFEST, encoding='utf-8'))
    except Exception as exc:
        bad.append(f'marketplace.json: unreadable, {exc}')
        return

    listed = {p.rstrip('/').split('/')[-1]
              for plugin in data.get('plugins', [])
              for p in plugin.get('skills', [])}
    on_disk = {d for d in os.listdir(SKILLS_DIR)
               if os.path.exists(os.path.join(SKILLS_DIR, d, 'SKILL.md'))}

    for name in sorted(on_disk - listed):
        bad.append(f'marketplace.json: "{name}" on disk but not listed in a plugin skills array')
    for name in sorted(listed - on_disk):
        bad.append(f'marketplace.json: "{name}" listed but not on disk')

    if os.path.exists(README):
        text = open(README, encoding='utf-8').read()
        linked = set(re.findall(r'\]\(skills/([a-z0-9-]+)\)', text))
        missing = on_disk - linked
        if missing:
            bad.append('README.md: skills table missing ' + ', '.join(sorted(missing)))


def main():
    bad = []

    if not os.path.isdir(SKILLS_DIR):
        print('no skills/ directory found')
        return 1

    for dirpath, _dirnames, filenames in os.walk(ROOT):
        if os.sep + '.git' in dirpath:
            continue
        # A template deliberately carries placeholder values in the places this
        # script checks for real ones, so checking it reports failures that are
        # the file doing its job.
        if os.path.basename(dirpath) == 'template' or os.sep + 'template' + os.sep in dirpath:
            continue
        for name in filenames:
            if not name.endswith('.md'):
                continue
            path = os.path.join(dirpath, name)
            text = open(path, encoding='utf-8').read()
            check_punctuation(path, text, bad)
            if name == 'SKILL.md':
                check_skill(path, text, bad)
                check_reference_depth(os.path.dirname(path), bad)

    check_manifest(bad)

    if bad:
        print(f'{len(bad)} problem{"s" if len(bad) > 1 else ""}:\n')
        for line in sorted(bad):
            print('  ' + line)
        print('\nRules are in CONTRIBUTING.md.')
        return 1

    skills = sorted(d for d in os.listdir(SKILLS_DIR)
                    if os.path.exists(os.path.join(SKILLS_DIR, d, 'SKILL.md')))
    print(f'{len(skills)} skill{"s" if len(skills) != 1 else ""} checked, all clear: ' + ', '.join(skills))
    return 0


if __name__ == '__main__':
    sys.exit(main())
