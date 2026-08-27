---
name: escalation
description: >
  Runs the first four hours of an account on fire: what to say before you know the answer, who to pull in, and what the customer actually wants, which is often not the fix. Trigger whenever the user says "escalation", "the account is escalating", "their VP is involved", "this has gone to their exec", "angry customer", "they are threatening to churn", "account on fire", "major incident with a customer", "they want a call today", "I need to escalate this internally", or describes a customer situation that has just moved above their usual contact. It separates the incident from the relationship damage, sets one owner and one cadence, decides who to pull in and when, and plans the repair step most teams skip. Use hard-conversation when you are the one delivering bad news that has not landed yet, and churn-postmortem when the account has already gone.
---

# Escalation

An escalation is not a big complaint. It is the moment the problem moved above the line where you normally operate, on their side or yours, and from then on you are managing two separate things: the incident, and what the incident did to the relationship.

Fixing the first does not fix the second, and the accounts that churn six months after a resolved incident are the ones where nobody worked on the second.

The failure this exists to prevent: **going quiet until you have the answer.** The silence is read as chaos or concealment, and both are worse than an update with nothing in it.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first, particularly what customer success can commit to without asking, which decides how much of the first hour you can hold alone. Where it is absent, carry on and name the assumption.

**Minimum: what happened and who is angry.** Enough for the holding response, the owner, the cadence and the pull-in decision.

**Better with** the support and incident record, the contract, and a current stakeholder map. The last one tells you whether the person escalating can actually end the relationship.

**Best with** a risk read already in hand, because it tells you whether this is an incident on a healthy account or the visible part of something older.

---

## Step 1: Establish what kind of escalation this is

Three kinds, and they need different things. Get this wrong and everything after it is wasted motion.

- **A failure escalation.** Something broke, or did not happen. The customer wants it fixed and wants to know it will not repeat
- **A relationship escalation.** Nothing is broken today. Accumulated frustration has found a trigger. The fix will not touch the cause, and treating it as a failure escalation makes it worse
- **A commercial escalation.** The heat is real but the destination is a negotiation. It appears near renewals and near budget cycles. Handle the substance honestly, and know what it is

Ask the question that separates them: **what specifically has to be true for this to be resolved?** A crisp technical answer means the first. A vague answer, or a list, means the second. An answer about terms means the third.

## Step 2: Respond before you have the answer

Within the first hour, and it does not require knowing anything yet.

The shape:

1. **Acknowledge the specific impact**, in their terms. Not "we understand your frustration". "This stopped your team invoicing for two days at month end"
2. **Say what you know and what you do not**, plainly
3. **Name the owner.** A person, not a team
4. **Give the next update time**, and make it soon and specific

That is the whole message. Do not attach a theory of the cause, do not attach an apology for something you have not established, and do not attach a fix date you cannot hold.

**Then hold the cadence even when there is nothing new.** "No change, next update at four" is worth sending. The gap between updates is where the customer decides how seriously you are taking it, and they fill silence with the worst available explanation.

`assets/escalation-log.md` carries the holding statement structure and the running log.

## Step 3: Find out what they actually want

Usually not the fix, or not only the fix. Ask directly, because the answer changes the plan and people guess it wrong:

- **To be heard**, when the same thing has been raised before and nothing changed. Then the fix without the acknowledgement lands as dismissal
- **Something to tell their own boss.** They have been escalated to, and they need a defensible answer by a specific time. Give them that, in writing, in a form they can forward
- **A guarantee it will not repeat**, which is usually about their own exposure rather than about your product
- **Compensation**, which is legitimate and is a commercial conversation, not a service one
- **An exit**, occasionally. Worth knowing early

**The forwardable answer is the most commonly missed.** Your contact is frequently not angry with you. They are exposed in front of someone else and need cover. Producing that document is often the single most useful thing available, and it costs nothing.

## Step 4: One owner, one channel

The second failure mode, after silence, is three people from your side responding in parallel with slightly different versions.

