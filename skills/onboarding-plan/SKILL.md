---
name: onboarding-plan
description: >
  Use when the user says "onboarding plan", "just closed a new customer", "kickoff is next week", "first 90 days", "time to first value", "is this customer really live", or names an account that signed recently. Produces a shared plan with a readiness call, success criteria that carry a baseline, dated milestones with owners on both sides, and a watchlist. Not for the sales handover itself (use handoff) or the long-run account plan (use account-plan).
---

# Onboarding Plan

A plan the customer can point to later: what value means for them, who owns each step, and what would tell you in week three that the year is going badly.

## Start here

If the user gave the account, what was sold, and who bought it, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. What was sold, the signature date, and the contract value
2. Who signed, who will use it, and the problem the customer said they were solving
3. What sales promised that may not be in the contract

Handover notes, the contract scope or a stakeholder list are a bonus. If an "Account context" block exists in the conversation, use it for segment and value metric.

## Do this

1. **Define value per customer before kickoff.** One sentence in their words, with a baseline, a target, a date and a named person on their side who owns the number. If they cannot state a baseline, making the baseline the first criterion is the plan.
2. **Audit the handover for what is missing.** Check six items: business objective, deal context, stakeholders including sceptics, open risks, every promise made in the sale, and the customer's own responsibilities. Each gap becomes a line in the plan.
3. **Validate, do not re-interrogate.** Draft the opener as "here is what we understand from your talks with sales, what would you change". Ask only operational questions: who approves change, the real integrations, whether the champion has changed.
4. **Separate first value from full value.** First value is the first result they care about, not finished configuration. Date five milestones: kickoff (a common default is within 14 days of signature), technical live, training, first go-live, and an ROI review tied to the original goals. Book the first cadence call within 30 days (a common default, set your own).
5. **Name customer owners with hours per week.** "The exec will handle it" is not an owner. Add the one early win achievable in week one or two.
6. **Write the watchlist** for weeks 1 to 4, using the signals in Rules, and warn the customer about the post-go-live dip.
7. **Confirm the criteria in writing the same day.** No written yes means no agreement.

## Output

Use this skeleton. Keep it shareable with the customer, minus the watchlist.

```
ONBOARDING PLAN: [Account] | [value] | signed [date] | kickoff by [date]

Call: READY TO KICK OFF / FIX THESE FIRST
Biggest risk: [one line]
Value in their words: [one sentence]

Success criteria
| Measure | Baseline | Target | By | Owner (theirs) | Tag |

Milestones
| Milestone | Date | Their owner | Our owner | Depends on |

Customer commitments: [name, hours per week, what]
Sold but not in scope: [promise, who made it, how to resolve]
Watchlist, weeks 1 to 4: [signal, threshold, action]

What I could not check
- [gap, marked (assumed, confirm) inline]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **Done means the customer can walk you through a result.** Go-live is a vendor event, adoption is a customer state, and the renewal is judged on the second.
- **A target without a baseline cannot be falsified.** At renewal nobody can prove it moved, so the argument for renewing is opinion.
- **Diagnose a refusal to commit.** Cannot articulate means no baseline exists (build one). Lacks authority is a sponsor problem (get 20 minutes with the budget holder). Hedging means a sponsor who will not say what good looks like will not defend the spend.
- **Fallback ladder when no outcome metric exists:** a leading metric with a baseline, then a named workflow live in production by a date, then a named person who will say it worked. Never close a plan with none.
- **Unwritten promises become scope disputes in month three.** Write each one down now, even the roadmap hints.
- **Sceptics belong on the stakeholder list.** They are the people most often left out and most often the ones who kill the renewal.
- **Plan the security and IT review.** Planned, it runs days. Found after kickoff, it is unbounded.
- **Perceived momentum outranks green metrics.** A customer who feels nothing is moving carries that feeling into renewal. Early warning signs: kickoff slips, sponsor skips it, shrinking attendance, environment provisioned and never used, blockers that age.

## Related (only if installed)

`handoff` if the sales transfer is the problem. `account-plan` when the first 90 days end. `stakeholder-map` for the sceptics.
