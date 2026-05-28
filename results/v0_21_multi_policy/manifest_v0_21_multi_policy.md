# OncoGuard-Response v0.21 Multi-Policy Evaluation Manifest

## Project

OncoGuard-Response

## Version

v0.21 multi-policy evaluation

## Baseline reference

Frozen baseline: `v0.20-pilot`

The v0.21 analysis builds on the frozen v0.20 pilot without modifying the original pilot outputs.

## Core methodological correction

The initial visit-level expansion copied trajectory-level evidence labels across all three visits in each trajectory. This produced artificial conflicts where later resolved continuation visits were still labeled as unresolved.

v0.21 corrected this by introducing:

`evidence_status_stage_adjusted`

This separates:

1. trajectory-level failure being tested, and  
2. visit-level authorization status at each decision point.

## Input files

- `../freeze_v0_20_pilot/trajectory_inventory_v0_20.csv`
- `../freeze_v0_20_pilot/failure_taxonomy_v0_20.csv`
- `../freeze_v0_20_pilot/results_v0_20.md`

## v0.21 generated data files

- `visit_level_policy_inputs_v0_21.csv`
- `visit_level_policy_inputs_v0_21_adjusted.csv`
- `policy_visit_scores_v0_21.csv`
- `policy_visit_scores_v0_21_adjusted.csv`
- `multi_policy_summary_v0_21.csv`
- `multi_policy_summary_v0_21_scored.csv`
- `multi_policy_summary_v0_21_adjusted_scored.csv`
- `action_evidence_conflict_audit_v0_21.csv`
- `action_evidence_conflict_summary_v0_21.csv`
- `policy_definitions_v0_21.csv`
- `v0_20_input_provenance_check.csv`

## v0.21 result narrative

- `results_v0_21_adjusted.md`
- `README_v0_21_multi_policy.md`

## v0.21 figures

- `figures/figure_1_v0_21_ptmar_by_policy.png`
- `figures/figure_2_v0_21_aacr_by_policy.png`
- `figures/figure_3_v0_21_defer_rate_by_policy.png`
- `figures/figure_4_v0_21_unsafe_authorization_by_policy.png`
- `figures/figure_5_v0_21_multi_policy_comparison.png`
- `figures/figure_index_v0_21.csv`
- `figures/figure_captions_v0_21.md`

## Final adjusted policy results

| Policy | PTMAR (%) | AACR (%) | Defer rate (%) | Unsafe authorization (%) | Correct authorization (%) |
|---|---:|---:|---:|---:|---:|
| Permissive | 26.7 | 73.3 | 0.0 | 26.7 | 73.3 |
| Standard | 0.0 | 100.0 | 26.7 | 0.0 | 100.0 |
| Conservative | 0.0 | 100.0 | 26.7 | 0.0 | 100.0 |

## Main interpretation

The permissive policy eliminated deferral but produced premature therapy misuse and unsafe authorization in 26.7% of visit-level evaluations. Standard and conservative policies eliminated observed PTMAR and unsafe authorization by respecting stage-adjusted authorization status.

## Manuscript takeaway

OncoGuard-Response can simulate therapeutic-response authorization policies over the same oncology visit trajectories, making continuation, deferral, and unsafe authorization tradeoffs measurable.
