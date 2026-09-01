# email critic

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of 32 AI skills for the work customer success actually does.**

Stress-tests a drafted customer email against the transcript and account context, then returns a verdict and a tightened version. Checks facts before prose, because that is where the damage is.

Part of the **Write to the customer** group in this library.

## Who this is for

For anyone drafting something a customer, or a customer's boss, is actually going to read.

## What this needs

Works with nothing but the draft itself. Gets better with the transcript, the thread, a voice guide.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the email-critic skill from https://github.com/CSPulse/customer-success-skills/tree/main/skills/email-critic, zip the email-critic folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/email-critic`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs all 32 skills at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
