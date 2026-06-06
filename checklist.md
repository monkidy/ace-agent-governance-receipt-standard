# Checklist

Status: Documentation standard.  
Runtime effect: None.

Use this checklist before connecting an agent to any tool that can change the world.

## First question

Can this agent act, or only propose?

If you cannot answer this in one sentence, the agent is not ready to be connected.

## Before granting a mandate

- [ ] The agent role is written in one line.
- [ ] The scope is named and bounded.
- [ ] The autonomy mode is set and justified.
- [ ] Allowed automation is listed explicitly.
- [ ] Blocked ungated actions are listed explicitly.
- [ ] Revocation conditions are listed.
- [ ] A human override exists and cannot be disabled.
- [ ] The lifecycle state is set, and is not ACTIVE by default.

## Before any outbound action

- [ ] The action was proposed, not assumed.
- [ ] The proposal names the gate required before acting.
- [ ] The gate has a named human or process responsible for it.
- [ ] A passed check is not treated as permission.

## After any action or refusal

- [ ] A receipt records what actually happened.
- [ ] The receipt names the mandate and the gate.
- [ ] The receipt does not claim to authorize the action.
- [ ] Open loops are listed or closed.

## Stop conditions

- [ ] No mandate means no action.
- [ ] No gate means no outbound action.
- [ ] No receipt means no durable proof.
- [ ] A revoked or expired mandate means stop.
- [ ] Human override is absolute.

## Rule

If the agent cannot produce a receipt, it should not act.
