# Example 2 — Proposed but not authorized

This example shows a useful action that cannot proceed until the required gate passes.

## Mandate

```yaml
schema_version: agent_mandate.v0
mandate_id: mandate-release-note-001
agent_role: release note assistant
scope_name: draft release notes
autonomy_mode: 2
lifecycle_state: ACTIVE
allowed_automation:
  - read approved changelog entries
  - draft release notes
  - propose publication text
blocked_ungated_actions:
  - publish release notes
  - tag a release
  - notify users
  - modify production configuration
evidence_requirement: every release note must cite an approved changelog entry
receipt_required: true
revocation_conditions:
  - human override
  - missing changelog evidence
  - attempted external publication
human_override_absolute: true
```

## Next best action

```yaml
schema_version: next_best_action.v0
action_id: nba-release-note-001
proposing_scope: release_notes
kind: proposal
summary: publish release notes after human review
proposed_action: publish the prepared release notes
required_gate: human_publication_review
evidence:
  - approved changelog entries reviewed
  - draft release notes prepared
admissible: true
display_line: release note candidate ready, publication gate required
```

## Receipt

```yaml
schema_version: outbound_action_receipt.v0
receipt_id: receipt-release-note-001
mandate_id: mandate-release-note-001
action_ref: nba-release-note-001
scope_name: release_notes
acted_at: 2026-06-06T11:00:00Z
action_summary: release notes were not published because the human publication gate had not passed
gate_passed: human_publication_review_not_passed
governor_walls_checked:
  - no external publication without review
  - no user notification without review
stop_condition_asserted: false
evidence:
  - proposed action required human_publication_review
  - no approval record present
outcome: rejected_at_gate
closeout_ref: closeout-release-note-001
```

## Lesson

A proposal can be good and still not be authorized.
