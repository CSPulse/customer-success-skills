# exec conversation

**Fifteen minutes is really eight. Lead with the conclusion.**

Someone hands you fifteen minutes with a CFO or VP two levels above your usual contact, and the instinct is to treat it like a bigger version of the meeting you'd have with your champion. That instinct produces the product tour: a warm handshake, a polite nod, and nothing at all. An executive isn't a more senior champion - different time horizon, different vocabulary. Your champion wants to know what's happening; the executive wants to know whether to keep spending money on this, and what it's costing them not to.

This skill prepares that meeting properly. It works out why the meeting actually exists - the champion showing progress, your side buying coverage, or a new executive auditing what their predecessor bought - because the reason changes what you should say. It finds what they're actually measured on, translates usage numbers into cost, risk, revenue, or time before you're in the room, writes a first sentence that would interest a stranger, narrows the ask to one thing only they can do, and protects the one relationship the meeting could damage: never surprise the champion in front of their own boss.

The failure this exists to prevent: **the product tour.** Fifteen minutes explaining what the platform does to someone who does not care what it does, ending in a warm handshake and nothing at all.

Part of the **Handle the conversation** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Find out why this meeting exists | Which of four reasons put it on the calendar, and what that means for what you should say |
| Work out what they're measured on | What they're accountable for this year, translated to cost, risk, revenue, or time |
| Write the first sentence | The outcome so far in their unit of measure, then the one thing you need - tested against whether a stranger would find it interesting |
| Pick the one ask | A single request, specific and small enough to answer in the room, that only they could do |
| Prepare two questions worth their time | Questions only they can answer, with one planted to draw out what your champion doesn't know |
| Protect the champion | A rule against surprising them with anything they haven't already seen, and an agreed split of who speaks when |
| Plan for eight minutes | A running order with a cut line, plus a shorter version if the meeting runs even tighter |
| Draft the five-line follow-up | Sent the same day, directly to them, written to be forwarded without your explanation attached |

---

## Who this is for

CSMs and account leads preparing any meeting where a senior customer-side person is the point, not just an attendee - a sponsor check-in, a first meeting with someone newly arrived, an escalation that's gone up, or a fifteen-minute slot at the end of a longer visit. It's not for a QBR or EBR with executives present, which `business-review` owns end to end, or a meeting whose whole content is bad news, where `hard-conversation` governs.

---

## What this needs

**Minimum:** their title and roughly why the meeting exists. Enough for a first sentence, one ask, and two questions.

**Better with:** whatever the champion can tell you about this person - what they were hired to do, what they've said about your product, what they're under pressure about this quarter. Ten minutes with the champion beforehand is the highest-return preparation available.

**Best with:** the account's outcome data in their unit of measure, their public commitments, and the original business case - enough to turn an assertion about value into a number they recognise.

Nothing here is required - where an `account-context` document is absent, this skill carries on and names the assumption.

---

## Install

**The easy way: one paste**

```
I want to install the exec-conversation skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/exec-conversation folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/exec-conversation` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the whole method - no reference files or templates, because the running order and the ask are specific to the meeting, not something a generic template would help with.

---

## What this does not do

- Does not plan for the full fifteen minutes - they join late and leave early, so it plans for eight
- Does not bring more than one ask - a meeting with three asks produces zero, because a busy person defers a list
- Does not take anything to the executive that the champion hasn't already seen - that ends the relationship that got you the meeting that afternoon
- Does not resolve a contradiction between what the executive says and what the champion said, in the room - it notes it and takes it away
- Does not route the follow-up through the champion - the record of the meeting goes to the person who was actually in it

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
