---
name: account-context
description: >
  Use when the user says "account context", "set up my context", "teach you my business", "my skills feel generic", "what does healthy look like for us". Runs a 60 second intake (five questions, one message) and returns a compact "Account context" block, under 40 lines, to paste into any chat or save. Optional deeper mode. Not for researching one customer (use handoff) or planning an account (use account-plan).
---

# Account Context

The user walks away with a block of facts about their business that makes every other answer specific instead of generic.

## Start here

If the user already pasted notes about their product, segments or contracts, skip to "Do this" and fill the block from those. If an "Account context" block already exists in the conversation, read it back in two lines, ask what changed, and update only that.

Otherwise ask these five questions in ONE message, numbered, and tell the user short answers are fine. Never wait for all five:

1. What does a customer say the product does for them, in their words, and what did it replace?
2. Who buys, who uses, and who signs? Are they different people?
3. Contract shape: seat or usage based, term length, notice period, auto-renew yes or no.
4. What number did the customer actually buy (the measure their leadership would check)? "Nobody knows" is a valid answer.
5. What usage pattern would worry you, and what pattern looks alarming on a dashboard but is fine?

## Do this

1. Fill the block from whatever came back. Use the customer's wording, not marketing copy. If the user pastes website copy, ask once for how a customer described it on a call.
2. Write every unknown as `NOT ESTABLISHED`, never a guess and never blank. A blank reads as "not applicable"; the marker reads as "go find this".
3. Treat an empty value metric as a finding, not a gap to skip. Write it plainly in the block.
4. If the user asks for the deeper mode, add up to six lines: segments and how deployments differ, seasonality, integrations that matter and what breaks if one disconnects, who owns renewal and expansion, what CS does not own, and the one fact a new CSM would get wrong in month one.
5. Keep the block under 40 lines. Tell the user to paste it at the top of any chat, or save it anywhere, and to re-check it when pricing or segments change.

## Output

Lead with the block itself. Then two lines: the gaps most worth closing and where the answer probably lives.

```
ACCOUNT CONTEXT: [Company] | [date]

Product, in customer words: [one sentence]. Replaced: [what they used before]
Buys / uses / signs: [roles]. CS meets the signer: always / sometimes / never
Contract: [model], [term], notice [days], auto-renew [yes/no]
Value metric: [the number the customer bought] or NOT ESTABLISHED
Healthy looks like: [rhythm, breadth]
Low usage is intended: yes / no  [why]
Worries me: [patterns]
Looks bad, is fine: [patterns]
[Deeper mode lines, if asked]

Close next: [two or three gaps, where the answer lives]

What I could not check
- [anything marked NOT ESTABLISHED and why]
```

A filled example is in `examples/sample.md`.
Match its length and specificity: real dates, real counts, no placeholders in the final output.

## Rules

- **Five questions, one message.** A long interview gets abandoned, and a half-filled block used today beats a perfect one never finished.
- **Ask for the buyer separately from the user.** In enterprise these are barely overlapping groups, and most bad risk reads confuse them.
- **The value metric is the highest-yield question.** If nobody can state the number the customer bought, healthy usage can still end in churn, and every later read should carry that caveat.
- **"Looks bad, is fine" is the valuable answer.** Compliance, audit and recovery tools are bought to sit unused; without this line a generic read flags healthy accounts.
- **Record notice periods exactly.** The opt-out date is renewal minus notice, and a wrong notice period moves the real deadline.
- **Facts about price, contract or security come from the user.** Mark them for confirmation; a confident wrong contract term spreads into every draft.
- **Stale context misleads.** Pricing changes, segments get renamed, the renewal owner moves. Date the block and re-check it when anything material changes (a common default is every two quarters, set your own).

## Related (only if installed)


`renewal-risk` and `health-score` read most from this block. `account-plan` uses it to judge what a good year looks like.
