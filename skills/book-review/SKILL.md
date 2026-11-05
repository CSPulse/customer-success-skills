---
name: book-review
description: >
  Use when the user says "review my whole book", "quarterly book review", "concentration risk in my book", "renewal cliff", "my book on a page", "where is my book exposed". Produces a one page review of the whole book: what changed since last time, concentration, the renewal calendar, health weighted by ARR, coverage gaps, expansion estimates, and exactly three decisions (stop, start, ask). Not for choosing this week's accounts (use book-triage) or checking a team's reads (use portfolio-review).
---

# Book Review

The monthly or quarterly look at the whole book, written so it ends in three decisions rather than a report.

## Start here

If the user pasted the account list with ARR, renewal date and a health read for each, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. The list: account, ARR, renewal date, notice period, health read (green, yellow, red) and last real touch
2. The date and headline numbers of the last review, if one exists
3. The user's touch cadence and whether the decider has been met on each renewing account

If an "Account context" block exists in the conversation, use it for what normal looks like. Without a last review, say so and set this one as the baseline.

## Do this

1. **Total the book and put changes first.** ARR, account count, red ARR, health mix. If there is a last review, list what moved (ARR, red ARR, the share of ARR in green) before anything else.
2. **Measure concentration.** Share of ARR in the top 1, 3, 5 and 10 accounts, and the largest single renewal month. Say how much of any cliff is not green.
3. **Lay out the renewal calendar** by month for 12 months, using opt-out dates where the notice period is known. Flag a month or quarter carrying an outsized share (a common default is over a quarter of ARR in one month, set your own).
4. **Weight health by ARR** and show it beside the count. Name which reads are the user's judgement and which are scores.
5. **Find coverage gaps.** Accounts past the cadence with no real touch (a human reply or a call), renewing accounts inside 180 days where the decider is unmet, and the overlap of quiet and not green.
6. **Estimate expansion** only on healthy, working deployments. Label every figure an estimate.
7. **End with three decisions:** one to stop, one to start, one to ask for. Add the accounts that earn standing attention outside weekly triage, and anything to confirm this week.

## Output

```
BOOK REVIEW: [owner] | [date] vs [last review date] | [n] accounts | $[ARR]

Decisions
Stop: ...   Start: ...   Ask: ...

What changed since [last review]
- [metric: was, now]

The book on a page
Concentration: top 1 / 3 / 5 / 10 = [share of ARR]
Renewal calendar: [months with ARR, accounts, share, health]
Health: [count] green of [n] but [share] of ARR | red ARR $[x]
Coverage gaps: [n] accounts $[x] past cadence | [n] $[x] decider unmet inside 180 days
Expansion (estimates): [account: range, signal]

Standing attention: [accounts, and why]
Confirm this week: [facts to check]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Count dollars, not accounts.** A book can be mostly green by count and half red by ARR, because the largest accounts carry the weight. Show both so the gap is visible.
- **Look for the cliff before the average.** When annual contracts were signed in one push, one month carries a large part of the book, and a reorg or an illness in that month hits all of it. Spread the work back from the cliff.
- **Quiet and not green together is the finding.** Avoidance shows as the oldest last touch on the yellow and red accounts. Either fact alone is common, both on one account is a decision waiting to be made.
- **Every start needs a stop.** Capacity is fixed, so a new program that replaces nothing is absorbed silently and something else slips. Name the stop, or the review has not decided.
- **Keep the shape identical every time.** A review with a new layout each month hides change. A fixed page lets the eye find what moved.
- **Standing attention is for accounts triage would starve.** The top accounts do not compete in weekly triage with this week's noise, so give them a fixed slot and a named owner.
- **Expansion is an estimate until the customer names a need.** A number in a review reads as a forecast and gets used as one, so show a range and the signal behind it.
- **If the cadence cannot be met in a calm month, the book is too big.** Say so with the count and dollars, because absorbing it quietly removes the evidence.

## Related (only if installed)

`book-triage` for this week's list. `coverage-model` when the book cannot be covered. `renewal-risk` for the depth read on any flagged account. `expansion-case` for an estimate worth pursuing.
