---
name: cs-scorecard
description: >
  Use when the user says "CS scorecard", "CS metrics", "what should we measure", "KPIs for my book", "how do I report on my team", "define our retention metrics". Builds a scorecard for a book, a team or the function with exact definitions (numerator, denominator, period, owner, what it hides), computes the values from a pasted account list, flags red lines and says what to change. Not for the board retention story (use nrr-narrative) or auditing a health model (use health-score).
---

# CS Scorecard

Paste an account list or a few numbers. Get a scorecard with exact definitions, the values computed from your paste with the arithmetic shown, the red flags and what to change.

## Start here

If the user pasted accounts with ARR at the start of the period and ARR now, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. The level and the reader: one CSM's book, a team, or the whole function
2. The list: account, ARR at the start of the period, ARR now, renewal date, health if the user has one
3. The period, and which metrics are already reported

If an "Account context" block exists in the conversation, use it for segment and what healthy looks like. Optional columns that unlock leading metrics: `last_contact, champion_engaged, active_seats, seats, success_plan, days_to_first_value`.

## Do this

1. **Fix the level and cadence.** Book: reviewed weekly by the CSM. Team: weekly or monthly by the lead. Function: quarterly for the board. Use the same definitions at all three so the numbers add up.
2. **Fix the cohort.** Accounts that existed on day one of the period. New logos in the period are excluded from retention and counted as new ARR.
3. **Compute the lagging set, showing the arithmetic.** Starting ARR, churn, contraction, expansion, gross retention, net retention, logo churn, ARR at risk. Print the gap between gross and net.
4. **Fill the leading set from what is pasted.** For each metric the paste cannot support, show the definition and write "not computable from this paste, needs [column]". Load `references/definitions.md` for the full list at each level.
5. **Pair each metric with a counter-metric** and state what it hides (touches against renewals kept, tasks on time against outcomes).
6. **Judge against the book's own trailing baseline.** If there is none, offer common starting targets labeled defaults and ask the user to set their own.
7. **Name up to three red flags and one change:** the metric to add, retire or redefine, and the decision it should drive.

## Output

Use this skeleton. Keep it to one page plus the arithmetic.

```
CS SCORECARD: [level] | [period] | [n] accounts, $[start ARR] at start
Headline: Gross [x]% beside net [y]%, gap [z] points. [One-line meaning.]

Lagging (what already happened)
| Metric | Value | Computed as | Owner | Hides |
Leading (what is about to happen)
| Metric | Value or "not computable" | Computed as | Owner | Counter-metric |

Arithmetic
[start, churn, contraction, expansion, each with the accounts behind it]

Red flags: [max 3, each with the number]
Change: [one metric to add or retire, one decision it drives]
Targets: [common defaults, set your own]   Cadence: [who reviews, how often]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Report gross next to net, every time.** The gap is expansion, and a few large expansions can hide logos leaving, so one number alone tells the wrong story.
- **Every metric has a numerator, denominator, period and owner.** Retention computed three ways produces three meetings about whose number is right.
- **Every count names its measure.** "2 of 20 starting logos churned" can be checked, while "low churn" cannot.
- **Pair each activity metric with an outcome.** Teams optimize what they are shown, so touches without renewals kept produces busy CSMs and flat retention.
- **Weight health by ARR, not by count.** Nine green accounts say little when four red ones carry a fifth of the revenue.
- **Use the book's own trailing baseline.** External benchmarks differ by definition and segment, so a peer's figure measures a different thing. Any number from this skill is a common default, set your own.
- **Leading metrics weekly, lagging monthly or quarterly.** Lagging figures move slowly, and reviewing them weekly produces false alarms.
- **A metric nobody can move is a report, not a scorecard.** Give each one an owner who can act on it, or drop it.
- **State coverage.** A figure from 14 of 20 accounts is labeled as such, because a partial paste read as the whole book misleads.

## Related (only if installed)

`nrr-narrative` to turn the gross and net bridge into the board slide. `health-score` to test whether the health column predicts churn. `book-review` or `portfolio-review` for what to decide from the numbers.
