# OncoGuard-Response v0.30 — Three-Model Comparison

## Overview

This analysis compares GPT-4o-mini, GPT-4.1, and Claude Sonnet 4.6 on the corrected OncoGuard-Response v0.24 clean 20-trajectory / 60-visit benchmark.

All models were evaluated on the same 60 visit-level therapeutic authorization prompts derived from the v0.24 benchmark.

## Benchmark

Benchmark version:

`v0.24-clean-20trajectory-benchmark`

Prompt file:

`results/v0_30_multi_model_eval/model_prompts_v0_30.csv`

## Summary results

| Metric | GPT-4o-mini | GPT-4.1 | Claude Sonnet 4.6 |
|---|---:|---:|---:|
| n | 60 | 60 | 60 |
| Schema conformance | 100.0% | 100.0% | 86.7% |
| AACR | 40.0% | 46.7% | 38.3% |
| PTMAR | 0.0% | 0.0% | 0.0% |
| Unsafe authorization | 0.0% | 0.0% | 0.0% |
| Defer rate | 56.7% | 70.0% | 70.0% |
| Over-deferral | 23.3% | 35.0% | 35.0% |
| Over-hold | 15.0% | 0.0% | 6.7% |
| Over-emergency management | 6.7% | 5.0% | 6.7% |
| Over-switch / premature switch | 3.3% | 3.3% | 1.7% |

## Key findings

All three models had 0.0% PTMAR and 0.0% unsafe authorization. None of the evaluated models prematurely authorized therapy continuation in the benchmark.

However, the models differed in deployment reliability and authorization calibration. GPT-4o-mini and GPT-4.1 achieved 100.0% schema conformance, whereas Claude Sonnet 4.6 achieved 86.7% schema conformance.

GPT-4.1 achieved the highest AACR at 46.7%, compared with 40.0% for GPT-4o-mini and 38.3% for Claude Sonnet 4.6.

Despite the absence of unsafe continuation, all models showed conservative authorization bias. GPT-4.1 and Claude Sonnet 4.6 each had a defer rate of 70.0% and 70.0%, respectively. GPT-4o-mini was less defer-heavy but showed more over-holding than GPT-4.1.

## Governance phenotypes

- GPT-4o-mini: schema-perfect conservative over-deferral / over-holding phenotype.
- GPT-4.1: schema-perfect conservative escalation phenotype with the highest AACR among tested models.
- Claude Sonnet 4.6: conservative escalation phenotype with lower schema conformance and very rare continuation.

## Interpretation

The three-model comparison demonstrates that avoiding unsafe continuation is necessary but not sufficient for oncology therapeutic-response AI safety. Across OpenAI and Anthropic model families, no model prematurely continued therapy in the benchmark, yet all models showed clinically meaningful authorization-calibration failures.

The dominant failure pattern was not permissive over-treatment; it was conservative over-escalation or treatment-delay behavior. This suggests that model safety evaluations should measure both unsafe action and excessive caution, because unnecessary deferral, holding, emergency escalation, or premature switching can also disrupt oncology care.

## Main takeaway

OncoGuard-Response reveals provider- and model-specific therapeutic authorization phenotypes. The benchmark distinguishes unsafe continuation risk from conservative treatment-delay risk and identifies schema conformance as a separate deployment-reliability dimension.
