---
name: expansion-case
description: >
  Builds the internal business case your champion has to carry without you in the room, rather than the pitch you would give. Trigger whenever the user says "expansion case", "business case", "upsell", "cross-sell", "expand the account", "they want to add seats", "second department", "justify the spend", "my champion needs to sell this internally", "build the case for", "how do I get budget for", or names an account and additional scope in the same breath. Also trigger when a customer asks what it would take to roll out further. It anchors on a problem their leadership already agreed exists, finds where the budget actually comes from, sizes the ask so it can survive one meeting, and answers the objections their finance team will raise before they raise them. Use business-review when the meeting is the value review, and renewal-negotiation when scope and price are being agreed together.
---

# Expansion Case

You are not going to present this. Your champion is, in a meeting you will not be in, to people who have never met you, against three other things asking for the same money.

That single fact decides everything about how it should be written. It is not a pitch with your logo on it. It is ammunition, in their language, short enough to be carried.

The failure this exists to prevent: **the beautiful deck that dies in someone's inbox**, because the champion could not defend slide four when their CFO pushed on it.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first: the value metric, the contract shapes and how segments differ. Where it is absent, carry on and name the assumption.

**Minimum: what you want to expand into and who would sponsor it.** Enough to produce the case structure, the likely objections and the sizing.

**Better with** current outcome data from the existing deployment, their stated goals, and the original business case. The first is what earns you the right to ask at all.

**Best with** a stakeholder map, because an expansion needs a budget holder who is frequently not the person you have been working with, and knowing whether you have met them changes the plan.

---

## Step 0: Check you have earned the ask

One question, and it disqualifies more expansions than any other: **is the first deployment demonstrably working, in a way the customer would state out loud?**

If not, stop. An expansion ask on an underperforming deployment does not merely fail. It tells the account that you are not paying attention, and it puts the renewal at risk to chase revenue that was never available. Fix phase one, then come back.

The tell: you can name the outcome the existing scope produced, in their measure, and a named person on their side would repeat that number in a meeting. Not "usage is healthy". A number they own.

---

## Step 1: Anchor on a problem their leadership already agreed exists

An expansion sold as an improvement competes with every other improvement. An expansion sold against a problem the leadership team has already named competes with nothing.

Find the anchor in their own words: a stated priority, a public commitment, a target they missed, a project already funded, something their executive said in the business review. Then write the case as the continuation of that, not as a new idea.

**If you cannot find an anchor, you do not have a case yet.** You have a product capability and an assumption. Say so rather than dressing it up.

## Step 2: Follow the money before you write anything

Budget comes from somewhere, and which somewhere changes the whole case.

- **An existing line** you are already on, extended. The easiest, and it needs a rate and a date rather than a case
- **A new ask in the next planning cycle.** Then the deadline is their planning cycle, not your quarter, and the case has to be in the champion's hands weeks before that
- **Someone else's budget**, in the department you are expanding into. Then your champion is not the buyer, and their job is an introduction rather than an argument. This is routinely missed
- **Displacing something.** Then the case includes what gets switched off, and you have made an internal enemy you should know about in advance

Name which one, and name the person who controls it. If that person has never been met, that is the first action rather than the case.

## Step 3: Write the money honestly

Three numbers, in their units, not yours.

- **What it costs.** All-in, including services, internal effort and the time their people will spend. A case that hides implementation effort is discovered at exactly the wrong moment
- **What it returns**, expressed the way they measure. Hours, error rate, cycle time, revenue, headcount avoided, risk reduced
- **When.** Payback period, and be conservative. A champion who quotes your optimistic number and misses it is damaged, and they will remember who gave them the number

Where a number is an estimate, mark it as an estimate and give the basis. A range with a stated assumption survives scrutiny. A precise figure with no basis does not survive a finance team, and they are the ones who will look.

**Use their own realised numbers wherever they exist.** "This is what the first deployment did for you" beats any benchmark, because it cannot be argued with by someone who does not believe vendor statistics, and they are right not to.

## Step 4: Size it so it can survive one meeting

The most common structural failure is asking for the whole thing at once.

