---
name: account-review
description: >
  Use when the user says "account on a page", "monthly account review", "account review for", "one page on [account]", "what changed on this account since last month", "run my monthly review". Produces a one page review in a fixed shape: what changed, health by part, goals and proof, who has not been met, open commitments, risks, expansion signal, the next 30 days and the single decision or ask. Not for the renewal call (use renewal-risk), the customer meeting (use business-review) or a twelve month strategy (use account-plan).
---

# Account Review

One page per account per month, in the same shape every time, so change is visible and one decision gets made.

## Start here

If the user pasted notes, usage, tickets or emails for one account plus ARR and renewal date, go. Last month's review, if pasted, makes the change section real. Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Account, ARR, renewal date, notice period
2. What happened this month: calls, people, usage, tickets, requests
3. Last month's review, or "none"

If an "Account context" block exists, use it for what normal looks like. Use whatever the user has connected opportunistically, and never require it.

## Do this

1. **Set the clock:** opt-out date = renewal date minus notice period. Report days to it, not to renewal.
2. **Change first.** Diff against last month: people, usage, requests, commitments, tickets. With no prior review, write "baseline month, no change shown" and make this page next month's comparison.
3. **Show health in parts,** never one blended color: usage, proof of value, relationship coverage, support, commercial. Each gets a number, its measure, a trend and a tag (`said`, `seen`, `inferred`). The weakest part sets the headline.
4. **Goals and proof.** One line per goal: baseline, now, target, newest customer-stated proof and its age. Mandatory, even if the line reads "no proof".
5. **People.** Named roles (champion, economic buyer, technical, any new name), met or not, last contact. Count roles met out of roles named.
6. **Commitments.** Firm promises open, ours and theirs, with days overdue. Mandatory.
7. **Risks and expansion.** Risks with a trigger date. Expansion only as a signal until the customer states a need; if sized, label it an estimate with its rule.
8. **Next 30 days** as dated actions, then **one decision or ask** for the user's manager or the user. Pick the one that moves the clock.

## Output

```
ACCOUNT REVIEW: [Account] | [ARR] | renews [date] | opt-out by [date] ([n] days) | [month]
Decision needed: [one]    Headline: [state, set by which part]

Changed since [last review date]
- [change, tag]

Health by part
| Part | Value (measure) | Trend | Tag |

Goals and proof
- [goal]: [baseline] to [now], target [x]; newest proof [date, who, age]

People: [n] of [n] named roles met
| Name | Role | Met | Last contact |

Commitments (firm, open): ours [n], theirs [n]
- [item, owner, due, days overdue]

Risks: [risk, trigger date]    Expansion: [signal, status, estimate if any]
Next 30 days: [date: action]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Keep it to one page.

## Rules

- **Same shape every month.** Change only shows when the page does not, and a reader who knows where to look reads it in two minutes.
- **One decision per review.** A page that asks for three things gets none, so choose the one that moves the clock.
- **Health stays in parts.** Averaging lets strong usage hide an unmet decider, and the weakest part is the one that renews or does not.
- **Proof and commitments cannot be skipped.** They are the first sections dropped under time pressure and the first things a renewal turns on.
- **Name the measure on every count.** "112 of 140 seats active in the last 30 days" can be challenged. "Usage is healthy" cannot.
- **Silence from a decider outranks good usage.** The people who run the tool are not the people who sign, so an unmet economic buyer is a finding, not a gap.
- **A signal is not an opportunity.** Someone mentioning a second site is a reason for a conversation. Size it only as an estimate and only on a deployment that works.
- **List what you could not check.** An unchecked ticket queue reads as a clean one.

## Related (only if installed)

`value-ledger` for the proof section. `commitments` for the ledger behind that section. `renewal-risk` when the headline turns to watch or worse. `stakeholder-map` for the people section.
