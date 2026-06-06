# Example 1 — Clean refusal

This example shows an agent refusing to publish because the filtering gate failed.

## Mandate

```yaml
schema_version: agent_mandate.v0
mandate_id: mandate-public-doc-review-001
agent_role: documentation reviewer
scope_name: public documentation draft
autonomy_mode: 2
lifecycle_state: ACTIVE
allowed_automation:
  - review draft files
  - identify publication blockers
  - propose edits
blocked_ungated_actions:
  - publish files
  - send messages
  - remove license terms
  - expose private information
evidence_requirement: every blocker must cite the file and section
receipt_required: true
revocation_conditions:
  - human override
  - private information detected
  - attempted publication
human_override_absolute: true
```

## Next best action

```yaml
schema_version: next_best_action.v0
action_id: nba-public-doc-001
proposing_scope: public_documentation
kind: refusal
summary: refuse publication because private information remains
refusal_reason: the draft contains private or project-specific references that require human removal
evidence:
  - filtering checklist failed
admissible: false
display_line: publication refused, filtering incomplete
```

## Receipt

```yaml
schema_version: outbound_action_receipt.v0
receipt_id: receipt-public-doc-001
mandate_id: mandate-public-doc-review-001
action_ref: nba-public-doc-001
scope_name: public_documentation
acted_at: 2026-06-06T10:00:00Z
action_summary: publication did not occur because filtering failed
gate_passed: filtering_gate_failed
governor_walls_checked:
  - no private information
  - no unapproved publication
stop_condition_asserted: true
evidence:
  - filtering checklist failed
outcome: refused
closeout_ref: closeout-public-doc-001
```

## Lesson

A refusal is a valid system output.
