# Voice Of Customer

**Paste what customers said across accounts. Get the monthly product report: themes ranked by accounts and ARR, the need under each request, the customers' own words, and the loop to close.**

**What goes wrong without it:** Letting the loudest account become the theme. One customer's request gets reported as what customers want.

Part of [customer-success-skills](../../#readme).

## What it does

1. Extract items
2. Classify each item
3. Group into themes
4. Count accounts, then ARR
5. Write the need
6. Flag who matters beyond ARR
7. Close the loop

## What you get

The answer comes first, then the reasoning. Every output ends with a list of what the skill could not check, so a gap shows up as a gap.

See a filled example for an invented company in [examples/sample.md](examples/sample.md).

Say things like:

- "voice of the customer"
- "VoC report"
- "what are customers asking for"
- "themes across my accounts"
- "product feedback report"
- "what are customers saying about the product"

## Who this is for

Written for CSMs, team leads and heads of customer success. Included in: `csm-toolkit`, `cs-team-lead-toolkit`, `cs-leader-toolkit`.

## What it needs

Nothing is required. Paste what you have and it works with that. These inputs help most:

1. The raw material, with the account name on each piece (call notes, thread excerpts, tickets)
2. ARR per account (rough is fine) and which accounts are strategic, a reference, or renewing soon
3. The period, and who reads the report (product, leadership)

Anything you leave out is listed under "What I could not check" instead of blocking the skill. No connector, file or other skill is needed.

## Install just this skill

```
I want to install the voice-of-customer skill from
https://github.com/CSPulse/customer-success-skills. Download or clone
the repository, then copy the skills/voice-of-customer folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

To install a role bundle or the whole set, see the [install section](../../#pick-your-role) of the main README.

## Rules it follows

- Count accounts, not mentions
- Show ARR next to the count, never instead of it
- Separate bug, gap and misunderstanding
- The request is rarely the need
- Keep the customer's own words
- Say which sources were read and which were not
- Close the loop, including on a no
- A fix that serves one account is a favor, not a theme

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
