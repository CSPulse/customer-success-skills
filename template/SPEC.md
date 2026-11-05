# Skill spec (v2)

The bar every skill in this library meets. Gold-standard reference: `skills/renewal-risk/` (SKILL.md, `references/`, `examples/sample.md`). Match its shape, density and tone.

## What a skill is here

One job, one fast path to something useful, one filled example of the output. Anyone should be able to install it, paste three lines about an account, and get a result they would forward to their manager.

## Folder

```
skills/<name>/
  SKILL.md             the method, 70 to 150 lines, under 6KB
  examples/sample.md   a COMPLETE filled output for an invented company (required)
  references/<x>.md    depth loaded only when a step needs it (optional, one level)
  assets/<x>.md        a blank template the user can fill by hand (optional)
```

No per-skill README. The root README is the catalog.

## SKILL.md shape

1. Frontmatter: `name` (equals folder) and `description` (block `>` form, at most 600 characters).
   - Start with "Use when the user says" followed by 4 to 6 literal phrases a CSM would type, then one sentence on what it produces, then "Not for X (use Y)".
   - Phrases must be distinctive. Do not claim a phrase another skill owns. See `docs/TRIGGERS.md` once it exists.
2. `# Title`, then one sentence: what the user walks away with.
3. `## Start here`: the minimum input; if present, go. Otherwise ask for at most 3 things in ONE message and proceed with whatever comes back. Never block on missing input.
4. `## Do this`: 4 to 7 imperative steps, 1 to 3 lines each. No essays.
5. `## Output`: the exact skeleton in a code block, verdict first, ending with `What I could not check`. Point to `examples/sample.md`.
6. `## Rules`: 5 to 8 judgement rules, each with the mechanism ("because"). This is the distinctive value. Cut anything a generic assistant would already do.
7. `## Related (only if installed)`: one line. Suggest siblings, never require them.

Do NOT include: "Failure modes", "What good looks like", philosophy intros, or restated steps. The rules section absorbs the best of those.

## Conventions every skill follows

- **Nothing is a prerequisite.** No `CLAUDE.md`, no connectors, no files, no voice guide, no `AskUserQuestion`, no folders. If the user has an "Account context" block in the conversation, use it. If a mailbox or recorder is connected, use it opportunistically. Never mention either as required.
- **Evidence tags.** Where facts feed a judgement, tag them `said` (someone told us, name who), `seen` (observed, say where) or `inferred` (our reading). Missing inputs are written `(assumed, confirm)` inline and listed under `What I could not check`.
- **Verdict first.** The call, the draft or the answer is the first thing in the output.
- **Dollars and dates, not colors.** Ranges with a number, deadlines with a day.
- **Never send, never write to a system.** Drafts only. The user presses send.
- **Facts about the product, price, contract or security come from the user.** Flag them for confirmation. Never assert them.
- **Sibling skills are suggestions.** Say "if `x` is installed". Never depend on one.

## Style

- US spelling. Plain words. Short sentences.
- No em dashes or en dashes. No curly quotes. Use commas, colons, full stops or a spaced hyphen.
- No statistics you cannot source. Mechanisms over numbers. Where a number is a default, call it "a common default, set your own".
- No real customer, employer or person names. Invented companies must be obviously invented, and the sample says so in one italic line.
- Third person when addressing nobody ("the user"); direct imperative in steps.

## The example is mandatory and is the test

`examples/sample.md` shows a realistic input (2 to 4 sentences, as a busy CSM would type it) and the complete output. If you cannot produce a convincing filled example, the skill is not ready. Keep it under about 60 lines.

## Checks run on every pull request

`tools/check.py`: line and size limits, frontmatter, description length, trigger phrase collisions, banned punctuation, example present, manifest and README in sync.
