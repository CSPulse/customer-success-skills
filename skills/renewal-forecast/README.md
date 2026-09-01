# renewal forecast

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Produces a renewal and expansion forecast that is a commitment with a stated confidence, not a sum of thirty separate opinions. The two most common ways a forecast goes wrong are structural rather than analytical: contraction never gets counted, and correlated risks get added up as though they were independent.

It reports three numbers instead of one - gross renewal dollars, contraction sized on its own line, and expansion kept separate so a good expansion quarter can't conceal a bad retention one - because most accounts labelled "at risk" aren't at risk of leaving, they're at risk of renewing 30% smaller, and a binary renew-or-not model can't represent that at all. Every category (commit, likely, at risk, lost, and a mandatory unknown) gets a written entry criterion made of evidence rather than a feeling, because without a permitted "unknown" category, unknowns get filed as likely by default. It pulls auto-renewing accounts out of the judgment pool so a passed notice window doesn't inflate apparent accuracy, and it separates a renewal that slipped a quarter from one that was actually lost, since the plays for each are opposite. The step most forecasts skip entirely: grouping the at-risk book by mechanism rather than by account, so thirty accounts flagged for the same price change or the same segment under pressure get forecast as the one correlated bet they actually are, instead of thirty independent coin flips that understate the real variance. It also tracks forecast-versus-actual per forecaster over time, to catch the sandbagger (an at-risk book that quietly renews at 95%) and the happy-ears (everything likely, evidence verbal and single-sourced) before their personalities become the number.

The failure this exists to prevent: **the logo forecast.** Ninety-four per cent of accounts renewing, reported as a healthy quarter, while the dollars come in eleven per cent light because a third of them renewed smaller.

Part of the **Lead the function** group in this library.

## Who this is for

For CS leaders and managers running the function itself, not a single account.

## What this needs

Works with nothing but the accounts up for renewal, their values and dates. Gets better with a risk read per account, and last quarter's forecast against actual.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the renewal-forecast skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/renewal-forecast,
zip the renewal-forecast folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/renewal-forecast`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
