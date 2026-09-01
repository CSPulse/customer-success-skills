# stakeholder map

**Maps who decides an account's outcome by what they can do to it, not by their job title.**

You've seen the contact list - fifteen names, titles, departments, all current - and nobody on it can say who signs the renewal, or whether anyone's ever spoken to them. An org chart tells you what people are called, not what happens to the account if one of them says no, leaves, or stops replying for three weeks. Those are different documents, and the confusion holds until the renewal goes sideways and nobody can explain why.

This skill sorts people by six positions defined by what they can do to the outcome - economic buyer, champion, sceptic, user, coach, gatekeeper - rather than seniority, and insists the sceptic goes on the map, since every account has one. It adds the column most relationship lists skip: have you actually met this person, only heard of them, or merely assumed the role exists. It turns single-threading into a count - how many people would need replacing if one left tomorrow - and tracks movement, since who's gone quiet tells you more than who's still there.

The failure this exists to prevent: **a beautifully complete contact list on an account nobody can name a decider for.**

Part of the **Read the account** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Sort by what they can do, not what they're called | Every name assigned to one of six positions - economic buyer, champion, sceptic, user, coach, gatekeeper - with the sceptic deliberately sought out, since it's the role most often left off |
| Add the column everybody skips | A "have you actually spoken to them" rating of Met, Aware-of, or Assumed for each person - with an Aware-of or Assumed economic buyer flagged as the account's single largest risk |
| Test for single-threading | A number, not an impression: how many people, across how many functions, would have to be replaced if one left tomorrow |
| Track movement, not just position | Who's new, who's left, who's gone quiet after previously responding, and whose remit changed without anyone logging it |
| Name the gaps and what closes them | Each missing relationship paired with a realistic route to close it and a date - an introduction, a business review invite, an exec-to-exec ask - rather than left as an observation |
| Write it down | The completed map, led with the answer to "who decides, and have we met them," using `assets/map-template.md` |

---

## Who this is for

CSMs and account managers walking into an account that's gone quiet, inheriting one they didn't build the relationships on, prepping for a first meeting on an unfamiliar account, or noticing a new executive has shown up on the customer side and needing to know fast what that changes.

---

## What this needs

**Minimum:** the names you know and roughly what they do. Gaps are the output here, not a blocker.

**Better with:** the last few months of email and meeting history, so "who used to respond and stopped" can be answered rather than guessed.

**Best with:** the original deal notes, which usually name the economic buyer and almost always name the sceptic nobody has thought about since. On an inherited account, `account-research` is what finds those notes.

Missing context never blocks this skill - where an `account-context` document exists, it uses who signs in this business (and whether CS ever meets them) to set the bar for the whole map; where it's absent, the skill carries on and names the assumption it's making.

---

## Install

**The easy way: one paste**

```
I want to install the stakeholder-map skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/stakeholder-map folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/stakeholder-map` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method, and `assets/map-template.md` is the map to fill in by hand, no assistant required.

---

## Where this comes from

The buyer-role taxonomy - economic buyer, user, coach, gatekeeper - descends from the buyer roles in Miller Heiman's Strategic Selling methodology, long used in enterprise sales to separate who funds a decision from who uses it from who can block it. This skill carries those roles past the sale into the ongoing account relationship, and adds the sceptic and the single-threading test as its own layer on top.

---

## What good looks like

- The first line names the decider and says whether you have met them
- The sceptic is on the map
- Single-threading has a number, not an impression
- Every gap has a named route and a date
- Someone picking up this account could tell who to call first, and why

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
