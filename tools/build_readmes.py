#!/usr/bin/env python3
"""Builds skills/<name>/README.md from each skill's own SKILL.md.

    python3 tools/build_readmes.py          # write every README
    python3 tools/build_readmes.py --check  # exit 1 if any README is out of date

A README is a standalone landing page: someone who arrives on it from a shared
link should not need to open SKILL.md. It is generated, so it cannot disagree
with the skill. The one hand-written line per skill (why it exists) lives in
tools/readme_why.tsv. Standard library only.
"""
import json
import os
import re
import sys
import textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, 'skills')
MANIFEST = os.path.join(ROOT, '.claude-plugin', 'marketplace.json')
WHY = os.path.join(ROOT, 'tools', 'readme_why.tsv')
REPO = 'https://github.com/CSPulse/customer-success-skills'

ROLES = {
    'csm-toolkit': 'CSMs',
    'cs-team-lead-toolkit': 'team leads',
    'cs-leader-toolkit': 'heads of customer success',
}


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def section(text, heading):
    m = re.search(r'^## ' + re.escape(heading) + r'[^\n]*\n(.*?)(?=^## |\Z)', text, re.S | re.M)
    return m.group(1).strip('\n') if m else ''


def load_why():
    out = {}
    for line in read(WHY).splitlines():
        if '\t' in line:
            k, v = line.split('\t', 1)
            out[k.strip()] = v.strip()
    return out


def load_bundles():
    data = json.loads(read(MANIFEST))
    bundles = {}
    for plugin in data.get('plugins', []):
        if plugin['name'] in ROLES:
            for s in plugin.get('skills', []):
                bundles.setdefault(os.path.basename(s.rstrip('/')), []).append(plugin['name'])
    return bundles


def numbered(block):
    return [re.sub(r'^\d+\.\s+', '', l).strip() for l in block.splitlines() if re.match(r'^\d+\.\s', l)]


def lead(item):
    m = re.match(r'\*\*(.+?)\*\*', item)
    if m:
        return m.group(1).rstrip('.:')
    return re.split(r'(?<=[.!?])\s', item)[0].rstrip('.')


def bullets(block):
    return [l[2:].strip() for l in block.splitlines() if l.startswith('- ')]


def you(text):
    """SKILL.md talks about 'the user'; a landing page talks to the reader."""
    for a, b in (("the user's", 'your'), ("The user's", 'Your'), ('the user', 'you'), ('The user', 'You')):
        text = text.replace(a, b)
    return text


def wrap(text, width=72):
    return '\n'.join(textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False))


def render(name, why=None, bundles=None):
    why = why if why is not None else load_why()
    bundles = bundles if bundles is not None else load_bundles()
    text = read(os.path.join(SKILLS, name, 'SKILL.md'))
    title = re.search(r'^# (.+)$', text, re.M).group(1).strip()
    after_h1 = text.split('\n# ', 1)[1].split('\n', 1)[1]
    promise = you(next(l.strip() for l in after_h1.splitlines() if l.strip()))
    desc = re.search(r'description: >\n((?:  .*\n)+)', text).group(1)
    phrases = re.findall(r'"([^"]{3,80})"', ' '.join(desc.split()))
    start = section(text, 'Start here')
    inputs = [you(s) for s in numbered(start)]
    steps = [lead(s) for s in numbered(section(text, 'Do this'))]
    rules = [lead(r) for r in bullets(section(text, 'Rules'))]
    roles = [ROLES[b] for b in ROLES if b in bundles.get(name, [])]
    in_bundles = [b for b in ROLES if b in bundles.get(name, [])]

    o = [f'# {title}', '', f'**{promise}**', '']
    o += ['**What goes wrong without it:** ' + why.get(name, ''), '']
    o += ['Part of [customer-success-skills](../../#readme).', '']
    o += ['## What it does', '']
    if steps:
        o += [f'{i}. {s}' for i, s in enumerate(steps, 1)]
    else:
        o += ['It answers in one pass and tells you what it could not check.']
    o += ['', '## What you get', '']
    o += ['The answer comes first, then the reasoning. Every output ends with a list of what the skill could not check, so a gap shows up as a gap.', '']
    o += ['See a filled example for an invented company in [examples/sample.md](examples/sample.md).', '']
    if phrases:
        o += ['Say things like:', '']
        o += [f'- "{p}"' for p in phrases]
        o += ['']
    o += ['## Who this is for', '']
    if roles:
        o += [f'Written for {", ".join(roles[:-1]) + (" and " if len(roles) > 1 else "") + roles[-1]}. Included in: ' + ', '.join(f'`{b}`' for b in in_bundles) + '.', '']
    else:
        o += ['Anyone doing customer success work.', '']
    o += ['## What it needs', '']
    o += ['Nothing is required. Paste what you have and it works with that. These inputs help most:', '']
    if inputs:
        o += [f'{i}. {s}' for i, s in enumerate(inputs, 1)]
    else:
        o += ['- Whatever you know about the situation']
    o += ['', 'Anything you leave out is listed under "What I could not check" instead of blocking the skill. No connector, file or other skill is needed.', '']
    o += ['## Install just this skill', '']
    prompt = (f'I want to install the {name} skill from {REPO}. '
              f'Download or clone the repository, then copy the skills/{name} '
              'folder into ~/.claude/skills/ (or .claude/skills/ if this is for '
              'one project only), keeping its own folder name. Tell me the exact '
              'folder path it landed in when you are done.')
    o += ['```', wrap(prompt), '```', '']
    o += ['To install a role bundle or the whole set, see the [install section](../../#pick-your-role) of the main README.', '']
    if rules:
        o += ['## Rules it follows', '']
        o += [f'- {r}' for r in rules]
        o += ['']
    o += ['---', '', f'MIT licensed. Part of [customer-success-skills]({REPO}).', '']
    return '\n'.join(o)


def main():
    why, bundles = load_why(), load_bundles()
    names = sorted(d for d in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, d)))
    stale = []
    for n in names:
        path = os.path.join(SKILLS, n, 'README.md')
        new = render(n, why, bundles)
        if '--check' in sys.argv:
            if not os.path.exists(path) or read(path) != new:
                stale.append(n)
        else:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new)
    if '--check' in sys.argv:
        for n in stale:
            print(f'README out of date or missing: skills/{n}/README.md')
        return 1 if stale else 0
    print(f'wrote {len(names)} READMEs')
    return 0


if __name__ == '__main__':
    sys.exit(main())
