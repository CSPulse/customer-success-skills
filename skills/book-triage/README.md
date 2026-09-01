# book triage

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Starts from the position that even coverage is not the goal, it's the failure: forty accounts touched equally is forty accounts touched too lightly to move anything, while the CSM doing it feels busy. This skill sorts by what changed in the last two to four weeks - usage composition, a person arriving or going quiet, a commercial event - rather than by health color or account size, both of which are largely static and surface the same accounts every week for no reason. It layers in the dates that actually bind (notice date and budget lock, not the renewal date itself), asks a harder question than "is this account okay" - if I spend four hours here this week, does anything actually move, or is the decision already made - and it deliberately hunts for the silent accounts at the bottom of the last-real-contact list, because the accounts with the fewest logged touches are disproportionately risky and disproportionately rated healthy simply because nobody has spoken to them recently enough to know otherwise.

The failure this exists to prevent: **the week spent on the accounts that asked** - attention allocated by who emailed loudest, which correlates with neither risk nor value, and which systematically starves the quiet accounts where the actual danger sits. The skill also forces the part everyone skips: an explicit not-this-week list, naming the accounts being consciously left alone along with the trigger that would change that, so a bad surprise later is a decision that was made in writing, not neglect nobody admitted to.

Part of the **Run the book** group in this library.

## Who this is for

For CSMs managing more accounts than they can give equal attention to, and being honest about the tradeoffs that forces.

## What this needs

Works with nothing but your account list with renewal dates and rough values. Gets better with usage trend, support activity, and last real contact dates.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the book-triage skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/book-triage,
zip the book-triage folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/book-triage`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
