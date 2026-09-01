# escalation

**Say something true and specific within the first hour, even though you do not have the answer yet.**

The account is on fire, and the instinct is to go quiet until you have a real answer. That's the mistake - silence reads as chaos or concealment, both worse than an update with nothing new in it.

This skill runs the first four hours: which of three things is actually happening (a failure, a relationship problem wearing a technical trigger, or a commercial negotiation with heat on it), one owner and one channel so the facts don't fragment, when pulling in an executive helps versus burns a card, and the repair step almost every team skips once the incident closes.

The failure this exists to prevent: **going quiet until you have the answer.** The silence is read as chaos or concealment, and both are worse than an update with nothing in it.

Part of the **Run the set-piece** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Establish what kind of escalation this is | Failure, relationship, or commercial - identified by what would actually resolve it, not by how loud it is |
| Respond before you have the answer | A holding statement: the specific impact, what's known and unknown, a named owner, and the next update time |
| Find out what they actually want | The real ask - often to be heard, or a forwardable answer for their own boss - asked directly rather than assumed |
| Set one owner, one channel | A single person sending everything customer-facing, and one written version of the facts everyone quotes from |
| Decide who to pull in, and when | The conditions that justify an executive, a proper brief for them, and the internal ask shaped in business terms |
| Separate the fix from the repair | A specific, visible commitment made after the incident closes - because the relationship damage runs on its own timeline |

---

## Who this is for

CSMs and account leads in the moment a problem has moved above where they normally operate - their VP is involved, the customer is threatening to churn, or a major incident just landed on an account. For delivering bad news that hasn't landed yet, `hard-conversation` is the better fit; once the account has actually gone, it's `churn-postmortem`.

---

## What this needs

**Minimum:** what happened and who is angry. Enough for the holding response, the owner, the cadence, and the pull-in decision.

**Better with:** the support and incident record, the contract, and a current stakeholder map - the map tells you whether the person escalating can actually end the relationship.

**Best with:** a risk read already in hand, because it tells you whether this is an incident on a healthy account or the visible part of something older.

Missing context never blocks this skill - where an `account-context` document is absent, it carries on and names the assumption, particularly around what CS can commit to without asking.

---

## Install

**The easy way: one paste**

```
I want to install the escalation skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/escalation folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/escalation` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method, and `assets/escalation-log.md` holds the holding-statement structure and running log - usable to track an incident without an assistant involved at all.

---

## What this does not do

- Does not speculate on cause under pressure - a theory offered early gets quoted back when the real cause turns out different
- Does not treat a relationship escalation as a failure escalation - the fix lands, the actual cause stays untouched, and the account leaves later looking unrelated
- Does not pull in an executive to demonstrate urgency - an unbriefed executive on the call tends to commit something that then has to be unpicked
- Does not declare the situation resolved when the ticket closes - the relationship damage runs on its own timeline and needs a deliberate repair step

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
