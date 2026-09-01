# stakeholder map

**Part of [customer-success-skills](../../#readme), CS Pulse's open library of AI skills for the work customer success actually does.**

Maps the people who decide an account's outcome by what they can do to it, not by their job title. An org chart tells you what people are called; this tells you what happens to the renewal if a given person says no, and what happens if they leave - and those are not the same document.

It sorts every person into one of six positions defined by function rather than seniority - economic buyer, champion, sceptic, user, coach, gatekeeper - because the same title maps differently at every company, and a person can hold more than one position at once. Getting the sceptic onto the list is treated as the actual point of the exercise: every account has one, and a map with no sceptic on it is incomplete, not exceptional. For each person it adds the column most maps skip entirely - met, aware of, or assumed - and if the economic buyer is anything less than met, that's named as the account's largest risk before anything else in the read, ahead of every usage signal. It then runs a concrete single-threading test (one relationship means no recovery path; two people on the same team is single-threading in disguise; three or more across functions is real coverage) and asks the harder version of the question: if the champion left this month, is there anyone left inside the account who could explain why they bought this in the first place. Movement gets tracked deliberately - who's new (a new executive reviews everything their predecessor bought, and that isn't negotiable), who's gone quiet after previously responding fast, whose remit changed without anyone logging it - and every identified gap gets a named route to closing it and a date, because a map that stops at "we don't know the economic buyer" has only described the problem.

The failure this exists to prevent: **a beautifully complete contact list on an account nobody can name a decider for.**

Part of the **Read the account** group in this library.

## Who this is for

For CSMs and account managers who need an honest read on an account, whether it is one they have run for years or one they just inherited.

## What this needs

Works with nothing but the names you know. Gets better with email and meeting history, the original deal notes.

Missing context never blocks this skill. It changes what the skill can honestly claim, and it names the checks it could not run rather than guessing around the gap.

## Install just this skill

**In the Claude app, no terminal needed.** Paste this into Claude:

```
Download the stakeholder-map skill from
https://github.com/CSPulse/customer-success-skills/tree/main/skills/stakeholder-map,
zip the stakeholder-map folder on its own, then upload it as a skill in Claude.
```

Or do it by hand: download this repository as a ZIP (or clone it), zip this folder (`skills/stakeholder-map`) on its own, then in Claude go to **Customize > Skills > Create skill > Upload a skill**. The folder name inside the ZIP has to match the `name` in `SKILL.md`.

## Want the whole library?

The [main README's Install section](../../#install) has the one-line plugin command that installs the whole library at once, plus the API and by-hand routes.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills), maintained by [CS Pulse](https://cspulse.com?ref=github).
