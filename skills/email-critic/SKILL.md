---
name: email-critic
description: >
  Stress-tests a customer email the user has already drafted and returns a straight verdict plus a tightened version, checked against the source transcript, the account plan and their voice principles rather than in a vacuum. Trigger whenever the user pastes or points at a draft email and asks any of: "is this good", "would you send this", "review this email", "critique this", "tighten this", "make this better", "does this sound right", "too long?", "what would you change", or shares a draft with no instruction at all - a bare draft is a request for a read on it. Also trigger when they say an email "feels off" or ask how a customer will take it. Use this for drafts that already exist; use call-recap when the input is a recording and no draft has been written yet.
---

# Email Critic

The user has a draft. The job is to tell them whether to send it, and if not, why and what to send instead.

The bar is not "is this polished". Polished emails fail all the time. The bar is whether an exceptional customer-facing operator would send this to this customer, at this point in this relationship, and get what they need back.

The failure this exists to prevent: **the draft that is checked for tone and never checked for truth.** A clumsy sentence costs you nothing. A date that is wrong, a commitment nobody made, or a name that has left the company becomes the customer's record of what you agreed, and no amount of polish makes it less wrong.

---

## What this needs

**Minimum: the draft.** Paste it and the review runs. With nothing else to check against, the review covers the writing but not the facts, and it says so rather than implying otherwise.

**Better with** the call transcript, the thread being replied into, account or contact notes, and a voice guide. Each one moves a check from "cannot verify" to "verified", and the accuracy check is the one that catches real damage.

Missing context never blocks the review. It changes what the review can honestly claim.

---

## Before you judge it

Two things first, and skipping them is what makes email feedback useless.

**Know what the email is for.** A recap, a nudge, an escalation, an ask, a piece of bad news, a note designed to be forwarded to someone's legal team. Each has a different shape and a different failure mode. If the purpose is genuinely unclear from the draft, say so - an email whose purpose you cannot name is usually an email the customer will not act on, and that is the most useful thing you can tell the user.

Where the draft goes to a list rather than a person, `customer-update` decides the segmentation and the shape before the wording is worth reviewing. Where the draft is meant to be forwarded to someone who was not in the room, `one-pager` is the format.

Where the draft is bad news the customer has not yet heard, the first question is not about the writing. It is whether this should be an email at all. `hard-conversation` covers that, and the strong version is almost always a call followed by this draft as the record.

**Get the source.** A draft cannot be judged against itself. Where the material exists, read it:

- The call transcript, if the email follows a call. Pull it from whichever meeting recorder is connected, or ask the user to paste it.
- The thread it is replying into, in Gmail or Superhuman. What did the customer actually ask?
- The account or contact notes, if the workspace keeps them, for who this person is and what is already owed them.
- A voice or style guide, if the workspace has one, for how the user writes.

If the user pasted a bare draft with no context and none is reachable, say what you could not check, and be explicit that you are reviewing the writing but not the facts. That distinction matters - most of the damage an email does comes from a wrong fact, not a clumsy sentence.

---

## The checks that find real problems

Work through these against the source, not from the draft alone.

**Accuracy.** Does the email claim something that did not happen? Does it upgrade a "let's look at that" into "as agreed"? Does it say something was sent that you cannot find? Does it commit the user to something they did not commit to on the call? This is the check that matters most and the one a polish pass skips entirely.

**Completeness.** Does it drop something the customer will notice is missing? A concern they raised, a question they asked, an owner, a date. Compressing is good, but a recap that quietly loses the customer's objection reads as not having listened.

**The ask.** Is there one? Is it near the top? Is it obvious what happens next and who does it? Is the user asking the customer to do work they could have done themselves, like reshaping data or picking a slot from nothing?

**The customer's read.** Go through it once as the recipient. Does it show they listened? Does it make the recipient more or less confident in them? Does it sound like a partner or a vendor chasing something? Would they reply today, or move it to later and forget?

**Length against purpose.** The test is not word count, it is whether replying is easier than reading. An executive nudge that runs three paragraphs is too long. A security note that runs a page may be exactly right.

**Voice.** Against the workspace's own voice or style guide, not against generic business-writing taste. The specific ones that recur: em dashes (never), "I" where "we" belongs, banned phrases, an opener that says nothing, a close that trails off.

---

## Say what you actually think

Weak drafts get told they are weak. The useful sentences are specific:

- "You are burying the ask in paragraph four."
- "This changes what was agreed on the call."
- "This answers their question and misses the opening."
- "This is polite and will not get a reply."
- "This sounds like a vendor chasing something."
- "The customer does not need this paragraph."
- "You are asking for something without saying why it matters to them."
- "I would not send this as written."

Two guardrails. Do not manufacture criticism to look rigorous - if the draft is good, the answer is "send it", and a review that always finds three problems is a review the user stops trusting. And every criticism names the fix. "Too verbose" is not feedback; "cut the second and third paragraphs, they restate the first" is.

---

## Scale the response to the draft

Match the weight of the answer to the state of the draft. Nobody needs six sections of analysis on an email that needed one word changed.

**Send it.** Say so in a sentence. Note anything small worth changing inline. Do not produce a rewrite of an email that does not need one.

**Nearly there.** A short verdict, the two or three things to change and why, then the revised email. No headings, no scorecard.

**Needs work.** A verdict, then what works, what does not, the single biggest opportunity from a customer success angle, then the rewrite. Keep the analysis shorter than the email.

**Do not send.** Say that first and say why. Then work out what the email should be doing before rewriting it, because the problem is usually that it is the wrong email rather than a badly written one.

Never give a numeric score. A number invented by the same model that is about to do the rewrite is not a measurement, and once it exists it starts driving the edit - cutting words to justify a conciseness figure rather than because the email needed cutting. The verdict sentence carries the same signal honestly.

---

## Rewriting

Rewrite to fix what you named, and nothing else.

- Preserve every fact, commitment, date, owner and nuance in the original. If shortening would cost one of those, keep it and cut elsewhere, and say what you kept and why.
- Never add a commitment, concern or next step that was not there. A recap becomes the customer's record, so an invented next step becomes a real obligation.
- Keep their voice. If the draft has a line that sounds like them, leave it alone even if you would have phrased it differently. The point is an email they send, not an email you would have written.
- If a claim in the original cannot be verified, do not launder it into cleaner prose. Pull it out and flag it.
- If only two changes are needed, make two changes.

Then check the fix is executable. Advice fails quietly this way: telling the user to raise something at Tuesday's sync when two of the three attendees have already declined it, or to ask a person who is on leave, or to attach documents nobody has produced. Whatever your rewrite depends on - a meeting happening, a person being available, a document existing - verify it the same way you verified the draft's claims. A critique that catches three errors and then introduces a fourth in its own recommendation has not helped.

Close by naming anything that still needs them: a fact you could not check, an address you could not find, a decision that is not yours.

---

## Reference

`references/by-email-type.md` covers what to check for recaps, follow-ups, escalations, forwardable notes, and bad news. Read the section that matches the draft in front of you.
