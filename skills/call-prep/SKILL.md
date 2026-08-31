---
name: call-prep
description: >
  Prepares a customer call around the one thing it has to produce, rather than around what you plan to say. Trigger whenever the user says "call prep", "prep me for", "I have a call with", "meeting in an hour", "what should I ask", "what do I need to know before", "help me prepare for this call", "agenda for", "talking points for", or names a customer and an upcoming meeting in the same breath. Also trigger when they are walking into an account they have just inherited, or a call they are dreading. It names the outcome, works out who is really in the room, surfaces what changed on the customer's side, finds the landmine, writes the questions including the one they are avoiding, and sets the ask and the fallback ask. Use business-review when the meeting is a QBR or EBR, exec-conversation when the senior person is the point of the meeting, and hard-conversation when the job is delivering bad news. Runs on what the user knows and names what it could not check.
---

# Call Prep

Most call prep is reading. You open the account, scan the notes, feel prepared, and walk into a meeting with no outcome attached to it.

Preparation is not the same as reassurance. This skill produces the four things that change how a call goes: the outcome, the room, the questions, and the ask.

The failure this exists to prevent: **the call that goes fine, generates a recap, and moves nothing.** Everyone leaves satisfied, the account is exactly where it was, and the next call has the same agenda.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first. It carries the product, the segments, the contract shapes and what healthy looks like in this business, which is what stops the questions coming out generic. Where it is absent, carry on and name the assumption.

**Minimum: who you are meeting and why.** Even a single line gets you an outcome, a set of questions and an ask. Everything unverified is marked unverified.

**Better with** the last call's notes or recap, recent email history, and the invite with its attendee list. Those three convert most of the guesses into facts.

**Best with** a stakeholder map and the account plan, because then the prep knows who is missing from the room rather than only who is in it.

Nothing here is required. If the call is in ten minutes, skip to **The ten-minute version** at the bottom.

---

## When this runs

Any customer call that is not a set piece: a check-in, a first meeting on an inherited account, a technical working session, a risk conversation, a discovery call inside an existing account.

**Do not run this for:**

- A QBR or EBR. `business-review` owns that meeting, including whether it should happen at all.
- A meeting whose point is a senior person on the customer side. `exec-conversation` has a different structure, because the constraint is fifteen minutes and no context.
- A call whose whole job is delivering bad news. `hard-conversation` scripts the part this skill would skip.

Where the call is a mix, prepare with this skill and read the relevant one for the part it covers.

---

## Step 1: Name the outcome, and make it verifiable

One sentence. What is true after this call that was not true before.

The test is whether you could be wrong about it. "Align on the rollout" cannot be failed, which means it is not an outcome. "Get a named owner and a date for phase two" can be failed by lunchtime.

Write it in the form: **by the end of this call, [named person] has [done or committed to a specific thing].**

If you cannot write that sentence, you have found the most useful thing in this prep. One of three is true:

- **The outcome belongs to a different meeting.** Say so and reshape the call.
- **The outcome needs someone who is not invited.** That is a room problem, not an agenda problem. Go to Step 2 and fix it.
- **There is no outcome.** The call is a cadence being served. The honest options are to cancel it, shorten it, or replace it with an email, and proposing one of those to the customer usually buys credibility rather than spending it. `weekly-plan` treats the hour freed this way as the trade that funds the protected block. A recurring call nobody has an outcome for is a recurring call the customer is looking for a reason to decline.

## Step 2: Work out who is really in the room

Go through the attendee list one name at a time. For each person:

- **What do they want out of this call**, which is rarely what you want
- **What can they actually authorise**, as opposed to influence
- **Have you met them**, or are you assuming a relationship from a shared thread

Then three checks the invite will not do for you:

1. **Who is missing.** If the outcome needs a decision and nobody in the room can make it, the call cannot succeed as scheduled. Fix that before the call, not during it. Ask your contact to bring them, or reset the outcome to something the room can actually deliver.
2. **Who they report to afterwards.** The real audience is often not on the invite. Someone in that room will summarise this call to a person you have never met, in two sentences. Decide what those two sentences should be and make sure they are sayable.
3. **Who is new.** A person attending for the first time changes the call. A new attendee on the customer side is either an evaluation, an escalation, or a handover, and it is worth knowing which before you start.

Where the relationship picture is thin or out of date, `stakeholder-map` does this properly, including who has gone quiet and whether the account is single-threaded.

## Step 3: Find what changed on their side

Prep instinctively rehearses your side: what shipped, what you delivered, what you want. The customer arrives carrying their own quarter.

Look for, and mark each as fact or inference:

- A change in their organisation. New leadership above your contact, a reorg, a layoff, a merger
- A change in their business. Their earnings, their peak season, a public incident, a launch
- A change in their use of the product. New teams on, teams gone quiet, a spike or drop, integrations added or removed
- A change in the commercial picture. A renewal date approaching, an invoice, a procurement or security review opening

If nothing here is knowable, say so plainly and make one of the questions in Step 4 do this job instead. A call that starts with a genuine question about their world is a better opening than a summary of yours.

## Step 4: Find the landmine

Every account has at least one thing the customer is quietly annoyed about. An open ticket with no owner. A commitment that slipped. An email that went unanswered for three weeks. A bill that surprised them.

