# ACE Agent Governance Receipt Standard

**A small, practical standard for keeping AI agents bounded, traceable, and revocable.**

New here? Start with [`START_HERE.md`](START_HERE.md). It explains the project in plain English, with no technical background required.

Prefer a visual explanation? Open [`VISUAL_OVERVIEW.md`](VISUAL_OVERVIEW.md) for diagrams and one-screen tables.

## The simple question

How do we know an AI agent stayed inside its limits?

This repository gives a small answer:

> Make the agent leave receipts.

A receipt is a short record that can be checked later. It should show what the agent was allowed to do, what it proposed, what happened, what did not happen, and what evidence exists.

## The four basic ideas

1. **Mandate** - what the agent is allowed to do.
2. **Next Best Action** - what the agent proposes before acting.
3. **Outbound Action Receipt** - what happened, what did not happen, and what evidence exists.
4. **Refusal Receipt** - why the agent did not act, and proof that no action ran first.

## Why this matters

AI agents can draft, edit files, call tools, trigger workflows, and interact with external systems.

That means teams need more than agent claims. They need records that answer:

- Was the agent allowed to do this?
- Did a human approval gate exist?
- What action was proposed?
- What action actually happened?
- What was refused?
- What proof shows that no side effect happened before a refusal?

This is the principle:

> Receipts over claims.

## Who this is for

This standard is useful for:

- people building AI agents;
- founders and operators using AI automation;
- compliance, legal, security, and risk teams;
- reviewers who need to inspect what an agent did or refused to do;
- non-technical stakeholders who need a simple audit trail.

You do not need to understand ACE internals to use this repository.

## Read this first

If you have 2 minutes:

1. Read [`START_HERE.md`](START_HERE.md).
2. View [`VISUAL_OVERVIEW.md`](VISUAL_OVERVIEW.md).
3. Open `examples/refusal-receipts/external-send.not-authorized.json`.
4. Look for `requested_action`, `policy`, `no_side_effect_attestation`, and `safe_next_action`.

If you are implementing:

1. Read `agent_mandate.v0.md`.
2. Read `next_best_action.v0.md`.
3. Read `outbound_action_receipt.v0.md`.
4. Read `specs/refusal-receipt.schema.json`.
5. Run `python tools/validate-refusal-receipts.py`.

## Quick example

A user asks an agent to send an external message.

The mandate says the agent may draft messages, but may not send them.

The agent must refuse before sending. The refusal receipt should show:

```text
requested_action: external_send
policy_that_fired: external_send_approval_missing
execution_started: false
external_calls_made: false
safe_next_action: draft the message for human review
```

That is the core idea: refusal with evidence, not refusal as a vague claim.

## Refusal Receipt Requirements

A credible refusal receipt must be emitted before any side effect or execution step runs.

It must include:

1. **Pre-execution emission** - the receipt is created before the action starts.
2. **Policy that fired** - the exact rule or boundary that denied the action.
3. **Agent context** - who the agent was, what role it had, and what boundary applied.
4. **No side-effect attestation** - proof that no file write, send, external call, or other side effect happened first.
5. **Replayability** - enough inputs for a reviewer to verify the same decision later.
6. **Verifiability** - a hash chain or signature.
7. **Safe next action** - what the operator can do next.

A refusal without proof is only another claim.

## Files in this repo

- `START_HERE.md` - plain English guide.
- `VISUAL_OVERVIEW.md` - diagrams and one-screen tables.
- `agent_mandate.v0.md` - template for agent boundaries.
- `next_best_action.v0.md` - template for proposed actions.
- `outbound_action_receipt.v0.md` - template for action and refusal records.
- `specs/refusal-receipt.schema.json` - minimal JSON schema for refusal receipts.
- `examples/refusal-receipts/` - concrete examples.
- `tools/validate-refusal-receipts.py` - dependency-free validator for examples.

## Validate examples locally

```bash
python tools/validate-refusal-receipts.py
```

Expected result:

```text
OK: examples/refusal-receipts/external-send.not-authorized.json
OK: examples/refusal-receipts/forbidden-write.refused.json
Validated 2 refusal receipt example(s).
```

## What this repo does not do

This repository does not run agents.

It does not grant authority.

It does not replace a policy engine.

It does not prove that a private implementation is safe.

It provides a small public standard for recording and checking agent boundaries, actions, refusals, and evidence.

## Design principles

### Closed by Default

Nothing is allowed unless a mandate, gate, or policy admits it.

### Evidence First

Important actions and refusals should leave inspectable evidence.

### Human Bounds

Agents may propose. Humans, mandates, and gates define what may execute.

### Receipts Over Claims

A claim is not enough. A receipt should be replayable, inspectable, and verifiable.

## Reader-first rule for ACE repos

Every ACE-related public repository should answer these questions near the top of its README:

1. What is this?
2. Who is it for?
3. What problem does it solve?
4. What should a non-technical reader read first?
5. What should a technical reader inspect?
6. What does this repo not do?
7. What is the current status?

This is the default standard for future ACE repo cleanup.

## License

Apache-2.0.
