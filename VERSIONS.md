# Versions

What changed, and when. Sixteen skills across seven planned categories, four of them complete.

## 1.4.0

**Added the validator and continuous integration.** `validate-skills.py` checks the structural rules on every skill: line limit, frontmatter name against folder, description length, heading against folder, manifest and README consistency, reference depth, punctuation. A GitHub Actions workflow runs it on every pull request and every push to main.

Until now those rules were enforced only by a hook on the maintainer's own machine, which never travels with a clone. Contributors arrive by fork, so they had nothing to run. The nine mechanical checkboxes in `CONTRIBUTING.md` are now one command, and the manual list is reduced to what a script cannot see.

Identity checking is deliberately not in the published script. A denylist inside a public repository publishes the names it exists to protect.

## 1.3.0

**Wave 1 complete: `renewal-negotiation`, `expansion-case`, `escalation`, `offboarding`.** Sixteen skills, four categories complete.

## 1.2.0

**Names aligned.** Marketplace is `cspulse`, plugin is `customer-success-skills`, matching the repository. Previously `cspulse-skills` and `cs-skills`, so the library answered to four names and the install command shared no words with the repository a reader had just added. Breaking for existing installs, done early because the cost only grows.

## 1.1.0

**Renamed from `cs-skills` to `customer-success-skills`,** and cut to customer success only. `renewal-risk-read` to `renewal-risk`, `business-review-prep` to `business-review`, `call-recap-follow-up` to `call-recap`. `chat-context` and `optimize-tokens` removed as general workflow skills that live in the personal library.

## 1.0.0

First release. Seven skills.
