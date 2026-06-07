# Agent Mandate v0

A mandate defines what an agent is allowed to do.

## Agent

```text
name:
role:
operator:
workspace:
date:
```

## Purpose

```text
This agent exists to:
```

## Allowed actions

```text
The agent may:
- read:
- draft:
- analyze:
- propose:
- modify:
```

## Forbidden actions

```text
The agent must not:
- send messages:
- publish:
- deploy:
- merge:
- trade:
- spend:
- access secrets:
- mutate live systems:
```

## Required evidence

```text
The agent must leave:
- source references:
- files changed:
- commands run:
- tests run:
- result:
- remaining risks:
```

## Stop conditions

```text
The agent must stop if:
- the mandate is unclear;
- a secret is required;
- approval is missing;
- the action would affect an external system;
- the risk exceeds the mandate;
- the operator revokes permission.
```

## Human approval

```text
approval_required_for:
approval_format:
approval_expiry:
revocation_path:
```

## Status

```text
MANDATE_STATUS:
- DRAFT
- ACTIVE
- EXPIRED
- REVOKED
```
