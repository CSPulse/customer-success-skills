# Sample output

*Invented example. Vendor "Ledgerline" and customer "Tamarack Logistics" are fictional. Input the user gave: "Lost Tamarack, $96k, notice came 2 October for a 15 November end date. They said budget cuts. Dana was our only contact for a year, then she moved teams in the spring. Usage was flat the whole time. Need a postmortem for Friday's churn review."*

---

```
POSTMORTEM: Tamarack Logistics | $96k | lost 15 Nov (notice 2 Oct)

Verdict: Mechanism was a sponsor change with no replacement relationship,
not budget. Preventable, and the signal was detectable in April.
Stated reason: "Budget cuts across vendors" - new Director of Ops to me, 2 Oct
Lost on 20 Jun (FY27 vendor shortlist agreed). Noticed on 2 Oct. Gap: 15 weeks.
Mechanism: Dana, our sponsor and the only person who knew why Tamarack bought
us, moved to a planning role in April. Her successor was never introduced
and inherited a vendor list with a cost-out target. With no one holding the
original business case (cut dock scheduling errors), we were judged on
price alone against a bundled tool already in the stack.

Detectable then                          | Hindsight only
- 11 Apr: Dana's out of office named     | - Usage "felt" flat
  a new role                             | - Tone of the June QBR invite
- 2 May: QBR invite declined, no reply   |
- 20 Jun: successor attended a call as   |
  observer, asked for seat count export  |

Stated reason versus mechanism: downstream. The budget cut was real, and
the value metric was not agreed, so the product competed on price.
Stopped being winnable: 20 Jun. Three months earlier (mid-March), an intro to
Dana's successor and a restated business case would have changed the shortlist.
Pattern: one of 4 losses this year where the sponsor changed role in the
prior 6 months and no second contact existed. Shared: mid-market, 12 month
terms, single threaded.

Changes
- Add "sponsor changed role or left" as a same-week alert | Ops lead | 1 Dec
- Require two named contacts on accounts over $75k at 6 months | CS director | 31 Jan
- Bring the 4 losses to the Q1 coverage review as one issue | me | 15 Dec
Not changing: no discount or feature change. Price was not the root cause.

What I could not check
- Whether the successor was asked about the original goal (no record found)
- Whether a competitor was involved (no evidence either way)
