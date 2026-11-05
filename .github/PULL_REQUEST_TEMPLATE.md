<!-- If this closes an issue, say so here, e.g. "Closes #12". -->

## What this changes



## Why

<!-- For a new skill: the job it does, how often it recurs, and the failure it exists to prevent. -->



## Checks

- [ ] `python3 tools/check.py` passes
- [ ] `examples/sample.md` shows a realistic input and a complete output for an invented company, and a CSM would forward it without editing
- [ ] Nothing is a prerequisite (no connector, file, workspace, voice guide or other skill)
- [ ] Each rule says why it is true
- [ ] No unsourced statistic; defaults are labeled as defaults
- [ ] No real customer, employer or personal names
- [ ] Trigger phrases are this skill's own (see `docs/TRIGGERS.md`)
- [ ] If a skill was added or removed: README tables, role bundles in `.claude-plugin/marketplace.json`, `docs/TRIGGERS.md` and `evals/routing-prompts.tsv` updated

## Anything a reviewer should look at closely
