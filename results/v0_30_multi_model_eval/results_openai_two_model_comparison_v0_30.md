# OncoGuard-Response v0.30 — OpenAI Two-Model Comparison

## Overview

This analysis compares GPT-4o-mini and GPT-4.1 on the corrected OncoGuard-Response v0.24 clean 20-trajectory / 60-visit benchmark.

Both models were evaluated on the same 60 visit-level therapeutic authorization prompts derived from the v0.24 benchmark.

## Benchmark

Benchmark version:

`v0.24-clean-20trajectory-benchmark`

Prompt file:

`results/v0_30_multi_model_eval/model_prompts_v0_30.csv`

## Summary results

| Metric | GPT-4o-mini | GPT-4.1 |
|---|---:|---:|
| n | 60 | 60 |
| Schema conformance | 100.0% | 100.0% |
| AACR | 40.0% | 46.7% |
| PTMAR | 0.0% | 0.0% |
| Unsafe authorization | 0.0% | 0.0% |
| Defer rate | 56.7% | 70.0% |
| Over-deferral | 23.3% | 35.0% |
| Over-hold | 15.0% | 0.0% |
| Over-emergency management | 6.7% | 5.0% |
| Over-switch / premature switch | 3.3% | 3.3% |

## Key findings

Both models achieved 100.0% schema conformance and 0.0% PTMAR / unsafe authorization, indicating that neither model prematurely continued therapy in the benchmark.

GPT-4.1 achieved higher AACR than GPT-4o-mini:

- GPT-4o-mini AACR: 40.0%
- GPT-4.1 AACR: 46.7%

However, GPT-4.1 was more defer-heavy:

- GPT-4o-mini defer rate: 56.7%
- GPT-4.1 defer rate: 70.0%

GPT-4.1 also showed higher over-deferral:

- GPT-4o-mini over-deferral: 23.3%
- GPT-4.1 over-deferral: 35.0%

## Governance phenotype

GPT-4o-mini demonstrated a schema-perfect conservative over-deferral / over-holding phenotype.

GPT-4.1 demonstrated a schema-perfect conservative escalation phenotype, with higher AACR but more frequent escalation rather than continuation.

## Interpretation

The comparison shows that larger model capacity did not eliminate authorization calibration failure. GPT-4.1 improved overall authorization alignment but remained highly conservative, frequently escalating evaluation when continuation was expected.

This supports the central OncoGuard-Response claim: oncology AI systems should not be evaluated only for avoidance of unsafe continuation. They should also be evaluated for treatment-delay risk, over-deferral, over-holding, premature switching, and wrong-channel escalation.

## Main takeaway

Both models avoided unsafe continuation, but both showed conservative authorization bias. GPT-4.1 improved AACR relative to GPT-4o-mini while increasing defer-heavy behavior. OncoGuard-Response therefore reveals a clinically meaningful governance tradeoff: safety against premature continuation may coexist with unnecessary treatment delay or interruption.
