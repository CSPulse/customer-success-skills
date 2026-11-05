# Sample output

*Invented example. Vendor "Ledgerline" and every customer named here are fictional. Input the user gave: "We are retiring the legacy CSV export API on 31 Jan 2027, replaced by the new Reports API. About 140 customers, 9 of them call the old endpoint daily. Contracts need 60 days written notice for removing a feature. Can you draft the notice?"*

---

```
SEND PLAN: Retiring the CSV export API | stops 31 Jan 2027 | 140 customers

Segments
- Materially affected (9): daily callers of the old endpoint. A named CSM
  calls each by Fri 13 Nov, before any broadcast. Engineer on the call.
- Affected, no action (about 45, assumed, confirm): use the export button in
  the app, which moves automatically. One line, no migration steps.
- Not affected (about 86, assumed, confirm): do not write. Add to the
  release notes only.

Notice date check: 60 days before 31 Jan is 2 Dec 2026. Send the written
notice by Mon 16 Nov to leave margin (assumed, confirm with legal).

Subject: Legacy CSV export API ends 31 Jan 2027 - migration guide inside

Hi [first name],

On 31 January 2027 we are retiring the legacy CSV export API
(/v1/export). It is replaced by the Reports API, which returns the same
data in the same columns.

If you call /v1/export from a script or integration, you need to switch
before 31 January. We expect the change to take one to three days of
developer time (assumed, confirm with engineering). If you only export
from the Ledgerline app, no action is needed from you.

What we are doing to help:
- Migration guide with side-by-side examples: [link]
- A sandbox key so you can test before cutover: reply to this message
- Free migration help from our engineers until 31 Jan

What does not change: your data, your column names, and your pricing.

Questions go to exports-help@[domain]; a person replies within one
business day.

Confirmed: stop date 31 Jan 2027; Reports API is live today.
Expected: sandbox keys ready by 24 Nov.
Next update: reminder to remaining callers on Mon 11 Jan, only if our
logs still show calls to the old endpoint.

Reply plan: owner Priya (support lead), window one business day.
Expected questions
- Can we get an extension? Pre-decide: one 60 day extension for named
  accounts that ask by 15 Dec, approved by the VP, not offered in the
  broadcast.
- Are the rate limits the same? (assumed, confirm: Reports API limit is
  higher)
- Will old files still download? Confirm with engineering before sending.

What I could not check
- Exact counts for the two lower segments
- Whether any contract grants a longer notice than 60 days
- Engineering's migration effort estimate
- Whether the Reports API rate limits match the old endpoint
```
