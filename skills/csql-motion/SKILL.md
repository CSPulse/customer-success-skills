---
name: csql-motion
description: >
  Designs how customer success generates and hands off qualified expansion leads without damaging the relationship that produced them. Trigger whenever the user says "CSQL", "customer success qualified lead", "CS sourced pipeline", "should CS sell", "hand leads to sales", "expansion motion", "CS to sales handoff", "how do we count CS influence", "attribution between CS and sales", or is designing or fixing how expansion signals move from customer success to a sales team. It defines what actually qualifies as a signal rather than a hunch, shapes the handoff as a warm introduction rather than a queued lead, settles attribution before the first one is passed, and names the kill criteria. Use expansion-case for the individual business case, and coverage-model for whether the team has capacity for this at all.
---

# CSQL Motion

Almost every one of these programmes fails the same way, and it is not a design problem. **The first badly handled handoff teaches the customer success team that flagging an opportunity gets a customer called by someone who has not read anything, and the flow of signals stops within a month.** After that the programme exists on a slide.

So this is mostly a design problem about trust, and only secondarily about lead definitions.

The failure this exists to prevent: **the lead dropped into a queue.** A CSM passes a real signal, it is worked by someone with no context, the customer experiences a cold sales approach from a company that is supposed to know them, and the CSM never passes another one.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first: the motion, the segments, and what customer success owns commercially here. That last one decides whether this programme is even the right shape. Where it is absent, carry on and name the assumption.

**Minimum: what you want CS to spot and who would work it.** Enough for a qualification definition, a handoff shape and an attribution rule.

**Better with** the historical expansion data, so qualification can be built from what actually converted rather than from what feels promising.

**Best with** the compensation plans of both teams, because those decide behaviour far more than any process document.

---

## Step 0: Decide whether CS should be selling at all

Ask before designing. Three honest positions exist:

- **CS spots and hands off.** The most common and usually the right one. CSMs are not compensated or trained to sell, and asking them to do it informally gets you neither
- **CS owns expansion end to end.** Legitimate, and it means the job description, the training and the compensation all change. If those have not changed, this position is not actually being taken, it is being assumed
- **CS does neither**, because the trust position is the asset and monetising it costs more than it earns. A real answer, particularly where the product is regulated, technical, or bought once

**A hybrid where CSMs are expected to sell but are neither trained nor paid for it is the worst of the three**, and it is the default when nobody makes this decision explicitly.

---

## Step 1: Define what actually qualifies

Without a written definition, every CSM invents their own, and the aggregate is noise that sales learns to ignore.

A qualifying signal is **behavioural or stated, not felt**:

- A stated need with a named owner. Someone said they need to do X, and X requires more than they have
- A usage boundary being hit. Seats near a limit, volume near a commitment, a team using something not in scope
- An organisational trigger. A new team, a new region, a merger, a mandate that extends the use case
- A repeated workaround that a paid capability solves
- An explicit ask. "Can we do this for the other division too"

**"They seem happy" does not qualify.** Nor does a high health score. Satisfaction and buying intent correlate weakly, and building a programme on satisfaction produces volume with no conversion, which is how these get cancelled.

Write it down. Two or three criteria, and require that the CSM name which one fired.

## Step 2: Design the handoff as an introduction, not a transfer

The single highest-leverage decision in the whole motion.

- **The CSM stays in the room.** Not as an observer, as the person who holds the relationship. A CSM who disappears at handoff has confirmed the customer's worst reading of what just happened
- **The context travels**, and it is read before contact. What has been said, what has already been discussed, what to avoid, who the sceptic is
- **No cold outreach to a warm account, ever.** The introduction comes from the person the customer already knows
- **Agree a response window.** A signal that sits for three weeks decays, and the CSM who raised it looks foolish to their own customer

Where sales cannot commit to reading context before contact, the programme should not start. That constraint is the programme.

## Step 3: Protect what the customer experiences

The whole asset here is that the CSM is the person who is not selling them anything. Spend that carelessly and it does not come back.

