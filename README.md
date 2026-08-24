# Skills

AI skills for customer success work, built for Claude. These are working skills rather than demos: each one came out of a job that kept repeating, and each one is written to fail loudly rather than quietly.

A skill is a folder with a `SKILL.md` in it. Claude reads the description, decides when the skill applies, and follows the instructions inside. Nothing here needs an API key or a build step.

## What's here

| Skill | What it does |
| :--- | :--- |
| [`call-recap-follow-up`](skills/call-recap-follow-up) | Turns a call into an honest read of how it went, plus every follow-up email it generated, grouped by recipient and staged as drafts. Recorder-agnostic: it uses whichever meeting tool you have connected, and asks you for the transcript when you have none. |
| [`email-critic`](skills/email-critic) | Stress-tests an email you have already drafted against the source transcript and the account context, then returns a verdict and a tightened version. Checks facts before prose, because that is where the damage is. |
| [`chat-context`](skills/chat-context) | Carries context between chats. Handoff mode writes a structured context file when a session ends; resume mode reads it back and states what was loaded before doing any work. |
| [`optimize-tokens`](skills/optimize-tokens) | Spots token-heavy requests before they run and proposes a cheaper approach that gets the same answer. Fires on request, or on its own when a task looks expensive. |

### They work without any setup

You do not need a workspace, a `CLAUDE.md`, a `MEMORY.md`, connectors or file access. Every skill states its floor in a **What this needs** section and runs from there:

| | Works with nothing but | Gets better with |
| :--- | :--- | :--- |
| `call-recap-follow-up` | a pasted transcript | a meeting recorder, a mailbox, account notes, a voice guide |
| `email-critic` | the draft itself | the transcript, the thread, account notes, a voice guide |
| `chat-context` | nothing — the handoff prints in chat to paste forward | file access, which turns handoffs into a saved trail with an index |
| `optimize-tokens` | nothing | nothing |

Missing context never blocks a skill. It changes what the skill can honestly claim, and each one says which checks it could not run rather than guessing around the gap.

## Install

### Claude Code

```
/plugin marketplace add CSPulse/Skills
/plugin install cs-skills@cs-pulse-skills
```

### Claude.ai and Cowork

Package the skill's folder as a ZIP, then go to **Customize > Skills**, click **+**, choose **Create skill** and then **Upload a skill**. The folder name inside the ZIP must match the skill's `name` in its frontmatter, or the upload is rejected. See [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

### Claude API

Follow the [Skills quickstart](https://docs.claude.com/en/api/skills-guide#creating-a-skill).

### By hand

Copy any skill folder into `~/.claude/skills/<skill-name>/` for all your projects, or `.claude/skills/<skill-name>/` inside one repo. It loads on the next session.

## Writing your own

[`template/SKILL.md`](template/SKILL.md) is a starting structure. Two things matter more than the rest:

The description is the trigger. Claude decides whether to run a skill by reading its description, so list the actual phrases someone says when they want it. A description that explains what the skill *is* rather than when it *fires* produces a skill that never runs.

Write instructions, not documentation. "Read the transcript in full" works. "This skill reads transcripts" does not.

Anthropic's [Agent Skills spec](https://github.com/anthropics/skills/tree/main/spec) is the reference for the format itself.

## Credits

Two skills worth having are other people's work and are not republished here. Go to the source:

- [garrytan/gstack](https://github.com/garrytan/gstack) — `office-hours` and the rest of Garry Tan's planning stack. MIT.
- [blader/humanizer](https://github.com/blader/humanizer) — strips AI-writing tells from text, built on Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). MIT.

## License

MIT. See [LICENSE](LICENSE).
