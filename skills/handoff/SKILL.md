---
name: handoff
description: >
  Runs a handover so the receiving side can actually take it: sales to customer success, customer success to support, or one CSM to another. Trigger whenever the user says "handoff", "handover", "handing over my accounts", "sales to CS handover", "transition the account", "I am leaving and need to hand over", "onboarding a new CSM", "what do I need to pass on", or names an account changing owner. It defines completeness from the receiving side rather than the leaving side, forces out the things that never make it into a system, sets an acceptance step with a date, and separates the internal transfer from what the customer is told. Use customer-update for the message to the customer, and account-research when the handover never happened and the history has to be reconstructed.
---

# Handoff

Every handover is declared complete by the person leaving. That single fact explains almost everything that goes wrong with them.

The failure this exists to prevent: **the account that arrives as a folder.** Documents, a CRM record, a link to a shared drive, and none of the four things that actually matter, all of which live in one person's head and leave with them.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first for the contract shapes and what customer success owns. Where it is absent, carry on and name the assumption.

**Minimum: the account and both names.** Enough to produce the checklist, the questions and the acceptance step.

**Better with** the account history, the open commitments and the last few months of correspondence, since that is where the undocumented promises are.

**Best with** thirty minutes of live overlap between the two people. Every written handover is a substitute for that conversation and a worse one.

---

## Step 1: Name the type, because they transfer different things

- **Sales to customer success.** The thing that must transfer is **the promise**: what was sold, on what expectation, and what was said that is not in the contract
- **CSM to CSM.** The thing that must transfer is **the relationship and the folklore**: who matters, who is difficult and why, what has already been tried, and what the customer should not have to explain again
- **Customer success to support**, or into a pooled or digital model. The thing that must transfer is **the context that stops the customer re-explaining themselves**, which is the entire reason they resent being moved

Each still needs the mechanics. Each fails on a different thing.

## Step 2: Ask the four questions that never make it into a system

These are what a folder cannot carry, and asking them directly is most of the value of this skill.

1. **What was promised that is not in the contract?** The roadmap remark in the deal cycle, the "we can probably do that", the timeline someone gave verbally. It exists on almost every account and it is what the renewal gets judged against
2. **Who is the sceptic?** Every account has one and they are almost never in the CRM. Not knowing who they are means walking into the first meeting without knowing where the resistance comes from
3. **What nearly went wrong, and what fixed it?** The incident, the escalation, the near-miss. It shapes how they read everything you do afterwards
4. **What would you do first if you were staying?** The single best question to ask a departing owner. It surfaces the thing they know matters and have not got to, which is exactly the thing no document records

Where the answer to any of these is "nothing", press once. Nothing is rare.

## Step 3: Let the receiving side define complete

**The structural fix, and the one thing that changes handover quality.** The person leaving cannot judge whether the person arriving can run the account, and has every incentive to believe they can.

- The receiver writes or accepts the checklist
- The receiver marks it complete, not the sender
- Anything the receiver cannot answer after reading it is an open item, and it goes back

This does not need process. It needs one sentence agreed at the start: **you tell me when this is done, not me.**

## Step 4: Transfer the mechanics, briefly

The part everyone does. Keep it short so it does not crowd out Step 2.

- Contract: term, renewal date, notice date, value, what is in scope
- Commitments outstanding, with dates and owners
- Open tickets, escalations, and anything in flight
- Stakeholders, roles, and who has actually been met
- Access: systems, shared folders, channels, calendar series, distribution lists
- Cadence: what meetings exist and what they are for

Where a stakeholder picture needs real work, `stakeholder-map` does it properly. Where the account is being inherited with no handover at all, `account-research` reconstructs it from the record.

## Step 5: Do it live, and time-box it

- **One live conversation beats any document.** Thirty minutes, the receiver asking, the sender answering, both looking at the same list
- **A joint customer call is worth more than both.** Introduce, hand over, and let the customer hear continuity rather than read about it
- **Put a date on it.** A handover with no deadline drifts until the sender leaves, at which point it is not a handover, it is an excavation. If the sender has a last day, the handover date is before it, not on it

## Step 6: Handle the customer-facing half separately

The internal transfer and the customer's experience of it are two different jobs, and doing the first well does not do the second at all.

The customer's real fear is not who the new person is. It is that the history goes away and they have to start again. Address that specifically, name what carries over, and never let them discover the change from an auto-reply. `customer-update` Step 6 covers the message.

Where the account is mid-escalation or close to a renewal, delay the change if you can. Where you cannot, the outgoing person hands over live rather than the incoming person introducing themselves cold.

## Step 7: Leave the receiver a first action

End with one thing the receiver should do in the first week, and why. It converts a folder into a starting point, and it is the clearest signal that the sender actually thought about the account rather than emptying their notes into a document.

---

## Output

1. **The type**, and therefore what must transfer
2. **The four answers**: the undocumented promise, the sceptic, the near-miss, and what they would do first
3. **The mechanics**: contract, commitments, open items, stakeholders, access, cadence
4. **The acceptance step**: who signs it off, which is the receiver, and by when
5. **The live session**, scheduled, and the joint customer call if there is one
6. **The customer-facing message**, separately
7. **The receiver's first action**
8. **What could not be transferred**, named rather than left implied

`assets/handover-checklist.md` is the same structure as a fill-in checklist.

---

## Failure modes

- **The sender declares it complete.** Structurally guaranteed to be optimistic
- **The account arrives as a folder.** Everything documented, nothing that matters
- **Never asking what was promised outside the contract.** It exists, and it surfaces at renewal
- **No sceptic named**, so the first meeting has an unexplained source of resistance in it
- **No live conversation.** A document is a substitute for one and a worse one
- **No date**, so it drifts to the sender's last day and becomes archaeology
- **Access transferred and context not.** The new person can log in and cannot answer a question
- **The customer finding out from an auto-reply**
- **A handover during an escalation or a renewal**, done anyway because a calendar said so
- **No first action**, so the receiver starts by reading rather than doing

---

## What good looks like

- The receiver said it was complete, and could answer questions about the account without opening anything
- The undocumented promise is written down, with who said it
- The sceptic has a name
- It happened live, before the sender's last week
- The customer heard it from a person, and knows what carries over
- There is one specific thing for the receiver to do in week one
- What could not be transferred is stated rather than quietly missing

---

## Related skills

- `customer-update` for the message to the customer, particularly a change of CSM
- `account-research` when there was no handover and the history has to be reconstructed
- `stakeholder-map` for the relationship picture in depth
- `onboarding-plan` for the sales-to-customer-success case, where the handover feeds the plan
- `offboarding` for the departure case, which is a different thing entirely

---

## Supporting files

- `assets/handover-checklist.md` - the checklist, signed off by the receiver, usable without an assistant
