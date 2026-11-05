---
name: handoff
description: >
  Use when the user says "handoff", "I am leaving this account", "hand over my accounts", "I just inherited this account", "taking over the account", "get me up to speed on this account". Two modes: OUTGOING forces out the four things that never reach a system, the open promises and the last five threads; INCOMING marks every claim documented, reported or folklore, then sets a first 14 days plan and a 30 day check. Not for the message to the customer (use customer-update) or a customer who is leaving (use offboarding).
---

# Handoff

A handover the receiver can run the account from: either the sender's brain emptied onto one page, or an inherited account audited down to what is actually known.

## Start here

Pick the mode from the user's words (leaving = OUTGOING, inherited = INCOMING). If the user gave the account, both names and the renewal date, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Account, ARR, renewal date, notice period, and which mode
2. Who is leaving and who is receiving, and the sender's last day
3. Whatever exists: CRM notes, the contract, recent emails or meeting notes

If an "Account context" block exists in the conversation, use it. Anything missing is marked "(assumed, confirm)" and listed at the end.

## Do this

1. **Set the clock.** Opt-out date = renewal date minus notice period. The handoff date is before the sender's last week, not on it. A common default: internal sync within about 2 business days of the decision, customer intro within about 5. Set your own.
2. **OUTGOING: force out the four.** (a) What was promised that is not in the contract, and who said it. (b) Who the sceptic is. (c) What nearly went wrong and what fixed it. (d) What the sender would do first if staying. Press once on "nothing".
3. **OUTGOING: list open promises and the last five threads and meetings.** Each promise: what, to whom, due date. Each thread: date, with whom, where it stands.
4. **OUTGOING: the receiver decides when it is done.** The receiver confirms they can answer questions without opening anything. Unanswered questions go back as open items.
5. **INCOMING: find the original promise** (business case, order form, email near signature) and quote it with source and date. If none exists, write "not documented" as the headline finding.
6. **INCOMING: mark every claim handed over** as `documented` (written, point at it), `reported` (a named person who was there, recently) or `folklore` (no source, or the source left). Treat folklore as a question, never as a fact.
7. **INCOMING: plan the first 14 days, then the 30 day check.** Days 1 to 3 internal questions to whoever sold or ran it. Days 4 to 10 read the record and meet the signer. Days 11 to 14 first customer call. At day 30 ask the customer: "what were you promised, and what is still missing?"

The customer-facing message is a separate job. Name what carries over, never let them find out from an auto-reply.

## Output

Use this skeleton. Keep it under two pages. The fillable checklist is `assets/handoff-checklist.md` (24 fields).

```
HANDOFF: [Account] | [ARR] | renews [date] | opt-out by [date] | OUTGOING / INCOMING

Verdict: [ready to hand over / not ready: n gaps] or [what this account really is]
Handoff by: [date] | Live session: [date] | Customer intro by: [date]

OUTGOING
Four that never reach a system: promised / sceptic / near miss / first move
Open promises: [what | to whom | due]
Last five threads and meetings: [date | with | where it stands]

INCOMING
Original promise: "[quote]" - [source, date]  (or: not documented)
Claims: [claim | documented / reported / folklore | source, date]
First 14 days: [day range | action | owner]
30 day check: [date] - the question to ask the customer

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`.

## Rules

- **The receiver declares it complete.** The sender cannot judge whether the receiver can run the account and is inclined to say yes.
- **An undocumented promise is the renewal's real scorecard.** A roadmap remark made in the deal is rarely in the CRM and is what the customer will measure you against.
- **The sceptic is never in the CRM.** Not knowing who they are means the first meeting has unexplained resistance in it.
- **Folklore shapes the approach before anyone is met.** Unsourced "difficult customer" stories cause months of avoidance, so verify or drop them.
- **A new executive above the contact is the biggest find.** They are reviewing what their predecessor bought, and you are on the list.
- **Access without context is a trap.** The receiver can log in and cannot answer a question, so list what carried over and what did not.
- **Do not hand over mid-escalation or inside a renewal window if the date can move.** If it cannot, do it live with the sender on the call.
- **Do not pretend in the first meeting.** The customer knows their own history and can tell, so ask questions instead.

## Related (only if installed)

`customer-update` for the message to the customer. `stakeholder-map` when the people picture needs depth. `renewal-risk` once the history is understood.
