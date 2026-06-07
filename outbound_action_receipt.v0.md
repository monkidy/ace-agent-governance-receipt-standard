# Outbound Action Receipt v0

A receipt records what happened.

It is not a promise.  
It is not a claim without evidence.

## Receipt

```text
receipt_id:
agent:
operator:
created_at:
```

## Action

```text
requested_action:
actual_action:
```

## Status

```text
status:
- COMPLETED
- REFUSED
- PARTIAL
- BLOCKED
- NOT_AUTHORIZED
```

## Boundary

```text
mandate_id:
approval_id:
action_class:
boundary_respected:
```

## Evidence

```text
sources_read:
files_created:
files_modified:
files_deleted:
commands_run:
tests_run:
test_result:
diff_summary:
```

## What did not happen

```text
no_send:
no_publish:
no_deploy:
no_merge:
no_secret_access:
no_external_action:
```

## Risk and residue

```text
remaining_risks:
known_gaps:
requires_human_review:
```

## Next action

```text
recommended_next_action:
```
