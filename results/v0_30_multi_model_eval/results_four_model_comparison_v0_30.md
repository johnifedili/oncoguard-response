# OncoGuard-Response v0.30 — Four-Model Comparison

## Overview

This analysis compares GPT-4o-mini, GPT-4.1, Claude Sonnet 4.6, and Gemini 3.1 Pro Preview on the corrected OncoGuard-Response v0.24 clean 20-trajectory / 60-visit benchmark.

All models were evaluated on the same 60 visit-level therapeutic authorization prompts derived from the v0.24 benchmark.

## Benchmark

Benchmark version:

`v0.24-clean-20trajectory-benchmark`

Prompt file:

`results/v0_30_multi_model_eval/model_prompts_v0_30.csv`

## Summary results

| Metric | GPT-4o-mini | GPT-4.1 | Claude Sonnet 4.6 | Gemini 3.1 Pro Preview |
|---|---:|---:|---:|---:|
| n | 60 | 60 | 60 | 60 |
| Schema conformance | 100.0% | 100.0% | 86.7% | 86.7% |
| AACR | 40.0% | 46.7% | 38.3% | 38.3% |
| PTMAR | 0.0% | 0.0% | 0.0% | 0.0% |
| Unsafe authorization | 0.0% | 0.0% | 0.0% | 0.0% |
| Defer rate | 56.7% | 70.0% | 70.0% | 60.0% |
| Over-deferral | 23.3% | 35.0% | 35.0% | 30.0% |
| Over-hold | 15.0% | 0.0% | 6.7% | 0.0% |
| Over-emergency management | 6.7% | 5.0% | 6.7% | 6.7% |
| Over-switch / premature switch | 3.3% | 3.3% | 1.7% | 3.3% |

## Key findings

All four models had 0.0% PTMAR and 0.0% unsafe authorization. None of the evaluated models prematurely authorized therapy continuation in the benchmark.

However, no model achieved high authorization calibration. AACR ranged from 38.3% to 46.7%.

GPT-4.1 achieved the highest AACR at 46.7%, but also showed the highest defer rate among the OpenAI models at 70.0%.

Claude Sonnet 4.6 and Gemini 3.1 Pro Preview both had lower schema conformance (86.7% and 86.7%, respectively), indicating provider-specific differences in structured-output reliability.

## Governance phenotypes

- GPT-4o-mini: schema-perfect conservative over-deferral / over-holding phenotype.
- GPT-4.1: schema-perfect conservative escalation phenotype with the highest AACR among tested models.
- Claude Sonnet 4.6: conservative escalation phenotype with schema fragility and very rare continuation.
- Gemini 3.1 Pro Preview: conservative over-deferral phenotype with schema fragility and low continuation frequency.

## Interpretation

The four-model comparison demonstrates that avoiding unsafe continuation is necessary but not sufficient for oncology therapeutic-response AI safety. Across OpenAI, Anthropic, and Google model families, no model prematurely continued therapy, yet all models showed clinically meaningful authorization-calibration failures.

The dominant failure mode was not permissive over-treatment; it was conservative over-escalation, over-deferral, over-holding, schema failure, or wrong-channel action selection. These behaviors can still be clinically important because unnecessary escalation, treatment delay, treatment interruption, or premature switching may disrupt oncology care.

## Main takeaway

OncoGuard-Response separates “not being unsafe” from “being clinically well-calibrated.” The benchmark reveals that models can achieve 0.0% premature therapy misuse while still failing therapeutic authorization calibration.
