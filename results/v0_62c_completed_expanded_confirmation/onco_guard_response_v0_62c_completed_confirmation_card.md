# OncoGuard-Response v0.62c — Completed Expanded Confirmation

## Purpose

v0.62c records completed author-domain confirmation for the 300-prompt expanded naturalistic pressure benchmark.

## Important caveat

This is author-domain expanded confirmation, not independent blinded multi-rater review.

For manuscript reporting, describe this as:

> author-domain expert expanded confirmation

not as:

> independent blinded expert adjudication

## Summary

| confirmation_version   | source_confirmation_package        | reviewer_id                | review_date   | confirmation_type                          | independent_blinded_review   | future_independent_review_recommended   |   n_reviewed_prompts |   n_layer1_human_pass |   n_layer2_human_pass |   n_layer3_human_pass |   n_model_testing_allowed_human | human_review_completed   | status                                        |
|:-----------------------|:-----------------------------------|:---------------------------|:--------------|:-------------------------------------------|:-----------------------------|:----------------------------------------|---------------------:|----------------------:|----------------------:|----------------------:|--------------------------------:|:-------------------------|:----------------------------------------------|
| v0.62c                 | v0.62b-expanded-human-confirmation | author_domain_reviewer_CJI | 2026-05-31    | author_domain_expert_expanded_confirmation | False                        | True                                    |                  300 |                   300 |                   300 |                   300 |                             300 | True                     | completed_author_domain_expanded_confirmation |

## Template confirmation summary

| pressure_template_id                |   n |   allowed |   mean_pressure_realism |   mean_cue_score |
|:------------------------------------|----:|----------:|------------------------:|-----------------:|
| T01_travel_urgency                  |  30 |        30 |                       3 |                0 |
| T02_reported_team_reassurance       |  30 |        30 |                       3 |                0 |
| T03_weaponized_complaint_channel    |  30 |        30 |                       4 |                0 |
| T04_prescriber_familiarity          |  30 |        30 |                       3 |                0 |
| T05_social_consensus                |  30 |        30 |                       3 |                0 |
| T06_supervisor_workflow_pressure    |  30 |        30 |                       3 |                0 |
| T07_infusion_chair_compounding      |  30 |        30 |                       3 |                0 |
| T08_toxicity_minimization           |  30 |        30 |                       3 |                0 |
| T09_progression_minimization        |  30 |        30 |                       3 |                0 |
| T10_protocol_waiver_prior_stability |  30 |        30 |                       3 |                0 |

## Expected-action confirmation summary

| expected_action               |   n |   allowed |   mean_pressure_realism |   mean_cue_score |
|:------------------------------|----:|----------:|------------------------:|-----------------:|
| continue_therapy              |  60 |        60 |                     3.1 |                0 |
| emergency_toxicity_management |  60 |        60 |                     3.1 |                0 |
| escalate_evaluation           |  60 |        60 |                     3.1 |                0 |
| hold_therapy                  |  60 |        60 |                     3.1 |                0 |
| switch_therapy                |  60 |        60 |                     3.1 |                0 |

## Model-testing rule

Only prompts in `v0_62c_model_testing_allowed_prompts.csv` may enter v0.63 expanded model evaluation.
