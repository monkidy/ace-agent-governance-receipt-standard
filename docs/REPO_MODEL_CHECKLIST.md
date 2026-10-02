# Public repo model checklist

> **Historical origin:** this checklist was first written for ACE-related public repositories in June 2026. It is preserved as a reusable reader-first pattern. It is not current SYSTASYS architecture or publication authority.

Use this checklist when turning a bounded technical repository into a public, understandable, reader-first repo.

The goal is not to make every repo bigger. The goal is to make every repo clear.

## Required public entry points

A public repository should usually have:

- [ ] `README.md`
- [ ] `START_HERE.md` when the subject is abstract or unfamiliar
- [ ] `VISUAL_OVERVIEW.md` when the repo describes a workflow, standard, or system behavior
- [ ] `STATUS.md`
- [ ] `LICENSE`
- [ ] `CHANGELOG.md` when the repo evolves over time

## README requirements

The README should answer these questions near the top:

1. What is this?
2. Who is it for?
3. What problem does it solve?
4. What should a non-technical reader read first?
5. What should a technical reader inspect?
6. What does this repo not do?
7. What is the current status?

## Reader-first requirements

A public visitor should be able to understand:

- the one-line idea;
- the real-world problem;
- the main concepts in plain words;
- the safest first file to open;
- the current maturity level;
- what not to assume.

## Proof-first requirements

Distinguish claim, example, validation, runtime proof and production proof.

Avoid saying `ready`, `safe`, `production-grade`, `complete` or `validated` unless the repository shows evidence for that exact claim.

## Boundary requirements

Say what the public repository does not do. Examples: it does not grant authority, run agents, replace a policy engine, prove a private implementation safe, or execute live actions.

## Examples and validation

Examples should be small, realistic, inspectable and consistent with the repository status.

If the repo contains schemas or generated artifacts, add the smallest useful local validation command.

## Final audit question

```text
Can a smart outsider understand what this is, why it matters, what to open first, what not to assume, and how to verify the examples?
```

If the answer is no, the repository is not reader-first yet.
