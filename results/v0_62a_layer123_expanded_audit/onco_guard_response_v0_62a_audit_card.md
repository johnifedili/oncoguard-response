# OncoGuard-Response v0.62a — Automated Layer 1–3 Audit

## Purpose

v0.62a performs an automated Layer 1–3 screen of the 300 naturalistic pressure prompts generated in v0.61.

This is not model testing. It is a pre-testing eligibility audit.

## Layer definitions

1. Layer 1 — Clinical validity
2. Layer 2 — Naturalistic pressure realism
3. Layer 3 — Cue-contamination audit

## Summary

| audit_version   | source_prompt_version            |   n_prompts |   n_unique_probe_ids |   n_layer1_auto_pass |   n_layer2_auto_pass |   n_layer3_auto_pass |   n_layer123_auto_pass |   n_model_testing_allowed_auto | audit_status                                    |
|:----------------|:---------------------------------|------------:|---------------------:|---------------------:|---------------------:|---------------------:|-----------------------:|-------------------------------:|:------------------------------------------------|
| v0.62a          | v0.61-pressure-prompt-generation |         300 |                  300 |                  300 |                  300 |                  300 |                    300 |                            300 | automated_screen_complete_human_review_required |

## Template summary

| pressure_template_id                |   n |   layer1_pass |   layer2_pass |   layer3_pass |   layer123_pass |   mean_pressure_realism |   mean_cue_score |
|:------------------------------------|----:|--------------:|--------------:|--------------:|----------------:|------------------------:|-----------------:|
| T01_travel_urgency                  |  30 |            30 |            30 |            30 |              30 |                       3 |                0 |
| T02_reported_team_reassurance       |  30 |            30 |            30 |            30 |              30 |                       3 |                0 |
| T03_weaponized_complaint_channel    |  30 |            30 |            30 |            30 |              30 |                       4 |                0 |
| T04_prescriber_familiarity          |  30 |            30 |            30 |            30 |              30 |                       3 |                0 |
| T05_social_consensus                |  30 |            30 |            30 |            30 |              30 |                       3 |                0 |
| T06_supervisor_workflow_pressure    |  30 |            30 |            30 |            30 |              30 |                       3 |                0 |
| T07_infusion_chair_compounding      |  30 |            30 |            30 |            30 |              30 |                       3 |                0 |
| T08_toxicity_minimization           |  30 |            30 |            30 |            30 |              30 |                       3 |                0 |
| T09_progression_minimization        |  30 |            30 |            30 |            30 |              30 |                       3 |                0 |
| T10_protocol_waiver_prior_stability |  30 |            30 |            30 |            30 |              30 |                       3 |                0 |

## Expected-action summary

| expected_action               |   n |   layer123_pass |   mean_pressure_realism |   mean_cue_score |
|:------------------------------|----:|----------------:|------------------------:|-----------------:|
| continue_therapy              |  60 |              60 |                     3.1 |                0 |
| emergency_toxicity_management |  60 |              60 |                     3.1 |                0 |
| escalate_evaluation           |  60 |              60 |                     3.1 |                0 |
| hold_therapy                  |  60 |              60 |                     3.1 |                0 |
| switch_therapy                |  60 |              60 |                     3.1 |                0 |

## Binding rule

No prompt may enter expanded model evaluation until human/expert confirmation is completed and `model_testing_allowed_human = TRUE`.
