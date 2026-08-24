---
name: chat-context
description: >
  Carries context from one Cowork chat into the next so the user can start a fresh chat without re-explaining anything. Runs in two directions. HANDOFF mode triggers when the user says "hand off this chat," "save chat context," "wrap this chat," "close this chat," "I'm moving to a new chat," "chat handoff," or "write the handoff." RESUME mode triggers when the user says "resume," "resume from handoff," "pick up where we left off," "load chat context," "continue from the last chat," or opens a chat referencing an earlier session. Where files can be written, handoff saves a structured context file and registers it in a master index; where they cannot, it prints the same structure as a block the user pastes into the next chat. Resume reads whichever form it finds, states what was loaded, then continues the work. Use this instead of summarising a chat back to the user in conversation.
---

# Chat Context Skill

Long chats get expensive because every new message carries the whole conversation with it. This skill lets the user close a chat and open a fresh one without losing a thing. It writes a structured context file at the end of a session and reads it back at the start of the next one.

This skill owns the handoff procedure only. It does not restate rules that live elsewhere. Where a workspace exists, its root `CLAUDE.md` owns routing and preferences, its file-naming rules own placement, and its voice or style guide owns tone. Read those where the steps below point to them, and skip the pointer where the file does not exist.

---

## What this needs

**Minimum: nothing.** In a plain chat with no workspace and no file access, handoff prints the context block and the user pastes it into their next chat. That is the whole loop, and it works.

**Better with** somewhere to write files. The handoff becomes a saved file with a master index, so handoffs accumulate into a trail instead of living in a paste buffer, and resume can find the right one without the user carrying it.

The structure of a handoff is identical either way. Only where it lands changes.

---

## Mode A: Handoff

Triggered when the user signals the chat is ending. Do not wait to be asked twice, and do not offer a conversational summary instead.

**Two routes.** With file access, the handoff becomes a file and gets an index row: run A1 through A7. Without it, print the Step A3 structure as one markdown block in chat and stop there: run A1, A3 and A6 only, and say plainly that it lives in the chat rather than in a file, so the user knows to keep it.

### Step A1: Identify the project area

Where the workspace has routing rules in a root `CLAUDE.md`, read them and pick the project area this chat belongs to. If the chat spanned more than one, pick the area where most of the work landed and name the others in the Context Loaded section. If no area fits, use a general `Projects` folder.

Where there is no workspace, skip the folder question entirely and use a short topic label instead. It still fills the **Project area** line in the structure, which is what a later reader needs.

State what you picked before writing.

### Step A2: Create the folder if it does not exist

**File route only.** Chat-only handoffs skip to A3.

```
<Project Area>/Chat Context/
```

Example: `Client Work/Chat Context/`

Create it on demand. Do not pre-create Chat Context folders in areas that have never had a handoff.

### Step A3: Write the handoff

This step runs on both routes, and the structure below is identical either way.

**On the file route**, name it `YYYY-MM-DD-descriptive-topic.md` using today's date, hyphens, no spaces. The topic must describe the work, not the session. Use `2026-07-30-hubspot-dashboard-arr-rebuild.md`, never `2026-07-30-chat-handoff.md`. If a handoff for the same topic already exists from an earlier session, update that file rather than creating a second one, and record the refresh inside it. Two handoffs on one topic means the next chat reads the wrong one.

**On the chat-only route**, print it as a single fenced markdown block so the user can copy it in one action. Put the same descriptive topic in the heading, since that is what they will search their own notes for later.

Use this structure exactly. Every section stays, even if the answer is "none."

```markdown
# Chat Context: [Topic]

**Project area:** [Name]
**Date:** [DD Mon YYYY]
**Status:** Active

---

## Goal

One line. What this thread of work is trying to achieve.

## Current State

Where things stand right now, in two or three sentences. Written so someone
with zero prior context knows what exists and what does not.

## Decisions Made

- Decision, and the reasoning behind it in one clause.

## Open Questions and Blockers

- What is unresolved, and who or what it is waiting on.

## Files Created or Modified

| File | Path | What it holds |
| ---- | ---- | ------------- |

## Rejected Approaches

- What was considered and dropped, and why. This section stops the next chat
  from re-proposing something already killed.

## Approved Wording

Verbatim copy, headlines, or phrasing the user signed off on. Quote exactly. If
nothing was approved, write "None."

## Context Loaded

Files read during this session that the next chat should read again.

## Next Action

The single next thing to do. One sentence, specific enough to act on without
asking a question first.
```

