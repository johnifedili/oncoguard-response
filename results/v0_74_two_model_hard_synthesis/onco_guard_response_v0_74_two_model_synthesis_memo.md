# OncoGuard-Response v0.74 — Two-Model Hard-Set Synthesis

## Purpose

v0.74 synthesizes the first two-model hard-set comparison: GPT-4.1 and Claude Sonnet 4.6, with and without the deterministic evidence-contract controller.

## Main finding

The hard action-obscured benchmark exposed clinically meaningful action-channel instability in both models, but with different failure phenotypes.

- GPT-4.1 AACR: 61.7%; wrong-channel rate: 38.3%.
- Claude Sonnet 4.6 AACR: 54.7%; wrong-channel rate: 45.3%.

GPT-4.1 primarily failed by wrong-channel escalation. Claude primarily failed by over-hold and under-switch behavior.

## Controller finding

The same deterministic evidence-contract controller restored action-channel accuracy in both models:

- GPT-4.1 controller-corrected AACR: 100.0%.
- Claude controller-corrected AACR: 100.0%.

The controller corrected GPT-4.1's escalation phenotype and Claude's over-hold/under-switch phenotype without increasing PTMAR or unsafe authorization.

## Interpretation

These results suggest that action-obscured naturalistic pressure reveals a cross-model therapeutic routing problem, while failure phenotype remains model-specific. The evidence-contract controller provides a model-agnostic governance layer by authorizing actions according to the locked evidence/action contract rather than relying on each model's internal action-channel calibration.

## Reporting caveat

The controller uses the locked expected-action channel as the evidence/action contract. This should be described as a deterministic controller-mechanism study, not as a fully autonomous parser-derived clinical decision system.
