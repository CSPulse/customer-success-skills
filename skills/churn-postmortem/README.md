# churn postmortem

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Works out why an account actually left, separating the reason the customer gave - polite, partly true, and almost never the mechanism - from the causal chain that produced it, and checks whether the loss was one of a correlated set rather than a one-off.

It marks two dates that get conflated: when the account was actually lost (a budget cycle, a sponsor's departure, a competitor selected) and when anyone on your side noticed. The gap between them is the finding, not the stated reason - a three-week gap is a save attempted late, a seven-month gap is a detection problem no amount of better save-playing fixes. It keeps what was genuinely detectable at the time in a column separate from what only looks obvious in hindsight, because only the first produces a change worth making: "the sponsor stopped replying in March" counts, "the tone of the February email" does not. The failure this exists to prevent: **"it was an acquisition" filed as a cause, concealing nine months of nobody calling** - a postmortem that produces a category instead of a mechanism changes nothing.

Part of the **Read the account** group in this library.

## Who this is for

For CSMs and account managers who need an honest read on an account, whether it is one they have run for years or one they just inherited.

## What this needs

Works with nothing but what you remember. Gets better with the account history, the support record, the original business case.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the churn-postmortem skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/churn-postmortem,
zip the churn-postmortem folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/churn-postmortem`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
