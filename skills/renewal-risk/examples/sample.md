# Sample output

*Invented example. Vendor "Ledgerline" and customer "Marlowe Freight" are fictional. Input the user gave: "Marlowe Freight, $180k ARR, renews 14 March, 60 day notice, my champion is Priya in compliance, usage looks fine, but she mentioned a new CFO."*

---

```
RENEWAL READ: Marlowe Freight | $180k | renews 14 Mar | opt-out by 13 Jan

Call: CONTRACT
Dollars: $110k to $180k, expected $135k   Confidence: medium

Decider: new CFO (name unknown), approves anything over $100k. Met: no.
Mechanism: The new CFO inherited a cost-out target and is reviewing every
vendor over $100k. Priya, our only active contact, runs the tool but does
not control the budget. If the CFO sees Ledgerline as compliance overhead
rather than a revenue protector, the likely outcome is a smaller tier, not
a replacement.

Evidence
- said    Priya: "the new CFO started in October" (call, 4 Nov)
- seen    Zero new seats provisioned since June (admin console)
- seen    Priya asked for a seat utilization export on 28 Oct
- inferred The utilization request is the CFO's team preparing for a
           negotiation, not routine admin
- seen    Usage is flat and steady, which is normal for audit tooling here

What would make me wrong
- Priya's export may be for an internal audit. Ask her what it is for.
- Flat usage plus a recent security re-review would also fit a routine
  governance cycle.

Play: Get 30 minutes with the CFO before 12 Dec, with Priya's sponsorship,
      framed around audit cost avoided, not product features.
Owner: me | By: 12 Dec
Need from my side: exec sponsor for one call, authority to hold price flat
                   for a 24 month term
Checkpoint: "If I have not met the CFO by 12 Dec, my director asks for the
             meeting at their level and I prepare the contraction case."

What I could not check
- Who else sits on the CFO's review panel
- Whether the original business case metric (audit response hours) was
  ever baselined for this account
```
