# Sample output

*Invented example. The customers (Fernwick Dental Group and the others) are fictional and the vendor sells a per-seat scheduling product. Input the user gave: "Scan my 15 accounts for expansion. Pricing is per seat, list is below with ARR, seats, 30 day active seats, usage change and what I have heard. Today is 5 Nov."*

---

```
EXPANSION SCAN: Thu 5 Nov 2026 | 15 scanned | 5 ranked | 2 on hold
Verdict: One real conversation (Fernwick), two worth a question (Orrin,
Harrow), two signals that need the customer to speak first. Weighted estimate
about $35,500. Unweighted expected is $108,750 (low $70,550), which it will not reach.

| # | Account            | ARR      | Conf | Low     | Expected | Weighted | Timing       |
| 1 | Fernwick Dental    | $96,000  | High | $24,000 | $36,000  | $21,600  | Now          |
| 2 | Orrin Logistics    | $150,000 | Med  | $11,250 | $18,750  | $5,625   | Now          |
| 3 | Harrow Street Vets | $54,000  | Med  | $9,600  | $14,400  | $4,320   | Now          |
| 4 | Nettlebrook Clinics| $118,000 | Low  | $17,700 | $23,600  | $2,360   | Next quarter |
| 5 | Quillfeather Foods | $64,000  | Low  | $8,000  | $16,000  | $1,600   | Next quarter |

Signals
1. said: regional manager asked about 3 more clinics (call, 29 Oct). seen: 76 of 80 seats used.
2. said: customs team asked for access (email, 28 Oct). said: dock turnaround 52 to 41 minutes
   (QBR, 8 Oct). Payer unknown, hence Medium.
3. said: practice manager asked if it covers boarding kennels (email, 3 Nov). Staff count inferred.
4. seen: usage up 34 percent (6,300 actions against 4,700). said: no-show rate 14 to 9 percent.
   Nobody has asked for more, so a question, not a pitch.
5. seen: 38 of 40 seats used. Nobody has said anything. Could be shared logins.

Hold (do not ask)
- Bramblecourt Homes | seats 58 of 60 | P1 sync bug open 19 days, champion's
  last reply terse (2 Nov) | fix by 20 Nov, rescan 4 Dec
- Pellam Marine | exec mention, second hand via champion | renews 12 Feb 2027,
  opt-out 14 Nov (90 day notice, confirm), decider unmet | settle renewal
  first, rescan 1 Mar

No signal: 8 accounts (Sundial, Tarn Road, Ulverston, Vantage Row, Willow Bend,
Yarrow, Zephyr Park, Ashgrove). Sundial is at 22 of 30 seats: the opposite problem.

Sizing assumptions (defaults, set your own)
- Unit price is ARR divided by seats bought: Fernwick $1,200, Orrin $750,
  Harrow $1,200, Quillfeather $1,600. Ignores discounts.
- Weights High 0.6, Medium 0.3, Low 0.1. Weighted is a ranking, not a forecast.
- Fernwick expected: 3 clinics x about 10 staff = 30 seats (assumed). Low is
  a quarter of 80 seats = 20. Orrin: 25 customs users expected, 15 low.
  Nettlebrook: a fifth of ARR expected, 15 percent low. Quillfeather: 10 seats
  expected, half of that low.

First conversation: Fernwick Dental, Marisol Veit (regional operations manager)
Open: "You mentioned the three clinics on Thursday's call. Before I send
  anything, help me picture how they schedule today."
Ask: What goes wrong at those clinics now? Who would run it day to day? Who
  signs, and when does that budget get set?
Listen for: a cost she already feels (missed chairs, overtime), a deadline,
  and whether her boss has asked or she is exploring.
Bring: Fernwick's own utilization (76 of 80 seats) as the reason this is
  easy. Offer a one-clinic pilot, not a quote.
Do not: name a price, mention a seat count first, or copy the AE yet.
Next: call by Fri 13 Nov. If she confirms need and budget, build the case with
  her (expansion-case), then the AE intro with her consent (csql-motion).
Log as: estimate $36,000, basis 30 seats x $1,200 (assumed), stage identified,
  5 Nov 2026.

What I could not check
- Whether sales already has an open opportunity at Fernwick or Orrin
- Real discounts, so unit prices are rough
- Why Nettlebrook usage rose (a one-off project or a real change)
```
