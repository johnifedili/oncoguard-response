# v0.80 Reproducibility Statement

All primary analyses were performed in the `oncoguard-response` repository on branch `v0.24-clean-benchmark-branch`.

Current provenance package commit:

- Branch: `v0.24-clean-benchmark-branch`
- Commit: `699272d075e1554b4122bf9d9a126bc1c415bf29`
- Package version: `v0.80`

## Locked prompt set

The primary hard benchmark input is:

`results/v0_66d_targeted_actioncue_repair/v0_66d_model_testing_allowed_hard_prompts.csv`

This prompt set contains 300 repaired hard action-obscured prompts and was used for GPT-4.1, Claude Sonnet 4.6, and Gemini Flash evaluations.

## Primary model runs

- GPT-4.1: v0.67
- Claude Sonnet 4.6: v0.72
- Gemini Flash: v0.75

## Controller runs

- GPT-4.1 controller: v0.68
- Claude controller: v0.73
- Gemini controller: v0.76

## Synthesis and manuscript artifacts

- Three-model hard-set synthesis: v0.77
- Results/Discussion skeleton: v0.78
- Full manuscript scaffold: v0.79

## Important methodological caveat

The deterministic evidence-contract controller uses the locked expected-action channel as the evidence/action contract. This package demonstrates a controller mechanism and benchmark-governance approach, not a fully autonomous parser-derived clinical decision system.
