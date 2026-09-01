# offboarding

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Runs a departure once the decision is genuinely final - the single most damaging thing this skill guards against is still trying to save an account that has already been lost, which converts whatever goodwill remains into irritation. It exists to prevent the account that goes cold the moment it is marked closed-lost: the data export drags, the exit conversation never gets asked for, and a customer who left for a fixable reason becomes one who tells people you were fine right up until you stopped caring.

Three jobs, run in order. First, the contractual work - notice, data handover, deletion obligations, access shutoff, final invoice - done faster than required, because slow data export is the detail people describe afterwards more than whatever product problem drove them out. Second, the exit conversation, asked for and held *separately* from the commercial wind-down so it doesn't read as a last sales pitch, using questions built to get past the polite answer: "When did you first start thinking about this?", "Was there a moment we could have changed it?", "What did you tell your own leadership about why?" - asked without defending, correcting, or explaining the roadmap, because one correction ends the honest version of the conversation. Third, treating the departing champion as a future pipeline event rather than a closed record, because champions move, and a clean exit with no pitch attached is what they remember when they land somewhere with budget again.

Part of the **Run the set-piece** group in this library.

## Who this is for

For CSMs running the big, mostly one-shot moments in an account's lifecycle, the ones with no redo if they go wrong.

## What this needs

Works with nothing but the account and the end date. Gets better with the contract, the account history, the original business case.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the offboarding skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/offboarding,
zip the offboarding folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/offboarding`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
