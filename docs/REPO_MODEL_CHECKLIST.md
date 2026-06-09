# ACE public repo model checklist

Use this checklist when turning an ACE-related repository into a public, understandable, reader-first repo.

The goal is not to make every repo bigger.

The goal is to make every repo clear.

## Required public entry points

Every public ACE repo should have:

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

## Visual requirements

If the repo contains a process, system, standard, pipeline, or governance model, include a visual overview.

Good visual elements:

- one flow diagram;
- one table that maps step to evidence;
- one example that fits on one screen;
- one mental model or checklist.

Mermaid diagrams are preferred because they render directly on GitHub and remain versionable as text.

## Proof-first requirements

Every repo should distinguish:

- claim;
- example;
- validation;
- runtime proof;
- production proof.

Avoid saying:

```text
ready
safe
production-grade
complete
validated
```

unless the repo shows evidence for that exact claim.

## Boundary requirements

Every public ACE repo should say what it does not do.

Examples:

- does not grant authority;
- does not run agents;
- does not replace a policy engine;
- does not prove a private implementation is safe;
- does not execute live actions.

## Example requirements

Examples should be:

- small;
- realistic;
- inspectable;
- linked from the README;
- consistent with the repo's status.

## Validation requirements

If the repo contains schemas, examples, or generated artifacts, add the smallest possible local validation command.

Prefer standard-library scripts before adding dependencies.

Example:

```bash
python tools/validate-refusal-receipts.py
```

## Status labels

Use explicit status labels.

Suggested labels:

```text
DRAFT_PUBLIC_V0
READER_FIRST_PUBLIC_V0
PUBLIC_READER_FIRST_VISUAL_V0
USABLE_REFERENCE_V0
IMPLEMENTATION_REQUIRED
RUNTIME_PROOF_REQUIRED
PRODUCTION_PROOF_REQUIRED
```

## Final audit question

Before calling a repo public-ready, ask:

```text
Can a smart outsider understand what this is, why it matters, what to open first, what not to assume, and how to verify the examples?
```

If the answer is no, the repo is not reader-first yet.
