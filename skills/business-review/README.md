# business review

**Build the review that earns the next meeting, not the one that fills the calendar slot.**

Buyers don't think business reviews are worthless - the same people who call most reviews checkbox exercises, too light on evidence of value, also call the review the single most critical moment for a supplier to prove itself, and a majority say they've walked away from a contract over exactly that. The bar isn't "did we present" - it's whether the customer leaves more confident, having made a decision, in a meeting where they talked more than you did.

This skill starts by checking whether the review should even happen - a live escalation, an absent decision-maker, or nothing changed since last time are all reasons to reschedule instead. Where it should, it forces the value case up a ladder from activity to outcome to business impact, built to survive being forwarded to the customer's own CFO, and pre-briefs the champion so nobody is surprised in front of their own executive.

The failure this exists to prevent: **fifty-five slides of usage data when the customer asked for four charts.**

Part of the **Run the set-piece** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Step 0: Decide whether to run one at all | A check against the conditions that mean this review will burn the format's credibility - no value story, an open escalation, the wrong cadence |
| Step 1: The one sentence | What the customer needs to walk away believing, written before a single slide exists |
| Step 2: Reconstruct their world | Their stated goals, their own public signals, every open loop from last time with current status |
| Step 3: The value case | A three-rung ladder - activity, outcome, business impact - with a baseline, a full cost, and an attribution assumption stated conservatively out loud |
| Step 4: Sequence it | Their business first, goals restated, progress against them, what isn't working, then the ask - three to five themes, roughly a third presenting and two thirds discussion |
| Step 5: Shape it for the room | Different content for the economic buyer, the champion, and operational users - not the same deck delivered three times |
| Step 6: Pre-brief the champion | The single step that prevents most of the failure modes: walked through the data, asked what they want, arranged to present their own wins |
| Step 7: Name the ask | One line stating what you're asking the customer to decide, do, or fund - explicitly allowed to be "no" |
| Step 8: Close the loop | A summary within 24 hours with decisions, owners, dates, and the next meeting already booked |

---

## Who this is for

Anyone prepping a QBR, EBR, or any named "business review" with a customer - and just as usefully, anyone who's been asked to run one and isn't sure it's the right meeting. It's built for the CSM or account lead who owns the relationship, not for someone building a template deck in isolation from the account's actual history.

---

## What this needs

**Minimum:** the account and the date. It builds the structure, the questions, and the ask from what you know, and marks plainly what it couldn't verify.

**Better with:** the customer's stated goals from the last review or the original business case, usage and outcome data, the history since the last meeting, and the attendee list.

**Best with:** a documented success measure agreed earlier. That's the difference between confirming value at the review and arguing for it in the room.

Missing context never blocks this skill - where value can't be proven numerically, it works down an explicit fallback ladder (have the customer say it themselves, document testimony, frame it net of their own cost, or name the measurement gap as next quarter's action) rather than padding the deck with activity metrics to fill the silence.

---

## Install

**The easy way: one paste**

```
I want to install the business-review skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/business-review folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/business-review` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the whole method - this skill has no separate templates or reference files.

---

## Where this comes from

The opening claim - that buyers rate business reviews the single most critical proof point a supplier gets, while also saying most of them are checkbox exercises light on evidence, and that a large share have walked away from a contract over exactly that - is drawn from published buyer-experience research on how customers actually experience these meetings, not from internal opinion. The value case's activity-outcome-business impact ladder reflects standard value-engineering practice: evidence that something ran, converted into the customer's own operational units, converted again into money or risk - because a number a customer can't rebuild themselves dies the moment they try to forward it.

---

## What this does not do

- It does not run a review to satisfy a cadence. Step 0 names the conditions - no value story, a live escalation, the wrong person in the room, nothing changed - under which the honest move is to reschedule or send a written update instead.
- It does not treat quarterly as the default cadence. It matches the interval to contract value, the customer's own decision cycle, and - the correction most suppliers skip - what cadence the customer actually says they want.
- It does not disguise an expansion pitch as a value review. Where more scope is warranted, that becomes a separate conversation (`expansion-case`), because customers punish the disguise, not the upsell itself.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
