# Sample output

*Invented example. Vendor "Quillbase" and every customer named are fictional. Input the user gave: "Forecast Q1 FY27 for me. CSV pasted below: 25 renewals, $3.08M ARR, columns as you asked. Finance wants GRR and NRR as a range by Friday, and I think the adapter sunset is the real risk."*

---

```
RENEWAL FORECAST: Q1 FY27 (1 Jan to 31 Mar 2027) | 25 renewals | $3,080k starting ARR

Call: Plan to $2,500k retained (81.2% GRR, 83.0% NRR). Range 62.6% to 95.4% GRR.
Low assumes every named bet fails at once. It is a floor, not a plan.
Biggest bet: v1 adapter retirement, $550k, swings GRR 12.4 points.

$k                       Low     Expected   High
Churn (logos lost)       1,041   485        60
Contraction (shrank)     112     95         83
Retained                 1,927   2,500      2,937
Expansion (separate)     20      55         100
GRR                      62.6%   81.2%      95.4%
NRR                      63.2%   83.0%      98.6%

Contraction is 95 of the 580 expected loss (16%). Known: Dunmore Logistics signed
at $105k, down from $120k. Expansion: 20 signed (Brightwater), +35 verbal
(Juniper Freight, said by their ops lead), +45 pending (Kestrel, Lumen) in High.

Pool            Accts  ARR    Entry test met
Commit            9    1,045  5 auto-renew, notice passed (615); 4 signed (430)
Likely            7      815  decider spoken to this quarter, no live risk signal
At risk           6      895  named mechanism, three groups below
Unknown           2      265  Westbrook Transit, Yarrow Clinics: no decider reached
Lost              1       60  Zenith Outdoor: notice served 18 Nov

Auto-renew split: passed 615 (5) | window open 520 (4) | actively decided 1,945 (16)
Window open: Westbrook 175 (notice 28 Feb), Kestrel 160 (12 Feb), Maple Row 110
(20 Feb), Orchard Supply 75 (5 Mar). Westbrook is Unknown AND on silence: first call.

Bets (resolves / fails, retained $k)
1. v1 adapter retires 31 Mar | Quarry Steel, Redfern Mfg, Sable Fab | 550
   Resolves: migration tool ships by 15 Feb, all three migrate: 522
   Fails: Quarry and Redfern leave, Sable renews flat: 140
   Odds 50/50 (inferred). Owner: product lead for 15 Feb, me for the migrations.
2. 9% price uplift from 1 Jan | Tolland Pharmacy, Umber Outfitters | 185
   Resolves: CRO approves a 12-month price hold by 15 Dec: 185
   Fails: Tolland leaves, Umber cuts to 48: 48
   Odds 60/40 (inferred, no CRO decision yet). Owner: me, with the CRO.
3. Ungrouped: Vantage Credit Union, 160. Acquirer standardizing on a competitor.
   Leaves (0) or 12-month bridge at 120. Odds 50/50 (inferred).

Slip, not loss: Lumen Schools 130 (board approves 9 Mar, paper may land after
31 Mar) and Northbank Credit 90 (security re-review). Counted in expected. Both
would renew in Q2: they hurt the quarter, not annual retention.

Calibration: no prior forecast supplied, so no forecaster adjustment (assumed, confirm).
What would make me wrong: bet 1 fails outright, which takes expected GRR to 75.0%.
Checkpoint: "If product has not confirmed 15 Feb in writing by 15 Dec, bet 1 moves
to the low case and I tell finance the same day."

What I could not check
- Whether any Commit auto-renewal has a seat reduction pending outside the CSV
- The odds on bets 1 to 3 are my judgement, not data
- Likely and Unknown ranges are the skill defaults, not this company's history
- Last quarter's forecast against actuals, so no per-person calibration
```
