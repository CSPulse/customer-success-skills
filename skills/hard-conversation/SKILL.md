---
name: hard-conversation
description: >
  Scripts the customer conversation you are putting off: a price increase, a feature you will not build, a commitment you missed, or a failure that cost them money. Trigger whenever the user says "hard conversation", "difficult conversation", "how do I tell them", "I have to tell the customer", "price increase", "raising their price", "we are not building", "roadmap no", "we missed the deadline", "we slipped", "the outage", "how do I break this to", "they are going to be angry", "I have been putting this off", or describes bad news they owe a customer. Also trigger when they ask you to soften a message that is honestly bad. It works out what is true and what you can offer before a word is said, writes the opening two sentences, sets the concession ladder and the walk-away in advance, and drafts the written record for afterwards. Use email-critic once the record is drafted, and exec-conversation when the conversation has escalated above your contact.
---

# Hard Conversation

The hard part is never the conversation. It is the four days before it, during which the situation gets worse and the customer finds out from someone else.

This skill does the work that makes the conversation short: deciding what is true, deciding what you can offer, and writing the first two sentences so you do not improvise them.

The failure this exists to prevent: **the runway.** Three paragraphs of context, a note of appreciation for the partnership, and the actual news in the fourth paragraph. The customer knew by the second sentence, spent the rest of it waiting, and now trusts the delivery less than the news.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first: contract shapes, segments, and what customer success can commit to without asking. That last one decides how much of this you can hold on your own authority. Where it is absent, carry on and name the assumption.

**Minimum: what happened and who it affects.** That is enough to produce the opening lines, the likely reactions and the record.

**Better with** the commitment as it was actually made, in writing. Almost every disagreement in these conversations is about what was promised, and the sentence that settles it is usually in an email nobody has reread.

**Best with** the contract, the account plan and a current risk read, because those decide how much of what you are about to say is a commercial event rather than a service one.

Nothing here is required.

---

## When this runs

Four situations, and they have different shapes. `references/by-scenario.md` covers each in detail:

1. **A commercial change**, usually a price increase or a term change
2. **A roadmap no**, a feature you will not build
3. **A missed commitment**, something you said would happen that did not
4. **A costly failure**, an outage, a bug or a data problem with a number attached

Read the general method below first, then the section for your case.

**Do not run this for:** an escalation already in progress with their executive team, where `exec-conversation` shapes the room, or a routine call that merely contains an awkward item, where `call-prep` covers it under the landmine step.

---

## Step 1: Decide whether it is happening today

The default answer is yes, and the reason is not courage. Every one of these conversations has a point after which you are no longer the person telling them. Their team finds out, or their finance team notices, or a status page does it for you. After that the conversation is not about the news, it is about why you did not say anything.

Two legitimate reasons to wait, and both come with a deadline attached:

- **You do not yet know something they will immediately ask**, and the answer is hours away, not days. Wait for the hours
- **You do not have authority to say what needs saying**, and the person who does is reachable today. Go to Step 2

Anything else is delay. Write down the hour you will have it by, and who you will tell if you do not.

**Do not wait for the fix.** Telling a customer about a problem and a plan is a normal conversation. Telling them about a problem they already noticed is an escalation.

## Step 2: Get straight what is true, and what you can actually offer

Before a word is said, write three lists. This is the step people skip, and skipping it is what produces the concession you have to retract.

**What is true.** The facts, with dates, separated from what you assume. Include the part that is unflattering to your side. If you are unsure about a cause, it goes in the "do not know yet" list, not into the conversation as a theory.

**What you do not know yet**, and when you will. This list is going to be spoken out loud, so make it honest and specific. "We do not know why yet, and we will have the root cause by Thursday" is a fine sentence. "It looks like it may have been a configuration issue" is a guess that will be quoted back to you.

**What you can offer, and on whose authority.** Credits, a discount, services hours, a roadmap commitment, an escalation path, an exec on the call. For each one, whether you can commit it yourself or need someone.

Then get the authority you need **before** the conversation. Going in without it produces one of two bad outcomes: you improvise something you cannot honour, or you say "let me check" to every question and the conversation achieves nothing except making them repeat it later to someone senior.

If you cannot get authority in time, say so plainly in the conversation rather than dodging. "I do not have the authority to commit to a credit today. I am asking for it, and you will have an answer by Friday" is a strong sentence. It is not the sentence you want to say, and it beats every alternative.

## Step 3: Pick the channel and the room

**Say it out loud first, then write it.** Bad news delivered by email lands worse than the same news delivered by voice, because the customer has no way to ask their first question and it becomes a document before it becomes a conversation. Call, then send the record.

The exception is a change that is genuinely administrative and affects a large population identically, where a written notice is the correct instrument and a call would be theatre. Even then, the named accounts get a call before the notice goes out.

**Who else is on it.** Add someone from your side only if they change what can be decided, and brief them properly. An unbriefed colleague on a hard call is worse than no colleague, because they will fill silence with reassurance you then have to take back.

**Who on their side.** Tell your champion before you tell their boss. A champion who learns bad news at the same time as their executive cannot help you and will remember it. If the news has to reach an executive, the strong version is your champion carrying it with your material, not you going around them.

## Step 4: Write the opening two sentences, literally