Break it into a first step small enough to be approved by the person your champion can actually reach, that produces a result inside one cycle, and that makes the next step obvious. Then say what the full picture looks like, so nobody feels misled later.

The test: **could your champion get a yes on this without a committee.** If not, it is too big, and the version you should write is the one that is not.

## Step 5: Answer the objections before they are raised

Their finance team, and the peer who wants the same money, will ask a predictable set. Put the answers in the document rather than leaving your champion to improvise.

- **"Why now, why not next year."** Expansion dies of no urgency far more than of no value. If there is no real reason for now, admit it and time the ask better
- **"What happens if we do nothing."** Answer in their cost, not your revenue
- **"Can we do this with what we already have."** Answer honestly. If they partly can, say which part, because the credibility you keep is worth more than the scope you lose
- **"What did the last thing we bought from them deliver."** Step 0 is what makes this answerable
- **"Who else is doing this."** A peer example, not a vendor statistic
- **"What is the exit."** What it costs to stop. Refusing to answer this reads as a trap

## Step 6: Write it for the room you will not be in

- **Their format, their vocabulary.** No product names where a plain description works, no tier names, no internal terminology of yours
- **One page, with the ask in the first three lines.** The rest is support for the person who has to defend it
- **No logo.** The moment it looks like a vendor document, it becomes a vendor document, and it is arguing rather than informing
- **A version they can forward**, and separately the two or three sentences they would say out loud. Those sentences are the part that actually travels

Then rehearse with the champion. Ask them to say the case back to you and listen for where they go vague. That spot is where it will fail, and it is fixable while you are still in the room.

## Step 7: Keep it separate from the renewal, unless you chose otherwise

Bundling an expansion into a renewal hands the customer one negotiation containing both of your asks, and the usual outcome is that the expansion buys the renewal discount.

Sometimes bundling is right, when the renewal is safe and the expansion is small. Make it a decision rather than an accident, and if they are bundled, `renewal-negotiation` covers the shape.

And never disguise an expansion ask as a value review. Customers do not punish the upsell. They punish the disguise.

---

## Output

1. **The Step 0 verdict**: is the existing deployment demonstrably working, and who would say so
2. **The anchor**: the problem their leadership already agreed exists, in their words
3. **Where the budget comes from**, and who controls it, and whether they have been met
4. **The three numbers**: cost all-in, return in their units, payback, with estimates marked
5. **The first step**, sized to survive one meeting, and the full picture behind it
6. **The six objections**, answered
7. **The one-page case** for the champion to carry, plus the two sentences they would say out loud
8. **What you could not check**

`assets/business-case.md` is the one-page document itself, written to be filled in and handed over.

---

## Failure modes

- **Asking on a deployment that is not working.** Puts the renewal at risk to chase revenue that was never there
- **No anchor.** A capability plus an assumption, presented as a case
- **Writing the pitch instead of the ammunition.** It reads as a vendor document the moment it reaches the second person
- **Asking for the whole thing.** A number that needs a committee, in a cycle that has no committee meeting scheduled
- **Optimistic numbers handed to a champion.** They quote it, they miss it, and they carry the damage
- **Vendor benchmarks** where the customer's own realised numbers were available
- **Not knowing whose budget it is.** Especially when the money sits in the department being expanded into, where your champion is a route rather than a buyer
- **Hiding the implementation effort**, which is found by the one person in the room who has done this before
- **Bundling it into the renewal by accident**, so the expansion pays for the discount
- **The value review that turns into an upsell.** They punish the disguise, not the ask

---

## What good looks like

- The champion can say the case in two sentences without reading it
- Every number is either theirs, or marked as an estimate with its basis shown
- The first step could be approved by one person
- The anchor is something their own leadership said, quoted back
- The document has no logo on it and no product tier names in it
- What happens if they do nothing is stated in their cost
- You know whose budget it is, and you have met them

---

## Related skills

- `business-review` for the meeting where the value that earns this gets established
- `stakeholder-map` for whether the budget holder has actually been met
- `renewal-negotiation` when scope and price are being agreed together
- `exec-conversation` when the ask needs a senior sponsor on their side
- `account-context` for the value metric the case has to be written in

---

## Supporting files

- `assets/business-case.md` - the one-page case, written for the champion to carry
