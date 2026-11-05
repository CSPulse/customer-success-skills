# Churn Postmortem

**A one-page postmortem that separates what the customer said from what actually caused the loss, and ends in one owned change.**

**What goes wrong without it:** "It was an acquisition" filed as the cause, hiding months of no contact. A postmortem that ends in a category changes nothing.

Part of [customer-success-skills](../../#readme).

## What it does

1. Quote the stated reason, date it, name who heard it, then set it aside
2. Build the timeline on the customer's calendar
3. Split signals into two columns
4. Write the mechanism as a causal chain
5. Test the stated reason against the mechanism
6. Name when it stopped being winnable
7. Check for a pattern

## What you get

The answer comes first, then the reasoning. Every output ends with a list of what the skill could not check, so a gap shows up as a gap.

See a filled example for an invented company in [examples/sample.md](examples/sample.md).

Say things like:

- "churn postmortem"
- "why did we lose them"
- "they did not renew"
- "post mortem on [account]"
- "what went wrong with [account]"
- "lessons learned from the loss"

## Who this is for

Written for CSMs, team leads and heads of customer success. Included in: `csm-toolkit`, `cs-team-lead-toolkit`, `cs-leader-toolkit`.

## What it needs

Nothing is required. Paste what you have and it works with that. These inputs help most:

1. Account, ARR lost, date the notice or non-renewal arrived
2. The reason the customer gave, who they gave it to, and when
3. What you remembers of the last six months: contacts, changes, silences

Anything you leave out is listed under "What I could not check" instead of blocking the skill. No connector, file or other skill is needed.

## Install just this skill

```
I want to install the churn-postmortem skill from
https://github.com/CSPulse/customer-success-skills. Download or clone
the repository, then copy the skills/churn-postmortem folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

To install a role bundle or the whole set, see the [install section](../../#pick-your-role) of the main README.

## Rules it follows

- A category is not a mechanism
- Hindsight is not detection
- Laundering is the common sin
- Do not blame the person who held the account
- Thirty losses with one mechanism is one product or pricing decision
- Not every loss earns a process change
- Unknown is a legitimate finding

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
