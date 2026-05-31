# OncoGuard-Response v0.62b — Expanded Human/Expert Confirmation Package

## Purpose

v0.62b creates the human/expert review package for confirming whether the 300 expanded naturalistic pressure prompts may proceed to model testing.

## Summary

| confirmation_version   | source_audit_version           |   n_auto_screened_prompts |   n_auto_eligible_for_human_confirmation |   n_confirmation_rows | human_review_completed   |   n_model_testing_allowed_human | status                                                     |
|:-----------------------|:-------------------------------|--------------------------:|-----------------------------------------:|----------------------:|:-------------------------|--------------------------------:|:-----------------------------------------------------------|
| v0.62b                 | v0.62a-layer123-expanded-audit |                       300 |                                      300 |                   300 | False                    |                               0 | expanded_human_confirmation_sheet_created_not_yet_reviewed |

## Template distribution

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

## Expected-action distribution

| expected_action               |   count |
|:------------------------------|--------:|
| continue_therapy              |      60 |
| escalate_evaluation           |      60 |
| hold_therapy                  |      60 |
| switch_therapy                |      60 |
| emergency_toxicity_management |      60 |

## Binding rule

No prompt may enter v0.63 model testing until `model_testing_allowed_human = TRUE`.
