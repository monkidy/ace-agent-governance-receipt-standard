# Example: proposed but not authorized

## Situation

The agent proposes updating a production workflow.

## Proposal

```text
recommended_action: update production workflow
action_class: SENSITIVE_ACTION
approval_required: true
```

## Gate

No human approval was provided.

## Result

```text
status: NOT_AUTHORIZED
actual_action: none
no_deploy: true
no_external_action: true
```

## Receipt

The agent records the proposal and waits for a human decision.
