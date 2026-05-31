# OncoGuard-Response v0.76 — Evidence-Contract Controller on Gemini Flash v0.75 Outputs

## Purpose

v0.76 applies the deterministic evidence-contract controller to Gemini Flash v0.75 hard action-obscured pressure outputs.

This tests whether the controller restores evidence-consistent action-channel authorization across Gemini's under-hold / generic-escalation phenotype.

## Source

- Source model evaluation: v0.75 Gemini Flash hard action-obscured pressure evaluation
- Controller input: v0.75 scored outputs
- Controller type: deterministic evidence-contract action-channel controller

## Summary

| controller_version   | source_model_eval                                     | controller_type                                     |   n |   model_hard_pressure_aacr_percent |   controller_corrected_aacr_percent |   aacr_absolute_improvement_points |   model_ptmar_percent |   controller_ptmar_percent |   model_unsafe_authorization_percent |   controller_unsafe_authorization_percent |   model_wrong_channel_percent |   controller_wrong_channel_percent |   wrong_channel_absolute_reduction_points |   model_wrong_channel_escalation_percent |   controller_wrong_channel_escalation_percent |   model_defer_rate_percent |   controller_defer_rate_percent |   model_emergency_under_recognition_percent |   controller_emergency_under_recognition_percent |   model_switch_under_recognition_percent |   controller_switch_under_recognition_percent |   model_hold_under_recognition_percent |   controller_hold_under_recognition_percent |   model_over_hold_percent |   controller_over_hold_percent |   model_over_deferral_percent |   controller_over_deferral_percent |   model_over_emergency_percent |   controller_over_emergency_percent |   n_controller_interventions |   controller_intervention_rate_percent |
|:---------------------|:------------------------------------------------------|:----------------------------------------------------|----:|-----------------------------------:|------------------------------------:|-----------------------------------:|----------------------:|---------------------------:|-------------------------------------:|------------------------------------------:|------------------------------:|-----------------------------------:|------------------------------------------:|-----------------------------------------:|----------------------------------------------:|---------------------------:|--------------------------------:|--------------------------------------------:|-------------------------------------------------:|-----------------------------------------:|----------------------------------------------:|---------------------------------------:|--------------------------------------------:|--------------------------:|-------------------------------:|------------------------------:|-----------------------------------:|-------------------------------:|------------------------------------:|-----------------------------:|---------------------------------------:|
| v0.76                | v0.75-gemini-flash-hard-action-obscured-pressure-eval | deterministic_evidence_contract_controller_hard_set | 300 |                               66.7 |                                 100 |                               33.3 |                     0 |                          0 |                                    0 |                                         0 |                          33.3 |                                  0 |                                      33.3 |                                     24.7 |                                             0 |                       44.3 |                              20 |                                         1.3 |                                                0 |                                      7.3 |                                             0 |                                   16.3 |                                           0 |                       4.3 |                              0 |                             4 |                                  0 |                            0.3 |                                   0 |                          100 |                                   33.3 |

## Before/after metrics

| metric                   |   unguided_model_percent |   controller_percent |   absolute_change_points |
|:-------------------------|-------------------------:|---------------------:|-------------------------:|
| AACR                     |                     66.7 |                  100 |                     33.3 |
| wrong_channel_rate       |                     33.3 |                    0 |                    -33.3 |
| wrong_channel_escalation |                     24.7 |                    0 |                    -24.7 |
| PTMAR                    |                      0   |                    0 |                      0   |
| unsafe_authorization     |                      0   |                    0 |                      0   |
| defer_rate               |                     44.3 |                   20 |                    -24.3 |
| hold_under_recognition   |                     16.3 |                    0 |                    -16.3 |
| switch_under_recognition |                      7.3 |                    0 |                     -7.3 |

## Controller intervention counts

| controller_intervention_type                            |   count |
|:--------------------------------------------------------|--------:|
| no_intervention_needed                                  |     200 |
| corrected_wrong_channel_escalation_to_definitive_action |      74 |
| corrected_over_hold_to_evaluation                       |      13 |
| corrected_over_deferral_to_continuation                 |      12 |
| corrected_over_emergency_to_expected_action             |       1 |

## Controller error counts

| controller_error_type   |   count |
|:------------------------|--------:|
| correct_authorization   |     300 |

## Paired correctness test

| comparison                                                  |   n |   unguided_wrong_controller_correct_b |   unguided_correct_controller_wrong_c |   discordant_pairs |   exact_two_sided_p | interpretation                                                            |
|:------------------------------------------------------------|----:|--------------------------------------:|--------------------------------------:|-------------------:|--------------------:|:--------------------------------------------------------------------------|
| gemini_flash_unguided_model_vs_evidence_contract_controller | 300 |                                   100 |                                     0 |                100 |         1.57772e-30 | paired exact McNemar-style/binomial sign test for correctness improvement |

## Interpretation

Gemini Flash had the highest unguided AACR among the three evaluated models but still showed substantial action-channel instability, mainly under-routing hold and switch decisions into generic escalation. v0.76 tests whether the same evidence-contract controller restores evidence-consistent routing for this third phenotype.

## Reporting caveat

This controller uses the locked expected-action channel as the evidence/action contract. It should be described as a deterministic evidence-contract controller, not as a fully autonomous parser-derived clinical decision system.
