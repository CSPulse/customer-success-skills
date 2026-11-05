---
name: call-prep
description: >
  Use when the user says "prep me for my call with", "call prep", "I have a call in an hour", "what should I ask them", "talking points for", "walking into this call cold". Produces a one-page prep sheet that opens with the 10-minute version (outcome, landmine, ask), then the fuller sheet if time allows. Not for a QBR (use business-review), a senior-executive meeting (use exec-conversation) or delivering bad news (use hard-conversation).
---

# Call Prep

A prep sheet the user can read in two minutes: what the call must produce, what will derail it, and what to ask for.

## Start here

If the user said who the call is with and why it exists, go. If the call is under 15 minutes away, produce only the 10-minute version.

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Who is on the call (names, roles) and what the user last heard from them
2. What the user wants out of it
3. Length of the call and time left to prepare

If an "Account context" block exists in the conversation, use it. Anything pasted (last recap, emails, invite) is a bonus.

## Do this

1. **Write the 10-minute version first, always.** Outcome, landmine, ask. This is the default output and the top of the page.
2. **Make the outcome failable:** "By the end of this call, [named person] has [committed to a specific thing]." If it cannot be written, say which it is: it belongs to another meeting, it needs someone not invited, or there is no outcome and the call should be shortened, cancelled or replaced by an email.
3. **Work the room.** For each attendee: what they want, what they can authorize, met or assumed. Name who is missing and who will retell this call to someone else, and what those two sentences should be.
4. **Find what changed on their side** (org, business, product use, commercial). Tag each `said`, `seen` or `inferred`.
5. **Name the landmine** (the thing they are quietly annoyed about) and decide: raise it first, or have a straight answer ready.
6. **Write three questions** whose answers could change what the user does next, plus the one being avoided and a decision on it.
7. **Set the ask, the fallback ask, the time budget and the cut line.** Add two lines for a complaint opener and for the decider not showing up.

## Output

```
CALL PREP: [Account] | [date, length] | [attendees]

10-minute version
Outcome: By the end of this call, [name] has [specific commitment].
Landmine: [thing] | First line: "[words]"
Ask: [named person] to [request] by [date]. Fallback: [what to accept]

Room
- [Name, role] | wants [x] | can authorize [y] | met / assumed
Missing: [who]. Will retell this to: [who] as "[two sentences]"

What changed on their side
- [said / seen / inferred] [fact]

Questions
1. / 2. / 3.
Avoiding: [question] | Ask now / Not yet, because [condition] by [date]

Time ([n] min, about [n-8] usable)
[minutes: block] ... Ask lands at minute [x]. Cut line: drop [y] first.

If it goes sideways
- Complaint first: [line]
- Decider absent: run it, outcome becomes [x]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its length and tone.

## Rules

- **No ask, no call.** A call that feels good and asks for nothing produces a recap and no movement, because the customer will not remember to act on their own.
- **"Align", "touch base" and "walk them through" are not outcomes.** They cannot be failed, so they are never achieved.
- **Name the landmine.** It comes up either way, and the version where the user is surprised by it is spent on the back foot, with the ask never reached.
- **Prepare questions, not a deck.** A deck dictates the running order and the questions never get asked. Send material before, or keep it as backup.
- **Budget for about 70 percent of the clock.** Joining, small talk and overrun eat the rest, so the ask goes before anything that could be sent by email.
- **Close with a yes or no, not "let me know".** The customer takes the next step only if it is easy to take.
- **A recurring call with no outcome is a call they are looking for a reason to decline.** Proposing to cancel or shorten it usually buys credibility.
- **Never invent attendee wants.** Mark them `inferred` and ask the champion to confirm, because a wrong guess shapes every question.

## Related (only if installed)

`stakeholder-map` when the room is unclear. `call-recap` afterwards. `renewal-risk` when the call exists because the account is in question.
