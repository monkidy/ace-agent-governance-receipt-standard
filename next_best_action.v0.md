# Next Best Action v0

A Next Best Action is a proposed action before execution.

It is not permission to act.

## Proposal

```text
proposal_id:
agent:
operator:
created_at:
```

## Recommended action

```text
I recommend:
```

## Why

```text
Reason:
```

## Scope

```text
files_or_systems_affected:
external_systems_affected:
expected_output:
```

## Action class

```text
action_class:
- READ_ONLY
- DRAFT_ONLY
- LOCAL_FILE_CHANGE
- EXTERNAL_ACTION
- SENSITIVE_ACTION
```

## Required approval

```text
approval_required:
approval_reason:
approval_expiry:
```

## Risk

```text
risk_level:
- LOW
- MEDIUM
- HIGH

risk_notes:
```

## Reversibility

```text
rollback_possible:
rollback_plan:
```

## Evidence expected

```text
receipt_required:
tests_required:
diff_required:
```

## Decision

```text
decision:
- PROPOSED
- APPROVED
- REFUSED
- DEFERRED
```