Name it before the call and decide one of two things:

- **You raise it first**, which costs you two minutes and buys the rest of the call, or
- **You have a straight answer ready** for when they raise it, which they will

There is no third option where it does not come up. The version where you are surprised by it is the version where you spend the call on the back foot and never reach your ask.

If the landmine is large enough to be the meeting, stop preparing this call and read `hard-conversation`.

## Step 5: Write the questions, including the one you are avoiding

**Three questions you will definitely ask.** Open, specific to this account, and answerable by the people in the room. Not "how are things going". Something closer to "when the finance team pulled the report last month, what did they do with it".

The test for a good question here: could the answer change what you do next. If not, it is small talk with a question mark.

**One question you have been avoiding.** Every account has one, and it is usually the same shape: who else are you looking at, is this budget still protected, does your new VP know we exist, are you actually going to use the second module you bought.

Decide now whether you are asking it, because in the moment you will not. If you decide not to, write down what has to be true before you do, and when. An avoided question does not expire, it just gets more expensive.

**Plan to talk less than you want to.** Prepare questions rather than a monologue. The specific trap is arriving with a deck and letting it become the agenda: the deck then dictates the running order, you present through it, and the questions never get asked. If there is material, send it before or bring it as backup, and do not open with it.

## Step 6: Set the ask, and the fallback ask

Every call ends with a request from you. Write both versions.

- **The ask.** What you want, said as a specific request of a named person with a date attached
- **The fallback.** What you will take if they say no, decided in advance so you do not improvise something worthless like "keep me posted"

The close cannot depend on the customer remembering you. Make the next step yours and leave them a yes or no. "Shall I set up fifteen minutes with you and the finance lead on Thursday" is an ask. "Let me know if that would be useful" is not.

## Step 7: Budget the time and decide what gets dropped

Most prep produces more material than the call can hold. A thirty-minute call is really twenty-two after joining, small talk and the overrun at the end.

Allocate the minutes, in order, and mark the point where the ask happens. Put the ask before the material you could send instead, not after.

Then write the cut line: **what you will drop if the call runs short.** Deciding that in advance is what stops the ask being the thing that gets dropped, which is what usually happens.

## Step 8: Prepare for it going sideways

Two lines, no more.

- **If they open with a complaint**, what you say before you have the answer. Usually: acknowledge the specific thing, state what you know and when you will know the rest, and ask for the call to continue
- **If the decider does not show**, whether you run the call anyway and what you downgrade the outcome to

---

## The ten-minute version

When the call is imminent, three things, in this order:

1. **The outcome.** One sentence, verifiable
2. **The landmine.** The thing they are annoyed about, and your first line on it
3. **The ask.** Who you are asking, for what, by when

Everything else is optional. A call with those three is better prepared than a call with an hour of reading behind it.

---

## Output

A prep sheet that fits on one page, in this order:

1. **The outcome**, one sentence, in the form that can be failed
2. **The room**: each attendee, what they want, what they can authorise, whether you have met them, and who is missing
3. **What changed** on their side, with fact and inference marked differently
4. **The landmine**, and your first line on it
5. **The questions**: three to ask, plus the one you are avoiding and your decision on it
6. **The ask and the fallback ask**
7. **The time budget**, with the cut line marked
8. **What you could not check**, named plainly

`assets/prep-sheet.md` is the same structure as a blank template. It is written to be filled in by hand without an assistant involved, and to be pasted back in afterwards so `call-recap` inherits what the call was supposed to produce.

---

## Failure modes

- **Prep as reading.** An hour in the account, no outcome, no ask. It feels like preparation and produces the same call you would have run cold
- **The deck as agenda.** Material prepared before the outcome, then presented in its own order, with the questions never reached
- **Preparing for the invite rather than the decider.** A well-prepared call with the people who cannot say yes
- **The unfalsifiable outcome.** "Align", "touch base on", "walk them through", "build the relationship". None of these can be failed, so none of them get achieved
- **Rehearsing your update.** Preparing what you will report rather than what you will ask. Your side of the account takes four minutes and they can read it
- **No ask.** The single most common defect, and it is invisible because the call still felt good
- **The passive close.** An ask that hands the work back to the customer. This is most tempting with the buyers slowest to reply, which is exactly where it fails
- **Skipping the landmine.** It comes up anyway, at the moment of your choosing or theirs, and theirs is worse
- **Over-preparation on a call that should not happen.** Two hours of prep on a cadence call with no outcome is two hours spent avoiding the decision to cancel it

---

## What good looks like

- The outcome is one sentence and someone else could tell you afterwards whether it happened
- The ask is a specific request of a named person with a date
- At least one question in the set could genuinely change what you do next
- The landmine is named before the call rather than discovered during it
- The prep fits on a page, and the ten-minute version is on the first three lines
- What could not be checked is written down rather than assumed away

---

## Related skills

- `stakeholder-map` for who is really in the room and who has gone quiet
- `business-review` when the meeting is a QBR or EBR
- `exec-conversation` when a senior person on the customer side is the point of the meeting
- `hard-conversation` when the landmine is the meeting
- `call-recap` for afterwards, which reads the prep sheet if you keep it
- `renewal-risk` when the call exists because the account is in question

---

## Supporting files

- `assets/prep-sheet.md` - the one-page template, usable without an assistant
