---
name: nrr-narrative
description: >
  Turns net and gross revenue retention into a story a board will follow, including what the headline number hides. Trigger whenever the user says "NRR", "net revenue retention", "GRR", "gross retention", "retention narrative", "board update on retention", "explain our retention numbers", "why did NRR drop", "retention story", "prepare the retention slide", or is presenting a retention number to a board, an investor or an executive team. It decomposes the ratio into expansion, price, contraction and churn, insists gross retention appears alongside net, distinguishes cohort from blended, and answers the only question a board is actually asking, which is whether the number is repeatable. Use renewal-forecast for the forward number and portfolio-review for the account reads underneath it.
---

# NRR Narrative

Net revenue retention is a ratio, and every ratio hides its composition. One hundred and ten per cent built on a price increase, one hundred and ten per cent built on seat growth in existing teams, and one hundred and ten per cent built on two enormous expansions covering broad contraction are three different companies with the same slide.

The failure this exists to prevent: **presenting the number without its composition**, which survives exactly one question from anyone who has seen this before, and which loses you the room for the rest of the meeting.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first: pricing model, contract shapes and segments. On consumption pricing, retention arithmetic behaves differently and the narrative has to say so. Where it is absent, carry on and name the assumption.

**Minimum: the retention numbers and the period.** Enough for a decomposition attempt and an honest list of what cannot be separated yet.

**Better with** the movement broken into expansion, price, contraction and churn, and the same numbers for prior periods.

**Best with** cohort data and segment-level retention, which is where the actual story almost always is.

---

## Step 1: Decompose before you narrate

Four movements. The number means nothing until they are separated:

- **Expansion.** More seats, more products, more usage, at existing prices
- **Price.** Uplift, list change, discount roll-off. **Revenue that arrived without the customer choosing to buy more**
- **Contraction.** Accounts that stayed and shrank
- **Churn.** Accounts that left

**Price and expansion are the pair that must never be merged.** Expansion is evidence customers want more. Price is evidence you charged more. Both are legitimate revenue and only one is a demand signal, and a board that discovers the difference after being shown a blended number treats every subsequent number as suspect.

Contraction is the movement most often left out entirely, and it is usually the largest of the two negatives.

## Step 2: Show gross retention next to net, always

**Gross retention is the honest number.** It cannot be rescued by expansion, so it says whether you keep what you have. Net retention says whether you grow inside the base. They answer different questions and only the pair is informative.

The specific thing this prevents: a business with strong expansion in a handful of accounts and a deteriorating base can hold net retention flat for several quarters while gross retention falls steadily. By the time net moves, the problem is two years old and structural.

If you present one number, present gross.

## Step 3: Say whether it is cohort or blended, and why that matters

Blended retention across the whole base flatters a company that is growing fast, because recently landed customers have not had time to churn yet. The faster new business grows, the more flattering it gets, which means the number improves for a reason unrelated to retention.

Cohort retention, tracking a group of customers landed in the same period over time, is what tells you whether the product actually holds people.

Say which you are showing. If you only have blended, say that, and say what it might be concealing. A board will forgive a gap you name and will not forgive one they find.

## Step 4: Find the concentration

The two questions that break most retention slides, and both are cheap to answer in advance:

- **How much of the expansion came from how few accounts?** If half of it came from three, the number is not a business property, it is three renewals, and it does not repeat by itself
- **Where is the churn concentrated?** By segment, by cohort, by product, by acquisition channel, by industry. Churn spread evenly is a product or pricing problem. Churn concentrated in one segment is a much more actionable finding and usually a much less alarming one

**A number that depends on a handful of accounts should be presented that way**, before someone else notices.

## Step 5: Answer the question they are actually asking

A board asks about NRR to work out one thing: **is this repeatable, and what would change it.**

So the narrative has to answer:

- **What drove it**, from the decomposition
- **How much of that recurs on its own.** A price uplift does not repeat next year unless you do it again, and doing it again has a cost
- **What is the leading indicator**, since retention is deeply lagging. Something you can show moving now that predicts the number two quarters out
- **What would you change it with**, and what that costs

Retention reported without a forward mechanism is a history lesson. The reason it is on the agenda is that somebody is deciding where to put money.

## Step 6: Name what the number hides, before anyone asks

Say it yourself. It costs one slide and it is the difference between a narrative and a defence.

Common concealments worth checking for:

- One large expansion covering broad contraction
- A price increase presented as growth
- Churn deferred rather than avoided, because accounts on multi-year terms cannot churn this year
- A definitional change mid-period, which is the one that ends credibility permanently if found rather than disclosed
- Improvement caused by losing the segment that was churning, which is a real improvement and a completely different story

**If a definition changed, lead with it.** Everything else in the deck depends on the audience believing the numbers are constructed honestly.

## Step 7: Write it as three sentences first

Before any slide: what happened, why, and what you are doing about it. Three sentences.

If it cannot be said in three, the analysis is not finished, and building a deck on unfinished analysis is how a retention review becomes forty minutes of questions about the axis labels.

---

## Output

1. **The decomposition**: expansion, price, contraction, churn, separated
2. **Gross and net together**, with gross leading
3. **Cohort or blended**, stated, with what blended may be concealing
4. **The concentration**: expansion in how few accounts, churn in which segment
5. **What recurs on its own**, and what does not
6. **The leading indicator**
7. **What the number hides**, disclosed rather than defended
8. **The three sentences**
9. **What you could not check**

---

## Failure modes

- **The headline with no composition.** Survives one question
- **Merging price and expansion.** One is a demand signal, one is not, and mixing them makes every later number suspect
- **Omitting contraction**, usually the larger negative
- **Net without gross.** Lets a deteriorating base hide behind a few large expansions for years
- **Blended presented as if it were cohort**, which flatters exactly in proportion to how fast you are growing
- **Not naming the concentration**, so somebody else does
- **No leading indicator**, leaving a lagging number with no forward handle
- **A definitional change not disclosed**, which is the one that ends credibility for good
- **Retention as a history lesson**, when the reason it is on the agenda is a spending decision
- **A deck built before the three sentences exist**

---

## What good looks like

- Gross and net are both on the page, and gross comes first
- Price is a separate line from expansion
- Contraction has its own number
- Whether it is cohort or blended is stated without being asked
- The concentration is disclosed by you
- There is one leading indicator with a mechanism behind it
- What the number hides was said before anyone had to ask
- The whole thing survives being reduced to three sentences

---

## Related skills

- `renewal-forecast` for the forward number this narrative is the backward half of
- `portfolio-review` for the account reads underneath the aggregate
- `churn-postmortem` for whether the churn shares a mechanism, which is what makes it a story rather than a rate
- `coverage-model` when the retention pattern is a coverage decision showing up in the numbers
- `one-pager` for the version the board member forwards afterwards

---

## Supporting files

None. The output is a decomposition and three sentences, both specific to the business, and a template would invite filling in boxes rather than doing the decomposition.
