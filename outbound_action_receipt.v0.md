# Outbound Action Receipt v0

Status: Documentation standard.  
Runtime effect: None.

An Outbound Action Receipt records what happened after a decision reached a gate.

Receipts prove; they do not authorize.

A receipt may record a completed action, a partial action, a gate rejection, or a refusal. The key point is that the record must say what actually happened.

## Required fields

```yaml
schema_version: outbound_action_receipt.v0
receipt_id: string
mandate_id: string
acted_at: ISO-8601 datetime
action_summary: string
gate_passed: string
evidence:
  - string
outcome: completed | partial | rejected_at_gate | refused
```

## Optional fields

```yaml
action_ref: string
scope_name: string
governor_walls_checked:
  - string
stop_condition_asserted: boolean
closeout_ref: string
```

## Field notes

### `gate_passed`

The explicit gate that allowed the action, or the gate that rejected it.

Examples:

```yaml
gate_passed: human_publication_review
gate_passed: security_review_failed
gate_passed: license_review_required
```

### `outcome`

Use one of:

```text
completed = the authorized action completed
partial = the authorized action partly completed
rejected_at_gate = the proposed action did not pass the gate
refused = the system refused to act
```

### `stop_condition_asserted`

Recommended default:

```yaml
stop_condition_asserted: false
```

If a stop condition exists, the action should not continue.

## Example: completed

```yaml
schema_version: outbound_action_receipt.v0
receipt_id: receipt-doc-2026-001
mandate_id: mandate-doc-review-2026-001
action_ref: nba-doc-2026-001
scope_name: documentation_review
acted_at: 2026-06-06T12:00:00Z
action_summary: published the reviewed documentation draft after human approval
gate_passed: human_publication_review
governor_walls_checked:
  - license present
  - private references removed
  - no external secrets
stop_condition_asserted: false
evidence:
  - human review marked complete
  - Apache-2.0 license present
  - filtering log complete
outcome: completed
closeout_ref: closeout-doc-2026-001
```

## Example: rejected at gate

```yaml
schema_version: outbound_action_receipt.v0
receipt_id: receipt-doc-2026-002
mandate_id: mandate-doc-review-2026-001
action_ref: nba-doc-2026-002
scope_name: documentation_review
acted_at: 2026-06-06T12:30:00Z
action_summary: publication did not occur because the filtering gate failed
gate_passed: human_publication_review_failed
governor_walls_checked:
  - private references removed
  - license present
stop_condition_asserted: true
evidence:
  - private reference found during review
outcome: rejected_at_gate
closeout_ref: closeout-doc-2026-002
```

## Rule

If there is no receipt, the system has no durable proof of what happened.
