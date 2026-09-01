# account context

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Runs once, interviewing the team for the handful of facts every other skill in this library needs before it can say anything useful: what the product actually does in the customer's own words, how segments really differ (not where they merely sound different), what the contract shapes mean for renewal, and - the highest-yield question, deliberately asked three separate ways because the first two tend to surface internal proxies instead - the number the customer actually bought. If nobody can answer that, the skill records the emptiness as a finding rather than skipping past it, because no-agreed-value-metric is the quiet mechanism behind most healthy-usage-still-churned accounts.

The failure this exists to prevent: **a renewal risk read that says "usage is down, this may indicate risk" with no idea that in this business, low usage is what a healthy compliance or audit deployment looks like.** Every gap it can't fill gets marked `NOT ESTABLISHED` rather than guessed at or left blank, so the finished document tells the next skill - or the next person - where to go looking instead of quietly pretending to be complete.

## Who this is for

For anyone setting up the library for their team. This runs once, and every other skill reads it instead of asking you again.

## What this needs

Works with nothing but five minutes and what you already know. Gets better with the pricing page, a sample contract, an original business case.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the account-context skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/account-context,
zip the account-context folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/account-context`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
