# Sample output

*Invented example. Vendor "Tallyfern" and customer "Greywell Insurance Group" are fictional. Input the user gave: "Greywell Insurance Group, $96k, 120 seats, only 31 active in the last 30 days (any case action). Renews 31 Jan, 60 day notice, champion is Tomas in claims ops. Per-team export: Claims-North 24 of 40, Claims-South 3 of 30, Underwriting 4 of 30, Service 0 of 20."*

---

```
ADOPTION READ: Greywell Insurance Group | $96k | renews 31 Jan 2027 | opt-out by Wed 2 Dec

Call: PARTLY FIXABLE
Shape: 31 of 120 seats took a case action in the 30 days to 4 Nov (26 percent).
Breadth: 2 of 4 teams have real use. Depth: not in the export (assumed, confirm).
Cause: one team only (Claims-South never started), then wrong people licensed
(Service) and a likely fit gap (Underwriting).

Evidence
- seen     Claims-North 24 of 40 active. Claims-South 3 of 30. Underwriting 4 of
           30. Service 0 of 20 (team export, 4 Nov)
- said     Tomas: "South's team lead left in August and nobody picked up the
           rollout" (call, 28 Oct)
- said     Tomas: "Service was a maybe when we signed, nobody scoped it" (28 Oct)
- said     Ines Varga, underwriting lead: "no referral-reason field, so we
           keep the old sheet" (email, 12 Oct)
- inferred South does the same work as North, which runs the tool, so the stall
           is a missing owner, not resistance
- inferred Underwriting's 4 users are a fit signal, not a training gap

Cohort to move first: Claims-South, 30 seats, 3 active. Same job as North, the
blocker is a vacant owner and no data loaded. Fastest to show a result.
Success test: "In the week of 23 Nov, at least 20 of 30 South handlers each work
5 or more claim files in Tallyfern."

30 days (start Mon 9 Nov)
| Week | Action | Ours | Theirs | Ask of customer |
| 9 to 13 Nov | Name a South owner. Load South's open files | me, support import by Fri 13 | Tomas names owner by Tue 10 | 30 minutes with the owner by Wed 11 |
| 16 to 20 Nov | Two 60 minute sessions on South's own live files, led by two North power users | me | owner releases all 30 handlers | Handlers released by Fri 20 |
| 23 to 27 Nov | Counting week. I post the daily count to the owner | me | owner runs a 10 minute check | Old tracker closed to new claims from Mon 23 |
| 30 Nov | Read the count, decide seats | me | Tomas | Seat call by Wed 2 Dec |
Exit test: Mon 30 Nov. Pass = 20 or more of 30. Partial = 10 to 19: hold South's
seats only if Tomas confirms a dated cutover in writing by Wed 2 Dec. Fail =
fewer than 10: size South to what is used.

Seat position (assumed, confirm): on a pass about 48 are active (24 + 20 + 4).
Add a quarter for headroom (a common default) and that is 60 seats, $48k, against
$96k today at $800 a seat. I raise it myself on the Thu 12 Nov call and reduce
at renewal, not mid-term. The price decision is my director's.
Fallback if the cause is fit: Underwriting. Do not train. Log the missing
referral-reason field with product in Ines's words by Fri 13 Nov and ask for a
yes or no with a date by Fri 20 Nov. No date: size Underwriting at 5 seats and
say why. Service: release the 20 seats at renewal unless Tomas scopes a use.

What I could not check
- Whether "case action" counts reading a case or only editing one
- What this period looked like last year (claims seasonality)
- Whether the South vacancy is already filled
- Who signs the renewal (Tomas is the champion, not confirmed as the signer)
- Whether the contract allows a seat reduction before renewal
```
