# ACE Agent Governance Receipt Standard v0

**How to keep AI agents bounded, traceable, and revocable.**

Status: Draft for human review.  
Runtime effect: None.  
This repository documents a governance pattern. It does not provide an autonomous agent system, a runtime, a deployment framework, or permission for any agent to act on the outside world.

## Why this exists

Teams are increasingly giving AI agents access to tools, repositories, tickets, files, messages, and operational workflows.

The risk is not only that an agent makes a mistake. The deeper risk is that nobody can clearly answer:

- What was this agent allowed to do?
- What was it forbidden to do?
- Was this an action, a proposal, or a refusal?
- Which gate was required before acting?
- What proof exists after the action?
- Who can revoke the mandate?

This standard gives a small, practical vocabulary for answering those questions.

## Core idea

An agent should not be treated as a magic assistant or a sovereign operator.

An agent should operate under a mandate.

A mandate defines:

- the agent role,
- its current lifecycle state,
- what it may automate,
- what it may not do without a gate,
- what evidence it must produce,
- how and when it can be revoked,
- whether a human override exists.

A proposed action is not an action.  
A passed check is not permission.  
A receipt proves what happened after the fact; it does not authorize the action.

## The three records

This standard uses three public records:

1. `agent_mandate.v0.md`  
   Defines the agent's bounded mandate.

2. `next_best_action.v0.md`  
   Defines a proposal, refusal, or no-action verdict. A proposal must name the gate required before it can become action.

3. `outbound_action_receipt.v0.md`  
   Defines the after-the-fact proof record for an action, refusal, or gate rejection.

## Minimal operating loop

```text
mandate -> proposal/refusal -> gate -> action or refusal -> receipt -> closeout
```

The loop is intentionally conservative:

```text
no mandate = no action
no gate = no outbound action
no receipt = no durable proof
revoked mandate = stop
expired mandate = stop
human override = absolute
```

## What this standard is

- A documentation standard.
- A lightweight governance pattern for AI-agent operations.
- A reusable checklist for deciding whether an agent can act or only propose.
- A public, generic extraction of a bounded-agent governance model.

## What this standard is not

- Not an autonomous firm.
- Not a live runtime.
- Not a trading, finance, legal, medical, or security product.
- Not a deployment framework.
- Not a replacement for human responsibility.
- Not permission for any agent to email, publish, merge, spend money, access secrets, or modify external systems.

## Repository contents

```text
.
├── README.md
├── LICENSE
├── MANIFEST.json
├── NOTICE
├── agent_mandate.v0.md
├── next_best_action.v0.md
├── outbound_action_receipt.v0.md
├── checklist.md
├── FILTERING_LOG.md
└── examples/
    ├── refused_action.md
    ├── proposed_not_authorized.md
    └── end_to_end_proposal_gate_receipt.md
```

## Recommended use

Use this standard before connecting an agent to any tool that can change the world.

Start with the checklist:

```text
Can this agent act, or only propose?
```

Then write the mandate.

Then require every proposed action to name its gate.

Then require every acted or refused decision to produce a receipt.

## License

Apache License 2.0.

---

© 2026 Hichem Benali · GitHub: [@monkidy](https://github.com/monkidy) · Part of the ACE project.
