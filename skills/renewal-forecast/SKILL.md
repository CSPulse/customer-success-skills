---
name: renewal-forecast
description: >
  Use when the user says "renewal forecast", "forecast the quarter", "what will we renew", "commit number", "GRR forecast", "roll up my team's renewals". Turns a list of renewing accounts into a dollar forecast with low, expected and high cases for gross and net retention, contraction on its own line, and at-risk accounts grouped by shared mechanism. Not for one account's read (use renewal-risk) or explaining past retention to a board (use nrr-narrative).
---

# Renewal Forecast

A dollar forecast for a renewal period, as a range the user can defend to finance: gross retention, net retention, contraction, and the one or two bets that move it.

## Start here

If the user has pasted or attached a list of renewing accounts, go straight to "Do this". A CSV and a plain pasted list both work.

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. The list, one row per account: account, ARR, renewal date, auto-renew (y/n), notice date, category (commit, likely, at risk, unknown, lost), reason. Any subset works.
2. The period, and any expansion already signed or verbally expected.
3. Last period's forecast against what landed, if the user has it.

Missing columns are inferred and tagged `(assumed, confirm)`. If an "Account context" block exists in the conversation, use it for pricing model and contract shapes.

## Do this

1. **Fix the pool.** Keep accounts renewing in the period. Starting ARR is their sum. Say that the denominator is this period's renewing ARR, not the whole base.
2. **Split by how each renews.** Auto-renew with the notice date passed is Commit. Auto-renew with the window still open stays in the judgement pool on its own line, because the customer can still serve notice. Opt-out date = renewal date minus notice period; flag any inside 30 days.
3. **Categorize on evidence.** Load `references/entry-criteria.md` for the tests and default ranges. No test passed means Unknown, never Likely. An account inside 90 days with no documented risk status is Unknown, because risk found late usually existed earlier.
4. **Group at-risk by mechanism.** One group per cause: a sunset, a price change, a segment, an acquirer. Price each group as two outcomes, resolves or does not. Low = every group fails, high = every group resolves, expected = the odds you state. Single-account risks stay ungrouped.
5. **Split every loss into churn and contraction.** Contraction gets its own line in all three cases. Expansion stays separate and is never netted against a loss.
6. **Compute.** GRR = retained / starting ARR. NRR = (retained + expansion) / starting ARR. Each as low, expected, high.
7. **Say what moves it.** Name the largest bet, its swing in GRR points, what resolves it and by when. Keep accounts that may slip a period apart from accounts that may leave.

## Output

Lead with the call. Use this skeleton exactly, with the numbers table in $k:

```
RENEWAL FORECAST: [period] | [n] renewals | $[x] starting ARR

Call: Plan to $[expected retained] ([GRR]% GRR, [NRR]% NRR). Range [low]% to [high]% GRR.
Biggest bet: [mechanism], $[x], swings GRR [n] points.

Numbers: churn | contraction | retained | expansion | GRR | NRR  x  low / expected / high
Pool: category | accounts | ARR | entry test met
Auto-renew split: passed | window open (names, notice dates) | actively decided
Bets: [mechanism] | accounts | $ | resolves: ... | fails: ... | odds | owner and date
Slip, not loss: [accounts, why, dollars]
Calibration: [adjustment applied, or none and why]
What would make me wrong: [one line, with the number it moves]
Checkpoint: "If [thing] has not happened by [date], [action]."

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its shape and length.

## Rules

- **Contraction is a line, not a footnote.** A renew-or-churn flag cannot represent an account that renews smaller, and those accounts often carry much of a shortfall.
- **Correlated risk is one bet.** Accounts at risk for the same reason resolve together, so adding their probabilities as if independent understates the spread. Low and high are therefore wide on purpose.
- **Unknown is a category.** Without it unknowns drift into Likely, the comfortable bucket, and the forecast inherits the optimism.
- **Silence is not Commit until the notice date passes.** An open-window auto-renewal depends on the customer doing nothing, and one reminder email can end that.
- **Show GRR beside NRR, GRR first.** A few large expansions can hold NRR flat while the base shrinks. The gap between the two is the story.
- **Slip is not loss.** A renewal that moves a period breaks this period's number, not the year's retention, and the cause is usually their procurement, signatures or budget cycle, not their satisfaction.
- **Adjust forecasters out loud.** If last period shows one person's Likely landing short, apply a stated adjustment. Silent discounting costs trust and teaches nothing.
- **Defaults are placeholders.** Every percentage in the references is a common default, set your own. After two periods, replace them with what landed.

## Related (only if installed)

`renewal-risk` for any single account in the pool. `portfolio-review` to challenge the reads before they enter the number. `nrr-narrative` to turn the result into the board story.
