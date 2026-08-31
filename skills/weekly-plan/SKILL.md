---
name: weekly-plan
description: >
  Shapes the week around the accounts that move rather than around the calendar that filled itself. Trigger whenever the user says "weekly plan", "plan my week", "how should I spend this week", "my calendar is full", "I have no time for proactive work", "plan Monday", "week ahead", "I am drowning", "everything is reactive", or describes a week where meetings have consumed the time. It starts from what has to be true by Friday, protects one block for the work that has no deadline, batches the reactive load, names the meetings to decline or shorten, and closes the week on what actually moved. Use book-triage first to decide which accounts deserve the time, since that is a different question from how the hours are arranged.
---

# Weekly Plan

A calendar left alone fills with other people's priorities. Not through anyone's fault: reactive work has deadlines attached and proactive work does not, so it wins every collision, every week, forever.

The failure this exists to prevent: **the full week where nothing moved.** Forty hours, thirty meetings, every one of them legitimate, and not one account in a different position on Friday than it was on Monday.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first, though this skill leans on it less than most. Where it is absent, carry on.

**Minimum: your calendar and a sense of what is urgent.** Enough to produce outcomes, a protected block and a decline list.

**Better with** the output of `book-triage`, which answers which accounts deserve the time. Without it, this skill arranges hours around whatever is loudest, which is the problem it exists to solve.

**Best with** an honest record of where last week actually went, because almost nobody's estimate of that survives contact with the evidence.

---

## Step 0: Decide the accounts before the hours

**Run `book-triage` first.** Which accounts and how the hours are arranged are different questions, and doing them in the wrong order produces a beautifully organised week spent on the wrong accounts.

If triage has been done, bring its list here. If not, do it, even roughly. Ten minutes of triage changes more than an hour of scheduling.

---

## Step 1: Write what has to be true by Friday

Three outcomes. Not a task list.

The difference matters. A task is "send the renewal proposal". An outcome is "the renewal proposal is with the buyer and a review meeting is booked". The first can be done on Friday afternoon and achieve nothing; the second forces the sequencing backwards.

Each outcome should be something a colleague could verify on Friday without asking you how it went.

**Three is the number.** Five outcomes is a wish, one is an under-used week.

## Step 2: Work backwards from the outcomes, not forwards from Monday

For each outcome, what has to happen and by when, including the parts that are not yours.

- **Anything needing someone else moves to Monday.** The single highest-value scheduling rule available. A request sent Wednesday for something needed Friday is a request that fails, and it fails in a way that looks like the other person's problem
- **Identify the one thing each outcome is actually blocked on.** Usually a decision, an introduction or a piece of information, and usually it is one thing
- **Put the hard thing early in the week and early in the day.** The avoided call does not get easier by Thursday, it gets more expensive

## Step 3: Protect one block for the work with no deadline

Proactive work loses to reactive work in every direct collision, because one has a date and the other does not. The only reliable fix is to give it a date by putting it in the calendar as an appointment.

- **One block, two hours, same time every week.** Consistency matters more than the size
- **Named for the specific thing**, not "proactive time", which is what an empty block gets called before it is given away
- **Treated as a real meeting.** If you would not cancel a customer call for the thing asking you to cancel this, do not cancel this

This is where the silent account from triage gets touched, the account plan gets updated, and the thing nobody is chasing you for gets done. Skip it for three weeks running and the book quietly reverts to whoever emails.

## Step 4: Batch the reactive load

Email, tickets, internal requests and Slack expand to fill whatever space they are given, and handled continuously they fragment every hour into pieces too small for anything else.

- **Two or three windows a day**, and a stated response expectation so nobody is waiting unknowingly
- **Genuine emergencies interrupt.** Everything else waits for a window. Very little is a genuine emergency, and the things that are will find you
- **Batch by type rather than by arrival.** All the CRM updates together, all the internal replies together. The switching cost is the real expense, not the work

## Step 5: Cut the calendar honestly

Look at every recurring meeting on the week and ask what it produces.

- **A recurring call with no outcome should be cancelled, shortened or made an email.** Proposing that to a customer usually buys credibility rather than spending it, because they have been wondering too. `call-prep` Step 1 covers what to do when a call has no outcome
- **Internal meetings where you are an observer.** Ask for the notes
- **Anything where you are the fourth person from your company.** Two of you is coverage, four is an audience
- **The meeting that exists to prepare for another meeting.** One of the two is unnecessary

Every hour you decline is an hour that goes to Step 3, and that is the trade worth naming out loud when you decline it.

## Step 6: Leave the week some slack

A week planned to capacity breaks on Tuesday, because something always arrives.

- **Leave a fifth of it unscheduled.** Not free time, absorption capacity
- **When nothing arrives, it goes to Step 3.** Which is a good week, not a wasted one

A plan with no slack is not a plan, it is a forecast that will be wrong by Tuesday afternoon.

## Step 7: Close the week

Fifteen minutes on Friday, and it is what makes next week's version better rather than identical.

- **What moved**, against the three outcomes, honestly
- **What did not, and why.** The reason matters more than the fact. Blocked on someone else, underestimated, or displaced by something reactive are three different problems with three different fixes
- **What carries**, and whether it should. Something carried three weeks is not a task, it is a decision you have not made
- **Where the time actually went**, roughly. Nobody's estimate survives this, and one honest look is worth more than any planning technique

---

## Output

1. **The triage list**, brought from `book-triage`, or a note that it was skipped and why
2. **Three outcomes**, verifiable by someone else on Friday
3. **The backward plan**, with everything needing another person on Monday
4. **The protected block**, named for its specific thing
5. **The reactive windows**, and the stated response expectation
6. **The decline list**, and what each declined hour is being traded for
7. **The slack**, roughly a fifth
8. **The Friday close**: what moved, what did not and why, what carries

`assets/weekly-sheet.md` is the same structure on one page.

---

## Failure modes

- **Planning hours before deciding accounts.** A well-organised week on the wrong book
- **A task list instead of outcomes.** Tasks can all be done while nothing moves
- **Five outcomes**, which is a wish
- **Requests to other people sent late in the week**, which fail in a way that looks like their fault
- **No protected block**, so proactive work loses every collision it will ever have
- **Calling the block "proactive time"**, which is the name an empty block has before it is given away
- **Continuous email**, which fragments every hour into pieces too small to use
- **Keeping a recurring call nobody can name an outcome for**, on both sides
- **A week planned to capacity**, which breaks on Tuesday
- **No Friday close**, so next week is identical to this one
- **Carrying the same item three weeks** and treating it as a task rather than an unmade decision

---

## What good looks like

- The three outcomes were decided before the calendar was looked at
- Everything needing someone else went out on Monday
- The protected block survived the week and had a specific name
- At least one recurring meeting was declined, shortened or converted
- A fifth of the week was unscheduled and it absorbed what arrived
- Friday's review said what did not move and why, not just what did
- Nothing has been carrying for three weeks unexamined

---

## Related skills

- `book-triage` first, to decide which accounts deserve the time
- `call-prep` for the recurring call that cannot name an outcome
- `account-plan` for the durable work the protected block usually serves
- `internal-escalation` when an outcome is blocked on someone else and Monday's request went unanswered

---

## Supporting files

- `assets/weekly-sheet.md` - the one-page week, usable without an assistant
