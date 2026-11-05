---
name: internal-ask
description: >
  Use when the user says "feature request", "raise this with product", "I need engineering to look at this", "get leadership involved", "I need an exception", "nobody is picking this up", "how do I get this prioritized". Writes the ask that gets your own company to act: lane A a product or engineering request framed as the job to be done, lane B an urgent ask of leadership, finance or legal in one sentence. Not for a customer escalating to you (use escalation) or news for a customer (use hard-conversation).
---

# Internal Ask

The user walks away with an internal request shaped for the people who must act, an honest size and severity, and the message to close the loop with the customer.

## Start here

If the user has said what they need, from whom, and by when, go. Otherwise ask in ONE message:

1. What the customer or account needs, and the date it matters
2. Who in your company owns the answer, if known
3. What you have already tried

Lane test: if the answer is a decision that one person can give this week, it is lane B. If it needs engineers to build or change something, it is lane A.

Never wait. If an "Account context" block exists in the conversation, use it. Gaps become "(assumed, confirm)".

## Do this

1. **Pick the lane.** A: roadmap or engineering (a gap, a request, a fix). B: urgent decision from leadership, finance or legal (exception, discount, commitment, priority call). If the thing is a bug, send it to support today; if the product already does it, fix that with the customer and do not submit.
2. **Lane A: translate to the job.** The job in the customer's words with no product vocabulary, what they do today, what it costs them in their unit. Record their proposed solution as a proposal, not the requirement. Do not design the fix.
3. **Lane A: size it honestly.** Count accounts with the job, not accounts that used the feature name. Contract value, segment shape, what happens if nothing changes. Write "annoyed, will renew" when that is true.
4. **Lane B: write one sentence**: "I need [named person] to [action] by [date], because [consequence]." Add what you tried, why the date is real and its source, and what you can accept instead.
5. **Check severity against your company's own definition.** Use the existing intake path and cycle, and tell anyone you go over before you do.
6. **Plan the loop.** Lane A: what the customer will be told and when, including on a no, with the honest alternative and no invented timeline. Lane B: you stay the customer's single contact and report back to everyone who helped.

## Output

```
INTERNAL ASK: Lane A / Lane B | [account] | decision or answer needed by [date]

The ask: [Lane B: I need X to Y by Z, because W]
         [Lane A: Product, please consider the job: ...]
Severity: [your company's term, with the reason]
Who can say yes: [name, role] | Path: [intake channel, cycle date]

Lane A
- Job (customer words): ...
- Today and what it costs: ...
- Accounts with the job: [n] | Value: $[x] | Segment: ...
- Customer proposed (not required): ...
- If nothing changes: ...
Lane B
- Tried so far: ...
- Why the date is real: [source]
- Acceptable fallback: ...

Evidence: [said / seen / inferred] [fact, source, date]
Customer message: [what they hear, when, including on a no]
Follow-through: [owner, next rung, deadline]

What I could not check
- [gap]
```

A filled example is in `examples/sample.md`.

## Rules

- **A request needs a name, an action and a date.** "Can someone look at this" has no owner, so it sinks to the bottom of a queue sorted by those things.
- **Forwarding the customer email transfers the request but none of the information.** It puts translation on the person least equipped and gets handled as a complaint.
- **Count jobs, not feature names.** Two requests for one job are one case, and finding that is most of the value you add.
- **Never inflate.** "They will churn" is checkable at the renewal, and the CSM who says it and is wrong is ignored next time, by everyone.
- **Use the existing path.** Going around it works once and costs the goodwill of the team you need next month.
- **Do not go over anyone silently.** They find out, so give them one line and a stated deadline first.
- **Close the loop, especially on a no.** Silence makes customers and colleagues stop telling you things; a clear no with an alternative is respected.
- **Escalation is not delegation.** Stay the customer's single contact, or the ask stalls and the customer hears nothing.

## Related (only if installed)

`renewal-risk` to test whether the gap truly threatens the renewal. `hard-conversation` to deliver a no. `churn-postmortem` when a gap caused a loss.
