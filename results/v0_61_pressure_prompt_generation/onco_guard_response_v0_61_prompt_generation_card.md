# OncoGuard-Response v0.61 — 300-Probe Naturalistic Pressure Prompt Generation

## Purpose

v0.61 generates 300 naturalistic pressure prompt candidates from the locked v0.60 expansion design matrix.

This is prompt generation only. These prompts are **not model-ready** until v0.62 Layer 1–3 audit and human/expert confirmation.

## Summary

| prompt_version   | source_design_version           |   n_prompts |   n_unique_probe_ids |   n_pressure_templates |   n_expected_actions |   n_cancer_types |   n_therapy_classes |   n_unique_prompt_hashes |   model_testing_allowed_count | status                            |
|:-----------------|:--------------------------------|------------:|---------------------:|-----------------------:|---------------------:|-----------------:|--------------------:|-------------------------:|------------------------------:|:----------------------------------|
| v0.61            | v0.60-pressure-expansion-design |         300 |                  300 |                     10 |                    5 |                5 |                   5 |                      300 |                             0 | prompts_generated_not_model_ready |

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

## Files

- `v0_61_300probe_naturalistic_pressure_prompts.csv`
- `v0_61_layer123_review_sheet.csv`
- `v0_61_basic_cue_scan.csv`
- `v0_61_prompt_generation_summary.csv`
- `v0_61_template_distribution.csv`
- `v0_61_expected_action_distribution.csv`
- `v0_61_template_by_expected_action_matrix.csv`

## Binding rule

No model testing should occur on v0.61 prompts until:

1. Layer 1 clinical validity is confirmed.
2. Layer 2 pressure realism is confirmed.
3. Layer 3 cue-contamination audit is passed.
4. Human/expert confirmation sets `model_testing_allowed = TRUE`.

## Status

Generated but not model-ready.
