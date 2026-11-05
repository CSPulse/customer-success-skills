# Sample output

*Invented example. Vendor "Fernhook" and customer "Cobalt Harbor Foods" are fictional. Input the user gave: "Cobalt Harbor's invoice sync has been failing silently since Monday, 212 invoices did not post, and it is month end. Their VP Finance, Lena Marsh, emailed our CEO this morning. My contact is Omar Reyes, AP manager, and he is the one who has to answer to her. $84k ARR, renews 28 Feb."*

---

```
ESCALATION: Cobalt Harbor Foods | failure, with relationship risk | Severity S1: update every 2 hours until all 212 invoices are posted and Omar confirms

1. HOLDING STATEMENT (send within the hour, from me to Omar, copy Lena)
Omar, since Monday 2 Nov, 212 of your invoices have not posted, which has
held up your month-end payments and close. That is on us. What we know: the
sync stopped without raising an alert. What we do not know yet: why, and
whether any invoice posted twice. Priya Nand on our engineering team owns
this and I am your single contact. Next update at 14:00 today, whether or
not there is news.

2. FORWARDABLE ANSWER for Lena Marsh (Omar can send as is)
Subject: Invoice posting delay, status at 12:00 Thu 5 Nov
Between Mon 2 Nov and Wed 4 Nov, 212 invoices from Fernhook's sync did not
post to your ledger. No data was lost (assumed, confirm); the invoices are queued. Today we are
reposting them in batches, starting with the 61 over $10,000, and checking
each against your ledger. Owner: Priya Nand. Next update 14:00, then every
two hours until all 212 are confirmed posted. Root cause will follow in
writing by Fri 6 Nov (assumed, confirm with engineering).

3. INTERNAL ASK to our VP Engineering and our CEO
Cobalt Harbor ($84k ARR, renews 28 Feb) has 212 unposted invoices at month
end and their VP Finance has written to our CEO. We have committed: an owner,
2 hour updates, and a root cause by Fri 6 Nov. I need today: a named
engineer full time until reposted, a yes or no on whether any invoice was
duplicated, and 15 minutes from our CEO to call Lena by 17:00.
Pull in: CEO, after the 14:00 update, because Lena has already gone above
Omar. Brief: facts above / cause and duplicates unknown / committed: owner,
cadence, root cause Friday / must not promise: a cause, a credit, a date for
full prevention / Omar wants cover to give Lena before 16:00.

4. OWNER AND CHANNEL
Owner: me. Channel: one email thread with Omar and Lena. Facts live in a
shared note updated by Priya every hour.

5. REPAIR PLAN (second pass, after the 212 are posted)
- Root cause in writing by Fri 6 Nov, with the alert gap and the fix.
- Ask Omar what it cost: late payment fees, overtime, Lena's board report.
- Repair commitment: a sync health alert to Omar's inbox, live by Fri 13 Nov.
- New people met: Lena Marsh (decides renewal). Book 20 minutes by 20 Nov.
- If this is the second incident this year, she gets an executive sponsor.

What I could not check
- Whether Lena or Omar signs the renewal (assumed Lena, confirm)
- Whether any invoice posted twice
- Whether this has happened before on this account
```
