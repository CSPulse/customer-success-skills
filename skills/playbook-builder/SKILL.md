---
name: playbook-builder
description: >
  Use when the user says "build a playbook", "turn this into a play", "we keep handling this differently", "write the play for", "make this repeatable", "standardize our response to". Turns a recurring situation (low adoption at day 45, a champion who left, a price increase) into a one-page play a team can adopt: trigger, owner, dated steps, exit criteria, message templates, what to measure. Not for one account's plan (use account-plan) or the message announcing a change to customers (use customer-update).
---

# Playbook Builder

A one-page play for a recurring situation, so every CSM on the team responds the same way and the response can be improved.

## Start here

If the user named the situation and what the team does today, go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back:

1. The situation, and roughly how often it happens ("new accounts go quiet after kickoff, a few a month").
2. What the team does today and where it goes wrong or differs by person.
3. Who would own the play, and how big the team is.

Anything missing is assumed and tagged `(assumed, confirm)`. If an "Account context" block exists in the conversation, use it for segments and contract shapes. If the user has a past case, ask for it: it becomes the test in step 7.

## Do this

1. **Write the trigger as something observable.** A signal, a threshold, a date or day count, who or what detects it, and how often it is checked. "Feels at risk" is not a trigger. Thresholds are a common default, set your own.
2. **Name one owner by role, and a backup.** Say what is not the owner's job and who they escalate to. A play with a team as owner has no owner.
3. **Write four to seven steps.** Each has an action, a day count from the trigger, and the thing that exists afterwards (a note in the record, a booked call, a changed plan). The first step lands within two business days. The last step is a decision.
4. **Write exit criteria in both directions.** Resolved means something observable, not "feels better". Escalate means what happens, who is told, and by which day. A play with no end becomes a status.
5. **Draft two or three message templates** in plain words with bracketed fields: the opening note to the customer, the invite to the working session, the escalation note to the manager. Drafts only; the owner edits and sends.
6. **Choose three measures:** one for whether the play ran (step one on time), one for whether it worked (exit criterion met by the deadline), one for cost (owner hours, customer reaction). Add a review date, for example after ten uses or one quarter.
7. **Test it on one real past case.** Walk it through the play. Where it breaks, fix the play. Report what the test changed.

## Output

Lead with the one-line verdict. Use this skeleton exactly:

```
PLAY READY: [name]. Trigger [signal], owner [role], ends by day [n].

Use when: [trigger: signal, threshold, detected by, checked how often]
Do not use when: [look-alikes that need a different play]
Owner: [role] | Backup: [role] | Escalates to: [role]

Steps
1. Day [n] | [action] | Leaves behind: [artifact]
...
Resolved when: [observable]
Escalate when: [observable] by day [n]: [who is told, what changes]

Messages (drafts): [short templates with bracketed fields]
Measures: ran on time | worked by deadline | cost. Review: [date or count]
Test case: [past case, what it changed in the play]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`. Match its shape and length.

## Rules

- **One trigger, one play.** A play that fires on three different signals gets three different responses and cannot be measured.
- **The trigger must be observable by someone who did not follow the account.** Otherwise it depends on one CSM's memory, which is the problem the play exists to remove.
- **The play ends.** A deadline and an escalation turn a monitoring habit into a response, because open-ended plays decay into status updates.
- **Say what not to do.** The failure shared by most CSMs, such as a generic check-in email, goes in the play as a stated mistake.
- **Write the response into the account record.** The next person on the account, or the review of the play, can only learn from what was written down.
- **Keep it to one page.** A play longer than a page is not opened in the middle of a week, so cut steps before adding them.
- **Templates are drafts, not scripts.** A customer can tell a pasted message, so the template carries structure and the owner supplies the specifics.
- **Do not build a play for a one-off.** Wait for the situation to recur at least three times (a common default, set your own), or the play fits an anecdote.

## Related (only if installed)

`account-plan` for the plan on one account. `customer-update` when the play needs a message to many customers. `coaching` for training the team on the play once it exists.
