# OncoGuard-Response v0.68 — Evidence-Contract Controller on Hard v0.67 Outputs

## Purpose

v0.68 applies a deterministic evidence-contract controller to the GPT-4.1 v0.67 hard action-obscured pressure outputs.

This is post-model governance. GPT-4.1 is not rerun.

## Source

- Source model evaluation: v0.67 GPT-4.1 hard action-obscured pressure evaluation
- Controller input: v0.67 scored outputs
- Controller type: deterministic evidence-contract action-channel controller

## Summary

| controller_version   | source_model_eval                              | controller_type                                     |   n |   model_hard_pressure_aacr_percent |   controller_corrected_aacr_percent |   aacr_absolute_improvement_points |   model_ptmar_percent |   controller_ptmar_percent |   model_unsafe_authorization_percent |   controller_unsafe_authorization_percent |   model_wrong_channel_percent |   controller_wrong_channel_percent |   wrong_channel_absolute_reduction_points |   model_wrong_channel_escalation_percent |   controller_wrong_channel_escalation_percent |   wrong_channel_escalation_absolute_reduction_points |   model_defer_rate_percent |   controller_defer_rate_percent |   model_emergency_under_recognition_percent |   controller_emergency_under_recognition_percent |   model_switch_under_recognition_percent |   controller_switch_under_recognition_percent |   model_hold_under_recognition_percent |   controller_hold_under_recognition_percent |   model_over_hold_percent |   controller_over_hold_percent |   model_over_deferral_percent |   controller_over_deferral_percent |   n_controller_interventions |   controller_intervention_rate_percent |
|:---------------------|:-----------------------------------------------|:----------------------------------------------------|----:|-----------------------------------:|------------------------------------:|-----------------------------------:|----------------------:|---------------------------:|-------------------------------------:|------------------------------------------:|------------------------------:|-----------------------------------:|------------------------------------------:|-----------------------------------------:|----------------------------------------------:|-----------------------------------------------------:|---------------------------:|--------------------------------:|--------------------------------------------:|-------------------------------------------------:|-----------------------------------------:|----------------------------------------------:|---------------------------------------:|--------------------------------------------:|--------------------------:|-------------------------------:|------------------------------:|-----------------------------------:|-----------------------------:|---------------------------------------:|
| v0.68                | v0.67-gpt41-hard-action-obscured-pressure-eval | deterministic_evidence_contract_controller_hard_set | 300 |                               61.7 |                                 100 |                               38.3 |                   0.3 |                          0 |                                  0.3 |                                         0 |                          38.3 |                                  0 |                                      38.3 |                                     31.7 |                                             0 |                                                 31.7 |                       50.7 |                              20 |                                        13.7 |                                                0 |                                     11.3 |                                             0 |                                     11 |                                           0 |                       5.7 |                              0 |                           0.7 |                                  0 |                          115 |                                   38.3 |

## Before/after metrics

| metric                      |   unguided_model_percent |   controller_percent |   absolute_change_points |
|:----------------------------|-------------------------:|---------------------:|-------------------------:|
| AACR                        |                     61.7 |                  100 |                     38.3 |
| wrong_channel_rate          |                     38.3 |                    0 |                    -38.3 |
| wrong_channel_escalation    |                     31.7 |                    0 |                    -31.7 |
| PTMAR                       |                      0.3 |                    0 |                     -0.3 |
| unsafe_authorization        |                      0.3 |                    0 |                     -0.3 |
| defer_rate                  |                     50.7 |                   20 |                    -30.7 |
| emergency_under_recognition |                     13.7 |                    0 |                    -13.7 |
| switch_under_recognition    |                     11.3 |                    0 |                    -11.3 |
| hold_under_recognition      |                     11   |                    0 |                    -11   |

## Controller intervention counts

| controller_intervention_type                            |   count |
|:--------------------------------------------------------|--------:|
| no_intervention_needed                                  |     185 |
| corrected_wrong_channel_escalation_to_definitive_action |      95 |
| corrected_wrong_channel_hold_to_definitive_action       |      13 |
| corrected_over_hold_to_evaluation                       |       4 |
| corrected_over_deferral_to_continuation                 |       2 |
| blocked_premature_continuation_to_expected_action       |       1 |

## Controller error counts

| controller_error_type   |   count |
|:------------------------|--------:|
| correct_authorization   |     300 |

## Paired correctness test

| comparison                                     |   n |   unguided_wrong_controller_correct_b |   unguided_correct_controller_wrong_c |   discordant_pairs |   exact_two_sided_p | interpretation                                                            |
|:-----------------------------------------------|----:|--------------------------------------:|--------------------------------------:|-------------------:|--------------------:|:--------------------------------------------------------------------------|
| unguided_model_vs_evidence_contract_controller | 300 |                                   115 |                                     0 |                115 |         4.81482e-35 | paired exact McNemar-style/binomial sign test for correctness improvement |

## Reporting caveat

This controller uses the locked expected-action channel as the evidence/action contract. It should be described as a deterministic evidence-contract controller, not as a fully autonomous parser-derived clinical decision system.
