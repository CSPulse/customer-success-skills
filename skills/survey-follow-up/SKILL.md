---
name: survey-follow-up
description: >
  Use when the user says "NPS response", "detractor", "low CSAT", "the survey came back", "they scored us a", "we got a promoter", "nobody answered the survey". Produces what the response means for this person and account, the move and its deadline, a draft message, the call questions, and how to log the risk. Not for asking a happy customer for a reference (use advocacy-ask) or a customer already escalating (use escalation).
---

# Survey Follow Up

A survey response turned into the right move, a draft, and an entry for the account record. Draft only, the user sends.

## Start here

If the user pasted the score, the scale, who answered and their comment, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. Score and scale (NPS 0 to 10, CSAT 1 to 5), the exact comment, and the date
2. Who answered: name, role, buyer or end user. Was the survey anonymous?
3. How many were sent and how many replied, plus the account's renewal date and any open issue

If an "Account context" block exists in the conversation, use it to judge health. Never block on a missing item.

## Do this

1. **Classify the response.** NPS: 0 to 6 detractor, 7 to 8 passive, 9 to 10 promoter. On other scales name the cut (a common default for CSAT: 1 or 2 is low, set your own). No response is its own category.
2. **Read who is speaking.** A score is one person. Say their role, whether they sign or use, and who did not answer. Never average scores across people.
3. **Set it against the account.** Health, renewal date, open issues. A low score from a signer is account risk. From a user at a healthy account it is person-level risk, still worth a fast call.
4. **Pick the move and its deadline.** Detractor: a call within about 48 hours (a common default). Passive: one question, "what would make it a 9?". Promoter: thank first, ask for advocacy only if the gate below passes. No response: try another person or channel.
5. **Draft the first message.** Detractor: request a call, thank them, no defense, no explanation. Include 3 call questions and a 4-line written follow-up to send within a working day of the call.
6. **Write the log entry:** risk level (person or account), the verbatim reason, the owner, and the signal that would escalate it.
7. **Check anonymity.** If the survey was anonymous, reply to the group, never to a guessed person.

## Output

```
SURVEY READ: [Account] | [survey, score, scale] | [who, role] | [date]
Category: DETRACTOR / PASSIVE / PROMOTER / NO RESPONSE - [what it means here]
Whose voice: [person] speaks for [themselves / a team]. Replied [n] of [n]. Silent: [who]

Move: [action] by [day, date]
Draft: [message]
Call questions: [3, in order]
After the call (within 1 working day): [4 lines: heard, will do, who, by when]

Log: [person / account risk] | [verbatim reason] | owner [x] | review [date]
Escalate if: [observable signal]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`.

## Rules

- **Call a detractor, do not email.** A written reply to a low score reads like a form, and the call within about 48 hours is when the person still wants to be heard.
- **Listen first and do not defend.** Explaining the product to an unhappy user ends the conversation, and a customer who stops telling you is the real churn.
- **Do not argue with a score.** It is a feeling on one day, so take the comment as the data and the score as the invitation.
- **Never average across people.** Scores of 9, 8, 8, 7 and 3 average 7.0 and give an NPS of 0, and neither number shows the one person who has a problem.
- **Silence is not consent.** Low response means the unhappy mostly stay quiet, so a good score from a few says little about the many who did not reply.
- **Close the loop in writing, including a no.** Feedback that vanishes teaches people that surveys are theater and lowers the next score. Promise an answer by a date, never a fix.
- **Ask a promoter for advocacy only if the account is healthy, has proof, and has not been asked in about 90 days (a common default, set your own).** The happiest customers get asked most and burn out. Otherwise thank them and ask what is working.
- **Log person-level risk as person-level.** Marking the whole account amber on one user's score trains the team to ignore flags.

## Related (only if installed)

`advocacy-ask` when a promoter passes the gate. `internal-ask` when the comment names a product gap. `escalation` if the detractor is a senior person who is already angry.
