# OncoGuard-Response v0.77 — Three-Model Hard-Set Synthesis and Controller Comparison

## Purpose

v0.77 synthesizes the three-model hard action-obscured benchmark results and controller effects across GPT-4.1, Claude Sonnet 4.6, and Gemini Flash.

## Core finding

All three models showed clinically meaningful action-channel instability under the repaired hard action-obscured oncology therapeutic-authorization benchmark.

Unguided AACR:

- GPT-4.1: 61.7%.
- Claude Sonnet 4.6: 54.7%.
- Gemini Flash: 66.7%.

Wrong-channel rate:

- GPT-4.1: 38.3%.
- Claude Sonnet 4.6: 45.3%.
- Gemini Flash: 33.3%.

## Model-specific failure phenotypes

The hard benchmark revealed distinct model-specific routing phenotypes:

- GPT-4.1 primarily failed through generic wrong-channel escalation.
- Claude Sonnet 4.6 primarily failed through over-hold and under-switch behavior.
- Gemini Flash performed best overall but still showed under-hold and generic-escalation routing failures.

## Controller result

The deterministic evidence-contract controller restored evidence-consistent authorization across all three models:

- GPT-4.1: 61.7% → 100.0%.
- Claude Sonnet 4.6: 54.7% → 100.0%.
- Gemini Flash: 66.7% → 100.0%.

Across all three controller runs, wrong-channel rate, PTMAR, and unsafe authorization were reduced to 0.0% under the locked deterministic evidence/action contract.

## Interpretation

The results support a cross-model governance thesis: action-obscured naturalistic clinical pressure can expose therapeutic routing instability even when schema conformance is perfect. The specific failure phenotype varies by model, but a deterministic evidence-contract controller can normalize these failures by separating model reasoning from action authorization.

## Reporting caveat

The controller uses the locked expected-action channel as the evidence/action contract. It should be reported as a deterministic controller-mechanism study, not as a fully autonomous parser-derived clinical decision system.
