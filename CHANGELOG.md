# Changelog

## 0.2.0 - 2026-06-09

### Added

- Added explicit Refusal Receipts Requirements to the README.
- Added `specs/refusal-receipt.schema.json`.
- Added public refusal receipt examples:
  - `examples/refusal-receipts/forbidden-write.refused.json`
  - `examples/refusal-receipts/external-send.not-authorized.json`
- Added `tools/validate-refusal-receipts.py`, a stdlib-only validator for refusal receipt examples.

### Changed

- Clarified that a refusal receipt is a specialized outbound action receipt.
- Clarified that credible refusal receipts must be emitted before execution.
- Clarified minimum refusal evidence:
  - policy that fired;
  - agent context at decision time;
  - no side-effect attestation;
  - replay inputs;
  - signed or hash-chained integrity.

### Notes

- This standard remains public and declarative.
- Runtime enforcement belongs in implementations.
- Receipts Over Claims and fail-closed behavior remain the foundation.
- The validation script is intentionally dependency-free. CI workflow automation can be added later if explicitly enabled.
