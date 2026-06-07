# ACE Agent Governance Receipt Standard

**A small, practical standard for keeping AI agents bounded, traceable, and revocable.**

Most AI-agent workflows fail in the same place: the agent can propose, act, or claim progress without leaving enough evidence for a human operator to know what happened.

This standard defines a minimal public pattern:

1. **Mandate** - what the agent is allowed to do.
2. **Next Best Action** - what the agent proposes before acting.
3. **Outbound Action Receipt** - what actually happened, with evidence and boundaries.

It is not a runtime.  
It is not a framework.  
It is not permission for an agent to act.

It is a simple governance layer for teams that want AI agents to remain bounded, auditable, and reversible.

---

## Why this exists

AI agents should not only answer.

They should leave evidence.

A useful agent system needs to answer three questions quickly:

- **Can this agent act, or only propose?**
- **What proof did it leave?**
- **Who can refuse, revoke, or review the action?**

This repo gives a compact, reusable shape for that.

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

Defines the proof left after an action or refusal.

It answers:

- what happened;
- what did not happen;
- what evidence exists;
- what boundary was respected;
- what remains unresolved.

---

## Core rule

> A proposal is not an action.  
> A receipt is not a claim.  
> A human approval gate is not optional.

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

---

## Examples

See `examples/`:

- `refused_action.md` - the agent refuses cleanly.
- `proposed_not_authorized.md` - the agent proposes, but does not act.
- `proposal_gate_receipt_chain.md` - proposal -> gate -> receipt.

---

## What this standard is good for

- AI coding agents
- research agents
- content assistants
- workflow automation
- operations assistants
- multi-agent coordination
- PR review and handoff workflows

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

---

## License

Apache-2.0.
