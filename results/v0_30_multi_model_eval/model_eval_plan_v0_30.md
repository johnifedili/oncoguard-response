# OncoGuard-Response v0.30 Multi-Model Evaluation Plan

## Purpose

v0.30 evaluates actual model behavior on the frozen OncoGuard-Response v0.21 pilot benchmark.

The goal is to determine whether different LLMs authorize therapy continuation, defer or escalate evaluation, hold therapy, switch therapy, or trigger emergency toxicity management across the same multi-visit oncology response scenarios.

## Frozen benchmark reference

Benchmark tag:

`v0.21-pilot-benchmark`

Frozen input file:

`results/freeze_v0_21_pilot_benchmark/visit_level_policy_inputs_v0_21_adjusted.csv`

## Evaluation unit

The evaluation unit is one visit-level oncology therapeutic authorization decision.

The frozen pilot contains:

- 20 oncology trajectories
- 3 visits per trajectory
- 60 visit-level decisions

## Allowed action labels

Models must choose exactly one of the following labels:

- `continue_therapy`
- `hold_therapy`
- `switch_therapy`
- `escalate_evaluation`
- `emergency_toxicity_management`

## Primary metrics

- PTMAR: premature therapy misuse action rate
- AACR: authorization alignment contract rate
- unsafe authorization rate
- defer rate
- over-deferral rate
- schema conformance rate
- dominant failure mode

## Initial model set

Initial planned models:

1. OpenAI model
2. Claude Sonnet
3. Gemini
4. Optional open-weight model later

## Comparison framework

Each model will be compared against:

- expected authorization action
- v0.21 standard policy baseline
- v0.22 permissive policy baseline
- v0.22 conservative-margin policy baseline

## Interpretation

The goal is not to claim real-world oncology safety rates from this pilot. The goal is to test whether OncoGuard-Response can reveal distinct model governance phenotypes, including unsafe permissive continuation, appropriate deferral, conservative over-deferral, wrong-channel authorization, and schema or instruction-following failure.
