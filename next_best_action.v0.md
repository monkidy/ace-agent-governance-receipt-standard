# Next Best Action v0

Status: Documentation standard.  
Runtime effect: None.

A Next Best Action record describes a proposal, a refusal, or a no-action verdict.

A proposal is not an action. It carries the gate that would be required before action.

## Required fields

```yaml
schema_version: next_best_action.v0
action_id: string
proposing_scope: string
kind: proposal | refusal | no_action
summary: string
```

## Optional fields

```yaml
proposed_action: string
required_gate: string
evidence:
  - string
refusal_reason: string
admissible: boolean
display_line: string
```

## Kinds

### `proposal`

Use when an action may be useful, but still requires a gate.

A proposal should include:

```yaml
required_gate: string
proposed_action: string
evidence:
  - string
admissible: true | false
```

### `refusal`

Use when the agent or system should not proceed.

A refusal should include:

```yaml
refusal_reason: string
admissible: false
```

### `no_action`

Use when doing nothing is the best outcome.

A no-action verdict should include:

```yaml
refusal_reason: string
```

## Example: proposal

```yaml
schema_version: next_best_action.v0
action_id: nba-doc-2026-001
proposing_scope: documentation_review
kind: proposal
summary: publish the cleaned documentation draft after human review
proposed_action: publish the reviewed documentation draft to the public repository
required_gate: human_publication_review
evidence:
  - checklist completed
  - license file present
  - private references removed
admissible: true
display_line: publication candidate ready, human review required
```

## Example: refusal

```yaml
schema_version: next_best_action.v0
action_id: nba-doc-2026-002
proposing_scope: documentation_review
kind: refusal
summary: refuse publication because private references remain
refusal_reason: private references were found in the draft
evidence:
  - filtering checklist failed
admissible: false
display_line: publication refused, filtering incomplete
```

## Rule

A suggested next step is still only a suggestion until the required gate passes.
