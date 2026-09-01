# coverage model

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Designs who gets a named CSM, who gets pooled, who gets digital-only, and states plainly what breaks at each line. Segments by what accounts actually need - value, complexity, potential - rather than revenue alone, because a small account with high complexity routinely costs more to serve than a large simple one and gets tiered as if it costs nothing.

It treats the CSM ratio as an output of cost-to-serve rather than an input you divide accounts by, and it will not let "digital" or "pooled" stand as a tier name unless the instrumentation, content, triggers and route back to a human that make the tier actually work are named and real - otherwise it calls the tier unserved and says so plainly. The last step tests the finished model against the accounts that actually churned in the last two years: if most of the real losses would have sat in a tier with no relationship signal, the model does not work no matter how clean the tiers look on a slide. The failure this exists to prevent: **the model designed backwards from headcount** - divide the number of CSMs by the number of accounts, call the result a ratio, and describe whatever it produces as a strategy.

Part of the **Lead the function** group in this library.

## Who this is for

For CS leaders and managers running the function itself, not a single account.

## What this needs

Works with nothing but the account list with values, and your headcount. Gets better with churn history by segment, usage data, support load per account.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the coverage-model skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/coverage-model,
zip the coverage-model folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/coverage-model`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
