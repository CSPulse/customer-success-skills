# email critic

**Not "is this polished" - would an exceptional operator send this, to this customer, at this point, and get back what they need.**

Most email review is a polish pass - tighten the sentences, fix the tone, call it done. Polished emails fail constantly, because the damage was never in the phrasing: it was the claim that upgraded "let's look at that" into "as agreed," the objection that quietly dropped out of the recap, the ask buried in paragraph four, or the commitment nobody actually made on the call.

This skill stress-tests a draft against its actual source - the call transcript, the thread it's replying into, account notes, a voice guide - rather than judging the writing alone. It checks accuracy against what happened, completeness against what the customer will notice missing, whether there's a clear ask near the top, and how it reads from the customer's chair. It gives a verdict scaled to the draft, from "send it" to "do not send it" and why, and never invents a numeric score, because a score the model is about to justify with its own rewrite ends up driving the edit.

The bar is not politeness. It is whether an exceptional customer-facing operator would send this to this customer, at this point in this relationship, and get what they need back.

Part of the **Write to the customer** group in [customer-success-skills](../../#readme).

---

## What it actually does

| Step | What you get |
| :--- | :--- |
| Establish what the email is for | The purpose named plainly - recap, nudge, escalation, ask, bad news - or a flag that the purpose is unclear |
| Pull the source | The call transcript, the thread, account notes, or a voice guide read before judgment, not after |
| Check accuracy | Every claim tested against what actually happened - no upgraded commitments, no invented agreements |
| Check completeness | Anything the customer will notice missing - a concern, a question, an owner, a date |
| Check the ask | Whether there is one, whether it's near the top, and whether it's asking the customer to do work they shouldn't have to |
| Read it as the customer | Whether it sounds like a partner or a vendor chasing something, and whether they'd reply today |
| Give a scaled verdict | Send it as-is, a short list of fixes, or a full rewrite - weighted to how much work the draft actually needs |
| Rewrite without inventing | A tightened version that keeps every fact, commitment, and the user's own voice - and flags anything it couldn't verify |

---

## Who this is for

Anyone about to send a customer-facing email who wants a straight read before it goes - CSMs sanity-checking a recap, a follow-up, an escalation, or a note they know will get forwarded to someone's legal team. It runs on a draft that already exists; for a recording with no draft written yet, `call-recap` is the starting point instead.

---

## What this needs

**Minimum:** the draft. Paste it and the review runs - it covers the writing but not the facts, and says so rather than implying otherwise.

**Better with:** the call transcript, the thread being replied into, account or contact notes, and a voice guide. Each one moves a check from "cannot verify" to "verified," and the accuracy check is the one that catches real damage.

Missing context never blocks this skill - it changes what the review can honestly claim, not whether it runs.

---

## Install

**The easy way: one paste**

```
I want to install the email-critic skill from
https://github.com/CSPulse/customer-success-skills. Download or clone the
repository, then copy the skills/email-critic folder into
~/.claude/skills/ (or .claude/skills/ if this is for one project only),
keeping its own folder name. Tell me the exact folder path it landed in
when you are done.
```

**In the Claude app (no terminal needed)**

1. Download this repository as a ZIP, or clone it
2. Zip the `skills/email-critic` folder on its own
3. In Claude, go to Customize, then Skills, then Create skill, then Upload skill
4. Upload the ZIP

**As a plugin, in Claude Code or Cowork**

```
/plugin marketplace add CSPulse/customer-success-skills
/plugin install customer-success-skills@cspulse
```

**Want the whole set?** The [main README's install section](../../#readme) installs all 32 skills at once.

**Or just read it.** `SKILL.md` is the method, and `references/by-email-type.md` breaks down the specific failure mode of a meeting recap, a follow-up, an escalation, a forwardable note, an executive email, and an intro request - worth a read on its own before you write the next one.

---

## What this does not do

- Does not manufacture criticism to look rigorous - if the draft is good, the answer is "send it"
- Does not assign a numeric score, because a score the model is about to justify with its own rewrite ends up driving the edit
- Does not add a commitment, concern, or next step that was not in the original - a recap becomes the customer's record
- Does not launder an unverifiable claim into cleaner prose - it pulls it out and flags it instead
- Does not recommend a fix that depends on something unverified - a meeting that already lost its attendees, a person who is on leave, a document nobody produced

---

MIT licensed. Part of [customer-success-skills](https://github.com/CSPulse/customer-success-skills).
