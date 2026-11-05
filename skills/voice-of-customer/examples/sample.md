# Sample output

*Invented example. Vendor "Brightlane" and every customer below are fictional. Input the user gave: "October notes from 8 accounts are below (6 call summaries, 5 email threads, 3 tickets). ARR: Northgate Freight 140k, Vantor Retail 120k (our reference account), Oakmere Foods 85k, Sundial Labs 71k, Harbor & Pine 62k, Wrenfield Clinics 56k, Quillfield Dental 48k, Pellman Logistics 38k. Product sync is Thursday 12 Nov."*

---

```
VOICE OF THE CUSTOMER: October 2026 | 8 accounts, $620k ARR read | 14 sources, 16 items
Headline: Scheduled exports lead on reach (3 accounts, $296k), but the invoice
double-posting bug is the one to fix first because it puts wrong money in
customers' books.

| # | Theme                          | Type             | Accounts | ARR   | Share of ARR read | Mentions |
| 1 | Scheduled exports to a drive   | Gap              | 3        | $296k | 48%               | 5        |
| 2 | Invoices posted twice by sync  | Bug              | 3        | $142k | 23%               | 7        |
| 3 | Bulk edit cannot be found      | Misunderstanding | 2        | $182k | 29%               | 3        |
(Ranked by accounts, then ARR. Shares overlap in no account, so 48 + 23 + 29 = 100%.)

Scheduled exports - gap - owner: product
Asked: a weekly CSV by email.   Need: the Monday finance close should not wait
on one person logging in (said by Northgate, inferred for the other two).
"Every Monday somebody on my team exports the same report by hand."
 - Northgate Freight, ops director, call 6 Oct
"Can the weekly summary drop into our shared drive instead of our inbox?"
 - Oakmere Foods, finance manager, email 14 Oct
Ask: size a recurring export with a drive destination, not email only.

Invoices posted twice - bug - owner: engineering
Asked: fix the duplicates.   Need: ledgers they can trust without checking
every line (said).
"I do not trust the sync anymore, I check every line."
 - Quillfield Dental, office manager, call 15 Oct
"Our auditor will ask why there are duplicates."
 - Wrenfield Clinics, finance lead, email 27 Oct
Cause: Pellman's ticket says it happens after the sync errors out (inferred
retry defect, engineering to confirm). Pellman filed 4 of the 7 mentions but
is one account, the smallest at $38k.
Ask: severity above a normal bug and a customer-safe workaround by Tue 10 Nov.

Bulk edit cannot be found - misunderstanding - owner: enablement
Asked: change many records at once.   Need: 300 row cleanup without an hour of
clicking (said by Harbor & Pine).
"I have 300 rows to change one at a time."
 - Harbor & Pine, ops lead, call 8 Oct
Ask: none for product. I will confirm with product where bulk edit lives (the
user to confirm it exists) and send the steps.

Flags: Vantor Retail ($120k, reference account) is in theme 3, so a personal
answer this week matters more than the ARR share suggests. Nobody here renews
inside 90 days (assumed, confirm against the renewal calendar).
Loop to close
- Theme 3: Harbor & Pine, Vantor - it exists, send steps - by Fri 6 Nov
- Theme 2: Pellman, Quillfield, Wrenfield - acknowledged, workaround, next
  update date - by Tue 10 Nov
- Theme 1: Northgate, Oakmere, Sundial - logged with three customers behind
  it, no date yet (a not-yet, said plainly) - by Fri 20 Nov, after the sync
Praise worth passing on: "Support fixed our login problem in an hour." -
Vantor Retail, admin, call 22 Oct. For the support lead, not product.

What I could not check
- Only 8 accounts were pasted; accounts with no notes are silent, not happy
- All voices are admins, finance and ops leads, with no end users
- Whether the three duplicate reports are one defect (cause is inferred)
- Renewal dates, so the 90 day flag is assumed clear
```
