# Sample output

*Invented example. Vendor "Ledgerline" and customer "Brightwater Clinics" are fictional. Input the user gave: "Brightwater Clinics, $150k, renews 14 May 2027, 60 day notice, auto-renews. I have met the compliance manager but never the CFO who signs. Today is 5 Nov 2026 and I have done nothing formal on this one."*

---

```
RENEWAL RUNWAY: Brightwater Clinics | $150k | renews 14 May 2027 | opt-out 15 Mar 2027

Verdict: Late by 50 days on the first checkpoint. 130 days to opt-out.
Biggest risk to the plan: the CFO who signs has never been met.

| Date        | Checkpoint (defaults)  | Action                                         | Owner         | Pass if                                       |
| 16 Sep 2026 | T-180 (missed)         | Document risk status, name the signer          | CSM           | Risk status written; signer named             |
| 15 Nov 2026 | T-120                  | Meet the CFO, or get the intro request sent    | CSM           | CFO call booked within 3 weeks                |
| 15 Dec 2026 | T-90                   | Value review against the original goal         | CSM + AE      | One page agreed with the compliance manager   |
| 14 Jan 2027 | T-60                   | Commercial position set, exec sponsor engaged  | CSM + Dir     | Renewal terms drafted and approved internally |
| 13 Feb 2027 | T-30                   | Verbal yes, or contraction case on the table   | CSM           | Written intent from the CFO or delegate       |
| 15 Mar 2027 | Opt-out date           | Contract status confirmed in writing           | CSM           | Renewal signed or notice risk cleared         |
| 14 May 2027 | Renewal date           | Term starts                                    | Renewals desk | Order form countersigned                      |

Late: this-week block (by 12 Nov)
1. Write the risk status in the account notes with the unmet signer as the reason (6 Nov)
2. Read the contract and confirm the 60 day notice clause and auto-renew wording (6 Nov)
3. Ask the compliance manager who signs and for an intro (9 Nov)
4. Send a 20 minute meeting request to the CFO, framed around audit response hours (10 Nov)
5. Pull usage and audit-response results for the value page (12 Nov)
Dropped from the full plan: an early QBR. A CFO call matters more.

Checkpoint: "If the CFO call is not booked by 15 Nov, my director sends the request
at executive level and I prepare a contraction case for 14 Jan."

What I could not check
- Notice clause text (60 days is the user's recollection, confirm)
- Brightwater's budget planning window, which may close before 15 Dec
- Whether the CFO is the final signer (assumed, confirm)
