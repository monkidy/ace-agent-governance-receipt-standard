# Example: proposal -> gate -> receipt chain

## 1. Mandate

```text
agent: docs-agent
allowed: edit markdown docs
forbidden: publish, deploy, send
```

## 2. Next Best Action

```text
proposal: update README wording
action_class: LOCAL_FILE_CHANGE
approval_required: false
```

## 3. Gate

```text
gate_result: allowed inside mandate
```

## 4. Receipt

```text
status: COMPLETED
files_modified: README.md
tests_run: markdown review
no_publish: true
no_external_action: true
boundary_respected: true
```

## 5. Review

The operator can inspect the diff and approve publication separately.
