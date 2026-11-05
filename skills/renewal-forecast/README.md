# Renewal Forecast

**A dollar forecast for a renewal period, as a range you can defend to finance: gross retention, net retention, contraction, and the one or two bets that move it.**

**What goes wrong without it:** A forecast counted in logos. It reports a healthy quarter while the dollars come in short because accounts renewed smaller.

Part of [customer-success-skills](../../#readme).

## What it does

1. Fix the pool
2. Split by how each renews
3. Categorize on evidence
4. Group at-risk by mechanism
5. Split every loss into churn and contraction
6. Compute
7. Say what moves it

## What you get

The answer comes first, then the reasoning. Every output ends with a list of what the skill could not check, so a gap shows up as a gap.

See a filled example for an invented company in [examples/sample.md](examples/sample.md).

Say things like:

- "renewal forecast"
- "forecast the quarter"
- "what will we renew"
- "commit number"
- "GRR forecast"
- "roll up my team's renewals"

## Who this is for

Written for team leads and heads of customer success. Included in: `cs-team-lead-toolkit`, `cs-leader-toolkit`.

## What it needs

Nothing is required. Paste what you have and it works with that. These inputs help most:

1. The list, one row per account: account, ARR, renewal date, auto-renew (y/n), notice date, category (commit, likely, at risk, unknown, lost), reason. Any subset works.
2. The period, and any expansion already signed or verbally expected.
3. Last period's forecast against what landed, if you has it.

Anything you leave out is listed under "What I could not check" instead of blocking the skill. No connector, file or other skill is needed.

## Install just this skill

```
I want to install the renewal-forecast skill from
https://github.com/CSPulse/customer-success-skills. Download or clone
the repository, then copy the skills/renewal-forecast folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

To install a role bundle or the whole set, see the [install section](../../#pick-your-role) of the main README.

## Rules it follows

- Contraction is a line, not a footnote
- Correlated risk is one bet
- Unknown is a category
- Silence is not Commit until the notice date passes
- Show GRR beside NRR, GRR first
- Slip is not loss
- Adjust forecasters out loud
- Defaults are placeholders

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
