---
name: day-plan
description: >
  Use when the user says "plan my day", "build my day around these meetings", "when do I do the recaps", "I have back to back calls today", "fit my replies around my calendar", "shut down time". Turns today's meetings, owed replies and top priorities into a timeline with prep before external calls, recaps within 30 minutes, reply sprints, one deep-work block and a shut-down time. Not for choosing which accounts get time this week (use book-triage) or ranking what you owe (use what-do-i-owe).
---

# Day Plan

Paste today's meetings, what you owe and your top priorities. Get a timeline that fits the day, a visible buffer, and what drops if the day overruns.

## Start here

If the user pasted today's meetings (time, who, and their time zone if it differs), go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Meetings today with start, end and who is on them (mark which are external)
2. Working hours, time zone, and personal blocks (lunch, school run, gym)
3. The owe list or the top 1 to 3 things that must move today

If an "Account context" block exists in the conversation, use it to judge which accounts are high stakes. If a calendar is connected, you may read it. Otherwise use the paste.

## Do this

1. **Date the day by its start.** A day that starts 6 pm and runs past midnight belongs to the date it started. Convert every meeting into the user's own clock and keep the other zone in brackets.
2. **Fix the immovable.** Meetings, then personal blocks, then the shut-down time. Mark which meetings are external.
3. **Scale prep to stakes.** A routine external check-in gets 10 minutes immediately before. A renewal, an exec, an unmet decider or an angry customer gets 20 to 30 (common defaults, set your own). Internal meetings get none.
4. **Place a recap after every external call,** starting within 30 minutes of the end, 10 to 15 minutes each.
5. **Put the hardest or most avoided task first,** before the inbox. Name it and say why it is the one.
6. **Fill the gaps in this order:** reply sprints (15 to 20 minutes, "reply now" items first), one protected deep-work block of 60 minutes or more, then the can-wait items. A fifth of the day left as buffer, visible and labeled, is a common default.
7. **Count honestly.** Add meeting, prep, recap, sprint and personal minutes. If they exceed the working day, say the day is overfull, name what to move or cut, and do not cram it.

## Output

Use this skeleton. Keep it to one page.

```
DAY PLAN: [weekday date] | [start] to [end] [zone] | [n] meetings, [min] min
Verdict: FITS / TIGHT / OVERFULL - [one line, with the minute count]
Hardest first: [task] because [reason]

Timeline
[start-end] [block] | [account, stakes, prep note]

Buffer: [min] visible, [min] resets. Booked: [min] of [min] working.

If the day overruns, drop in this order
1. [block] moves to [day, time]
Never drop: [blocks and why]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Recaps within 30 minutes, not "later".** Memory of who said what decays within hours, and the commitments in the call go with it.
- **Prep is scaled to what can go wrong.** A flat 10 minutes before every call wastes time on easy ones and short-changes the renewal with an unmet decider.
- **No more than three meetings back to back without a reset.** By the fourth the quality of listening falls and recaps pile up unwritten.
- **A plan with no slack breaks by mid-day.** The first overrun cascades into every later block, so show the buffer as a block and defend it.
- **Say overfull out loud.** A cramped plan hides the real decision, which is what to cancel, move or hand off. Name the item and the new slot.
- **The hardest task goes before the inbox.** Avoided work gets avoided again when the day fills up, and email always feels more urgent than it is.
- **Protect one deep block and say what it is for.** An unlabeled "focus time" is the first thing a colleague books over.
- **Time zones are where plans fail.** Convert once, write both clocks, and flag any meeting that crosses the user's start or end of day.

## Related (only if installed)

`what-do-i-owe` to build the list this plan consumes. `call-prep` for the long prep slots. `call-recap` for the recap blocks. `book-triage` for the week.