- **Never let the value conversation become the sales conversation in the same meeting.** Customers do not punish the upsell; they punish the disguise. `business-review` says the same and it holds here
- **The CSM can raise a possibility and should not negotiate.** Those are different roles and the customer can feel the switch
- **A no must be genuinely free.** If declining an expansion changes the service they get, they will notice, and everything the CSM says afterwards is discounted

## Step 4: Settle attribution before the first lead moves

**Attribution arguments kill these programmes**, and they always start after the first meaningful deal rather than before.

Decide, in writing, in advance:

- **What counts as CS-sourced** against CS-influenced, and the test that separates them
- **Whether both teams can claim the same deal.** Usually they should. Double-counting for recognition while counting once for revenue is a workable answer, and pretending the question will not arise is not
- **What the CSM actually gets.** Recognition, a spiff, quota relief, or a line in their review. **If the honest answer is nothing, say so**, and expect the volume that nothing buys
- **Who owns the number** when it is missed

Compensation shapes behaviour more than any process document. A motion where sales is paid and CS is not produces exactly the effort that ratio implies.

## Step 5: Measure the two things that matter

Volume is a vanity metric here and it is usually the one reported.

- **Conversion rate of CSQLs**, against sales' other sources. If CS-sourced leads convert better, which they usually should, that is the argument for the programme and for what CS gets from it
- **Relationship cost.** Harder and more important. Track whether accounts that went through the motion show any change in engagement, satisfaction or renewal behaviour afterwards. **If nobody measures this, the programme's main risk is invisible by design**

Also track how many CSMs are contributing. If it is three people out of twenty, the programme is three people, and the design has not worked.

## Step 6: Write the kill criteria

Programmes like this rarely get stopped, they get quietly ignored, which is worse because the slide stays.

Decide up front what would end it: a conversion rate below a threshold, a measured relationship cost, contribution concentrated in a handful of people after two quarters, or a single serious incident where a customer relationship was damaged by a handoff.

Then review against those, honestly, on a date set now.

---

## Output

1. **The position**: spot and hand off, own it end to end, or deliberately neither
2. **The qualification criteria**, two or three, written, with the CSM naming which fired
3. **The handoff design**: who introduces, what context travels, the response window
4. **What protects the customer's experience**, including that a no is free
5. **The attribution rule**, and what the CSM actually gets, stated even when it is nothing
6. **The two measures**: conversion against other sources, and relationship cost
7. **Contribution spread** across the team
8. **The kill criteria**, and the review date
9. **What you could not check**

---

## Failure modes

- **The lead dropped into a queue.** One bad handoff ends the flow of signals within a month
- **No written qualification**, so every CSM invents their own and sales learns to ignore the aggregate
- **Building on satisfaction.** "They seem happy" produces volume and no conversion
- **The CSM disappearing at handoff**, which confirms the customer's worst reading
- **Cold outreach to a warm account**
- **Expecting CSMs to sell without changing the job, the training or the pay.** The worst of the three positions and the default when nobody decides
- **Attribution settled after the first big deal** rather than before
- **Measuring volume**, which is the vanity metric here
- **Never measuring relationship cost**, which makes the programme's main risk invisible by design
- **Three contributors out of twenty**, reported as a team motion
- **No kill criteria**, so it is quietly ignored rather than stopped, and the slide remains

---

## What good looks like

- The position was decided explicitly, and the compensation matches it
- Qualification is written, behavioural, and the CSM names which criterion fired
- The introduction comes from the person the customer already knows, and they stay in the room
- Context is read before contact, every time
- Declining costs the customer nothing they would notice
- Attribution was agreed before the first lead moved
- Conversion is compared against sales' other sources, and relationship cost is actually tracked
- More than a handful of the team contributes
- There is a written condition under which this stops

---

## Related skills

- `expansion-case` for the individual business case once a signal is qualified
- `business-review` for keeping the value conversation and the sales conversation apart
- `coverage-model` for whether the team has the capacity for this at all
- `advocacy-ask` for the other place CS is asked to monetise trust, with the same asymmetry
- `internal-escalation` when the handoff process itself is the thing that needs fixing

---

## Supporting files

None. The output is a position, a definition, an attribution rule and a kill condition, all of which are company-specific decisions rather than documents.
