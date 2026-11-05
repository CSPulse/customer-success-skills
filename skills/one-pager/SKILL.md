---
name: one-pager
description: >
  Use when the user says "one pager", "something they can forward", "my sponsor needs to send this up", "summary for their boss", "leave-behind", "brief for their leadership". Writes the single page a sponsor forwards without editing, conclusion in the first three lines, plus the line the forwarder types above it. Not for a budget case for more scope (use expansion-case), the review meeting itself (use business-review) or a list broadcast (use customer-update).
---

# One Pager

The user walks away with one page, in the sponsor's words, that a stranger can act on in forty seconds, and the covering line to send it.

## Start here

If the user has said what happened, who forwards it and who reads it, go. Otherwise ask in ONE message:

1. What should the reader know or decide
2. Who forwards it, and to whom (the reader was not in the room)
3. The sponsor's own words for the project and metrics

Never wait. If an "Account context" block exists in the conversation, use its value metric as the unit. Gaps become "(assumed, confirm)".

## Do this

1. **Name the document type** before writing: decision (reader must choose), information (reader must hold an accurate view), or advocacy (forwarder is arguing for something). A decision brief with no decision in it is the common failure.
2. **Write the first three lines**: the conclusion; why it matters to them in cost, risk, revenue or time; the ask, or "nothing is being asked."
3. **Use the forwarder's vocabulary.** Their project name, their metric names. No product tiers, no logo, no vendor template.
4. **Add three or four short sections**, each heading meaningful alone. One page means one page; if it does not fit, cut scope.
5. **Make every number theirs and checkable**: their unit, a source and date, estimates labeled with the basis.
6. **Answer the one question the forwarder will get** (cost, what if we stop, is it working, who else): inside the page, briefly.
7. **Write the forwarder line**: one or two sentences the sponsor would actually type. Deliver as body text, not a PDF, and ask the sponsor to read it first.

## Output

```
TYPE: decision / information / advocacy | For: [reader] | Via: [sponsor]

[Line 1: conclusion]
[Line 2: why it matters to them]
[Line 3: the ask, or none]

[Heading]: [short paragraph]
[Heading]: [short paragraph]
[Heading]: [short paragraph]

Numbers: [value, their unit, source, date, actual or estimate]
The question they will ask: [question] - [answer]

Forwarder line: "[what the sponsor types above it]"
Before it goes: sponsor reads it; no claim they do not hold

What I could not check
- [gap]
```

Decision briefs list the options considered and what happens if the reader does nothing.

A filled example is in `examples/sample.md`. `assets/one-pager-template.md` is the same page to fill by hand.

## Rules

- **The sponsor is the client.** Their name is on it when they send it, so a claim they do not already believe gets deleted, and they trust your next page less.
- **Conclusion in the first three lines.** Most readers stop there, and that is a successful page, not a failed one.
- **No logo, no branding.** The moment it looks like a vendor document it is read as a pitch, not as information.
- **Their words, not yours.** Every product or tier name costs a line of explanation and marks the page as external.
- **A number nobody can check is decoration.** Only your dashboard can confirm it, so nobody can disagree, so nobody believes it.
- **Shrinking the font is avoiding the cut.** Length reads as effort to the writer and as an obstacle to the reader.
- **The forwarder line does more work than the page.** Almost nobody writes it for the sponsor, so the highest-leverage sentence is left to someone in a hurry.
- **Ship editable text.** A PDF cannot be pasted into a message, and the sponsor will paste it.

## Related (only if installed)

`expansion-case` when the page is a budget case. `business-review` when it is the leave-behind from a review. `email-critic` on the covering message.
