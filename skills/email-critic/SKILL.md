---
name: email-critic
description: >
  Use when the user says "would you send this", "review this email", "tighten this", "does this sound right", "how will the customer take this", or pastes a draft with no instruction. Checks the draft against the call or thread it came from, then returns a plain verdict and a tightened version. Never a numeric score. Not for turning a recording into emails (use call-recap) or a message to a whole list (use customer-update).
---

# Email Critic

The user walks away knowing whether to send the draft, what is wrong with it, and a version that fixes only that.

## Start here

If the user pasted a draft, go. Better with the call transcript or the thread it replies into. If neither is there, ask once, in one message, for:

1. The source: transcript, notes or the customer email being answered
2. Who it goes to and what the user needs back
3. Anything the user already owes this person

Never wait. With no source, review the writing only and say so under What I could not check.

## Do this

1. **Name what the email is for** in one line: recap, nudge, ask, escalation, bad news, forwardable note. If you cannot name it, that is the verdict.
2. **Check facts against the source first.** Every date, number, name, owner and commitment. Flag anything upgraded ("let's look at that" became "as agreed"), anything claimed as sent that you cannot see, anything the user did not commit to. Load `references/by-email-type.md` for the section matching this type.
3. **Check what the customer will notice missing**: the objection they raised, the question they asked, an owner, a date.
4. **Check the ask.** One ask, near the top, small enough to answer from a phone, addressed to a named person.
5. **Read it as the recipient.** Would they reply today, or file it? Does it sound like a partner or a vendor chasing?
6. **Give the verdict**, scaled to the draft: Send it / Nearly there / Needs work / Do not send. Then the tightened version.
7. **Verify the fix is executable.** If the rewrite relies on a meeting happening, a person being available or a file existing, check that against the source too.

## Output

```
Verdict: [Send it / Nearly there / Needs work / Do not send] - [one sentence why]

Purpose: [what this email is for]

Wrong or unverified
- [claim] | source says: [what actually happened] | fix: [change]

What to change
- [specific problem] -> [specific fix]

Tightened version
[subject]
[body, preserving every fact, owner and date]

What I kept and why: [anything that could have been cut but was not]

What I could not check
- [gap]
```

Send it: one sentence and any tiny inline fix, no rewrite. Do not send: say what the email should be before rewriting. A filled example is in `examples/sample.md`.

## Rules

- **Truth before tone.** A clumsy sentence costs nothing; a wrong date or an invented commitment becomes the customer's record of what was agreed.
- **No score, ever.** A number from the model about to do the rewrite starts driving the edit (cutting words to justify a concision figure) instead of fixing the draft.
- **Do not manufacture criticism.** A review that always finds three problems stops being believed. If it is good, say send it.
- **Every criticism names its fix.** "Too long" is noise; "cut paragraphs two and three, they restate one" is feedback.
- **Rewrite only what you named.** Keep the user's voice and every fact, owner and date. A recap becomes the record, so an added next step becomes a real obligation.
- **Pull out what you cannot verify** instead of laundering it into cleaner prose, and flag it.
- **No house style the user has not stated.** Judge against this conversation, not generic taste about punctuation or banned words.
- **A chase must change shape.** If this is the third ask, repeating it harder fails; remove the blocker for them or ask what is in the way.
- **Bad news is a call first.** If the customer has not heard it yet, say the email should be the record of a conversation, not the conversation.

## Related (only if installed)

`customer-update` when the draft goes to a list. `one-pager` when it must be forwarded. `hard-conversation` when it carries news the customer has not heard.
