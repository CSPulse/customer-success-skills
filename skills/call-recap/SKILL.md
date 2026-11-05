---
name: call-recap
description: >
  Use when the user says "recap this call", "here is the transcript", "what do I owe after that call", "write the follow-ups", "emails from this call", "what did you make of that call". Produces a 150-word honest read, a table of every email the call generated, each draft in chat, and a 5-line CRM note. Not for preparing a call (use call-prep) or polishing an email already written (use email-critic).
---

# Call Recap

An honest read of the call, every email it created (not just the recap), and a CRM note, all in chat from a pasted transcript.

## Start here

If the user pasted a transcript, go. Otherwise ask for it in ONE message with the attendee names and the call date, and say a summary alone gives a shallower read. Never build a recap from a title, an invite or a link you cannot open.

If a recorder or mailbox is connected, you may fetch the transcript and look up addresses and threads. Otherwise use what was pasted and mark gaps.

If an "Account context" block exists in the conversation, use it. Auto-transcripts mangle names, so check spellings against what the user typed.

## Do this

1. **Read the transcript, not the summary.** Customer wording lives in the specifics, and summaries keep categories and drop them.
2. **Write the honest read in 150 words or fewer:** what moved and who committed, what is at risk (especially promises resting on work nobody has started), the opening that went past, the sharpest customer line quoted, and whether any "needs approval" block was real. Say so plainly if the call was warm and moved nothing.
3. **List every email the call generated, from commitments not topics.** Each "I will send", "can you introduce me" and "let us find time" is an email, including internal ones. Group by recipient: one email per recipient, one ask each.
4. **Ground every claim** before it reaches a draft. Tag what was said on the call with the line it came from. What is already true (sent, signed, promised earlier) needs the user to confirm. Product, price and security statements are flagged, never asserted.
5. **Draft each email in chat.** Short, ask near the top, the customer's own words where they help. Flags go under the draft, never inside it. Read each once as the recipient.
6. **Write the CRM note:** exactly five lines.

## Output

```
CALL READ: [Account] | [date] | [attendees]
[150 words or fewer: moved / at risk / missed / sharpest line in quotes]

EMAILS THIS CALL GENERATED ([n])
| # | To | Purpose | Reply or new | Send when |

DRAFTS
1. To: [name, address or "[address needed]"]  Subject: [subject]
[body]
Flag: [grounding gap, product claim, or whose email this really is]

CRM NOTE
Outcome: [one line]
Commitments ours: [what, by when]
Commitments theirs: [what, by when]
People: [new names, roles, what they own]
Risk and next step: [one line, with a date]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Load `references/email-craft.md` when drafting a forwardable note, an intro nudge or a follow-up.

## Rules

- **One email per recipient.** Topic-shaped emails make the customer reconcile three threads. The exception is a note meant to be forwarded, which cannot carry an unrelated ask.
- **The transcript hedge belongs in the email.** "Let us look at that" is not "we agreed", because an upgraded maybe becomes a promise the user now owes.
- **Never write "as discussed, we sent X" unless the user confirms it was sent.** Calls compress memory, and a false "sent" either exposes a miss or sends them looking for nothing.
- **Never guess an address or a spelling.** Write "[address needed]" because a wrong send to a senior person costs more than the question.
- **Context goes in the flag, the ask goes in the email.** The customer wants to answer fast, not read the reasoning.
- **Someone else's topic is someone else's email.** If the CEO told them they would come back on terms, mark who should confirm before the user proposes any.
- **Order the sends.** An email that waits on another (a date from engineering, an intro) goes second, because sending it early commits the user to something unconfirmed.
- **A newer written record beats the call.** Where an email or contract disagrees with what was said aloud, say they disagreed rather than silently picking one.
- **Hold flagged drafts back.** A draft with an unverified security or price claim is one keystroke from a customer, so say which drafts are not ready.
- **Name the weak call.** Warm rapport with no adoption conversation is a weak call, and a flattering read cannot be acted on.

## Related (only if installed)

`call-prep` before the next call. `email-critic` to check a draft against the transcript. `stakeholder-map` when a new name matters.
