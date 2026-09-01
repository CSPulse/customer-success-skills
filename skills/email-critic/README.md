# email critic

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Takes a drafted customer email and tells the user whether to send it - not whether it reads well, but whether an exceptional customer-facing operator would send this to this customer, at this point in the relationship, and get back what they need. It checks the draft against the source it came from - the call transcript, the thread being replied into, account notes, a voice guide - rather than judging it in a vacuum. Most feedback on an email is polish. The check that finds real damage is accuracy: whether the draft quietly upgrades "let's look at that" into "as agreed," claims something was sent that never was, or drops a concern the customer raised without anyone noticing.

The failure this exists to prevent: **grading the prose while the facts drift.** A clean, well-organized email that misstates what was agreed does more damage than a clumsy one that gets it right, and a review that only checks tone would wave it straight through. It also refuses to manufacture criticism to look rigorous - a genuinely good draft gets "send it" in one sentence - and it never issues a numeric score, because a number invented by the same model about to do the rewrite stops reporting the problem and starts driving the edit.

Part of the **Write to the customer** group in this library.

## Who this is for

For anyone drafting something a customer, or a customer's boss, is actually going to read.

## What this needs

Works with nothing but the draft itself. Gets better with the transcript, the thread, a voice guide.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the email-critic skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/email-critic,
zip the email-critic folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/email-critic`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
