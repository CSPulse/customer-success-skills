# nrr narrative

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Turns a net revenue retention number into a board narrative that survives more than one question. One hundred and ten per cent built on a price increase, one hundred and ten built on organic seat growth, and one hundred and ten built on two huge expansions covering broad contraction are three different companies with the same slide - and the failure this exists to prevent is presenting the headline with no composition, which is the one thing a board member who has seen this before will always ask about first.

It decomposes the ratio into expansion, price, contraction and churn, and treats merging price with expansion as the single most damaging shortcut available - one is evidence customers want more, the other is evidence you charged more, and a board that finds out later that they were blended stops trusting every number after it. It insists gross retention sits next to net, because gross is the number that cannot be rescued by a handful of large expansions and net can hide a deteriorating base behind them for years. It states plainly whether the number is cohort or blended, since blended retention flatters a company in direct proportion to how fast it is growing new business, for reasons that have nothing to do with retention. And it forces the concentration question before anyone else asks it - how many accounts drove the expansion, and where exactly the churn clusters - because a number produced by three renewals is not a business property, however it is described on the slide.

Part of the **Lead the function** group in this library.

## Who this is for

For CS leaders and managers running the function itself, not a single account.

## What this needs

Works with nothing but the retention numbers and the period. Gets better with the movement split four ways, and cohort or segment data.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the nrr-narrative skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/nrr-narrative,
zip the nrr-narrative folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/nrr-narrative`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
