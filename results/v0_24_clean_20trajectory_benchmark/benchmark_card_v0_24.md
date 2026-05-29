# OncoGuard-Response v0.24 Clean 20-Trajectory Benchmark Card

## Benchmark name

OncoGuard-Response v0.24 Clean 20-Trajectory Benchmark

## Purpose

OncoGuard-Response is a multi-visit oncology therapeutic-response authorization benchmark. It evaluates whether AI systems authorize therapy continuation, defer or escalate evaluation, hold therapy, switch therapy, or trigger emergency toxicity management across longitudinal oncology evidence states.

The benchmark is designed to evaluate therapeutic authorization behavior rather than single-turn oncology treatment recommendation accuracy.

## Version

`v0.24-clean-20trajectory-benchmark`

## Why v0.24 was created

An integrity audit found that the earlier active v0.21 benchmark artifacts contained only 13 trajectories and 39 visit-level decisions, corresponding to OGR_TRJ_011 through OGR_TRJ_023.

The missing trajectories OGR_TRJ_004 through OGR_TRJ_010 were recovered from the temporary runtime source directory and copied into the persistent Google Drive repository. v0.24 rebuilds the benchmark directly from the complete persistent JSON source files.

## Scope

This release is a clean pilot benchmark containing 20 synthetic oncology response trajectories and 60 visit-level therapeutic authorization decisions.

It is intended for:

- benchmark validation
- model-behavior phenotyping
- therapeutic authorization policy simulation
- multi-model evaluation
- failure taxonomy development

It is not intended to estimate real-world oncology model safety rates.

## Composition

The benchmark contains:

- 20 trajectories
- 3 visits per trajectory
- 60 visit-level therapeutic authorization decisions
- Trajectory IDs: OGR_TRJ_004 through OGR_TRJ_023

## Source files

Trajectory source JSON files are stored in:

`data/trajectories/v0_pilot/`

The clean v0.24 inventory is stored at:

`results/v0_24_clean_20trajectory_benchmark/trajectory_inventory_v0_24.csv`

The clean v0.24 visit-level authorization file is stored at:

`results/v0_24_clean_20trajectory_benchmark/visit_level_policy_inputs_v0_24_adjusted.csv`

## Allowed authorization actions

The benchmark uses five therapeutic authorization labels:

- `continue_therapy`
- `escalate_evaluation`
- `hold_therapy`
- `switch_therapy`
- `emergency_toxicity_management`

## Expected action distribution

| Expected action | Count |
|---|---:|
| continue_therapy | 28 |
| escalate_evaluation | 15 |
| hold_therapy | 9 |
| switch_therapy | 6 |
| emergency_toxicity_management | 2 |

## Stage-adjusted authorization status distribution

| Stage-adjusted evidence status | Count |
|---|---:|
| authorized_or_resolved | 28 |
| unresolved_needs_more_evidence | 15 |
| active_toxicity_or_safety_hold | 9 |
| progression_or_failure_confirmed | 6 |
| emergency_toxicity_confirmed | 2 |

## Benchmark design

Each trajectory represents a longitudinal oncology response-management scenario across three visits. The benchmark evaluates whether an AI system selects an authorization action that is appropriate for the current visit-level evidence state.

The benchmark includes scenarios involving:

- authorized continuation after sufficient evidence
- missing critical evidence requiring escalation
- incomplete or unresolved safety assessment
- active toxicity requiring therapy hold
- confirmed progression requiring switch
- emergency toxicity requiring urgent management
- discordance between tumor response and patient safety state
- narrative pressure or anchoring that should not override evidence

## Labeling pipeline

The benchmark was authored as a synthetic oncology therapeutic-response authorization dataset.

Each trajectory includes:

- trajectory ID
- title
- action path
- failure being tested
- authorization dependency
- source JSON reference

Each visit-level record includes:

- trajectory ID
- visit number
- expected action
- inferred evidence state
- stage-adjusted evidence status
- failure being tested
- authorization dependency
- source JSON reference

## Metrics supported

Primary metrics include:

- PTMAR: premature therapy misuse action rate
- AACR: authorization alignment contract rate
- unsafe authorization rate
- defer rate
- over-deferral rate
- over-hold rate
- over-emergency-management rate
- over-switch rate
- schema conformance rate
- dominant error phenotype

## Known limitations

This is a pilot benchmark with important limitations:

- synthetic trajectories
- modest sample size
- no external oncology expert adjudication yet
- limited treatment class diversity
- visit-level decisions are correlated within trajectories
- compact authorization labels are derived from authored synthetic cases
- not intended to represent all oncology response-management situations
- not intended to estimate real-world oncology AI safety rates

## Intended use

This benchmark should be used to evaluate whether AI systems respect therapeutic authorization thresholds across sequential oncology visits.

It can identify model governance phenotypes such as:

- unsafe permissive continuation
- appropriate authorization
- conservative over-deferral
- over-holding
- wrong-channel escalation
- premature switching
- excessive emergency escalation
- schema failure

## Future directions

Future benchmark expansions should include:

- 50–100+ trajectories
- richer semi-structured oncology visit records
- cancer type and treatment class stratification
- biomarker, imaging, toxicity, and organ-function fields
- external oncology expert review
- multi-model evaluation
- confidence intervals and subgroup analyses
- real-world or semi-synthetic EHR-style trajectories

## Recommended citation language

OncoGuard-Response v0.24 is a clean 20-trajectory, 60-visit pilot benchmark for evaluating oncology therapeutic-response authorization across longitudinal evidence states.
