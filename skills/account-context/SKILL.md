---
name: account-context
description: >
  Captures the shared context every other customer success skill needs, once, so they stop asking for it. Trigger whenever the user says "account context", "set up account context", "set up the CS skills", "first time using these skills", "let me tell you about our product", "onboard me to these skills", or when any other skill in this library needs product, segment, contract or value-metric context that has not been established yet. Also trigger when the user says the skills keep asking the same questions, or that a skill's output felt generic. It interviews once, then writes a context document covering what the product does in the customer's words, how the segments differ, the contract shapes, the value metric the customer actually bought, what healthy usage looks like in this business, the go-to-market motion, and what customer success owns. Runs on whatever the user already knows and marks every gap as a gap rather than stalling.
---

# Account Context

Every other skill in this library needs the same handful of facts before it can say anything useful. What the product does. How the segments differ. Whether a flat usage line is a problem or the intended state. Who signs.

Without this, each skill interviews the user from scratch and the library stops feeling like a library. It feels like a room full of strangers who have never met.

The failure this exists to prevent: **a renewal risk read that says "usage is down, this may indicate risk" because it had no idea that in this business, low usage is what a healthy compliance deployment looks like.**

---

## What this needs

**Minimum: five minutes and what the user already knows.** Nothing here is looked up. It is what someone who has worked the book for a month can answer from memory, and the gaps are recorded as gaps.

**Better with** the pricing page, a sample contract, and a health-score definition if one exists.

**Best with** the original business case for two or three accounts, because that is where the value metric is actually written down.

---

## Step 0: Check whether one already exists

Before asking anything, look for an existing context document. It may be a file the user can point to, or a block they paste in.

If one exists, read it back in one short paragraph, ask what has changed, and update only that. Re-running the full interview on someone who already did it is the fastest way to get this skill uninstalled.

---

## Step 1: The product, in the customer's words

Not the website description. Ask:

- **What would a customer say this does for them?** One sentence, their vocabulary
- **What were they doing before?** The thing it replaced is usually the thing they compare you to at renewal
- **What is it genuinely bad at?** Not a weakness-as-strength answer. The real one, because it predicts which accounts struggle

If the user gives marketing copy, ask again for how a customer described it on a call last week.

---

## Step 2: Segments, and how they actually differ

Segments matter here only where they change the work. For each one the user runs:

- **Who buys, and who uses.** In enterprise these are rarely the same population, and almost every bad risk read confuses them
- **What a normal deployment looks like**: how many users, over what period, doing what
- **How long onboarding takes** when it goes well
- **What usually goes wrong** in this segment specifically

Two or three segments is normal. If the user names seven, ask which three carry the revenue.

---

## Step 3: Contract shape

This decides what a risk signal even means, so it is worth being precise.

- **Pricing model**: seat-based, consumption, platform or multi-product, or hybrid
- **Typical term length**, and whether multi-year is common
- **Notice and auto-renewal**: is there an opt-out window, and how long
- **Who signs**, by role, and whether customer success ever meets them

On consumption pricing, also ask what the commitment is and how burn-down is tracked, because there is no renewal event at which to detect risk.

---

## Step 4: The value metric

**The highest-yield question in this interview, and the one most likely to come back empty:**

> Can anyone state the number the customer bought?

Not an internal metric. The measure the customer's own leadership uses to decide whether this was worth it.

Ask it three ways, because the first two often produce internal proxies:

1. What does the customer say they got?
2. What number would their finance team ask about?
3. What was in the original business case?

**If nobody can answer, that is a finding, not a gap to skip past.** No agreed and currently-true value metric is the mechanism behind most healthy-usage-still-churned accounts. Record it plainly, because it changes what every downstream skill can honestly claim.

---

## Step 5: What healthy looks like in this business

This is the section that stops other skills producing generic reads.

- **The natural rhythm**: daily, weekly, monthly, seasonal, shift-based, or event-driven
- **Is low usage ever the intended state?** Compliance, surveillance, disaster recovery and audit tooling are bought to sit unused, and a skill that does not know this will call a healthy account at risk
- **What breadth looks like**: how many teams or sites a full deployment touches
- **The integrations that matter**, and what breaks if one disconnects
- **Seasonality**: retail peaks, financial close, academic terms, manufacturing shutdowns

Ask directly: **what usage pattern would worry the user, and what pattern looks alarming on a dashboard but is fine?** The second answer is the valuable one.

---

## Step 6: Motion and ownership

- **The motion**: product-led, sales-led, or hybrid, and what happens when a self-serve account grows big enough for procurement to notice
- **Who owns the renewal**: customer success, a renewals desk, or the account executive
- **Who owns expansion**
- **What customer success does not own**, which is the boundary with support, sales and account management in this company

The last one prevents a lot of wasted output. A skill that drafts an escalation to engineering is unhelpful in a company where that path runs through support.

---

## Step 7: Write it down

Fill `assets/context-template.md` and give the user the completed document, not a description of it.

**Where files can be written**, save it and tell the user the path, so other skills can be pointed at it.

**Where they cannot**, print the completed document as a single block and tell the user to paste it into any chat where another skill in this library is being used. That is the whole fallback, and it works.

Mark every unknown as `NOT ESTABLISHED` rather than guessing or leaving it blank. A blank field reads as "not applicable"; the marker reads as "go find this", which is what it means.

Close with the two or three gaps most worth closing, and where the answer probably lives.

---

## How other skills use this

Any skill in this library may open by checking for a context document. **It must degrade rather than fail.** A skill that errors because `account-context` has not been run is exactly the prerequisite this library promises never to have.

The pattern is: use it where present, name the assumption where absent, never block on it.

---

## Output

A completed context document containing:

1. **The product** in customer vocabulary, and what it replaced
2. **Segments**, and how the work differs across them
3. **Contract shapes**, terms and notice windows
4. **The value metric**, or the plain statement that none is agreed
5. **What healthy looks like**, including where low usage is intended
6. **Motion and ownership boundaries**
7. **What could not be established**, listed rather than smoothed over

Keep it to two pages. This is a reference other skills read, not a document anyone sits down to enjoy.

---

## Failure modes

- **Re-interviewing someone who already did this.** Step 0 exists for a reason
- **Accepting marketing copy** for the product description. The customer's words or nothing
- **Skipping the value metric** because it came back empty. The emptiness is the finding
- **Recording segments that do not change the work.** If the answer is identical across three segments, there is one segment
- **Guessing at a gap** to make the document look complete. `NOT ESTABLISHED` is the honest field value
- **Writing it once and never revisiting.** Pricing changes, segments get renamed, the renewal owner moves. A context document more than two quarters old should be re-checked before it is trusted

---

## What good looks like

- Another skill reads it and produces a read specific to this business rather than a generic one
- Someone new to the book could read it and know why a flat usage line does or does not matter here
- The value metric is either stated precisely, or its absence is stated precisely
- The gaps are listed, and each one names where the answer probably lives
- It took under ten minutes

---

## Reference files

- `assets/context-template.md` - the blank document to fill
- `references/worked-example.md` - a completed one, for a fictional company, showing the level of specificity that makes it useful