- **One named owner** on your side who sends everything customer-facing. Everyone else feeds them
- **One channel.** If it is running in email and a call and a shared channel at once, consolidate and say so
- **One version of the facts**, written down internally, updated as it changes, so that everyone quoting it quotes the same thing

## Step 5: Decide who to pull in, and when

Pulling your executive in is a card you hold once. Spend it too early and you have nothing left when it gets worse; too late and it reads as reluctance.

Pull in an executive when:

- Their executive is already involved, and the levels should match
- What the customer needs committing is above your authority, and waiting would take days
- The relationship rather than the incident is the problem, and the message is that this account matters

Do not pull one in to demonstrate urgency. An unbriefed executive on an escalation call makes commitments you then have to unpick, which is worse than not having them there.

**Brief whoever you pull in properly:** the facts, what is unknown, what has been committed, what must not be promised, and what the customer actually wants from Step 3.

**Internally, escalate in a different register.** Your engineering and leadership teams need the business impact, the revenue at stake, what you have committed and what you need, not the emotional temperature. `hard-conversation` covers the customer-facing version of bad news; the internal ask is a separate message and usually a shorter one.

## Step 6: Separate the fix from the repair

The incident closes. The relationship does not close with it, and this is the step almost everyone skips because the pressure comes off.

Once the immediate thing is resolved:

- **Say what happened and what changes**, in writing, once the cause is actually known rather than suspected
- **Ask what it cost them.** Most people avoid this because the answer might be expensive. Ask anyway. It tells you whether this was an inconvenience or a broken plan with their own executive attached, and those are different accounts from that day forward
- **Do the repair deliberately.** A specific commitment, met visibly, inside a short window. Not a gesture. Something they asked for
- **Re-multithread.** An escalation surfaces people you have never met, often including the person who actually decides. That is the one genuinely useful by-product, and `stakeholder-map` is where it lands
- **Record it.** This is an input to the renewal read and, if it comes to it, to `churn-postmortem`

Watch for the account that goes quiet and cooperative immediately after resolution. That is frequently not relief.

---

## Output

1. **Which kind of escalation** this is, and the evidence
2. **The holding statement**, written out, ready to send
3. **What they actually want**, from Step 3, marked as asked or assumed
4. **The owner, the channel and the update cadence**
5. **The pull-in decision**: who, when, and their brief
6. **The internal ask**, in business terms
7. **The repair plan**, with a specific commitment and a date
8. **What you could not check**

---

## Failure modes

- **Going quiet until you have the answer.** The silence is read as chaos or concealment
- **Treating a relationship escalation as a failure escalation.** The fix arrives, the cause is untouched, and the account leaves later looking unrelated
- **Speculating on cause under pressure.** The theory gets quoted back when the real cause turns out different
- **Three responders, three versions.** Every inconsistency is read as evasion
- **Burning the executive card early**, or sending an unbriefed one who commits something unpickable
- **Missing the forwardable answer.** Your contact needs cover in front of their own boss more often than they need a fix today
- **A fix date you cannot hold**, offered to make the first call end
- **Declaring it resolved when the ticket closes.** The relationship damage has its own timeline
- **Skipping the repair step** because the pressure came off
- **Reading post-resolution quiet as relief.** Sometimes it is the decision being made elsewhere

---

## What good looks like

- Something specific and true was said inside the first hour, before anything was known
- The cadence held even when there was nothing new
- One person sent everything, and the facts never varied between messages
- What they actually wanted was asked, not assumed
- The person who was exposed in front of their own boss got something they could forward
- A repair commitment was made, met and visible
- Someone new was met, and the map is better than it was
- Nobody promised a cause before it was known

---

## Related skills

- `hard-conversation` when you are delivering the bad news rather than reacting to it
- `stakeholder-map` for the people an escalation surfaces, including the ones you had never met
- `renewal-risk` afterwards, because a resolved escalation still moves the read
- `exec-conversation` when their executive is in the room
- `churn-postmortem` if it did not hold

---

## Supporting files

- `assets/escalation-log.md` - the holding statement and the running log, usable without an assistant
