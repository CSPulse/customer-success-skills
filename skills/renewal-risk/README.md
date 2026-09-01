# renewal risk

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Produces a defensible read on whether an account will renew - the decision, the decider, the mechanism, the evidence, the dollars at stake and the play - rather than a colour on a dashboard. It's built on one distinction most risk reads get wrong: usage tells you about the user, but the renewal is decided by the buyer, and in enterprise those two populations barely overlap.

It sets the clock to the customer's calendar rather than the CSM's - their budget planning cycle, their notice date, their fiscal year end - because a renewal date ninety days out can sit on either side of a budget lock that already happened. Before any signal analysis it forces a plain answer to who makes the decision and whether you've ever spoken to them; if the decider can't be named, that's the risk, and it outranks everything else on the account. Signals are then read in five tiers of decision-weight, where a Tier 1 signal (an unmet economic buyer, a single-threaded relationship, no agreed value metric) beats any amount of Tier 2 comfort (usage level, which is nearly worthless - trajectory, breadth against depth, and failure rate carry the actual signal), followed by procurement tells that read as helpfulness but are actually negotiation prep already underway (utilisation data requests, a mid-term security re-review, a request to shorten the term), support and sentiment patterns, and organizational change. Every signal then gets normalized against segment, pricing model, motion and industry, because the same signal means opposite things in an enterprise committee-driven renewal versus a usage-led PLG account. The output is a causal mechanism, not a category - "usage is down 40%" is an observation; "the team driving 70% of usage was cut, the incoming VP has a stated consolidation mandate and hasn't met us" tells you who to call - and it argues against itself before concluding, naming what evidence would prove the read wrong and forecasting dollars (full renewal, likely contraction and its size, downside) instead of a binary logo flag.

The failure this exists to prevent: **"at risk, low usage."** That sentence states a category, names no mechanism, and implies no action - the most common line in a risk review and the least useful one.

Part of the **Read the account** group in this library.

## Who this is for

For CSMs and account managers who need an honest read on an account, whether it is one they have run for years or one they just inherited.

## What this needs

Works with nothing but what you know about the account. Gets better with usage data, mailbox history, the account plan.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the renewal-risk skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/renewal-risk,
zip the renewal-risk folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/renewal-risk`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
