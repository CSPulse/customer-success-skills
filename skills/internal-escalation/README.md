# internal escalation

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Gets your own company to act on an account, on the customer's behalf, addressed to people who did not choose that account and are measured on something else. The failure it exists to prevent is "can someone please look at this" - a message that names no decision, no deadline and no owner, so it sinks to the bottom of a queue sorted by things it does not have.

It starts by forcing a choice most escalations skip: are you asking for a decision, work, presence, or just cover - because those four go to different people, and most failed escalations are a request for work sent to someone who can only give a decision. It finds who actually holds that authority rather than who is senior, shapes the same situation differently for engineering, leadership and sales because each needs a different fact set, and compresses the ask into one sentence - "I need [named person] to [specific action] by [date], because [what happens otherwise]" - with what you already tried attached, since that is the first question you'll be asked. It refuses to inflate severity, because the credibility cost is permanent and your colleagues pay it on their next escalation, and it insists you go one rung at a time and tell people before you go over their heads, because skipping levels gets a fast answer once and a lasting reputation.

Part of the **Work it internally** group in this library.

## Who this is for

For CSMs who need their own company to act, not just the customer.

## What this needs

Works with nothing but what you need and by when. Gets better with the contract value, what you have already tried, your company's escalation process.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the internal-escalation skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/internal-escalation,
zip the internal-escalation folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/internal-escalation`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
