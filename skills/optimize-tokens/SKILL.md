---
name: optimize-tokens
description: >
  Token optimization advisor for the user. Triggers in two situations:
  (1) When the user explicitly says "optimize tokens", "reduce tokens", "token efficient", or asks how to prompt better for efficiency.
  (2) When a request is detectably token-heavy - e.g., involves processing many files, large rewrites, multi-step research, full document generation, long context dumps - and a lighter approach could achieve the same result.
  Always prioritize quality over reduction. This skill is about eliminating waste, not restricting output.
  Use this skill proactively when you sense the request could be restructured to save significant tokens without quality loss.
---

# Optimize Tokens

The goal is simple: help the user get the same quality output with less token waste. Not fewer results - fewer unnecessary round-trips, context repetition, and bloated prompts.

**Core principle**: Quality comes first. Token savings that compromise output are not savings - they're regressions. Always confirm the quality bar before optimizing.

---

## What this needs

Nothing. No workspace, no connectors, no files. It works in any chat from the first message.

---

## When this skill fires

### Case 1: Explicit request
The user says something like "optimize my tokens", "how should I prompt this to save tokens", or "make this more efficient."

→ Analyze their current or upcoming request and show them a rewritten version that achieves the same outcome with less waste.

### Case 2: Proactive detection
You detect the request is likely to consume a disproportionate number of tokens due to:
- Large file inputs (pasting full documents when only a section is needed)
- Vague open-ended asks that will require extensive clarification loops
- Requests for full rewrites when targeted edits would suffice
- Repeating context that was already established in this session
- Multi-step tasks where the scope could be batched or narrowed

→ Flag it before starting. Show the optimized version. Confirm before proceeding.

---

## The two-gate confirmation system

Before doing any work, run through these two gates in order:

### Gate 1: Quality check
Always ask (or assess from context): **What quality level does this output need?**

- **Publication / external-facing**: High bar. Don't cut corners. Proceed with full quality even if it costs more tokens.
- **Internal / draft / exploratory**: Medium bar. Optimization is welcome.
- **Quick reference / personal use**: Low bar. Aggressive efficiency is fine.

If unsure, ask: *"This looks like [output type] - should I optimize for speed/efficiency, or does this need full quality?"*

Do not skip this. A token-efficient but wrong output is worse than an expensive correct one.

### Gate 2: Task complexity check
Some tasks are inherently expensive - they require full context, multiple files, or detailed output by nature. Before applying optimization:

Ask yourself: *Can this task actually be made lighter without losing something important?*

If the answer is **no** - e.g., generating a full PPTX deck, doing a deep analysis across 10 files, writing a 2,000-word article - say so clearly:

> "This task genuinely needs full token usage to do it well - [reason]. Want me to go ahead without optimization?"

Wait for confirmation before proceeding.

---

## How to show the optimized prompt

When rewriting or improving a prompt for efficiency, always show it in this format:

---
**What you sent / were about to send:**
> [original request or a paraphrase of it]

**Why it's heavy:**
[1-2 sentences on what's driving the token cost]

**Leaner version:**
> [rewritten prompt - concrete, specific, scoped]

**What changes:**
[What gets cut and why it doesn't affect quality]

**Quality impact:** None / Minimal / Moderate - [brief note]

---

Keep this format tight. Don't over-explain. The goal is for the user to immediately see the difference and decide.

---

## Common optimization patterns

**1. Scope the input**
Instead of: "Here's my whole document, give me feedback"
Better: "Here's section 2 of my doc [paste]. What's unclear or missing?"

**2. Specify output format upfront**
Instead of: "Can you help me with this email?"
Better: "Write a 3-sentence follow-up email to a churned customer. Direct tone. No fluff."

**3. Eliminate context repetition**
If content was already shared earlier in the session, reference it - don't re-paste it.
"Use the newsletter draft from earlier" > pasting the full draft again.

**4. Batch the asks**
Instead of 3 separate messages, combine: "Do X, then Y, then give me Z - all in one response."

**5. Replace open-ended with constrained**
Instead of: "What should I do about this customer?"
Better: "Give me 3 options to handle a churned customer who cited pricing. Bullet format."

**6. Point at context instead of re-explaining**
If a person, project, or piece of context has been explained before, point to wherever it lives - a memory file, a project doc, an earlier message in this session - rather than re-describing it.

---

## What NOT to optimize

Don't suggest cutting these - they protect quality:
- Context that is genuinely new and hasn't been established
- Creative or strategic tasks where exploration is the point
- Tasks with external-facing or high-stakes output
- Tasks the user has confirmed need full treatment (Gate 2)

---

## Tone

Be direct. Don't be preachy about token usage. One flag, one rewrite, one confirmation - then move. The user doesn't need a lecture; they need a better prompt and a green light.
