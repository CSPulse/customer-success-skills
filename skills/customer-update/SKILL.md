---
name: customer-update
description: >
  Writes the proactive message nobody wants to send: an incident, a delay, a deprecation, a price change, planned maintenance, or a change of CSM. Trigger whenever the user says "customer update", "notify customers", "we need to tell them", "announcement to customers", "we are deprecating", "end of life", "maintenance window", "outage notice", "I am handing over my accounts", "changing CSM", "tell them about the delay", or describes news that has to reach a list of customers rather than one person. It segments by impact rather than by mailing list, leads with what changes for them, says plainly whether action is needed, and writes to survive a forward to their executive and their legal team. Use hard-conversation when the news is going to one account by voice, escalation when something is already on fire, and email-critic once a draft exists.
---

# Customer Update

A customer update is not an email to a person. It goes to a list, it gets forwarded to people who were never on the list, and it is read in eleven seconds by someone with no context who wants to know one thing: **does this affect me, and do I have to do anything.**

Answer that in the first two lines or the rest is not read.

The failure this exists to prevent: **the update written from your side of the glass.** A paragraph about your infrastructure, your roadmap process or your team change, with the thing that actually affects them somewhere in the middle, unmarked.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first: the segments and the contract shapes. Those decide who gets which version. Where it is absent, carry on and name the assumption.

**Minimum: what is changing, when, and who it touches.** Enough for the segmentation, the subject line and the draft.

**Better with** the account list with contract and usage detail, so impact can be assessed rather than assumed, and any legal or security obligation attached to the notice.

**Best with** a prior update of the same type that went well or badly, because the format matters more than the wording and yours may already be set.

---

## Step 1: Decide whether this is one message or several

The most consequential decision and the one made least deliberately.

**Segment by impact, never by mailing list.** If five per cent of the list is badly affected and ninety-five per cent barely is, one message does both jobs badly: it buries the five per cent in general reassurance and alarms the ninety-five per cent about something that does not concern them.

Sort the list into:

- **Materially affected**, who need specifics, a named contact and probably a call before the notice
- **Affected in a way that needs no action**, who need one clear line saying exactly that
- **Not affected**, who should usually not be written to at all

Then decide the channel per group. **Named accounts in the first group get a person, not a broadcast**, and they get it before the general notice goes out. A large customer learning about a deprecation from a mass email is a preventable escalation.

`references/by-update-type.md` covers how the six common types differ.

## Step 2: Write the subject line first, and make it the news

Most of the value sits here, because a large share of recipients read nothing else.

- **Say the thing.** "Scheduled maintenance, 12 March, 30 minutes" beats "An important update about your service"
- **Never use urgency the content does not carry.** "Important" and "Action required" on something that needs no action costs you the next one
- **Include the date where there is one.** People triage on dates
- If action is genuinely required, say so in the subject, and only then

## Step 3: Lead with what changes for them

First line: what is changing and when, in their terms.

Second line: what it means for them.

Third line: what they need to do, or that they need to do nothing.

**"No action is needed from you" is a load-bearing sentence.** Write it explicitly whenever it is true. Its absence is read as an ask, and an unclear ask generates support tickets from people trying to work out whether they are safe.

Then the detail, then the contact, then the timeline. Background and cause come last if at all. Nobody has ever forwarded an update because it explained the vendor's internal process well.

## Step 4: Say what you know, mark what you do not

Where facts are still moving, split them plainly: what is confirmed, what is expected, and when the next update comes.

**Never publish a cause before it is established.** A speculated cause in a written notice is quoted back at you when the real one turns out different, and unlike a conversation it is a document.

**A dated next update is a commitment.** Only put a date in if you will send something on that date, including when nothing has changed. Missing a self-imposed update date does more damage than the original problem, because it is the one part of this that was entirely within your control.

## Step 5: Write it to survive a forward

Assume every update reaches an executive who has never heard of you, a security or procurement team, and occasionally a lawyer.

- **No internal shorthand.** No product tier names, no sprint or release vocabulary, no service names only your engineers use
- **No blame**, directed at a team, a vendor or a customer
- **No liability language** where money or data is involved, and where either is, someone with commercial authority reads it before it goes
- **A single topic.** Two announcements in one message means one of them is missed, and it will be the one you cared about

## Step 6: Handle the change of CSM properly, because it is not an announcement

The most commonly botched update in customer success, and it is a relationship event wearing the clothes of an admin notice.

To the customer it reads as one of three things: you are being downgraded, your account is not important, or the person who understood you has gone. Left to a mass email or an auto-reply, it reads as all three.

- **Tell named accounts personally, before anything general goes out.** Ideally the outgoing CSM says it, which is the version that does not read as abandonment
- **Introduce a person, not a role.** A name, and one specific thing about them relevant to this account
- **Say what carries over**, concretely. The open items, the commitments, the history. This is the actual fear
- **Overlap where you can.** One joint call beats any written handover
- **Never let them find out from an auto-reply or a bounced email.** That is the version that gets remembered

## Step 7: Decide who answers the replies

An update generates replies, and an unanswered one is worse than no update.

Name the owner, set the window, and prepare the two or three answers you know are coming. Where the update goes to a list, brief support before it sends rather than after.

---

## Output

1. **The segmentation**: materially affected, affected but no action, not affected, with the channel for each
2. **The named accounts** getting a personal message first, and who sends it
3. **The subject line**, carrying the news
4. **The update itself**, leading with what changes for them and stating plainly whether action is needed
5. **Confirmed against expected**, with the next update date if one is promised
6. **The reply plan**: owner, window, and the anticipated questions
7. **What you could not check**

---

## Failure modes

- **One message to the whole list.** Buries the badly affected, alarms the unaffected
- **Written from your side of the glass.** Your process, your roadmap, your reorganisation, with their impact somewhere in the middle
- **A subject line that hides the news.** "An important update about your service" is triaged as marketing
- **Omitting "no action needed"** when it is true, which converts a notice into an ask and generates tickets
- **Publishing a cause before it is established**, in writing, where it becomes a document
- **Promising a next update and missing it.** The one part that was entirely within your control
- **Two announcements in one message.** One of them is missed
- **Urgency the content does not carry.** It works once
- **A CSM change sent as a mass email**, or discovered from an auto-reply
- **Nobody owning the replies**, so an update that went well becomes silence in a thread

---

## What good looks like

- Someone reading only the subject line and first two lines knows whether it affects them and whether to act
- The badly affected heard from a person before the notice went out
- "No action is needed" appears where it is true
- No cause is asserted that is not established
- It reads sensibly to someone forwarded it with no context
- Every promised update date was met, including the ones with nothing new
- The replies had an owner before it sent

---

## Related skills

- `hard-conversation` when the news goes to one account and should be spoken before it is written
- `escalation` when something is already on fire and the update is part of an incident
- `email-critic` on the draft before it goes
- `one-pager` when the update needs a forwardable summary attached
- `offboarding` for the wind-down notices at the end of a term

---

## Supporting files

- `references/by-update-type.md` - how incident, delay, deprecation, pricing, maintenance and CSM-change updates differ
