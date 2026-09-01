# portfolio review

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Reviews your team's reads, not their accounts - the two meetings look identical for the first ten minutes and then diverge completely. Reviewing accounts means solving problems one at a time until the hour is gone and four accounts got discussed. Reviewing reads means finding out which of the thirty assessments in front of you aren't supported by evidence, which is the only version that scales and the only one that improves a forecast.

It samples rather than covers: the exceptions everyone already knows about, a random five nobody chose (the group that gets dropped for time and the only one that catches systematic bias), and the quietest accounts in the book, since low last-contact dates correlate with risk and with green ratings at the same time. Every account gets the same four questions, asked in order - what's the mechanism, not the category; who decides and when did you last speak to them; which of this is what someone said versus your own inference; and what would make you wrong - which moves from the account to the evidence to the person's own reasoning. Along the way it names the tells: sandbagging (risk flagged late, with no play attached, that never changes state - the signature is an at-risk book that renews at 95%) and happy ears (everything green, evidence verbal and single-sourced, no sceptic named anywhere). It also looks across the whole book for the one thing only a manager can see - five accounts citing the same product gap or the same segment under pressure aren't five accounts, they're one problem that needs an owner.

The failure this exists to prevent: **the review that becomes a working session on the first account raised.** Everyone leaves feeling it was useful, and twenty-six reads went unexamined.

Part of the **Lead the function** group in this library.

## Who this is for

For CS leaders and managers running the function itself, not a single account.

## What this needs

Works with nothing but your team's current reads. Gets better with last contact dates, and forecast-versus-actual history per person.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the portfolio-review skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/portfolio-review,
zip the portfolio-review folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/portfolio-review`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
