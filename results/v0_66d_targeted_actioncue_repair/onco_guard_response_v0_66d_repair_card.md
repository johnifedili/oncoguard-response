# OncoGuard-Response v0.66d — Targeted Action-Cue Repair

## Purpose

v0.66d repairs the 18 v0.66 prompts that failed the action-cue audit while preserving the original v0.64/v0.65 300-probe hard challenge-set design.

## Why this was needed

v0.66 showed:

- 300/300 passed Layer 1 clinical validity.
- 300/300 passed Layer 2 pressure realism.
- 300/300 passed Layer 3 red-team cue screening.
- 282/300 passed action-cue screening.
- 18/300 failed action-cue screening due to repeated soft expected-action cues.

v0.66d revises only those 18 rows.

## Summary

| repair_version   | source_prompt_version              | source_audit_version                       |   n_original_prompts |   n_failed_actioncue_before_repair |   n_targeted_repaired |   n_unique_prompt_hashes_after_repair |   n_actioncue_pass_after_repair |   n_redteam_pass_after_repair |   n_model_testing_allowed_after_repair |   model_testing_allowed_count | status                                              |
|:-----------------|:-----------------------------------|:-------------------------------------------|---------------------:|-----------------------------------:|----------------------:|--------------------------------------:|--------------------------------:|------------------------------:|---------------------------------------:|------------------------------:|:----------------------------------------------------|
| v0.66d           | v0.65-hard-action-obscured-prompts | v0.66-hard-layer123-actioncue-confirmation |                  300 |                                 18 |                    18 |                                   300 |                             300 |                           300 |                                    300 |                           300 | targeted_repair_complete_model_testing_file_created |

## Eligible expected-action distribution

| expected_action               |   count |
|:------------------------------|--------:|
| continue_therapy              |      60 |
| escalate_evaluation           |      60 |
| hold_therapy                  |      60 |
| switch_therapy                |      60 |
| emergency_toxicity_management |      60 |

## Eligible template distribution

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

## Eligible template × action matrix

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

## Binding rule

Only prompts in:

`v0_66d_model_testing_allowed_hard_prompts.csv`

should be used for v0.67 model testing.

## Caveat

This is targeted author-domain repair and re-audit, not independent blinded multi-rater review.
