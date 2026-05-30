# OncoGuard-Response v0.41 Case Generation Card

## Purpose

v0.41 generates synthetic oncology trajectory JSON files from the locked v0.40 expanded benchmark design matrix.

## Source design

- Source: v0.40 design matrix
- Design: 100 trajectories × 3 visits
- Visit-level decisions: 300

## Generated artifacts

- JSON trajectory directory: `data/trajectories/v0_41_expanded_300visit/`
- Trajectory inventory: `results/v0_41_case_generation/v0_41_trajectory_inventory.csv`
- Visit-level inventory: `results/v0_41_case_generation/v0_41_visit_level_inventory.csv`

## Summary

| generation_version   | source_design_version   |   n_trajectories |   n_visits |   n_json_files |   n_cancer_types |   n_therapy_classes |   n_patterns |
|:---------------------|:------------------------|-----------------:|-----------:|---------------:|-----------------:|--------------------:|-------------:|
| v0.41                | v0.40                   |              100 |        300 |            100 |                5 |                   5 |            4 |

## Expected action distribution

| expected_action               |   count |   percent |
|:------------------------------|--------:|----------:|
| continue_therapy              |     175 |      58.3 |
| escalate_evaluation           |      63 |      21   |
| hold_therapy                  |      37 |      12.3 |
| switch_therapy                |      13 |       4.3 |
| emergency_toxicity_management |      12 |       4   |

## Evidence-status distribution

| evidence_status_stage_adjusted   |   count |   percent |
|:---------------------------------|--------:|----------:|
| authorized_or_resolved           |     175 |      58.3 |
| unresolved_needs_more_evidence   |      63 |      21   |
| active_toxicity_or_safety_hold   |      37 |      12.3 |
| progression_or_failure_confirmed |      13 |       4.3 |
| emergency_toxicity_confirmed     |      12 |       4   |

## Notes

These cases are synthetic and are intended for benchmark/controller evaluation, not clinical decision-making. The cases preserve the locked v0.40 design matrix and generate structured longitudinal oncology visits with labels for therapeutic authorization.
