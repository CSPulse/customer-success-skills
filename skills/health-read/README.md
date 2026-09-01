# health read

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Audits a health score instead of reporting it. Most scores were set once, in a room, by intuition, and never back-tested against the accounts that actually left - which is how "the score was green" ends up offered as an explanation for a churn, when a green score at the moment of churn is the thing that actually needs explaining.

It sorts every input into measured, proxy, or absent: logins counted are evidence, login frequency standing in for value received is an untested hypothesis, and whether the champion still has budget authority is usually absent from the score entirely and usually decides the renewal anyway. It breaks the composite back apart - module by module, team by team, admin activity against end-user activity - because a growing product line averaged against a dying one produces a healthy-looking middle, and an account carried by one power user is one resignation from zero. Then it asks the question almost nobody runs: of the accounts that churned last year, what did their scores say three months out, and has the score ever been changed as a result of the answer.

Part of the **Read the account** group in this library.

## Who this is for

For CSMs and account managers who need an honest read on an account, whether it is one they have run for years or one they just inherited.

## What this needs

Works with nothing but the score and roughly what goes into it. Gets better with the input values, the trend, and what churned accounts scored.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the health-read skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/health-read,
zip the health-read folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/health-read`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
