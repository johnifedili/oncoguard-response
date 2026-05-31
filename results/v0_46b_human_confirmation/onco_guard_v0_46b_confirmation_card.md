# OncoGuard v0.46b Human/Expert Confirmation Package

## Purpose

v0.46b creates the human/expert review package for confirming whether v0.46 naturalistic pressure probes may proceed to model testing.

## Source

- v0.46: naturalistic pressure pilot
- v0.46a: automated Layer 1–3 audit

## Files

- `v0_46b_human_confirmation_sheet.csv`
- `v0_46b_reviewer_view.csv`
- `v0_46b_human_confirmation_instructions.md`
- `v0_46b_confirmation_summary.csv`
- `v0_46b_template_distribution.csv`
- `v0_46b_expected_action_distribution.csv`

## Summary

| confirmation_version   | source_audit_version   |   n_auto_screened_probes |   n_auto_eligible_for_human_confirmation |   n_confirmation_rows | human_review_completed   |   n_model_testing_allowed_human | status                                            |
|:-----------------------|:-----------------------|-------------------------:|-----------------------------------------:|----------------------:|:-------------------------|--------------------------------:|:--------------------------------------------------|
| v0.46b                 | v0.46a-layer123-audit  |                       30 |                                       30 |                    30 | False                    |                               0 | human_confirmation_sheet_created_not_yet_reviewed |

## Pressure-template distribution

| pressure_template_id             |   count |
|:---------------------------------|--------:|
| T01_travel_urgency               |       5 |
| T02_reported_team_reassurance    |       5 |
| T03_weaponized_complaint_channel |       5 |
| T04_prescriber_familiarity       |       5 |
| T05_social_consensus             |       5 |
| T06_supervisor_workflow_pressure |       5 |

## Expected-action distribution

| source_expected_action        |   count |
|:------------------------------|--------:|
| escalate_evaluation           |      12 |
| hold_therapy                  |       6 |
| switch_therapy                |       6 |
| emergency_toxicity_management |       6 |

## Binding rule

No probe may enter v0.47 model testing until human/expert review confirms:

1. Layer 1 clinical validity
2. Layer 2 pressure realism
3. Layer 3 low cue contamination

and sets:

`model_testing_allowed_human = TRUE`
