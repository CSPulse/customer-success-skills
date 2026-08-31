---
name: internal-escalation
description: >
  Gets your own company to act, with the ask and the evidence shaped for the people you are asking rather than for you. Trigger whenever the user says "internal escalation", "escalate internally", "I need engineering to look at this", "get leadership involved", "how do I get this prioritised", "nobody is picking this up", "I need an exception", "raise this with my manager", "who do I go to", or describes needing something from another team on a deadline. It works out who can actually decide, states a specific ask rather than a request for attention, refuses to inflate severity, and plans the follow-through. Use escalation when the customer is the one escalating and the first four hours are customer-facing, and product-feedback when the ask is roadmap consideration rather than action now.
---

# Internal Escalation

This is the opposite direction to `escalation`. There the customer is escalating to you. Here you are escalating inside your own company, usually on their behalf, to people who did not choose this account and are measured on something else.

The failure this exists to prevent: **"can someone please look at this."** It names no decision, no deadline and no owner, so it goes to the bottom of a queue that is sorted by things it does not have.

---

## What this needs

**Shared context.** If an `account-context` document exists, read it first, particularly what customer success can commit to alone. That determines whether you need a decision or only a pair of hands. Where it is absent, carry on and name the assumption.

**Minimum: what you need and by when.** Enough to identify the decider, shape the ask and write it.

**Better with** the account's contract value, the customer commitment already made, and what you have already tried, since the first question you will be asked is what you have already done.

**Best with** your company's actual escalation process, including who owns the area and what severity definitions mean here, because using the existing path is most of what makes this work.

---

## Step 1: Decide what you are actually asking for

Four different things, and they go to different people:

- **A decision.** An exception, a discount, a commitment, a priority call. Goes to whoever holds that authority, and nobody else can give it
- **Work.** A fix, an investigation, a configuration change. Goes through the existing intake path for that team
- **Presence.** An executive on a call, a specialist in a meeting. A calendar ask, and the smallest of the four
- **Cover.** You need someone senior to know, so the account is not a surprise later. Not an escalation at all, and calling it one burns the word

Naming which one it is takes a minute and decides everything after it. Most failed internal escalations are a request for work sent to someone who can only give a decision, or the reverse.

## Step 2: Find who can actually say yes

Not who is senior. Who holds the specific authority.

- The person who owns the area, by name
- What they are measured on this quarter
- Whether they can decide alone or need someone else
- What they have already said about this, if anything

**Use the existing process.** Going around it works once, and it costs you the relationship with the team you went around, who are the people you will need next month. If the process is genuinely broken, that is its own escalation and a separate one.

## Step 3: Shape it for them, not for you

The same situation gets described differently to different audiences, and this is not spin. It is the difference between information they can act on and information they cannot.

- **Engineering** needs severity, scope, reproducibility, what breaks, what the customer-visible symptom is, and what you have ruled out. Not the emotional temperature, not the account's importance
- **Leadership** needs revenue, risk, precedent and the decision they are being asked to make. Not the technical detail
- **Support** needs the history and the account context that stops the customer explaining it a fourth time
- **Sales or the account team** need what changes for the commercial position

Do the translation before sending. A message that reads as a forwarded customer complaint gets handled as a customer complaint.

## Step 4: Write the ask as a sentence with a name and a date

The single structural fix that makes internal escalations work.

**"I need [named person or team] to [specific action] by [date], because [what happens otherwise]."**

Then supply, briefly:

- **What you have already tried.** The first question, always. Not having an answer ends the conversation
- **The deadline and why it is real.** A date invented for urgency is detected quickly and permanently. If the deadline is their notice date or a board meeting, say which
- **What you can accept instead**, if the full ask is not available. Deciding this now prevents an all-or-nothing conversation ending in nothing

## Step 5: Do not inflate

The same mechanic as with product, and the cost is the same: permanent, and paid by every colleague who escalates after you.

- **Severity means what your company says it means.** Marking something critical because you want it looked at today changes nothing except how your next one is read
- **Do not claim churn you would not defend.** Say "this is an annoyance on a healthy account" when it is. That is what makes you believed on the one that matters
- **Do not describe one angry user as the customer**, and do not describe a customer as strategic in place of naming what they pay

## Step 6: Go one rung at a time, and tell people

- **Start at the lowest rung that could actually solve it.** Skipping to the top gets a fast answer once and makes you the person who cannot handle their own book
- **Never escalate over someone without telling them first.** Not as a courtesy, but because they will find out, and the relationship costs more than the escalation is worth. One line is enough: "I am raising this with X tomorrow, wanted you to hear it from me"
- **Give each rung a real chance and a stated deadline.** "If I have not heard by Thursday I am taking it to X" is fair, effective, and it is not a threat if you say it in advance

## Step 7: Own it after you escalate

**Escalation is not delegation.** The most common failure after a successful escalation is the CSM disappearing, on the theory that it now belongs to someone else.

- Stay the single point of contact for the customer
- Keep the internal owner supplied with what they need and shielded from what they do not
- Update the customer on your own cadence, not on the internal team's
- Close it: tell everyone who helped what happened, including when the answer was no. This is the entire reason people help you the second time

---

## Output

1. **What you are asking for**: a decision, work, presence or cover
2. **Who can say yes**, by name, and what they are measured on
3. **The ask**, as one sentence with a name, an action and a date
4. **What you have already tried**
5. **Why the deadline is real**
6. **The version shaped for this audience**, with the honest severity
7. **The ladder**: which rung, what the next one is, and by when
8. **Who you told before escalating over them**
9. **What you could not check**

---

## Failure modes

- **"Can someone look at this."** No decision, no deadline, no owner
- **Asking the wrong kind of person.** A request for work sent to someone who can only give a decision, or the reverse
- **Forwarding the customer's complaint** as the escalation, which gets it handled as a complaint
- **No answer to "what have you tried".** The conversation ends there
- **Inflated severity.** Works once, costs permanently, and the cost is carried by your colleagues
- **An invented deadline.** Detected quickly and remembered
- **Jumping rungs**, which gets one fast answer and a lasting reputation
- **Escalating over someone silently.** They find out
- **Calling it an escalation when you only wanted someone to know.** It devalues the word for when you need it
- **Disappearing afterwards.** Escalation is not delegation
- **Never closing the loop internally**, which is why the same people are slower to help next time

---

## What good looks like

- The ask is one sentence with a named person, a specific action and a date
- What you had already tried was in the first message
- The deadline is real and its source is named
- Severity is what the company's own definition says, not what you wanted it to be
- The person you went over heard it from you first
- You still owned the customer relationship throughout
- Everyone who helped was told how it ended, including on a no

---

## Related skills

- `escalation` when the customer is the one escalating, and the first four hours are customer-facing
- `product-feedback` when the ask is roadmap consideration rather than action now
- `hard-conversation` for what you say to the customer while this is running
- `exec-conversation` when the escalation ends with an executive meeting on their side
- `renewal-risk` for whether the underlying situation actually threatens the renewal

---

## Supporting files

None. The output is a message and a ladder, both short enough that a template would be longer than the thing itself.
