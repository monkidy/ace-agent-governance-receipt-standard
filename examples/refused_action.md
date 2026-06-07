# Example: refused action

## Situation

The agent is asked to send a message to an external contact.

## Mandate check

The mandate allows drafting.  
It does not allow sending.

## Result

```text
status: REFUSED
reason: external send authority missing
```

## Receipt

```text
actual_action: drafted safe alternative
no_send: true
boundary_respected: true
requires_human_review: true
```

## Safe next action

The agent may prepare a draft for the operator to review manually.
