# OncoGuard v0.46c Completed Human Confirmation Card

## Purpose

v0.46c records completed author-domain confirmation for the v0.46 naturalistic pressure pilot after the v0.46a automated Layer 1–3 audit and v0.46b human-confirmation package.

## Important interpretation

This is a pilot author-domain confirmation, not independent blinded multi-rater review.

For manuscript reporting, this should be described as:

> author-domain expert pilot confirmation

not as:

> independent expert adjudication

Future scaled benchmark versions should use independent multi-rater review.

## Source

- v0.46: naturalistic pressure pilot
- v0.46a: automated Layer 1–3 audit
- v0.46b: human/expert confirmation package
- v0.46c: completed author-domain confirmation

## Summary

| confirmation_version   | source_confirmation_package     | reviewer_id                | review_date   | confirmation_type                       | independent_blinded_review   | future_independent_review_recommended   |   n_reviewed_probes |   n_layer1_human_pass |   n_layer2_human_pass |   n_layer3_human_pass |   n_model_testing_allowed_human | human_review_completed   | status                                     |
|:-----------------------|:--------------------------------|:---------------------------|:--------------|:----------------------------------------|:-----------------------------|:----------------------------------------|--------------------:|----------------------:|----------------------:|----------------------:|--------------------------------:|:-------------------------|:-------------------------------------------|
| v0.46c                 | v0.46b-human-confirmation-sheet | author_domain_reviewer_CJI | 2026-05-31    | author_domain_expert_pilot_confirmation | False                        | True                                    |                  30 |                    30 |                    30 |                    30 |                              30 | True                     | completed_author_domain_pilot_confirmation |

## Template-level confirmation

| pressure_template_id             |   n |   allowed |   mean_pressure_realism |   mean_cue_score |
|:---------------------------------|----:|----------:|------------------------:|-----------------:|
| T01_travel_urgency               |   5 |         5 |                       3 |                0 |
| T02_reported_team_reassurance    |   5 |         5 |                       3 |                0 |
| T03_weaponized_complaint_channel |   5 |         5 |                       4 |                0 |
| T04_prescriber_familiarity       |   5 |         5 |                       3 |                0 |
| T05_social_consensus             |   5 |         5 |                       3 |                0 |
| T06_supervisor_workflow_pressure |   5 |         5 |                       3 |                0 |

## Expected-action confirmation

| source_expected_action        |   n |   allowed |   mean_pressure_realism |   mean_cue_score |
|:------------------------------|----:|----------:|------------------------:|-----------------:|
| emergency_toxicity_management |   6 |         6 |                 3.16667 |                0 |
| escalate_evaluation           |  12 |        12 |                 3.16667 |                0 |
| hold_therapy                  |   6 |         6 |                 3.16667 |                0 |
| switch_therapy                |   6 |         6 |                 3.16667 |                0 |

## Files

- `v0_46c_completed_human_confirmation_sheet.csv`
- `v0_46c_model_testing_allowed_probes.csv`
- `v0_46c_completed_confirmation_summary.csv`
- `v0_46c_template_confirmation_summary.csv`
- `v0_46c_action_confirmation_summary.csv`

## Model-testing rule

Only probes with:

`model_testing_allowed_human = TRUE`

may enter v0.47 model testing.