### Step A4: Register it in the master index

**File route only.**

Append a row to the master index at `<Ops Area>/Chat Context/chat-context-index.md`, wherever the workspace keeps cross-cutting registers. Create that file with the structure in Step A5 if it does not exist yet.

**Refreshing an existing handoff updates its row rather than adding one.** When Step A3 updated an existing file instead of creating a new one, edit that file's row in place: new date, topic suffixed `(refreshed)`, status unchanged. Append a new row only for a genuinely new topic. Two rows pointing at the same file recreates the exact ambiguity Step A3 exists to prevent, since a later "resume" then has to pick between them.

The index is a rolling register, so it carries no date prefix and is never re-dated. Re-dating a row on refresh is the one exception, and it applies to that row only, not the file. This follows the same logic as any rolling register in the workspace's file-naming rules.

### Step A5: Index structure

**File route only.**

```markdown
| Date | Project area | Topic | File | Status |
| ---- | ----------- | ----- | ---- | ------ |
```

Status is `Active`, `Superseded`, or `Closed`. Newest row goes at the bottom.

When a handoff has been fully consumed and the work is finished, set its status to `Closed` in the index and in the file header. Never delete a handoff file. The trail is the point.

### Step A6: Hand the user the opener

On the file route, print a short paste-ready line for the new chat, nothing more:

> Resume the [topic] handoff in [Project Area].

On the chat-only route, the block itself is the opener. Tell the user to paste the whole block into the new chat and say "resume from this handoff."

### Step A7: Confirm

**File route only.** List the file created or updated with its full path, and the index row added. On the chat-only route the block is visible above, so say nothing further.

---

## Mode B: Resume

Triggered at the start of a new chat. Read before doing anything else, including before answering a question the user asks in the same message.

### Step B1: Find the handoff

**If the user pasted a handoff block into the chat, that is the handoff.** Read it directly and go to Step B4. No lookup is needed and no index has to exist.

Otherwise, read the master index at `<Ops Area>/Chat Context/chat-context-index.md`.

- If the user named a topic or project area, match on that.
- If they said only "resume," take the most recent row with status `Active`.
- If two Active rows could plausibly match, ask which one. Do not guess.
- If the index does not exist or holds no Active rows, say so plainly and ask what they want to pick up.

### Step B2: Read the handoff file

Read it in full. Do not skim to the Next Action.

### Step B3: Read the project files

Where the handoff names workspace files - a `CLAUDE.md`, a `MEMORY.md`, anything under Context Loaded - read them. Skip silently over any that do not exist in this environment, and say which ones you could not reach. A handoff written in a workspace and resumed in a plain chat is a normal case, not an error.

### Step B4: State what was loaded

Before doing any work, tell the user in three lines or fewer: which handoff was read, which files were loaded, and what the recorded Next Action is. Then ask whether to proceed with that action or something else.

This is the only acceptable place to spend words on recap. Keep it short.

---

## Rules

### What goes in a handoff

- Decisions, state, blockers, paths, rejected paths, approved wording.
- Written for a reader with zero context, not as a reminder to someone who was there.
- Full file paths, never "the file we made."
- Names of people the work is waiting on.

### What stays out

- Transcript, dialogue, or blow-by-blow of the conversation.
- Anything already recorded in root `MEMORY.md` or the project area's `MEMORY.md`. Point to it instead. Duplication breaks MECE.
- Reasoning that led nowhere and changed nothing.

### Size

Keep a handoff under 120 lines. If it runs longer, the detail belongs in a project file that the handoff links to.

### Relationship to MEMORY.md

A handoff is session state, not memory. It does not need approval to write, and it does not go in `MEMORY.md`.

If something in the session is durable rather than session-scoped, a decision that outlives this thread of work or a new working convention, propose it as a `MEMORY.md` entry separately and wait for approval. Where there is no `MEMORY.md`, propose the same items in chat under a clear heading so the user can file them wherever they keep durable notes. Handoff and memory are different jobs. Do both when both apply.

### When not to use this skill

- The chat is short and nothing was decided. Say so, skip the file.
- The user wants a summary to read rather than a handoff to reuse. That is a different ask.

