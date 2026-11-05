# Sample output

*Invented example. Vendor "Ledgerline" and its health score are fictional. Input the user gave: "Audit our health score. It is 40% logins, 30% tickets, 20% NPS, 10% seats used. Last year 14 accounts churned and 11 of them were green or yellow three months before. Weights were set by a former ops lead in 2023 and never changed."*

---

```
HEALTH SCORE: AUDIT | Ledgerline account health score (2023 model)

Verdict: Treat as an adoption score only; do not act on it alone.
Confidence: medium (14 churns is too few to tune weights, enough to doubt them).

Inputs
| Input        | Weight | Class    | Note                                              |
| Logins       | 40%    | proxy    | Stands in for value; audit tools are meant to sit idle |
| Tickets      | 30%    | measured | Low tickets scored high, but silent accounts also file none |
| NPS          | 20%    | inferred | Answered by users, not by the signer; response rate unknown |
| Seats used   | 10%    | measured | Fine, but tracks headcount not outcomes             |

Backtest (90 days before churn)
- 14 churned; 11 were green or yellow (79%), 3 red
- Of 22 accounts red a year ago, 3 churned, 19 renewed (false alarm rate 86%)
- 6 of the 14 had a sponsor change in the prior 6 months; the score has no input for it
- Weights have never changed since 2023.

Hidden by averaging
- Two-module accounts: reporting module up 30%, ingestion module down 60%, composite flat
- One analyst produced most logins on 8 of the 14 churned accounts

Blind to: sponsor change, signer contact, notice-date questions, budget status, competitor activity.

Fix first
1. Add two buyer-side inputs: sponsor contact in the last 60 days and executive meeting in the last 120 days | Ops lead | 15 Dec
2. Score logins as change against each account's own trailing 6 month baseline | Analytics | 15 Dec
3. Rerun the backtest quarterly and log hits and misses | CS director | 31 Jan

What I could not check
- Score history by month (only the 90 day snapshot was supplied)
- NPS response rate and who answered
- Expansion outcomes, so I cannot say whether green accounts grew
