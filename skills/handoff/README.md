# handoff

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Runs a handover so the receiving side can actually take the account, not just receive it. It forces out four questions that never make it into a CRM record: what was promised that isn't in the contract, who the account's unnamed sceptic is, what nearly went wrong and what fixed it, and what the departing owner would do first if they were staying. It also flips who gets to declare the handover complete - the receiver signs off, not the sender, because the person leaving has every incentive to believe the person arriving is ready.

The failure this exists to prevent: **the account that arrives as a folder** - documents, a CRM record, a shared-drive link, and none of the four things that actually matter, all of which lived in one person's head and left with them. It insists on thirty minutes of live conversation over any document, puts a hard date on the handover so it can't drift to the sender's last day, and ends with one specific first action for the receiver's first week - proof the sender actually thought about the account instead of just emptying their notes into a document.

Part of the **Work it internally** group in this library.

## Who this is for

For CSMs who need their own company to act, not just the customer.

## What this needs

Works with nothing but the account and both names. Gets better with the account history, open commitments, thirty minutes of live overlap.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the handoff skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/handoff,
zip the handoff folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/handoff`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
