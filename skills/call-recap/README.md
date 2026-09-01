# call recap

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Turns a recorded customer call into an honest read of it, plus the full set of emails it generated - grouped by recipient, written in the user's voice, staged as drafts. A call is not one email; it is a set of them, sitting with different people, blocked on each other in a specific order, and the ones the user forgets to write are usually the ones that would have moved the account.

It pulls the complete transcript rather than the AI summary, because a summary keeps the category - "filtering for quality" - and drops the sentence the customer actually used to describe the problem, which is the sentence that should shape the draft. Every claim that reaches a draft is grounded to a source before it is allowed in: what was said or agreed comes from the transcript, what is already true about the account comes from the mailbox and account plan and never from the call itself (people compress and misremember out loud), and anything about what the product does, collects or costs gets flagged for a human rather than asserted. The failure this exists to prevent: **writing a tidy recap to the coordinator, feeling done, and leaving the three emails that actually move the account unwritten.**

Part of the **Handle the conversation** group in this library.

## Who this is for

For anyone who has just come off a customer call and needs the follow-through captured before it evaporates - not just a recap to the coordinator, but the full set of emails the call actually generated.

## What this needs

Works with nothing but a pasted transcript. Gets better with a meeting recorder, a mailbox, account notes.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the call-recap skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/call-recap,
zip the call-recap folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/call-recap`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
