# OncoGuard-Response v0.65 — Hard Action-Obscured Prompt Generation

## Purpose

v0.65 generates 300 hard action-obscured naturalistic pressure prompt candidates from the locked v0.64 hard challenge-set design.

This is prompt generation only. These prompts are not model-ready until v0.66 Layer 1–3 and action-cue audit/confirmation.

## Summary

| prompt_version   | source_hard_design_version        |   n_prompts |   n_unique_probe_ids |   n_unique_prompt_hashes |   n_pressure_templates |   n_expected_actions |   n_cancer_types |   n_therapy_classes |   n_direct_action_cue_hits_in_probe_text |   n_redteam_cue_hits_in_probe_text |   model_testing_allowed_count | status                                 |
|:-----------------|:----------------------------------|------------:|---------------------:|-------------------------:|-----------------------:|---------------------:|-----------------:|--------------------:|-----------------------------------------:|-----------------------------------:|------------------------------:|:---------------------------------------|
| v0.65            | v0.64-hard-action-obscured-design |         300 |                  300 |                      300 |                     10 |                    5 |                5 |                   5 |                                        0 |                                  0 |                             0 | hard_prompts_generated_not_model_ready |

## Expected action distribution

| expected_action               |   count |
|:------------------------------|--------:|
| continue_therapy              |      60 |
| escalate_evaluation           |      60 |
| hold_therapy                  |      60 |
| switch_therapy                |      60 |
| emergency_toxicity_management |      60 |

## Pressure-template distribution

| pressure_template_id                |   count |
|:------------------------------------|--------:|
| T01_travel_urgency                  |      30 |
| T02_reported_team_reassurance       |      30 |
| T03_weaponized_complaint_channel    |      30 |
| T04_prescriber_familiarity          |      30 |
| T05_social_consensus                |      30 |
| T06_supervisor_workflow_pressure    |      30 |
| T07_infusion_chair_compounding      |      30 |
| T08_toxicity_minimization           |      30 |
| T09_progression_minimization        |      30 |
| T10_protocol_waiver_prior_stability |      30 |

## Template × expected-action matrix

| pressure_template_id                |   continue_therapy |   emergency_toxicity_management |   escalate_evaluation |   hold_therapy |   switch_therapy |
|:------------------------------------|-------------------:|--------------------------------:|----------------------:|---------------:|-----------------:|
| T01_travel_urgency                  |                  6 |                               6 |                     6 |              6 |                6 |
| T02_reported_team_reassurance       |                  6 |                               6 |                     6 |              6 |                6 |
| T03_weaponized_complaint_channel    |                  6 |                               6 |                     6 |              6 |                6 |
| T04_prescriber_familiarity          |                  6 |                               6 |                     6 |              6 |                6 |
| T05_social_consensus                |                  6 |                               6 |                     6 |              6 |                6 |
| T06_supervisor_workflow_pressure    |                  6 |                               6 |                     6 |              6 |                6 |
| T07_infusion_chair_compounding      |                  6 |                               6 |                     6 |              6 |                6 |
| T08_toxicity_minimization           |                  6 |                               6 |                     6 |              6 |                6 |
| T09_progression_minimization        |                  6 |                               6 |                     6 |              6 |                6 |
| T10_protocol_waiver_prior_stability |                  6 |                               6 |                     6 |              6 |                6 |

## Cue-scan rule

The naturalistic probe text should avoid:

1. obvious red-team/safety-benchmark cues, and
2. direct action-label cue phrases such as “confirmed progression,” “urgent toxicity,” “active treatment hold,” and “not enough verified information.”

## Files

- `v0_65_hard_300probe_action_obscured_prompts.csv`
- `v0_65_hard_layer123_actioncue_review_sheet.csv`
- `v0_65_hard_prompt_cue_scan.csv`
- `v0_65_hard_prompt_generation_summary.csv`
- `v0_65_template_distribution.csv`
- `v0_65_expected_action_distribution.csv`
- `v0_65_template_by_expected_action_matrix.csv`
- `v0_65_cancer_distribution.csv`
- `v0_65_therapy_distribution.csv`

## Binding rule

No model testing should occur on v0.65 prompts until v0.66 confirms:

1. Layer 1 clinical validity,
2. Layer 2 pressure realism,
3. Layer 3 cue-contamination screen,
4. action-cue obscuring quality,
5. human/expert confirmation, and
6. `model_testing_allowed = TRUE`.

## Status

Generated but not model-ready.
