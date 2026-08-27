---
name: renewal-negotiation
description: >
  Prepares the renewal conversation itself: what you will concede, what you will not, what the walk-away is, and what they are going to ask for. Trigger whenever the user says "renewal negotiation", "they want a discount", "renewal conversation", "they are asking for a better price", "procurement is involved", "negotiating the renewal", "they want to cut seats", "how much should I give", "what do I concede", "they mentioned a competitor", or names a renewal and a number in the same breath. Also trigger when a customer asks for utilisation data, seat counts or contract copies ahead of a renewal, which is negotiation preparation rather than admin. Use renewal-risk when the job is deciding whether they will renew at all, and hard-conversation when the job is delivering a price increase they have not heard yet. This is for the conversation where both sides know a number is being agreed.
---

# Renewal Negotiation

Every concession you make in this conversation is permanent unless you deliberately make it temporary, and the discount you give in the last week of a quarter sets the price for every year after it.

The failure this exists to prevent: **negotiating price before value is established.** If the customer has not agreed that the thing is worth having, you are not negotiating a price. You are arguing about a number with nothing on the other side of the scale, and you will lose that argument every time.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first: contract shapes, pricing model, segments, and who signs in this business. That decides what you can move without asking. Where it is absent, carry on and name the assumption.

**Minimum: the account, the date and roughly what they pay.** Enough for a concession ladder, a walk-away and the likely asks.

**Better with** the contract itself, particularly the notice date, the auto-renewal clause and any uplift or index clause. Those three decide the shape of the conversation more than anything you will say in it.

**Best with** a current risk read and the original business case, because the first tells you how much leverage you actually have and the second tells you what value you are entitled to point at.

---

## Before anything else: have you earned the right to negotiate

Run `renewal-risk` first if the read is not already done. Negotiation prep on an account whose decider you have never met is prep for the wrong conversation.

Two questions decide whether this skill is the right one:

- **Is value agreed?** Can you name a number the customer would accept as what they got. If not, the meeting to run is a value conversation, and negotiating now trades your price against nothing.
- **Is this a negotiation or a decision already made?** A request for a downgrade is lagging. If the scope decision has already been taken internally, you are being informed, not negotiated with, and the play is different.

---

## Step 1: Work out both walk-aways, and be honest about theirs

**Yours.** The point below which you would rather lose the account than renew it. Write the number. An unwritten walk-away moves under pressure, which is the same as not having one.

**Theirs, which is the one people get wrong.** The customer's alternative is almost never "switch next month". It is usually one of:

- **Do nothing**, which is available, free, and their most common real alternative
- **Renew smaller** while they evaluate, which costs them nothing and preserves optionality
- **Switch**, which carries migration cost, retraining, re-integration and internal political risk that the person threatening it may not personally be carrying

The gap between the alternative they describe and the alternative they have is your actual leverage. Ask what they have already seen, who has run it, and what the migration would involve. A competitor named without a demo behind it is a procurement tactic. A competitor with a signed pilot is a different conversation.

Be equally honest in the other direction. If they are one of three accounts holding up a segment, your walk-away is not real either.

## Step 2: Read the contract before you read the room

Three clauses set the shape and most CSMs discover them late:

- **The notice date.** After it passes, the renewal happens whether or not the conversation goes well. Before it, they hold an option
- **Auto-renewal.** Whether silence renews or lapses inverts who is under time pressure
- **Uplift or index clause.** If an increase is already contracted, you are enforcing a term rather than asking for one, and that is a much stronger position said plainly

Also find the term end, the fiscal year end and any co-term or ramp already agreed.

## Step 3: Know what the other side is measured on

You are usually negotiating with two parties who want different things.

**The business owner** wants the outcome to continue and does not want a project. Their nightmare is disruption, not price.

**Procurement** is usually measured on savings against the previous number or against the first number quoted, expressed as a percentage. That matters because **it means they need a win, not necessarily your money.** Things that read as a win and cost you far less than a rate cut:

- Payment terms, annual instead of quarterly, or the reverse if cash is their issue
- A longer term at the same rate, which is a discount in their model and revenue certainty in yours
- Capped uplift for the next two renewals
- An added module or seat band at no incremental charge, where marginal cost is near zero
- Services or training hours
- A better SLA, where you can actually meet it

If a procurement party appears mid-term and starts asking for utilisation data and contract copies, that is this conversation beginning, and it started before you were told.

## Step 4: Build the concession ladder, with a price on every rung

