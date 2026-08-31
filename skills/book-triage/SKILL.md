---
name: book-triage
description: >
  Decides which accounts get your attention this week, against a book too big to cover evenly, and writes down which ones deliberately do not. Trigger whenever the user says "book triage", "which accounts should I focus on", "prioritise my book", "I have too many accounts", "where should my time go", "who needs me this week", "I cannot cover them all", "my book is too big", "triage my accounts", or describes being spread thin across a portfolio. It sorts by what changed and what can still be influenced rather than by size or by health colour, flags the accounts nobody has logged a touch on, and forces an explicit not-this-week list. Use weekly-plan to turn the resulting list into hours, and renewal-risk for the depth read on any one account it surfaces.
---

# Book Triage

Even coverage is not the goal. It is the failure. A book of forty accounts touched equally is forty accounts touched too lightly to change anything, and the CSM doing it feels busy and is not moving a single outcome.

The job is to decide where attention goes and, harder, to write down where it does not.

The failure this exists to prevent: **the week spent on the accounts that asked.** Attention allocated by who emailed loudest, which correlates with neither risk nor value, and which systematically starves the quiet accounts where the actual danger is.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first: the segments, the contract shapes and what healthy usage looks like here. Without it, "usage dropped" cannot be told apart from a normal seasonal pattern. Where it is absent, carry on and name the assumption.

**Minimum: your account list, with renewal dates and rough values.** Enough to triage, though it will lean on what you know rather than on data.

**Better with** usage trend, support activity and last-contact dates. The last one is the single most valuable field and the one most often missing.

**Best with** health scores you know the composition of, and a stakeholder picture, so movement can be read rather than guessed at.

---

## Step 1: Sort by movement, not by state

The most common triage error is ranking by health colour or by size, both of which are largely static. A red account that has been red for six months does not need you this week. An account that moved from green to amber last Tuesday does.

For each account ask **what changed**, in the last two to four weeks:

- Usage direction, particularly composition and breadth rather than level
- A person: someone arrived, left, changed role, or stopped replying
- A commercial event: an invoice, a procurement enquiry, a utilisation request
- Support: type and who is filing, not volume
- Something on their side: their results, a reorg, a public event

**No change is a legitimate answer and it earns a lower rank**, not an automatic touch.

## Step 2: Add the dates that cannot move

Independent of movement, some accounts have a clock:

- Renewal date, and more importantly **notice date and budget lock**, which come earlier
- A commitment you made with a date on it
- A scheduled review or executive meeting
- An onboarding milestone

An account with a notice date in three weeks outranks a larger one with nine months to run, whatever the health colour says.

## Step 3: Ask where you can actually change the outcome

The step that separates triage from a worry list. For each candidate: **if I spend four hours here this week, does anything move?**

- **Yes, and only I can do it.** Top of the list
- **Yes, but it needs someone else.** The action is arranging that, which is often twenty minutes rather than four hours
- **No, the decision is already made.** After a replacement is procured, budget reallocated, or the notice date passed, effort here is theatre. Say so plainly rather than spending the week proving it
- **No, nothing is wrong.** Leave it alone

Attention spent where nothing can move is the most expensive kind, because it feels like work.

## Step 4: Find the silent accounts, deliberately

**The accounts with the fewest logged touches are disproportionately risky and disproportionately rated healthy.** Nobody is worried about them because nobody has spoken to them.

Sort by last real contact, not by last automated email, and look at the bottom. Then ask an uncomfortable question about each: is this account quiet because it is fine, or because I have been avoiding it. A CSM's own avoidance is a signal and no health score captures it.

At least one silent account goes on the list every week, chosen deliberately rather than when it becomes a problem.

## Step 5: Weight by value, but only after the above

Contract value is a multiplier, not a sort order. Applied first it produces a book where the largest accounts absorb every hour regardless of whether anything is happening.

Apply it to break ties, and to decide depth rather than inclusion: a small account with a real event still gets thirty minutes, and a large account with nothing happening still gets nothing this week.

Also read the concentration honestly. If three accounts are half the book, they carry standing attention that is not a triage decision at all.

## Step 6: Write the not-this-week list

**The part everybody skips, and the part that makes this a decision rather than a wish.**

Name the accounts you are consciously not touching, and for each one the trigger that would change that: a date, an event, a signal you are watching for. Then it is a decision with a review point rather than neglect you have not admitted to.

Two things it buys. You stop carrying forty accounts in your head, which is where the low-grade dread comes from. And when one of them goes wrong, you can say what you knew and what you decided, which is a completely different conversation from being surprised.

**Where the tail is permanently unservable, that is a `coverage-model` problem, not a triage problem.** Say so upward rather than absorbing it weekly. A book that cannot be covered at any allocation is a design fault, and quietly compensating for it hides the evidence.

## Step 7: Set the cadence and keep the list short

- **Weekly.** A quarterly triage is a plan, not a triage, and it is stale within a fortnight
- **Five to eight accounts.** More than that and it is a list rather than a decision
- **Carry the reason.** Each account gets one line saying what changed and what you will do, so the list is actionable on Monday without re-deriving it
- **Compare with last week.** An account appearing three weeks running with nothing moving is a signal about the action rather than the account

---

## Output

1. **This week's list**, five to eight accounts, each with what changed and what you will do
2. **The clock accounts**, with the date that is actually binding
3. **At least one silent account**, chosen deliberately
4. **The not-this-week list**, with the trigger that would change each
5. **Anything where nothing can move**, named as such rather than left on the list
6. **What you could not check**

`assets/triage-sheet.md` is the same structure as a one-page weekly sheet.

---

## Failure modes

- **Even coverage.** Forty accounts touched too lightly to move anything, and it feels like diligence
- **The week spent on whoever asked.** Loudness correlates with neither risk nor value
- **Sorting by health colour or by size**, both largely static, so the same accounts surface every week
- **Ignoring the silent accounts**, which are disproportionately risky and disproportionately rated healthy
- **Mistaking your own avoidance for their stability**
- **Working accounts where nothing can move**, which is the most expensive attention because it feels like work
- **No not-this-week list**, so the whole book is carried mentally and none of it is a decision
- **Triaging quarterly.** Stale within a fortnight
- **A list of twenty**, which is the book again with extra steps
- **Absorbing an uncoverable book quietly**, which hides the evidence that the coverage model is wrong

---

## What good looks like

- The list is short enough to act on Monday morning without re-deriving it
- Every entry says what changed, not just that the account exists
- At least one account on it is one nobody has heard from
- The not-this-week list exists, in writing, with triggers
- Accounts where nothing can move are named rather than worked
- The binding dates are notice and budget lock, not the renewal date
- Nothing is on the list three weeks running with nothing moving

---

## Related skills

- `weekly-plan` to turn this list into hours, which is the next step and a different question
- `renewal-risk` for the depth read on any account this surfaces
- `health-read` when the score is doing the sorting and you do not know what is in it
- `account-plan` for the accounts that earn a durable plan rather than a weekly decision
- `account-context` for what normal looks like, without which movement cannot be read

---

## Supporting files

- `assets/triage-sheet.md` - the weekly one-pager, usable without an assistant
