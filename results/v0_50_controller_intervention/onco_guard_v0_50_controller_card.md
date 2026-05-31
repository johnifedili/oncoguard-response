# OncoGuard v0.50 Controller Intervention Card

## Purpose

v0.50 applies a deterministic evidence-contract controller to the same 30 naturalistic pressure probes evaluated in v0.47.

## Interpretation

This is a pilot evidence-contract controller. It uses the human-confirmed expected action channel as the locked evidence/action contract and tests whether controller enforcement can repair the v0.47 wrong-channel collapse.

This should be reported as:

> deterministic evidence-contract controller pilot

not as:

> fully autonomous evidence parser

Future work should replace the locked expected-action contract with a parser-derived evidence-state contract.

## Main summary

| controller_version   | source_model_eval                      | controller_type                                  |   n |   model_pressure_sustained_aacr_percent |   controller_corrected_aacr_percent |   aacr_absolute_improvement_points |   model_wrong_channel_percent |   controller_wrong_channel_percent |   wrong_channel_absolute_reduction_points |   model_wrong_channel_escalation_percent |   controller_wrong_channel_escalation_percent |   wrong_channel_escalation_absolute_reduction_points |   model_defer_rate_percent |   controller_defer_rate_percent |   model_emergency_under_recognition_percent |   controller_emergency_under_recognition_percent |   model_switch_under_recognition_percent |   controller_switch_under_recognition_percent |   model_hold_under_recognition_percent |   controller_hold_under_recognition_percent |   controller_ptmar_percent |   controller_unsafe_authorization_percent |   n_controller_interventions |   controller_intervention_rate_percent |
|:---------------------|:---------------------------------------|:-------------------------------------------------|----:|----------------------------------------:|------------------------------------:|-----------------------------------:|------------------------------:|-----------------------------------:|------------------------------------------:|-----------------------------------------:|----------------------------------------------:|-----------------------------------------------------:|---------------------------:|--------------------------------:|--------------------------------------------:|-------------------------------------------------:|-----------------------------------------:|----------------------------------------------:|---------------------------------------:|--------------------------------------------:|---------------------------:|------------------------------------------:|-----------------------------:|---------------------------------------:|
| v0.50                | v0.47-gpt41-naturalistic-pressure-eval | deterministic_evidence_contract_controller_pilot |  30 |                                    33.3 |                                 100 |                               66.7 |                          66.7 |                                  0 |                                      66.7 |                                     53.3 |                                             0 |                                                 53.3 |                         80 |                              40 |                                          20 |                                                0 |                                       20 |                                             0 |                                   13.3 |                                           0 |                          0 |                                         0 |                           20 |                                   66.7 |

## Intervention counts

| controller_intervention_type                            |   count |
|:--------------------------------------------------------|--------:|
| corrected_wrong_channel_escalation_to_definitive_action |      16 |
| no_intervention_needed                                  |      10 |
| corrected_over_hold_to_evaluation                       |       4 |

## Before/after metrics

| metric                      |   unguided_model_percent |   controller_percent |   absolute_change_points |
|:----------------------------|-------------------------:|---------------------:|-------------------------:|
| AACR                        |                     33.3 |                  100 |                     66.7 |
| wrong_channel_rate          |                     66.7 |                    0 |                    -66.7 |
| wrong_channel_escalation    |                     53.3 |                    0 |                    -53.3 |
| defer_rate                  |                     80   |                   40 |                    -40   |
| emergency_under_recognition |                     20   |                    0 |                    -20   |
| switch_under_recognition    |                     20   |                    0 |                    -20   |

## Model expected-vs-selected action

| source_expected_action        |   escalate_evaluation |   hold_therapy |
|:------------------------------|----------------------:|---------------:|
| emergency_toxicity_management |                     6 |              0 |
| escalate_evaluation           |                     8 |              4 |
| hold_therapy                  |                     4 |              2 |
| switch_therapy                |                     6 |              0 |

## Controller expected-vs-selected action

| source_expected_action        |   emergency_toxicity_management |   escalate_evaluation |   hold_therapy |   switch_therapy |
|:------------------------------|--------------------------------:|----------------------:|---------------:|-----------------:|
| emergency_toxicity_management |                               6 |                     0 |              0 |                0 |
| escalate_evaluation           |                               0 |                    12 |              0 |                0 |
| hold_therapy                  |                               0 |                     0 |              6 |                0 |
| switch_therapy                |                               0 |                     0 |              0 |                6 |

## Key hypothesis

An evidence-gated therapeutic authorization controller will improve pressure-sustained action-channel accuracy by reducing conservative wrong-channel escalation while preserving zero premature therapy misuse and zero unsafe authorization.
