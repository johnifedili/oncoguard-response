# OncoGuard-Response v0.66 — Hard Layer 1–3 + Action-Cue Audit and Confirmation

## Purpose

v0.66 validates the v0.65 hard action-obscured prompts before model testing.

It combines:

- v0.66a automated Layer 1–3 + action-cue audit,
- v0.66b human/expert confirmation package,
- v0.66c completed author-domain confirmation and model-testing-allowed file.

## v0.66a automated audit summary

| audit_version   | source_prompt_version              |   n_prompts |   n_unique_probe_ids |   n_layer1_auto_pass |   n_layer2_auto_pass |   n_layer3_redteam_pass |   n_actioncue_auto_pass |   n_layer123_actioncue_auto_pass |   n_model_testing_allowed_auto |   mean_hardness_score |   median_hardness_score |   n_low_hardness |   n_moderate_hardness |   n_high_hardness | audit_status                                    |
|:----------------|:-----------------------------------|------------:|---------------------:|---------------------:|---------------------:|------------------------:|------------------------:|---------------------------------:|-------------------------------:|----------------------:|------------------------:|-----------------:|----------------------:|------------------:|:------------------------------------------------|
| v0.66a          | v0.65-hard-action-obscured-prompts |         300 |                  300 |                  300 |                  300 |                     300 |                     282 |                              282 |                            282 |                  9.63 |                      10 |                0 |                     0 |               300 | automated_screen_complete_human_review_required |

## Hardness distribution

| hardness_label   |   count |
|:-----------------|--------:|
| high_hardness    |     300 |

## Template audit summary

| pressure_template_id                |   n |   auto_pass |   mean_pressure_realism |   mean_actioncue_score |   mean_hardness |   low_hardness |   moderate_hardness |   high_hardness |
|:------------------------------------|----:|------------:|------------------------:|-----------------------:|----------------:|---------------:|--------------------:|----------------:|
| T01_travel_urgency                  |  30 |          29 |                       3 |                   0.73 |            9.63 |              0 |                   0 |              30 |
| T02_reported_team_reassurance       |  30 |          28 |                       3 |                   0.83 |            9.63 |              0 |                   0 |              30 |
| T03_weaponized_complaint_channel    |  30 |          28 |                       4 |                   0.83 |            9.63 |              0 |                   0 |              30 |
| T04_prescriber_familiarity          |  30 |          28 |                       3 |                   0.83 |            9.63 |              0 |                   0 |              30 |
| T05_social_consensus                |  30 |          28 |                       3 |                   0.83 |            9.63 |              0 |                   0 |              30 |
| T06_supervisor_workflow_pressure    |  30 |          28 |                       3 |                   0.83 |            9.63 |              0 |                   0 |              30 |
| T07_infusion_chair_compounding      |  30 |          28 |                       3 |                   0.83 |            9.63 |              0 |                   0 |              30 |
| T08_toxicity_minimization           |  30 |          29 |                       3 |                   0.73 |            9.63 |              0 |                   0 |              30 |
| T09_progression_minimization        |  30 |          28 |                       3 |                   0.83 |            9.63 |              0 |                   0 |              30 |
| T10_protocol_waiver_prior_stability |  30 |          28 |                       3 |                   0.83 |            9.63 |              0 |                   0 |              30 |

## Expected-action audit summary

| expected_action               |   n |   auto_pass |   mean_pressure_realism |   mean_actioncue_score |   mean_hardness |   low_hardness |   moderate_hardness |   high_hardness |
|:------------------------------|----:|------------:|------------------------:|-----------------------:|----------------:|---------------:|--------------------:|----------------:|
| continue_therapy              |  60 |          52 |                     3.1 |                   0.8  |            9.53 |              0 |                   0 |              60 |
| emergency_toxicity_management |  60 |          60 |                     3.1 |                   0.8  |            9.5  |              0 |                   0 |              60 |
| escalate_evaluation           |  60 |          60 |                     3.1 |                   0.82 |            9.65 |              0 |                   0 |              60 |
| hold_therapy                  |  60 |          50 |                     3.1 |                   0.82 |            9.48 |              0 |                   0 |              60 |
| switch_therapy                |  60 |          60 |                     3.1 |                   0.83 |           10    |              0 |                   0 |              60 |

## v0.66b confirmation package summary

| confirmation_version   | source_audit_version                 |   n_auto_screened_prompts |   n_auto_eligible_for_human_confirmation |   n_confirmation_rows | human_review_completed   |   n_model_testing_allowed_human | status                                                 |
|:-----------------------|:-------------------------------------|--------------------------:|-----------------------------------------:|----------------------:|:-------------------------|--------------------------------:|:-------------------------------------------------------|
| v0.66b                 | v0.66a-hard-layer123-actioncue-audit |                       300 |                                      282 |                   282 | False                    |                               0 | hard_human_confirmation_sheet_created_not_yet_reviewed |

## v0.66c completed confirmation summary

| confirmation_version   | source_confirmation_package    | reviewer_id                | review_date   | confirmation_type                                | independent_blinded_review   | future_independent_review_recommended   |   n_reviewed_prompts |   n_layer1_human_pass |   n_layer2_human_pass |   n_layer3_human_pass |   n_actioncue_human_pass |   n_model_testing_allowed_human |   mean_hardness_score | human_review_completed   | status                                              |
|:-----------------------|:-------------------------------|:---------------------------|:--------------|:-------------------------------------------------|:-----------------------------|:----------------------------------------|---------------------:|----------------------:|----------------------:|----------------------:|-------------------------:|--------------------------------:|----------------------:|:-------------------------|:----------------------------------------------------|
| v0.66c                 | v0.66b-hard-human-confirmation | author_domain_reviewer_CJI | 2026-05-31    | author_domain_expert_hard_challenge_confirmation | False                        | True                                    |                  282 |                   282 |                   282 |                   282 |                      282 |                             282 |                  9.74 | True                     | completed_author_domain_hard_challenge_confirmation |

## Binding rule

Only prompts in:

`v0_66c_model_testing_allowed_hard_prompts.csv`

may enter v0.67 model testing.

## Caveat

This is author-domain hard challenge confirmation, not independent blinded multi-rater review.
