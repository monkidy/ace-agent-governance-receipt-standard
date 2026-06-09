# Project status

## Current status

```text
PUBLIC_READER_FIRST_VISUAL_V0
```

This repository is an early public standard.

It is usable as a reference for:

- explaining agent receipts to non-technical readers;
- describing mandate, proposal, action receipt, and refusal receipt concepts;
- showing concrete refusal receipt examples;
- validating refusal receipt examples with a small local script;
- serving as a model for future ACE public repositories.

## What is stable enough to reuse

- The reader-first README structure.
- The plain English `START_HERE.md` entry point.
- The `VISUAL_OVERVIEW.md` flow and table pattern.
- The core terms: mandate, next best action, outbound action receipt, refusal receipt.
- The refusal receipt minimum requirements.
- The example-first structure.
- The local validator pattern.

## What is still early

- The JSON schema is intentionally minimal.
- The validator checks core invariants, not full JSON Schema compliance.
- No automated CI workflow is enabled yet.
- The standard is public and declarative; enforcement belongs in implementations.

## What this repo should not claim

This repository should not claim that any private implementation is safe, complete, production-ready, or formally verified.

It provides a public standard and examples. Runtime enforcement must be proven separately.

## Current closeout

The current closeout target is complete:

```text
README: reader-first
START_HERE: plain English
VISUAL_OVERVIEW: diagrams and tables
REFUSAL_SCHEMA: present
REFUSAL_EXAMPLES: present
VALIDATOR: present
LICENSE: present
STATUS: present
MODEL_CHECKLIST: present
```
