# health read

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of 32 AI skills for the work customer success actually does.**

Audits an account health score instead of reporting it. Separates what is measured from what is inferred, finds the inputs that are proxies, and asks whether the score has ever been tested against accounts that actually left.

Part of the **Read the account** group in this library.

## Who this is for

For CSMs and account managers who need an honest read on an account, whether it is one they have run for years or one they just inherited.

## What this needs

Works with nothing but the score and roughly what goes into it. Gets better with the input values, the trend, and what churned accounts scored.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the health-read skill from https://github.com/CSPulse/customer-success-skills/tree/main/skills/health-read, zip the health-read folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/health-read`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs all 32 skills at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
