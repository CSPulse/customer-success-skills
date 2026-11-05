---
name: skill-name
description: >
  Use when the user says "literal phrase one", "literal phrase two", "literal phrase three", or describes [the situation in plain words]. [One sentence on what it produces.] Not for [adjacent job] (use sibling-skill).
---

# Skill Name

One sentence: what the user walks away with.

## Start here

If the user has already given [the minimum input], go straight to "Do this".

Otherwise ask for these in ONE message, then proceed with whatever comes back. Never wait for a complete answer:

1. [Input 1, the one that changes the answer most]
2. [Input 2]
3. [Input 3]

Anything missing becomes a line under "What I could not check", not a reason to stop.

## Do this

1. [Imperative step, one to three lines.]
2. [Imperative step.]
3. [Imperative step.]

Six steps at most. If a step needs more than a screen of explanation, move the detail to `references/` and say when to load it.

## Output

Lead with the verdict or the thing the user will send. Use this skeleton exactly:

```
[Headline: the call, the draft, or the one-line answer]

[Block 1]
[Block 2]

What I could not check
- [gap 1]
- [gap 2]
```

A filled example is in `examples/sample.md`. Match its shape and length.

## Rules

Five to eight judgement rules, each with the mechanism behind it. This is where the skill earns its place over a plain prompt.

- **[Rule].** [Why it is true.]

## Related (only if installed)

One line: which sibling skill to suggest next, and when. Suggest, never require.
