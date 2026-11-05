---
name: mutual-action-plan
description: >
  Use when the user says "mutual action plan", "shared plan with the customer", "joint plan with dates", "customer-facing timeline", "owners on both sides", "they keep missing their dates". Produces a plan of at most twelve rows with named owners on both sides and agreed dates, the decision points, shared risks and a review cadence, plus a three line cover note. Not for the internal readiness call and watchlist (use onboarding-plan) or a twelve month internal strategy (use account-plan).
---

# Mutual Action Plan

A plan the customer can read, edit and forward: their goal in their words, dated rows owned by both sides, and the decisions that gate them.

## Start here

If the user gave the type (onboarding, expansion or renewal), the goal date and who is on each side, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. The type and the outcome in the customer's own words, with the date that matters to them
2. Named people on their side and the sponsor, and the user's own team
3. Dates already fixed: contract, freezes, holidays, budget or board dates

A signed order form or kickoff notes are a bonus. If an "Account context" block exists in the conversation, use it. Anything the customer has not said yes to is marked "Proposed".

## Do this

1. **Write the goal in their words.** One sentence, with a date, using their names for things. If you cannot quote them, mark it "Proposed".
2. **Work backward from the fixed date.** Place their freezes, holidays and approvals first, then the milestones around them.
3. **Give both sides rows.** Count them. If their side holds fewer than a third, find what they must supply, decide, approve and attend. One named owner per row.
4. **Make decisions rows.** Each has a decider, what they need to decide, and the date. Say what slips, day for day, if it is late.
5. **List needs, then risks.** Each row names what it waits on. Keep three shared risks at most, each with a trigger and a mitigation.
6. **Set the cadence.** A short fixed review with named attendees and one rule: a row on their side that slips is raised with their sponsor that week, as a joint reset.
7. **Cut to twelve rows or fewer.** Detail lives in the user's own tracker. Then write the three line cover note.

## Output

Use this skeleton. Everything above the line is shareable. Everything below stays with the user.

```
MUTUAL ACTION PLAN: [Customer] and [Vendor] | [type] | goal date [date]

Goal (their words): "[sentence]"
Sponsors: [name, customer] | [name, vendor]

| # | Milestone or DECISION | Owner (side) | Date | Needs | Status |
(Status: Agreed or Proposed. At most 12 rows.)

If a decision is late: [decision, what slips]
Shared risks: [risk, trigger, mitigation]
Review: [day, length, attendees]. [The slip rule, in friendly words.]

Cover note (3 lines, to send with the plan)

--- below this line is for the user, not the customer ---
Proposed, not yet agreed: [dates and owners]
What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Dates are agreed, not imposed.** A date the customer did not accept is one nobody on their side owns. Mark it "Proposed" until they say yes, and move it only in the open.
- **Both sides own rows.** A plan where only the vendor has tasks is a to-do list with the customer's name on it. Their rows are what hold the plan up.
- **Twelve rows or fewer (a common default, set your own).** A longer plan is not maintained, so it stops being true. Subtasks belong in the user's own tracker.
- **Use their words for things.** A plan in the vendor's jargon cannot be forwarded to their boss, and the sponsor has to carry it upward.
- **Decisions are rows with a date.** Most slips are a decision nobody was asked to make, not unfinished work, so put the decider and the deadline where everyone sees them.
- **A slipping row on their side is an early warning.** A customer who stops doing their rows has often moved the priority, so raise it with the sponsor the same week, before a month of silence.
- **Write nothing you would not show them.** The plan is shared, so worries about the customer go in the private block below the line, never in a cell.
- **Do not invent their commitments.** A row the customer never agreed makes this a vendor document with their name on it. Product, price and security statements come from the user, who confirms them.

## Related (only if installed)

`onboarding-plan` for the internal readiness call and watchlist. `account-plan` for the longer strategy. `expansion-case` or `renewal-runway` when this plan serves an expansion or a renewal.
