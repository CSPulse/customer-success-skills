# escalation

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Runs the first four hours of an account on fire: what to say before you know the answer, who to pull in, and what the customer actually wants, which is often not the fix itself. It opens with the question that separates three situations that need three different responses: "what specifically has to be true for this to be resolved?" A crisp technical answer means something broke and needs fixing. A vague answer, or a list, means accumulated frustration found a trigger - a relationship escalation a fix won't touch. An answer about terms means the real destination is a negotiation. It then sets one named owner, one channel, and a holding cadence that runs even when there's nothing new to report, because "no change, next update at four" beats silence every time.

The failure this exists to prevent: **going quiet until you have the answer.** The silence gets read as chaos or concealment, and both are worse than an honest update with nothing in it. It also catches the step most teams skip once the pressure comes off: asking what the incident actually cost the customer, planning a deliberate repair rather than a gesture, and treating a suddenly cooperative, quiet account after resolution as a possible sign the decision is already being made elsewhere - not as relief.

Part of the **Run the set-piece** group in this library.

## Who this is for

For CSMs managing an account that has just moved above its usual temperature - one of the big, mostly one-shot moments with no redo if it goes wrong.

## What this needs

Works with nothing but what happened and who is angry. Gets better with the incident record, the contract, a stakeholder map.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the escalation skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/escalation,
zip the escalation folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/escalation`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
