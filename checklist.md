# Agent Mandate v0

Status: Documentation standard.  
Runtime effect: None.

An Agent Mandate defines the bounded, traced, revocable scope under which an AI agent may operate.

An agent has no standing permission to act. It may only operate inside a granted mandate and only within the limits of that mandate.

## Required fields

```yaml
schema_version: agent_mandate.v0
mandate_id: string
agent_role: string
scope_name: string
autonomy_mode: integer
lifecycle_state: PROPOSED | REVIEWED | GRANTED | ACTIVE | REVOKED | EXPIRED | CLOSED
allowed_automation:
  - string
blocked_ungated_actions:
  - string
revocation_conditions:
  - string
human_override_absolute: true
```

## Optional fields

```yaml
valid_until: ISO-8601 datetime
evidence_requirement: string
receipt_required: boolean
governor_walls:
  - string
```

## Field notes

### `mandate_id`

A stable identifier for the mandate.

Example:

```yaml
mandate_id: mandate-doc-review-2026-001
```

### `agent_role`

The role the agent is allowed to perform.

Examples:

```yaml
agent_role: documentation reviewer
agent_role: repository assistant
agent_role: research summarizer
agent_role: quality auditor
```

### `scope_name`

The bounded work area.

Examples:

```yaml
scope_name: public documentation draft
scope_name: internal ticket triage
scope_name: read-only research packet
```

### `autonomy_mode`

A simple numeric mode. Each organization may define its own ladder.

Recommended baseline:

```text
0 = documentation only
1 = read-only internal analysis
2 = draft proposals
3 = prepare internal records
4 = gated outbound action
5+ = organization-specific, requires explicit governance
```

No agent self-promotes. Moving up requires a new mandate or explicit gate.

### `lifecycle_state`

A mandate should never be treated as active unless the lifecycle state says it is active.

```text
PROPOSED = drafted, not usable
REVIEWED = checked, not yet granted
GRANTED = approved but not necessarily running
ACTIVE = usable within scope
REVOKED = stopped
EXPIRED = no longer valid
CLOSED = completed and archived
```

### `allowed_automation`

What the agent may do without another gate.

Examples:

```yaml
allowed_automation:
  - read files in the approved folder
  - summarize findings
  - draft a pull request description
  - propose a response
```

### `blocked_ungated_actions`

What the agent may not do unless a separate gate explicitly allows it.

Examples:

```yaml
blocked_ungated_actions:
  - send messages
  - publish content
  - merge code
  - modify production systems
  - access secrets
  - spend money
  - create external accounts
```

### `revocation_conditions`

Conditions that immediately end the mandate.

Examples:

```yaml
revocation_conditions:
  - human override
  - expired valid_until
  - scope violation
  - missing evidence
  - attempted blocked action
  - unsafe or non-compliant output
```

### `human_override_absolute`

Must be `true`.

```yaml
human_override_absolute: true
```

The human override cannot be disabled by an agent, tool, workflow, model, or automated process.

## Example

```yaml
schema_version: agent_mandate.v0
mandate_id: mandate-doc-review-2026-001
agent_role: documentation reviewer
scope_name: public documentation draft
autonomy_mode: 2
lifecycle_state: ACTIVE
allowed_automation:
  - read the draft files
  - identify unclear language
  - propose edits
blocked_ungated_actions:
  - publish the draft
  - send messages to external people
  - change license terms
  - access secrets
evidence_requirement: every proposal must cite the file and section reviewed
receipt_required: true
governor_walls:
  - no external action
  - no secret access
  - no license change
revocation_conditions:
  - human override
  - attempted publication
  - uncited factual claim
  - expired mandate
valid_until: 2026-12-31T23:59:59Z
human_override_absolute: true
```

## Rule

A mandate is a leash, not a crown.
