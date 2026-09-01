# handoff

**Run the handover so the receiving side can actually take it - not the one the leaving side declares done.**

Every handover you've ever received was declared complete by the person leaving - who has every incentive to believe the account is fine and no way to judge whether the person arriving can actually run it. What shows up instead is a folder: documents, a CRM record, a shared drive link, none of the four things that actually matter, because those live in one person's head and leave with them.

This skill flips who defines "complete": the receiver writes or accepts the checklist and marks it done, not the sender. It asks the four questions no system captures - what was promised outside the contract, who the unnamed sceptic is, what nearly went wrong, what the departing owner would do first if they were staying - adapts to three transfer types (sales to CS, CSM to CSM, CS to support, each losing something different when rushed), and keeps the internal transfer separate from the customer's experience of the change, since handling one well does nothing for the other.

The failure this exists to prevent: **the account that arrives as a folder**, with everything documented and nothing that matters.

Part of the **Work it internally** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Step 1: name the type | The specific thing each handover type loses if rushed - the promise (sales to CS), the relationship and folklore (CSM to CSM), or the context that stops the customer re-explaining themselves (CS to support) |
| Step 2: the four questions a folder can't carry | What was promised outside the contract, who the sceptic is, what nearly went wrong and what fixed it, and what the departing owner would do first if they were staying |
| Step 3: the receiver defines complete | The structural fix - one sentence agreed up front: you tell me when this is done, not me |
| Step 4: the mechanics | Contract terms, outstanding commitments with owners and dates, open tickets, stakeholders, access, and the meeting cadence - done briefly, so it doesn't crowd out Step 2 |
| Step 5: live, and time-boxed | Thirty minutes of live conversation over a document, a joint customer call where possible, and a date on the whole thing before the sender's last day |
| Step 6: the customer-facing half | A separate message addressing the customer's real fear - that history disappears and they start over - handled so they never hear it from an auto-reply |
| Step 7: the receiver's first action | One specific thing to do in week one, so the account starts as a starting point rather than a reading assignment |

---

## Who this is for

Anyone giving up an account or taking one on - a CSM leaving a role, a manager reassigning a book, an AE handing a new close to CS, or CS handing a customer into support or a pooled model. It's equally built for the receiver who suspects a past handover never really happened and needs to know what to press on now.

---

## What this needs

**Minimum:** the account and both names. Enough to produce the checklist, the four questions, and the acceptance step.

**Better with:** the account history, open commitments, and the last few months of correspondence - that's where the undocumented promises live.

**Best with:** thirty minutes of live overlap between the two people. Every written handover is a substitute for that conversation, and a worse one.

Missing context never blocks this skill - where an `account-context` document doesn't exist, it carries on and names the assumption instead.

---

## Install

**The easy way: one paste**

```
I want to install the handoff skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/handoff folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/handoff` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method, and `assets/handover-checklist.md` is the same structure as a fill-in checklist, usable without an assistant at all.

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
