# customer update

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Writes the proactive message nobody wants to send - an incident, a delay, a deprecation, a price change, planned maintenance, a change of CSM - segmented by impact rather than by mailing list, because one message trying to serve both the badly-affected slice of the list and the unaffected majority does both jobs badly.

The subject line has to carry the actual news ("Scheduled maintenance, 12 March, 30 minutes," not "An important update about your service"), and "no action is needed from you" is treated as a load-bearing sentence that has to be written explicitly whenever it is true - its absence gets read as an ask and generates support tickets from people trying to work out if they are safe. A CSM change gets the same rigour as an outage notice: named accounts hear it from a person before anything general goes out, because left to a mass email or an auto-reply it reads as a downgrade, an unimportant account, or an abandonment, usually all three at once. The failure this exists to prevent: **the update written from your side of the glass** - a paragraph about your infrastructure, your roadmap process, or your reorganisation, with the thing that actually affects the customer buried, unmarked, somewhere in the middle.

Part of the **Write to the customer** group in this library.

## Who this is for

For anyone drafting something a customer, or a customer's boss, is actually going to read.

## What this needs

Works with nothing but what is changing, when, and who it touches. Gets better with the account list with contract detail, any notice obligation.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the customer-update skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/customer-update,
zip the customer-update folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/customer-update`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
