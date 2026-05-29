# OncoGuard-Response v0.24 Clean 20-Trajectory Benchmark Manifest

## Project

OncoGuard-Response

## Version

v0.24 clean 20-trajectory benchmark

## Purpose

This manifest documents the corrected clean 20-trajectory benchmark rebuild used as the source of truth for final model evaluation.

## Reason for rebuild

A benchmark integrity audit found that the earlier active v0.21 files contained only 13 trajectories and 39 visit-level decisions:

- OGR_TRJ_011 through OGR_TRJ_023
- 13 trajectories
- 39 visits

The missing trajectories were found in the temporary runtime source directory:

- OGR_TRJ_004 through OGR_TRJ_010

These missing JSON files were copied into the persistent Google Drive repository. v0.24 rebuilds the benchmark from the complete persistent JSON source set.

## Source trajectory directory

`data/trajectories/v0_pilot/`

## Included trajectory IDs

- OGR_TRJ_004
- OGR_TRJ_005
- OGR_TRJ_006
- OGR_TRJ_007
- OGR_TRJ_008
- OGR_TRJ_009
- OGR_TRJ_010
- OGR_TRJ_011
- OGR_TRJ_012
- OGR_TRJ_013
- OGR_TRJ_014
- OGR_TRJ_015
- OGR_TRJ_016
- OGR_TRJ_017
- OGR_TRJ_018
- OGR_TRJ_019
- OGR_TRJ_020
- OGR_TRJ_021
- OGR_TRJ_022
- OGR_TRJ_023

## Benchmark size

| Item | Count |
|---|---:|
| Trajectories | 20 |
| Visits per trajectory | 3 |
| Visit-level decisions | 60 |

## Generated files

| File | Description |
|---|---|
| `trajectory_inventory_v0_24.csv` | Clean 20-trajectory inventory built from JSON source files |
| `visit_level_policy_inputs_v0_24_adjusted.csv` | Clean 60-row visit-level authorization input file |
| `benchmark_card_v0_24.md` | Benchmark documentation card |
| `manifest_v0_24_clean_20trajectory_benchmark.md` | This manifest |

## Build scripts

| Script | Purpose |
|---|---|
| `eval/build_trajectory_inventory_from_json_v0_24.py` | Builds trajectory inventory directly from persistent JSON files |
| `eval/build_visit_level_policy_inputs_v0_24.py` | Expands inventory into visit-level authorization rows and stage-adjusted status labels |

## Expected action counts

| Expected action | Count |
|---|---:|
| continue_therapy | 28 |
| escalate_evaluation | 15 |
| hold_therapy | 9 |
| switch_therapy | 6 |
| emergency_toxicity_management | 2 |

## Stage-adjusted status counts

| Evidence status | Count |
|---|---:|
| authorized_or_resolved | 28 |
| unresolved_needs_more_evidence | 15 |
| active_toxicity_or_safety_hold | 9 |
| progression_or_failure_confirmed | 6 |
| emergency_toxicity_confirmed | 2 |

## Important provenance note

The previous 39-row GPT-4o-mini run should be treated as exploratory only because it used an incomplete active benchmark artifact.

Final model evaluation should use:

`results/v0_24_clean_20trajectory_benchmark/visit_level_policy_inputs_v0_24_adjusted.csv`

## Recommended final evaluation flow

1. Freeze v0.24 benchmark artifacts.
2. Tag Git state as `v0.24-clean-20trajectory-benchmark`.
3. Regenerate model prompts from the v0.24 clean 60-row file.
4. Run checkpointed model evaluation.
5. Score outputs.
6. Generate model figures.
7. Produce model-specific result markdown.
8. Repeat for additional models.

## Main interpretation

v0.24 restores the intended 20-trajectory / 60-visit pilot benchmark and provides a clean, reproducible foundation for model-behavior phenotyping in oncology therapeutic-response authorization.
