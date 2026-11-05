# Versions

## 2.1.1

Restored a `README.md` in every skill folder, as a standalone landing page for the skill. They are generated from each skill's own `SKILL.md` by `tools/build_readmes.py`, so a README cannot disagree with its skill, and `tools/check.py` fails if one is missing or out of date. Closes #47.

## 2.1.0

Twenty-one new skills covering the daily work, proof of value, money and the team, found by mapping the whole job of a CSM, a team lead and a head of CS. 54 skills in total.

- **Your day:** `what-do-i-owe`, `day-plan`, `status-update`, `commitments`.
- **Prove value and grow:** `value-ledger`, `adoption-plan`, `account-review`, `mutual-action-plan`, `expansion-scan`, `usage-email`, `survey-follow-up`, `voice-of-customer`.
- **Save, price and collect:** `save-plan`, `price-increase`, `invoice-chase`, `sales-handoff`.
- **Lead a team or the function:** `cs-scorecard`, `team-rollup`, `book-review`, `csm-ramp`, `csm-hiring`.
- Role bundles, the `cs-start` router, README, trigger map and the routing test prompts updated to match.

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
- Removed per-skill READMEs. Restored in 2.1.1.

## 1.4.0 and earlier

Initial library of 32 skills and a structural validator. See git history.
