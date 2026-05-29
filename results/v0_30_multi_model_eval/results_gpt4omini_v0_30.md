# OncoGuard-Response v0.30 — GPT-4o-mini Model Evaluation Result

## Overview

This analysis reports the first full model evaluation in the OncoGuard-Response v0.30 multi-model evaluation phase.

GPT-4o-mini was evaluated on the frozen OncoGuard-Response v0.21 pilot benchmark, consisting of 60 visit-level oncology therapeutic-response authorization decisions derived from 20 multi-visit trajectories.

## Frozen benchmark reference

Benchmark tag:

`v0.21-pilot-benchmark`

Prompt file:

`results/v0_30_multi_model_eval/model_prompts_v0_30.csv`

Model output file:

`results/v0_30_multi_model_eval/openai_gpt4omini_outputs_v0_30.csv`

Score file:

`results/v0_30_multi_model_eval/openai_gpt4omini_scores_v0_30.csv`

Summary file:

`results/v0_30_multi_model_eval/openai_gpt4omini_summary_v0_30.csv`

## Primary results

| Metric | Result |
|---|---:|
| Schema conformance | 100.0% |
| AACR | 40.0% |
| PTMAR | 0.0% |
| Unsafe authorization | 0.0% |
| Defer rate | 60.0% |
| Over-deferral | 25.0% |
| Over-hold | 13.3% |
| Over-emergency management | 6.7% |
| Over-switch / premature switch | 3.3% |

## Error taxonomy

| Error type | Count |
|---|---:|
| Correct authorization | 24 |
| Over-deferral when continuation authorized | 15 |
| Over-hold when continuation authorized | 8 |
| Under-action escalation instead of definitive safety action | 7 |
| Over-emergency management | 4 |
| Over-switch or premature switch | 2 |

## Selected action distribution

| Selected action | Count |
|---|---:|
| escalate_evaluation | 36 |
| hold_therapy | 11 |
| emergency_toxicity_management | 6 |
| switch_therapy | 4 |
| continue_therapy | 3 |

## Expected versus selected action interpretation

Across the 60 visit-level decisions, GPT-4o-mini selected `continue_therapy` only 3 times.

Among 28 visits where the benchmark expected `continue_therapy`, GPT-4o-mini selected:

| Selected action when continuation was expected | Count |
|---|---:|
| continue_therapy | 3 |
| escalate_evaluation | 15 |
| hold_therapy | 8 |
| emergency_toxicity_management | 1 |
| switch_therapy | 1 |

Thus, GPT-4o-mini selected continuation in only 3 of 28 continuation-authorized visits, or 10.7%.

## Governance phenotype

GPT-4o-mini demonstrated a schema-perfect conservative over-deferral phenotype.

The model produced valid structured JSON outputs for all 60 prompts and avoided premature therapy continuation entirely. PTMAR and unsafe authorization were both 0.0%.

However, this safety profile came with substantial over-conservatism. The model frequently escalated evaluation, held therapy, or selected higher-intensity safety actions when the benchmark expected continuation.

## Clinical interpretation

The GPT-4o-mini result demonstrates that oncology AI safety cannot be evaluated only by the absence of unsafe continuation. A model may avoid premature therapy authorization while still creating clinically relevant risks through unnecessary deferral, treatment interruption, or escalation.

This finding supports the central OncoGuard-Response framing: therapeutic-response AI systems should be evaluated not only for unsafe action, but also for authorization calibration across sequential oncology visits.

## Main takeaway

GPT-4o-mini was highly schema-conformant and avoided unsafe therapeutic continuation, but showed a strong conservative bias. Its dominant failure mode was over-deferral when continuation was authorized.

This first v0.30 model result shows that OncoGuard-Response can phenotype model behavior as more than simply correct or incorrect. It can distinguish unsafe continuation risk from conservative treatment-delay risk.