Write it before the meeting. Three rungs and a floor.

For each rung: **what you give, what you get, and what it costs you.** Nothing is given free. Not because trading is a technique, but because a free concession tells them the price was never real, and it invites the next ask.

What to ask for in return, in rough order of what they can actually say yes to:

- A longer term
- A reference call, case study or logo rights
- An executive sponsor meeting
- A commitment on scope, seats or an expansion date
- Faster payment terms
- An introduction to a peer or another business unit

**Prefer a one-time credit over a rate cut.** A credit costs you once. A rate cut compounds for every year that follows and becomes the number the next negotiation starts from. If you have to move on rate, cap the term or attach an uplift so the discount has an end date.

**Decide what is not on the table** and write the sentence you will use. "We are not able to move on that" said once and repeated in the same words is stronger than a reason defended three times. Repeating a justification under pressure reads as negotiation.

## Step 5: Take time seriously, because it is usually theirs

The party with a deadline concedes. Work out honestly who has one.

- **Your quarter end is leverage against you** the moment they know when it is. Assume they do
- **Their notice date and budget lock are leverage for you**, if you know them and they have not already passed
- **A short extension is a concession**, not a neutral act, and it is often the cheapest one available when the alternative is a bad number agreed under pressure

Never let a deal be won by the calendar and call it a negotiation. A number agreed in the last three days of a quarter is a number you will explain to your successor.

## Step 6: Handle the four asks you will get

**"We need a discount."** Ask what it is for. Budget cut, a benchmark they were shown, or a target they have been given are three different problems with three different answers. Never move on the first ask.

**"We are only using 60% of our seats."** True, and lagging. This is a value conversation wearing a commercial costume. Separate the rightsizing from the rate, and do not give both.

**"Competitor X quoted us half."** Ask what is in their quote. Half-priced quotes are usually half the scope, first-year only, or exclude the services line. Get it on the table rather than matching a number you have not seen.

**"We want to go month to month."** They are buying optionality, and it usually costs you more than the discount would have. Price it accordingly and say why.

## Step 7: Decide what happens if it stalls

- **Who escalates, on both sides**, and whether you have an executive relationship to use. If you do not, `exec-conversation` covers building one, and it is too late to start this week
- **What you do if they go silent.** Silence near a notice date is not neutral
- **The one thing you will not do**, written down, so it survives the third call

---

## Output

1. **The read on whether this is a negotiation at all**, and whether value is agreed
2. **Both walk-aways**, yours as a number, theirs as an honest assessment of their real alternative
3. **The contract facts**: notice date, auto-renewal, uplift, term end
4. **What each party is measured on**
5. **The concession ladder**: three rungs, each with what you give, what you get, and what it costs
6. **What is not on the table**, and the sentence you will use
7. **The time picture**, with whose deadline is real
8. **What you could not check**

`assets/negotiation-plan.md` is the same structure as a one-page plan you can fill in by hand.

---

## Failure modes

- **Negotiating before value is agreed.** The single largest one. Price against nothing loses
- **Conceding on the first ask.** It teaches them the number was soft and there are three more asks coming
- **The rate cut that outlives everyone.** Permanent margin given away to solve a one-year problem, and it becomes the starting number next time
- **Free concessions.** Anything given without a return tells them the price was never real
- **Discovering the notice date late.** The whole shape of the conversation is set by a clause nobody read
- **Believing the competitor.** A named vendor with no demo behind it is a tactic. Ask what they have actually seen
- **Bundling the expansion into the renewal** without deciding to. It hands them one negotiation with two of your asks in it
- **Quarter-end capitulation.** A number set by your calendar rather than by the value
- **Taking the threat at face value from someone who does not carry the switching cost.** The person threatening migration is frequently not the person who would run it

---

## What good looks like

- The walk-away was written down before the first call and did not move
- Every concession bought something, and you can say what
- Anything given on rate has an end date or a cap attached
- Procurement got a win that was not your margin
- You know what their real alternative is, not the one they described
- The number was agreed on value and timing, not on your quarter

---

## Related skills

- `renewal-risk` for whether they will renew at all, run before this
- `business-review` for establishing the value this conversation depends on
- `hard-conversation` when you are the one delivering a price increase
- `exec-conversation` when it escalates above your usual contact
- `expansion-case` when the renewal and an expansion are being discussed together
- `churn-postmortem` if it does not land

---

## Supporting files

- `assets/negotiation-plan.md` - the one-page plan, usable without an assistant
