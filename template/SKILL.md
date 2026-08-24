---
name: skill-name
description: >
  One paragraph covering what the skill does and, more importantly, when to
  fire it. List the exact phrases a user says when they want this. Claude
  matches on this text, so vague descriptions produce a skill that never
  triggers. Name any sibling skill it should defer to.
---

# Skill Name

One or two sentences on what this skill is for and what it produces.

---

## What this needs

State the floor first: the least a user can have and still get value. Then what
improves it, and what each missing piece costs.

Write this section even when the answer is "nothing". A reader deciding whether
to install should not have to infer their setup from Step 3.

The rule underneath it: nothing in a published skill may be a prerequisite.
Workspace files, connectors and file access are all upgrades. A skill that
errors because a `CLAUDE.md` is missing gets uninstalled.

---

## When this runs

The trigger conditions in plain language. Include the cases where it should
*not* run, and which skill handles those instead.

---

## Step 1: [Action]

Instructions written as directives to Claude, not as description. "Read the
transcript in full" beats "this skill reads transcripts."

Where the skill depends on something in the user's workspace — a style guide,
an accounts folder, a naming convention — say so as an optional input and
degrade gracefully when it isn't there.

## Step 2: [Action]

Keep steps short enough to follow under load. If a step needs more than a
screen of explanation, move the detail into `references/` and link to it.

---

## Output

State exactly what the skill produces and where it lands: a file, a set of
drafts, a table in chat. Ambiguity here is what makes a skill feel unreliable.

---

## Failure modes

The things that go wrong with this specific job, and what to do instead. This
section is what separates a skill from a prompt.

---

## Supporting files

- `references/<topic>.md` — detail loaded only when the step needs it
- `assets/<template>.md` — templates the skill writes from
