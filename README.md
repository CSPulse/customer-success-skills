# Skills

AI skills for customer success work, built for Claude. These are working skills rather than demos: each one came out of a job that kept repeating, and each one is written to fail loudly rather than quietly.

A skill is a folder with a `SKILL.md` in it. Claude reads the description, decides when the skill applies, and follows the instructions inside. Nothing here needs an API key or a build step.

## What's here

### Customer success

| Skill | What it does |
| :--- | :--- |
| [`renewal-risk-read`](skills/renewal-risk-read) | Produces a defensible read on whether an account will renew — the decision, the decider, the mechanism, the dollars and the play. Built on the principle that usage tells you about the user while the renewal is decided by the buyer. |
| [`business-review-prep`](skills/business-review-prep) | Prepares a QBR or EBR that earns the next meeting: the customer's business first, value proved to a standard finance would accept, three to five themes, and an explicit ask. Tells you when a business review is the wrong meeting to run. |
| [`onboarding-plan`](skills/onboarding-plan) | Builds a first-90-days plan aimed at a result the customer can point to, with success criteria carrying a baseline and the early signals that predict a bad year. |
| [`call-recap-follow-up`](skills/call-recap-follow-up) | Turns a call into an honest read of how it went plus every follow-up email it generated, grouped by recipient and staged as drafts. Recorder-agnostic. |
| [`email-critic`](skills/email-critic) | Stress-tests a drafted customer email against the transcript and account context, then returns a verdict and a tightened version. Checks facts before prose. |

### General

Useful in any role, included because customer success work runs long sessions and heavy context.

| Skill | What it does |
| :--- | :--- |
| [`chat-context`](skills/chat-context) | Carries context between chats. Handoff writes a structured context file; resume reads it back and states what was loaded. |
| [`optimize-tokens`](skills/optimize-tokens) | Spots token-heavy requests before they run and proposes a cheaper approach that gets the same answer. |

### They work without any setup

You do not need a workspace, a `CLAUDE.md`, connectors or file access. Every skill states its floor in a **What this needs** section and runs from there — most work from what you paste into the chat. Missing context never blocks a skill; it changes what the skill can honestly claim, and each one says which checks it could not run rather than guessing around the gap.

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
