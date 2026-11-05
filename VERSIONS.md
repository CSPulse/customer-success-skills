# Versions

## 2.0.0

A rebuild, based on an audit of the 1.x library and research into how customer success work is done and how other skill libraries are used.

**What was wrong.** Strong ideas, hard to adopt. Skills were 9 to 15KB of essay prose; only one had a filled example; several quietly depended on the author's own setup (`CLAUDE.md`, a voice guide, an accounts folder) despite the "nothing is a prerequisite" rule; there was no front door; triggers collided; the README opened with philosophy rather than output.

**What changed.**
- Every skill rewritten to a short, executable format (70 to 150 lines): fast intake that never blocks, a fixed output skeleton that leads with the verdict, rules with their mechanism, and a mandatory filled `examples/sample.md`.
- Added `cs-start` (routing, a 60 second demo, anonymize-for-sharing), `renewal-runway`, `champion-loss`, `health-score`, `internal-ask` and `playbook-builder`.
- Merged `weekly-plan` into `book-triage`, `account-research` into `handoff`, `health-read` into `health-score`, and `product-feedback` plus `internal-escalation` into `internal-ask`.
- Role bundles: `csm-toolkit`, `cs-team-lead-toolkit`, `cs-leader-toolkit`. The `customer-success-skills` plugin still installs everything.
- Removed invented statistics and author-specific style rules.
- New `tools/check.py` replaces `validate-skills.py` and enforces the spec, including trigger phrase collisions.
- Removed per-skill READMEs. The root README is the catalog.

## 1.4.0 and earlier

Initial library of 32 skills and a structural validator. See git history.
