# churn postmortem

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of 32 AI skills for the work customer success actually does.**

Works out why an account actually left, separating the reason given from the mechanism. Keeps what was detectable at the time apart from what is only obvious in hindsight, and checks whether the loss was one of a correlated set.

Part of the **Read the account** group in this library.

## Who this is for

For CSMs and account managers who need an honest read on an account, whether it is one they have run for years or one they just inherited.

## What this needs

Works with nothing but what you remember. Gets better with the account history, the support record, the original business case.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the churn-postmortem skill from https://github.com/CSPulse/customer-success-skills/tree/main/skills/churn-postmortem, zip the churn-postmortem folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/churn-postmortem`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs all 32 skills at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
