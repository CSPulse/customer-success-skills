# Sample output

*Invented example. Vendor "Tallyfield" and customer "Northgate Dental Group" are fictional. Input the user gave: "Northgate Dental, $96k, renews 31 Jan. Kickoff goals (12 Feb): no-shows from 14% to 9% by year end, front desk reminder calls from 22 hrs a week to 8, and 'a better online rating', no number. Elena (practice director) emailed on 14 Oct: 'No-shows are down to 10.5% from 14%. The reminders are doing it.' Tomas (front desk lead) said on 9 Jun it was about 15 hrs a week. Elena also mentioned a 24-hour cancellation fee that started 3 Aug. About 3,000 appointments a month, $140 a missed slot, her figures at kickoff. We sent 41,200 reminders in September."*

---

```
VALUE LEDGER: Northgate Dental Group | $96k | renews Sun 31 Jan 2027 (87 days) | as of Thu 5 Nov 2026
Position: 1 of 3 goals is provable today, and that one has a confounder. A finance reader would accept the no-show drop with the fee change named. The hours goal is stale and the rating goal cannot be proved.

GOALS
| Goal (their words) | Measure | Baseline | Now | Target by 31 Dec | Progress | Proof status |
| Fewer missed appointments | No-show rate | 14% | 10.5% | 9% | 3.5 of 5 points = 70% | Customer-stated, 22 days old |
| Less time on reminder calls | Front desk hours per week | 22 | 15 | 8 | 7 of 14 hours = 50% | Customer-stated, 149 days old |
| A better online rating | Public rating | missing | unknown | none set | not computable | None |

PROOF LOG (all rows proposed until you confirm)
| Date | Goal | Kind | Evidence | Said by / source | Type | Age |
| Wed 14 Oct | No-shows | Quote + metric | "No-shows are down to 10.5% from 14%. The reminders are doing it." | Elena Marsh, practice director, email | customer-stated | 22 days |
| Tue 9 Jun | Hours | Metric | Reminder calls "about 15 hours a week" | Tomas Reyes, front desk lead, call | customer-stated | 149 days |
| Sep | none | Activity | 41,200 reminders sent | platform report | vendor-computed | shows use, not value |

Attribution: a 24-hour cancellation fee began Mon 3 Aug (said, Elena). Both it and the reminders could cut no-shows, and Elena credits the reminders alone. State the drop as "down 3.5 points since the rollout", not "caused by us", until she splits it.
Estimate: 3,000 appointments x 3.5 points = 105 fewer no-shows a month; 105 x $140 = $14,700 a month, $176,400 a year. Inputs are Elena's kickoff figures (said, not re-checked); treat as an upper bound before the fee change is netted out.

Gaps
- Hours: 149 days old. Ask Tomas to time one normal week.
- Rating: no baseline and no target. Pull today's public rating and review count as the baseline, then ask Elena for a target.
- Fee change: ask Elena for her own split of the drop.

Ask: Elena, by Fri 13 Nov, a two-line reply confirming the figure and splitting reminders from the fee, and permission to quote her in the renewal summary.
Draft:
Subject: Your no-show numbers, one thing to get right
Elena, in your 14 Oct note you said no-shows are down to 10.5% from 14%. That is the number I want to carry into your January renewal conversation, so I would like it to be yours and exact. Could you reply with two things: the figure and the period it covers, and roughly how much of the drop you would put down to the reminders versus the August cancellation fee? A rough split is fine. And may I quote your answer in the summary your leadership sees? Dana

What I could not check
- Whether 3,000 appointments and $140 a slot still hold
- Whether the 10.5% covers the full month or a partial one
- The current public rating and review count
```
