# Sample output

*Invented example. "Brindlewood Payroll" and its numbers are fictional. Input the user gave: "310 accounts, $18.6M ARR, 6 CSMs. Leadership wants a coverage model for planning and asked whether we need more headcount. Everyone under $20k is effectively ignored today. I have the last two years of churn, 31 accounts."*

---
```
COVERAGE MODEL: Brindlewood Payroll | 310 accounts | $18.6M ARR | 6 CSMs

Call: Four tiers fit 6 CSMs only after moving 36 accounts down, stretching Tier B to
a six-week cadence, and adding a champion-change trigger for the bottom two tiers.
Unchanged, the book needs 7.1 CSMs and the 1.1 gap lands on Pooled, unseen.

Tier        Accts  ARR      Coverage                  Cadence          Hrs  FTE   Up-trigger
A Named+      24   $7,200k  named CSM, exec sponsor   monthly + QBR    160  2.74  n/a
B Named       24   $3,860k  named CSM                 every 6 weeks     60  1.03  ARR over $250k
C Pooled      98   $4,660k  pod of 2 CSMs, queue      quarterly check   25  1.75  3 sev-1 tickets in 60 days
D Digital    164   $2,880k  triggers + library        none, on trigger   4  0.47  seats over 90% for 30 days
Total        310  $18,600k                                                   5.99

Entry rules: A = ARR $250k+ or 3+ integrations or regulated. B = $90k to $250k.
C = $20k to $90k. D = under $20k, one team, no integrations. Complexity moved 9
accounts: 5 up (under $100k, multi-entity or regulated), 4 down (over $150k, one
team, no integrations).

Capacity. Before moves: A 24x160 + B 46x70 + C 90x25 + D 150x4 = 9,910 h required
vs 6 x 1,400 = 8,400 h available. Gap 1,510 h (hours per account assumed, confirm).
Closed by choice, not absorption:
- Move 22 Tier B accounts under $90k to Pooled: saves 990 h
- Tier B cadence monthly to every 6 weeks on the 24 that stay: saves 240 h
- Move the 14 smallest Pooled accounts to Digital once the admin-change trigger
  is live (Ops, 31 Jan): saves 294 h
After: 8,386 h of 8,400. Overall 52 accounts per CSM, but it runs from 9 in A to 350 in D.

Not served
- A: nothing cut, but named CSMs absorb unlogged work. Cap new A entries at 2 per CSM.
- B: no QBR deck, an async quarterly report instead. Not seen: exec shifts between calls.
- C: no continuity, the pod rotates. Customers re-explain. Not seen: slow decline
  unless the usage trigger fires.
- D: no human unless a trigger fires. No relationship signal at all.
Digital needs: seat events (live) | 8 of 12 library articles (4 to write by 31 Jan) |
triggers owned by Ops | route to the pod queue, 1 business day. If the admin-change
trigger is not live by 31 Jan, D is unserved, and we say so.

Transitions
- Down: the named CSM calls with the reason and introduces the pod. Pod lead does a
  30-day check.
- Up: pod CSM briefs the new named CSM using the handoff doc before the move.
- Temporary elevation: pod lead approves, 60 days maximum, end date in the account record.

Back-test: 31 churned accounts, $2,460k, placed in the new tiers.
A 2, B 4: a named CSM would have seen 5 of those 6. C 13, D 12.
Missed: 14 accounts ($440k; 5 in C, 9 in D) left after the champion or admin changed
while usage stayed flat (said, exit notes). Usage triggers alone miss 14 of 31.
Fix: add admin-deactivated and champion job-change alerts to C and D before launch.
Review date: 30 Jun 2027, re-run the back-test on first-half churn.

What I could not check
- Real hours per account: these are the CS lead's estimates, not timesheets
- Churn reasons come from exit notes, not interviews
- Whether product can emit an admin-change event by 31 Jan
```
