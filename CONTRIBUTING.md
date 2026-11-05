# Contributing

The most valuable contribution is telling us a skill is wrong. These are written by practitioners, but nobody has run accounts in every industry, segment and pricing model.

## Three ways to help

1. **A skill is wrong or thin.** Open an issue: what happens in your world, and what the skill assumed instead. "Procurement starts eleven months out in healthcare because the clinical committee sets budget in Q1" is a fix. "The timing is off" is not.
2. **A skill is missing.** Describe the job, how often it recurs, and what good output looks like. It has to be a job with a right and a wrong way to do it.
3. **You wrote one.** Open a pull request.

## Writing a skill

Read [template/SPEC.md](template/SPEC.md). Copy [template/SKILL.md](template/SKILL.md). Match the shape of `skills/renewal-risk/`.

The two rules everything holds:

- **Nothing is a prerequisite.** No connector, file, workspace, voice guide or other skill. Missing input changes what a skill claims, never whether it runs.
- **Ship the filled example.** `examples/sample.md` shows a realistic input and the complete output for an invented company. If you cannot write a convincing one, the skill is not ready.

Before you open the pull request:

```
python3 tools/check.py
```

Then check the things a script cannot see:

- [ ] The example is something a CSM would forward without editing
- [ ] Each rule says why it is true, not just that it is
- [ ] No statistic without a named source (defaults are labeled as defaults)
- [ ] No real customer, employer or person names
- [ ] The trigger phrases belong to this skill and not a sibling's
- [ ] README table, role bundles in `.claude-plugin/marketplace.json` and `docs/TRIGGERS.md` updated

Pull requests are read as a diff. Expect questions on any claim about how customer success works that does not say where it came from.
