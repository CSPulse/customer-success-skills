# renewal negotiation

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Prepares the renewal conversation itself: what you'll concede, what you won't, both sides' walk-aways, and what they're actually going to ask for. Every concession made in this conversation is permanent unless deliberately made temporary, and the discount given in the last week of a quarter sets the price for every year after it.

It starts by checking whether this is even the right meeting - is value already agreed, and is this a live negotiation or a decision already taken internally that you're being informed of rather than negotiated with - because negotiating price before value is established means arguing about a number with nothing on the other side of the scale. It works out both walk-aways honestly, including the customer's real alternative rather than the one they describe: "do nothing" and "renew smaller while evaluating" are both more common and more likely than the competitor switch that gets threatened, and a named competitor with no demo behind it is a procurement tactic, not a decision. It reads the three contract clauses that set the whole shape of the conversation before reading the room - notice date, auto-renewal, and any uplift clause already in force - and separates what the business owner wants (continuity, no disruption) from what procurement is measured on (a percentage saved against the last number, which means they need a win, not necessarily your margin, and a longer term or better payment terms can buy that win far more cheaply than a rate cut). The concession ladder gets built in advance, three rungs and a floor, with what you give, what you get, and what it costs written down for each - because a free concession tells the customer the price was never real. It closes with the four asks a CSM will actually get in this conversation and how to handle each one: the vague discount ask, the "we're only using 60% of seats" rightsizing dressed as a commercial issue, the competitor quote with no scope attached, and the request to go month-to-month.

The failure this exists to prevent: **negotiating price before value is established.** If the customer hasn't agreed the thing was worth having, there's no negotiation happening - just an argument about a number, and it's an argument you lose every time.

Part of the **Run the set-piece** group in this library.

## Who this is for

For CSMs running the big, mostly one-shot moments in an account's lifecycle, the ones with no redo if they go wrong.

## What this needs

Works with nothing but the account, the date and roughly what they pay. Gets better with the contract, especially notice date and uplift clause.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the renewal-negotiation skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/renewal-negotiation,
zip the renewal-negotiation folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/renewal-negotiation`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
