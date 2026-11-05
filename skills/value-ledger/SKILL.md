---
name: value-ledger
description: >
  Use when the user says "value ledger", "what has the customer actually achieved", "do we have proof of value", "capture their success goals", "what is our evidence of ROI", "log this win". Produces a goals table (customer's measure, baseline, now, target), a dated proof log tagged customer-stated or vendor-computed, the gaps, and one ask to capture the next proof in writing. Not for the review meeting itself (use business-review) or sizing an expansion (use expansion-case).
---

# Value Ledger

What the customer set out to achieve and the proof they are getting it, in one place the QBR, the renewal read and the sponsor's own business case can all draw from.

## Start here

If the user pasted goals, notes, emails or call summaries for one account, go. Also useful: the renewal date and today's date. Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. What the customer said they bought this to achieve, in their words
2. Any result they have mentioned since: a number, a quote, a milestone
3. The renewal date

If an "Account context" block exists, use it. If a ledger from last time is pasted, update it and show what changed.

## Do this

1. **Write each goal in the customer's measure,** not ours: what they count on their own scoreboard. Add baseline, now, target and target date. A blank is written "baseline missing", never filled.
2. **Compute progress** as (baseline minus now) divided by (baseline minus target), and show the arithmetic.
3. **Log proof** one row each: date, goal, kind (quote, metric, milestone, outcome), the words or number, who said it and where, and its type: `customer-stated` or `vendor-computed`. Activity (logins, messages sent) is not proof of value: say so.
4. **Age every row.** Flag a goal whose newest customer-stated proof is older than 90 days (a common default, set your own), and any account renewing within that window with none.
5. **Attribute honestly.** List what else changed in the period (a policy, hiring, season, another tool). State the claim at the strength the evidence supports.
6. **Price it only from the customer's inputs,** shown with the inputs and labeled an estimate.
7. **End with one ask:** the smallest request that gets the next proof in the customer's own words, in writing, plus a draft.

## Output

```
VALUE LEDGER: [Account] | renews [date] ([n] days) | as of [date]
Position: [x of y goals provable today; what a skeptical finance reader would accept]

GOALS
| Goal (their words) | Measure | Baseline | Now | Target by [date] | Progress | Proof status |

PROOF LOG (all rows proposed until you confirm)
| Date | Goal | Kind | Evidence | Said by / source | Type | Age |

Attribution: [what else changed]
Estimate: [value, with each input and its source]

Gaps
- [goal, what is missing, how to get it]

Ask: [who, what, by when]
Draft: [short message]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`.

## Rules

- **Value lives in the customer's measure.** Their approver answers to their scoreboard, and a vendor metric gets read as the vendor's marketing.
- **No baseline, no proof.** "Down to 10" means nothing without "from what". Capture it now, or say it is missing and from whose records it can be rebuilt.
- **Customer-stated beats vendor-computed.** "Your tool, your math" ends the argument faster than any dashboard, so lead with their words and treat ours as support.
- **Evidence ages.** A quote from last spring reads as history at renewal. Refresh before it is needed, not during.
- **Say what else changed.** Correlation sells until a finance reader asks about the fee change. A claim with its confounder named survives; one without gets discounted whole.
- **Anything proposed is a proposal.** An assistant or analyst suggesting a row does not make it proof. The user confirms each, because an overstated line damages the champion who carries it.
- **Get the champion to say it in writing.** An email survives their moving on and travels without you, which a slide of ours never does.
- **Never invent a number.** Every figure comes from the paste or is marked missing.

## Related (only if installed)

`business-review` to turn the ledger into the meeting. `expansion-case` when proof supports a bigger ask. `renewal-risk` reads it as evidence.
