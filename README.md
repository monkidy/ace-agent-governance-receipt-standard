# ACE Agent Governance Receipt Standard

**A small, practical standard for keeping AI agents bounded, traceable, and revocable.**

Most AI-agent workflows fail in the same place: the agent can propose, act, refuse, or claim progress without leaving enough evidence for a human operator to know what happened.

This standard defines a minimal public pattern:

1. **Mandate** - what the agent is allowed to do.
2. **Next Best Action** - what the agent proposes before acting.
3. **Outbound Action Receipt** - what actually happened, what did not happen, and what evidence exists.

A **Refusal Receipt** is a specialized outbound action receipt. It records why an action did not run.

It is not a runtime.  
It is not a framework.  
It is not permission for an agent to act.

It is a simple governance layer for teams that want AI agents to remain bounded, auditable, and reversible.

---

## Why this exists

AI agents should not only answer.

They should leave evidence.

A useful agent system needs to answer five questions quickly:

- **Can this agent act, or only propose?**
- **What proof did it leave?**
- **Who can refuse, revoke, or review the action?**
- **Which policy or boundary admitted or denied the action?**
- **Can the decision be replayed and verified later?**

This repo gives a compact, reusable shape for that.

---

## Core rule

> A proposal is not an action.  
> A refusal is not a vague claim.  
> A receipt is not evidence unless it can be checked.  
> A human approval gate is not optional for sensitive actions.

---

## The three documents

### `agent_mandate.v0.md`

Defines the agent boundary.

It answers:

- what the agent is;
- what it may do;
- what it must never do;
- what evidence it must leave;
- when it must stop.

### `next_best_action.v0.md`

Defines a proposed action before execution.

It answers:

- what the agent wants to do next;
- why;
- what files, systems, or people it would affect;
- what risks exist;
- what approval is required.

### `outbound_action_receipt.v0.md`

Defines the proof left after an action, blocked action, or refusal.

It answers:

- what happened;
- what did not happen;
- what evidence exists;
- what boundary was respected;
- what remains unresolved.

A refusal receipt is a specialized outbound action receipt for actions denied before execution.

---

## Refusal Receipts Requirements

A refusal receipt records that an agent did **not** execute a requested action because a mandate, policy, approval gate, or runtime boundary denied it.

A credible refusal receipt must be emitted **before any side effect or execution step runs**.

Minimum requirements:

1. **Pre-execution emission**
   - The receipt must be created at decision time.
   - It must state that execution did not start.
   - It must not be generated after a failed or partial side effect and presented as a refusal.

2. **Policy that fired**
   - The receipt must identify the policy, mandate rule, approval gate, or boundary that denied the action.
   - The reason must be specific enough to replay the decision.
   - Examples: `writes_allowed=false`, `approval_missing`, `external_send_not_authorized`.

3. **Agent context at decision time**
   - The receipt must include the agent identity, role, action class, active mandate or boundary, operator, and relevant approval state.
   - It should include enough context to distinguish `not allowed` from `not attempted`.

4. **Attestation of no execution**
   - The receipt must include proof or attestations that no side effect ran.
   - At minimum, it should state:
     - `execution_started: false`
     - `side_effects_detected: false`
     - `write_operations_made: false`
     - `external_calls_made: false`
   - When possible, it should include empty or inspected execution surfaces, such as no files modified, no outbound call receipt, no order id, no send id, no deployment id.

5. **Replayability**
   - The receipt must include the inputs needed to replay the denial:
     - requested action;
     - mandate or policy reference;
     - decision timestamp;
     - checks run;
     - expected denial result.
   - A reviewer should be able to verify that the same request under the same boundary would be refused again.

6. **Verifiability**
   - The receipt must be signed or hash-chained.
   - For a small implementation, a hash chain is enough:
     - canonical receipt JSON;
     - SHA-256 content hash;
     - previous receipt hash or chain anchor.
   - Stronger implementations may add a detached signature.

7. **Safe next action**
   - The receipt should state the safe path forward:
     - ask for human approval;
     - create a new mandate;
     - reduce scope;
     - stay in draft mode;
     - stop.

Why this is critical:

A refusal without proof is just another agent claim.  
Receipts over claims means the system must prove not only what it did, but also what it refused to do before execution.

---

## Minimal refusal receipt shape

See:

```text
specs/refusal-receipt.schema.json
```

Recommended example path:

```text
examples/refusal-receipts/
```

---

## Quick start

Use the checklist first:

```text
Can this agent act, or only propose?
```

Then require the three artifacts:

```text
agent_mandate.v0.md
next_best_action.v0.md
outbound_action_receipt.v0.md
```

For sensitive actions, keep the agent in proposal mode unless a human operator explicitly authorizes the action.

For denied actions, require a refusal receipt before any execution attempt.

---

## Examples

See `examples/`:

- `refused_action.md` - the agent refuses cleanly.
- `proposed_not_authorized.md` - the agent proposes, but does not act.
- `proposal_gate_receipt_chain.md` - proposal -> gate -> receipt.
- `refusal-receipts/forbidden-write.refused.json` - write denied inside a read-only boundary.
- `refusal-receipts/external-send.not-authorized.json` - external send denied because approval is missing.

---

## What this standard is good for

- AI coding agents
- research agents
- content assistants
- workflow automation
- operations assistants
- multi-agent coordination
- PR review and handoff workflows
- denial and refusal audit trails

---

## What this standard does not do

This standard does not grant:

- runtime authority;
- merge authority;
- send authority;
- trading authority;
- wallet authority;
- deployment authority;
- human approval authority.

It helps you describe and verify those boundaries.

The standard is public and declarative.  
Actual policy engines, governors, deny functions, and runtime enforcement belong in implementations.

---

## Design principles

### Closed by Default

Nothing is allowed unless the mandate, gate, or policy admits it.

### Evidence First

Every meaningful action or refusal should leave inspectable evidence.

### Human Bounds

Agents may propose. Humans, mandates, and gates define what may execute.

### Receipts Over Claims

A claim is not enough. A receipt should be replayable, inspectable, and verifiable.

---

## License

Apache-2.0.
