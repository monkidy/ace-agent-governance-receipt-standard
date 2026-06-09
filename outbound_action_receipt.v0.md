# Outbound Action Receipt v0

A receipt records what happened, what did not happen, and what evidence exists.

It is not a promise.  
It is not a claim without evidence.  
It is not permission to act.

---

## Receipt

```text
receipt_id:
receipt_type:
agent:
operator:
created_at:
```

Recommended `receipt_type` values:

```text
ACTION_RECEIPT
REFUSAL_RECEIPT
BLOCKED_ACTION_RECEIPT
PARTIAL_ACTION_RECEIPT
```

---

## Action

```text
requested_action:
actual_action:
```

For a refusal receipt:

```text
requested_action: the action that was requested or proposed
actual_action: none
execution_started: false
```

---

## Status

```text
status:
- COMPLETED
- REFUSED
- DENIED
- PARTIAL
- BLOCKED
- NOT_AUTHORIZED
```

Use:

- `REFUSED` when the agent or governor refuses before execution;
- `DENIED` when a policy or gate explicitly denies the action;
- `NOT_AUTHORIZED` when required approval or mandate is missing.

---

## Boundary

```text
mandate_id:
proposal_id:
approval_id:
action_class:
boundary_respected:
```

---

## Policy or gate decision

Required for refusal, denial, and not-authorized receipts.

```text
policy_id:
policy_name:
rule_id:
decision:
refusal_reasons:
checks_run:
```

The reason must be specific enough to replay.

Examples:

```text
writes_allowed=false
approval_missing
external_send_not_authorized
action_class_exceeds_mandate
secret_access_forbidden
```

---

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

For refusal receipts, evidence should prove the denial happened before execution.

---

## What did not happen

```text
no_send:
no_publish:
no_deploy:
no_merge:
no_secret_access:
no_external_action:
no_write:
no_order:
no_wallet_action:
```

---

## No side-effect attestation

Required for refusal receipts.

```text
execution_started: false
side_effects_detected: false
write_operations_made: false
external_calls_made: false
runtime_action_id: none
outbound_request_id: none
```

A refusal receipt should not hide a failed or partial action. If any side effect happened, use `PARTIAL` or `BLOCKED`, not `REFUSED`.

---

## Integrity

A receipt should be signed or hash-chained.

```text
content_hash:
previous_receipt_hash:
signature:
chain_anchor:
```

For small implementations, a SHA-256 hash chain is sufficient.  
For stronger systems, add a detached signature.

---

## Replay

```text
replay_inputs:
verification_steps:
expected_result:
```

A reviewer should be able to verify that the same request under the same boundary would be refused again.

---

## Risk and residue

```text
remaining_risks:
known_gaps:
requires_human_review:
```

---

## Next action

```text
recommended_next_action:
```
