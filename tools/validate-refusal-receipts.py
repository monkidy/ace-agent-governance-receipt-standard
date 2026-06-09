#!/usr/bin/env python3
"""Validate ACE refusal receipt examples with no external dependencies.

This is intentionally small. It does not replace full JSON Schema validation.
It checks the core proof invariants that make a refusal receipt credible:
pre-execution emission, policy decision, no side effects, replay, and integrity.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "specs" / "refusal-receipt.schema.json"
EXAMPLES_DIR = ROOT / "examples" / "refusal-receipts"

REQUIRED_TOP_LEVEL = {
    "schema_version",
    "receipt_id",
    "receipt_type",
    "status",
    "created_at",
    "emitted_before_execution",
    "agent_context",
    "requested_action",
    "policy",
    "decision",
    "no_side_effect_attestation",
    "integrity",
    "replay",
    "safe_next_action",
}

REQUIRED_AGENT_CONTEXT = {
    "agent_id",
    "agent_role",
    "operator",
    "workspace",
    "action_class",
    "boundary_mode",
    "approval_state",
}

REQUIRED_POLICY = {"policy_id", "policy_name", "rule_id", "reason"}
REQUIRED_DECISION = {"decision_id", "result", "checks_run", "refusal_reasons"}
REQUIRED_ATTESTATION = {
    "execution_started",
    "actual_action",
    "side_effects_detected",
    "write_operations_made",
    "external_calls_made",
    "files_modified",
    "commands_run",
    "proof",
}
REQUIRED_REPLAY = {"replay_inputs", "verification_steps", "expected_result"}

VALID_STATUS = {"REFUSED", "DENIED", "NOT_AUTHORIZED"}
VALID_ACTION_CLASS = {
    "READ_ONLY",
    "DRAFT_ONLY",
    "LOCAL_FILE_CHANGE",
    "EXTERNAL_ACTION",
    "SENSITIVE_ACTION",
}
VALID_APPROVAL_STATE = {"PRESENT", "MISSING", "EXPIRED", "REVOKED", "NOT_REQUIRED"}
VALID_INTEGRITY_METHOD = {"hash_chain", "signature", "hash_chain_and_signature"}


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - CLI diagnostics
        raise AssertionError(f"{path}: invalid JSON: {exc}") from exc


def require_keys(path: Path, obj: dict[str, Any], keys: set[str], label: str) -> None:
    missing = sorted(keys - set(obj))
    if missing:
        raise AssertionError(f"{path}: missing {label} keys: {', '.join(missing)}")


def require_non_empty_list(path: Path, obj: dict[str, Any], key: str) -> None:
    value = obj.get(key)
    if not isinstance(value, list) or not value:
        raise AssertionError(f"{path}: {key} must be a non-empty list")


def validate_integrity(path: Path, integrity: dict[str, Any]) -> None:
    method = integrity.get("method")
    if method not in VALID_INTEGRITY_METHOD:
        raise AssertionError(f"{path}: integrity.method invalid: {method!r}")
    content_hash = integrity.get("content_hash")
    if not isinstance(content_hash, str) or not content_hash.startswith("sha256:"):
        raise AssertionError(f"{path}: integrity.content_hash must start with sha256:")
    if method in {"hash_chain", "hash_chain_and_signature"}:
        if not integrity.get("previous_receipt_hash") and not integrity.get("chain_anchor"):
            raise AssertionError(
                f"{path}: hash-chain integrity needs previous_receipt_hash or chain_anchor"
            )
    if method in {"signature", "hash_chain_and_signature"}:
        signature = integrity.get("signature")
        if not isinstance(signature, dict) or not signature.get("algorithm") or not signature.get("value"):
            raise AssertionError(f"{path}: signature integrity needs algorithm and value")


def validate_receipt(path: Path) -> None:
    data = load_json(path)
    if not isinstance(data, dict):
        raise AssertionError(f"{path}: receipt root must be an object")

    require_keys(path, data, REQUIRED_TOP_LEVEL, "top-level")

    if data["schema_version"] != "ace.refusal_receipt.v0":
        raise AssertionError(f"{path}: schema_version must be ace.refusal_receipt.v0")
    if data["receipt_type"] != "refusal_receipt":
        raise AssertionError(f"{path}: receipt_type must be refusal_receipt")
    if data["status"] not in VALID_STATUS:
        raise AssertionError(f"{path}: status invalid: {data['status']!r}")
    if data["emitted_before_execution"] is not True:
        raise AssertionError(f"{path}: emitted_before_execution must be true")

    agent_context = data["agent_context"]
    if not isinstance(agent_context, dict):
        raise AssertionError(f"{path}: agent_context must be an object")
    require_keys(path, agent_context, REQUIRED_AGENT_CONTEXT, "agent_context")
    if agent_context["action_class"] not in VALID_ACTION_CLASS:
        raise AssertionError(f"{path}: action_class invalid: {agent_context['action_class']!r}")
    if agent_context["approval_state"] not in VALID_APPROVAL_STATE:
        raise AssertionError(f"{path}: approval_state invalid: {agent_context['approval_state']!r}")

    policy = data["policy"]
    if not isinstance(policy, dict):
        raise AssertionError(f"{path}: policy must be an object")
    require_keys(path, policy, REQUIRED_POLICY, "policy")

    decision = data["decision"]
    if not isinstance(decision, dict):
        raise AssertionError(f"{path}: decision must be an object")
    require_keys(path, decision, REQUIRED_DECISION, "decision")
    if decision["result"] not in VALID_STATUS:
        raise AssertionError(f"{path}: decision.result invalid: {decision['result']!r}")
    require_non_empty_list(path, decision, "checks_run")
    require_non_empty_list(path, decision, "refusal_reasons")

    attestation = data["no_side_effect_attestation"]
    if not isinstance(attestation, dict):
        raise AssertionError(f"{path}: no_side_effect_attestation must be an object")
    require_keys(path, attestation, REQUIRED_ATTESTATION, "no_side_effect_attestation")
    expected_false = [
        "execution_started",
        "side_effects_detected",
        "write_operations_made",
        "external_calls_made",
    ]
    for key in expected_false:
        if attestation[key] is not False:
            raise AssertionError(f"{path}: {key} must be false")
    if attestation["actual_action"] != "none":
        raise AssertionError(f"{path}: actual_action must be none")
    if attestation["files_modified"] != []:
        raise AssertionError(f"{path}: files_modified must be empty")
    if attestation["commands_run"] != []:
        raise AssertionError(f"{path}: commands_run must be empty")
    require_non_empty_list(path, attestation, "proof")

    validate_integrity(path, data["integrity"])

    replay = data["replay"]
    if not isinstance(replay, dict):
        raise AssertionError(f"{path}: replay must be an object")
    require_keys(path, replay, REQUIRED_REPLAY, "replay")
    require_non_empty_list(path, replay, "replay_inputs")
    require_non_empty_list(path, replay, "verification_steps")
    if not isinstance(replay["expected_result"], str) or not replay["expected_result"].strip():
        raise AssertionError(f"{path}: replay.expected_result must be non-empty")

    if not isinstance(data["safe_next_action"], str) or not data["safe_next_action"].strip():
        raise AssertionError(f"{path}: safe_next_action must be non-empty")


def main() -> int:
    load_json(SCHEMA_PATH)
    examples = sorted(EXAMPLES_DIR.glob("*.json"))
    if not examples:
        print(f"FAIL: no refusal receipt examples found in {EXAMPLES_DIR}", file=sys.stderr)
        return 1

    failures = 0
    for path in examples:
        try:
            validate_receipt(path)
        except AssertionError as exc:
            failures += 1
            print(f"FAIL: {exc}", file=sys.stderr)
        else:
            print(f"OK: {path.relative_to(ROOT)}")

    if failures:
        return 1
    print(f"Validated {len(examples)} refusal receipt example(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
