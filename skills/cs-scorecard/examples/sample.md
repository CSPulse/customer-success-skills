# Sample output

*Invented example. Every account below is fictional. Input the user gave: "Build me a scorecard for my team's 20 account book, trailing 12 months to 31 Oct 2026. ARR a year ago was $2,000k. Churned: Alder Print $90k, Brindle Tools $45k. Contracted: Cobalt Dairy 120 to 90, Dunmore Tiles 80 to 60, Elmstead Co-op 60 to 50. Expanded: Fenwick Labs 150 to 195, Garrow Foods 100 to 130, Hollin Press 70 to 85, Ivybridge Mills 50 to 60. The other 11 are flat at $1,235k. Red now: Juniper Haulage $210k (sponsor left, renews 15 Jan), Kestrel Optics $120k, Dunmore $60k (renews 28 Dec), Lowmoor Steel $40k."*

---

```
CS SCORECARD: team book | 1 Nov 2025 to 31 Oct 2026 | 20 accounts, $2,000k at start
Headline: Gross 90.3% beside net 95.3%, a 5.0 point gap. The book shrank 4.7%
even with $100k of expansion, and 45% of that expansion is one account.

Lagging (what already happened)
| Metric          | Value  | Computed as                         | Owner   | Hides                         |
| Gross retention | 90.3%  | (2,000 - 135 - 60) / 2,000          | CS lead | Ignores expansion             |
| Net retention   | 95.3%  | (1,805 + 100) / 2,000               | CS lead | One large win can mask losses |
| Logo churn      | 10.0%  | 2 logos lost / 20 at start          | CS lead | $45k and $90k count equally   |
| Contraction     | 3.0%   | 60 / 2,000                          | CSM     | Often precedes churn          |
| ARR at risk     | 22.6%  | 430 red / 1,905 ending ARR          | CSM     | Depends on who flags          |

Leading (what is about to happen)
| Metric                  | Value          | Computed as                  | Counter-metric             |
| Health, ARR-weighted    | green 56.4%    | 1,075 / 1,905                | Score 90 days before churn |
|                         | yellow 21.0%   | 400 / 1,905                  |                            |
|                         | red 22.6%      | 430 / 1,905                  |                            |
| Health, by count        | 9 green of 18  | 9 / 18 = 50%                 | (shown to compare)         |
| Champion coverage       | not computable | needs champion_engaged column| Accounts with a second contact |
| Adoption, breadth       | not computable | needs active_seats, seats    | Key feature use            |
| Contact cadence         | not computable | needs last_contact           | Renewals kept per touch    |

Arithmetic
Start 2,000 | churn 135 (Alder 90, Brindle 45) | contraction 60 (Cobalt 30,
Dunmore 20, Elmstead 10) | expansion 100 (Fenwick 45, Garrow 30, Hollin 15,
Ivybridge 10) | ending ARR from the same 18 accounts 1,905.
Net minus gross = 5.0 points. Top 3 accounts at end (largest flat account 260, Juniper
210, Fenwick 195) = 665 / 1,905 = 34.9% of ARR.

Red flags
1. Net 95.3% against a 100% default: expansion did not cover the losses.
   Without Fenwick, net is (1,805 + 55) / 2,000 = 93.0%.
2. $430k red is 22.6% of ARR, and $270k of it renews by 3 Feb 2027: Juniper
   Haulage $210k (15 Jan) and Dunmore Tiles $60k (28 Dec). Dunmore contracted
   in the period and is red, the pattern that precedes a loss.
3. Gross sits 0.3 points above the 90% default and logo churn sits on the 10%
   line, so one more mid-size loss tips both.

Change: add a champion_engaged column this month, because the Juniper sponsor
loss lives in notes, not in any metric. Decision it drives: renewal reads on
Juniper and Dunmore before Fri 20 Nov.
Targets (common defaults, set your own): gross 90%, net 100%, logo churn under
10%. Replace with this book's trailing baseline after two more quarters.
Cadence: CSMs weekly on leading rows, team lead monthly on lagging rows.

What I could not check
- Whether Alder or Brindle were red 90 days before leaving (no earlier health)
- Renewal dates for Kestrel and Lowmoor, assumed beyond 3 Feb 2027 (confirm)
- ARR inputs as pasted, with no check against the billing ledger
- New logos in the period, excluded here by definition
```
