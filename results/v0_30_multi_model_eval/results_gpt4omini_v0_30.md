# OncoGuard-Response v0.30 — GPT-4o-mini Model Evaluation Result

## Overview

This analysis reports the corrected source-of-truth GPT-4o-mini evaluation for the OncoGuard-Response v0.30 model evaluation phase.

GPT-4o-mini was evaluated on the clean OncoGuard-Response v0.24 benchmark, consisting of 20 synthetic oncology therapeutic-response trajectories and 60 visit-level authorization decisions.

## Benchmark reference

Benchmark version:

`v0.24-clean-20trajectory-benchmark`

Benchmark source file:

`results/v0_24_clean_20trajectory_benchmark/visit_level_policy_inputs_v0_24_adjusted.csv`

Prompt file:

`results/v0_30_multi_model_eval/model_prompts_v0_30.csv`

Model output file:

`results/v0_30_multi_model_eval/openai_gpt4omini_outputs_v0_30.csv`

Score file:

`results/v0_30_multi_model_eval/openai_gpt4omini_scores_v0_30.csv`

Summary file:

`results/v0_30_multi_model_eval/openai_gpt4omini_summary_v0_30.csv`

Figure directory:

`results/v0_30_multi_model_eval/figures_gpt4omini_v0_30/`

## Model evaluated

| Field | Value |
|---|---|
| Model | GPT-4o-mini |
| Benchmark | v0.24 clean 20-trajectory benchmark |
| Visit-level decisions | 60 |
| Prompt format | Structured JSON-only therapeutic authorization prompt |
| Allowed actions | continue_therapy, escalate_evaluation, hold_therapy, switch_therapy, emergency_toxicity_management |

## Primary results

| Metric | Result |
|---|---:|
| Schema conformance | 100.0% |
| AACR | 40.0% |
| PTMAR | 0.0% |
| Unsafe authorization | 0.0% |
| Defer rate | 56.7% |
| Over-deferral | 23.3% |
| Over-hold | 15.0% |
| Over-emergency management | 6.7% |
| Over-switch / premature switch | 3.3% |

## Error taxonomy

| Error type | Count |
|---|---:|
| Correct authorization | 24 |
| Over-deferral when continuation authorized | 14 |
| Over-hold when continuation authorized | 9 |
| Under-action escalation instead of definitive safety action | 7 |
| Over-emergency management | 4 |
| Over-switch or premature switch | 2 |

## Selected action distribution

| Selected action | Count |
|---|---:|
| escalate_evaluation | 34 |
| hold_therapy | 13 |
| emergency_toxicity_management | 6 |
| switch_therapy | 4 |
| continue_therapy | 3 |

## Expected versus selected action interpretation

Across the 60 visit-level decisions, GPT-4o-mini selected `continue_therapy` only 3 times.

Among 28 visits where the benchmark expected `continue_therapy`, GPT-4o-mini selected:

| Selected action when continuation was expected | Count |
|---|---:|
| continue_therapy | 3 |
| escalate_evaluation | 14 |
| hold_therapy | 9 |
| emergency_toxicity_management | 1 |
| switch_therapy | 1 |

Thus, GPT-4o-mini selected continuation in only 3 of 28 continuation-authorized visits, or 10.7%.

## Governance phenotype

GPT-4o-mini demonstrated a schema-perfect conservative over-deferral phenotype.

The model produced valid structured JSON outputs for all 60 prompts and avoided premature therapy continuation entirely. PTMAR and unsafe authorization were both 0.0%.

However, this safety profile came with substantial over-conservatism. The model frequently escalated evaluation, held therapy, or selected higher-intensity safety actions when the benchmark expected continuation.

## Clinical interpretation

The corrected GPT-4o-mini result shows that oncology AI safety cannot be evaluated solely by the absence of unsafe continuation. A model may avoid premature therapy authorization while still creating clinically relevant risks through unnecessary deferral, treatment interruption, or escalation.

This result supports the central OncoGuard-Response framing: therapeutic-response AI systems should be evaluated for authorization calibration across sequential oncology visits, not merely for whether they avoid unsafe continuation.

## Main takeaway

GPT-4o-mini was highly schema-conformant and avoided unsafe therapeutic continuation, but showed a strong conservative bias. Its dominant failure mode was over-deferral when continuation was authorized.

This corrected v0.30 result demonstrates that OncoGuard-Response can phenotype oncology AI behavior as more than simply correct or incorrect. It can distinguish unsafe continuation risk from conservative treatment-delay risk.

## Provenance note

This result supersedes earlier exploratory GPT-4o-mini outputs generated before the benchmark integrity correction. Prior 39-row outputs and earlier mismatched 60-row summaries should be treated as exploratory or obsolete.

The source-of-truth result is the GPT-4o-mini evaluation run on the v0.24 clean 20-trajectory / 60-visit benchmark.
