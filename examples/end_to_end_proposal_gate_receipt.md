# Example 3: End-to-end proposal, gate, receipt

This example shows a full chain: mandate, proposal, gate, receipt, closeout.

## 1. Mandate

```yaml
schema_version: agent_mandate.v0
mandate_id: mandate-doc-package-001
agent_role: documentation packaging assistant
scope_name: public documentation package
autonomy_mode: 2
lifecycle_state: ACTIVE
allowed_automation:
  - assemble markdown files
  - check internal links
  - verify license file exists
  - produce a publication checklist
blocked_ungated_actions:
  - publish repository
  - change license
  - include private information
  - contact external people
evidence_requirement: every publication proposal must include license, filtering, and example checks
receipt_required: true
governor_walls:
  - no external publication without human review
  - no private information
  - license must be present
revocation_conditions:
  - human override
  - missing license
  - private information found
  - attempted publication without review
human_override_absolute: true
```

## 2. Proposal

```yaml
schema_version: next_best_action.v0
action_id: nba-doc-package-001
proposing_scope: public_documentation_package
kind: proposal
summary: package is ready for human publication review
proposed_action: publish the documentation package to a public repository
required_gate: human_publication_review
evidence:
  - LICENSE present
  - filtering checklist complete
  - examples included
  - no private references found by agent review
admissible: true
display_line: documentation package ready for human review, not yet publishable
```

## 3. Gate result

```yaml
gate_id: human_publication_review
gate_result: passed
reviewed_by: human_operator
reviewed_at: 2026-06-06T12:00:00Z
conditions_checked:
  - Apache-2.0 license present
  - no private references
  - no secrets
  - examples readable
  - no claim of autonomous runtime
```

## 4. Receipt

```yaml
schema_version: outbound_action_receipt.v0
receipt_id: receipt-doc-package-001
mandate_id: mandate-doc-package-001
action_ref: nba-doc-package-001
scope_name: public_documentation_package
acted_at: 2026-06-06T12:10:00Z
action_summary: documentation package approved for publication after human review
gate_passed: human_publication_review
governor_walls_checked:
  - license present
  - filtering complete
  - no private information
  - no external action before gate
stop_condition_asserted: false
evidence:
  - gate human_publication_review passed
  - filtering checklist complete
  - examples present
  - runtime claims absent
outcome: completed
closeout_ref: closeout-doc-package-001
```

## 5. Closeout

```yaml
closeout_id: closeout-doc-package-001
status: closed
summary: publication gate passed and receipt recorded
open_loops:
  - none
```

## Lesson

The governance value is the chain, not the agent.

```text
mandate -> proposal -> gate -> receipt -> closeout
```