Not bullet points. The actual words, written down, because this is the part that goes wrong under pressure.

The shape:

1. **The news, plainly, in the first sentence.** Name the thing. No preamble, no gratitude for the partnership, no "I wanted to reach out"
2. **What it means for them, in the second.** Their impact, in their terms, not your process

Then stop. Do not attach the explanation, do not attach the apology to the explanation, and do not ask for a reaction. "I hope you understand" and "I know this is not what you wanted to hear" both invite the customer to manage your feelings, which is not their job at that moment.

**Own precisely the part that is yours.** Under-apologising reads as indifference. Over-apologising is worse than it looks: it makes the whole situation your fault, it invites a larger claim, and on a commercial decision it tells the customer your own company was wrong, which is a position you cannot then negotiate from.

**Apology and explanation are separate acts, in that order, and the second one is optional.** An explanation offered before the apology is an excuse. An explanation offered before they ask is a defence of your team's process, which is not a thing they want. Say the thing, take the impact, and explain when asked.

## Step 5: Set the concession ladder and the walk-away

Decide in advance, in writing:

- **The first thing you will offer**, and when
- **The second**, and what has to happen for it to be needed
- **What you will not give**, and the sentence you will say instead
- **The walk-away.** The point at which you stop conceding and let them make their decision

Improvised concessions are the durable damage in these conversations. A credit given in the moment to end an uncomfortable call becomes the baseline for the next incident and a line item in the next negotiation. Anything you give should be something you would be willing to give again on the same facts.

**Give the reason once.** Repeating a justification under pressure reads as negotiation, and it invites them to keep pushing to see what changes. State it, then hold it in the same words.

## Step 6: Plan the silence and the three reactions

**Silence after the news is correct.** The urge to fill it is what produces the runway in spoken form. Say the two sentences and wait, however long it takes.

Prepare a line for each of the three reactions, since they need different things:

- **Anger.** They need to be heard before they can hear anything. Do not defend, do not explain, do not correct a detail that is slightly wrong. Acknowledge the specific impact, not the emotion. "That cost your team two days at month end" beats "I understand you are frustrated"
- **Cold.** Short answers, no visible reaction, meeting ends early. This is the dangerous one, and it is routinely read as "that went well". Assume the decision is being made elsewhere and ask directly what happens next on their side
- **Negotiation.** They move straight to what they want. This is the best of the three, because the relationship is intact enough to trade. Go to your ladder and do not go past it

**Do not resolve it in the room if the answer requires someone who is not there.** Give the date instead.

## Step 7: Write the record

Same day. Short. It exists to be forwarded.

- What is true, in their terms
- What you have committed to, with names and dates
- What is still open, and when they will hear
- Nothing new, and nothing softer than what you said out loud

**Write the version that survives a forward.** Assume it reaches their executive and yours. That means no internal shorthand, no blame directed at a colleague or a team, and no language that concedes liability if there is money involved. Where there is a number attached to the failure, have someone with commercial authority read it before it goes.

Run it through `email-critic` if you want it checked against the transcript before sending.

---

## Output

1. **The decision on timing**, and the deadline if it is not today
2. **What is true, what is unknown, and what you can offer**, with the authority for each
3. **The channel and the room**, including who is briefed and who is told first
4. **The opening two sentences**, written out
5. **The concession ladder and the walk-away**
6. **A line for each of the three reactions**
7. **The written record**, drafted
8. **What you could not check**

---

## Failure modes

- **The runway.** Context before news. They know by sentence two and stop trusting the delivery
- **Waiting for the fix.** The window in which you are the one telling them is short and it closes quietly
- **Going in without authority.** Either an improvised offer you cannot honour, or a call that achieves nothing but a repeat with your manager on it
- **Over-apologising.** Especially on a commercial decision, where apologising for the decision tells them your own company got it wrong and destroys the position you have to hold
- **The soft maybe.** A no delivered as a maybe to avoid the moment. It costs more later than the no would have cost now, and it keeps the request alive for years
- **Explaining first.** An explanation before an apology is an excuse. An explanation before it is asked for is a defence of your process
- **Improvised concessions.** They set precedent, they reappear in the next negotiation, and they cannot be withdrawn
- **Ambushing the champion.** Telling their boss before telling them ends the relationship you most need
- **Reading cold as fine.** The quiet call is the one that has already been decided elsewhere
- **Delivering it by email because it is easier.** It is easier, and it converts a conversation into a document with no chance to ask a question
- **Speculating on cause.** A theory offered under pressure becomes the version they quote back when the real cause turns out different

---

## What good looks like

- The customer heard it from you, first, and by voice
- The news is in the first sentence and their impact is in the second
- Everything offered was decided before the call and could be offered again on the same facts
- What you do not know is stated as unknown, with a date
- The champion was told before their executive
- The written record says exactly what was said out loud, no softer
- The conversation was short

---

## Related skills

- `email-critic` for the written record before it goes
- `exec-conversation` when it has escalated above your usual contact
- `call-prep` when the hard item is one part of a wider call
- `renewal-risk` when the conversation is a commercial change on an account already in question
- `churn-postmortem` if it did not hold

---

## Supporting files

- `references/by-scenario.md` - the four scenarios and how each one differs
