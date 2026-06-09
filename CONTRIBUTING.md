# Contributing

This repository is a small public standard.

Contributions should keep it clear, practical, and proof-first.

## Contribution principles

1. **Keep it understandable**
   - A first-time public reader should understand the purpose quickly.
   - Avoid unexplained jargon.
   - Add examples when introducing new concepts.

2. **Keep it small**
   - This is not a framework.
   - This is not a runtime.
   - Prefer minimal templates, schemas, examples, and checks.

3. **Receipts over claims**
   - Do not add claims that cannot be inspected.
   - Prefer records, examples, validation steps, or clear limitations.

4. **Fail closed**
   - Sensitive or unclear actions should default to no action.
   - Refusals should be explicit, replayable, and verifiable.

5. **Separate standard from implementation**
   - This repo describes public patterns.
   - Runtime enforcement belongs in implementations.
   - Do not imply that a private system is safe because this standard exists.

## Good contributions

Good contributions include:

- clearer plain English explanations;
- better examples;
- tighter refusal receipt requirements;
- simple validation checks;
- diagrams or tables that make the standard easier to understand;
- corrections that reduce ambiguity.

## Avoid

Avoid:

- marketing claims;
- vague safety language without evidence;
- large framework-like additions;
- hidden implementation assumptions;
- claims of production readiness;
- adding dependencies unless clearly justified.

## Before opening a change

Ask:

```text
Does this make the standard easier to understand, verify, or reuse?
```

If not, do not add it.
