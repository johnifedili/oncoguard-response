# OncoGuard-Response v0.73 — Evidence-Contract Controller on Claude v0.72 Outputs

## Purpose

v0.73 applies the deterministic evidence-contract controller to Claude Sonnet v0.72 hard action-obscured pressure outputs.

This tests whether the controller restores evidence-consistent action-channel authorization across Claude's distinct failure phenotype.

## Source

- Source model evaluation: v0.72 Claude Sonnet hard action-obscured pressure evaluation
- Controller input: v0.72 scored outputs
- Controller type: deterministic evidence-contract action-channel controller

## Summary

| controller_version   | source_model_eval                                      | controller_type                                     |   n |   model_hard_pressure_aacr_percent |   controller_corrected_aacr_percent |   aacr_absolute_improvement_points |   model_ptmar_percent |   controller_ptmar_percent |   model_unsafe_authorization_percent |   controller_unsafe_authorization_percent |   model_wrong_channel_percent |   controller_wrong_channel_percent |   wrong_channel_absolute_reduction_points |   model_wrong_channel_escalation_percent |   controller_wrong_channel_escalation_percent |   model_defer_rate_percent |   controller_defer_rate_percent |   model_emergency_under_recognition_percent |   controller_emergency_under_recognition_percent |   model_switch_under_recognition_percent |   controller_switch_under_recognition_percent |   model_hold_under_recognition_percent |   controller_hold_under_recognition_percent |   model_over_hold_percent |   controller_over_hold_percent |   model_over_deferral_percent |   controller_over_deferral_percent |   n_controller_interventions |   controller_intervention_rate_percent |
|:---------------------|:-------------------------------------------------------|:----------------------------------------------------|----:|-----------------------------------:|------------------------------------:|-----------------------------------:|----------------------:|---------------------------:|-------------------------------------:|------------------------------------------:|------------------------------:|-----------------------------------:|------------------------------------------:|-----------------------------------------:|----------------------------------------------:|---------------------------:|--------------------------------:|--------------------------------------------:|-------------------------------------------------:|-----------------------------------------:|----------------------------------------------:|---------------------------------------:|--------------------------------------------:|--------------------------:|-------------------------------:|------------------------------:|-----------------------------------:|-----------------------------:|---------------------------------------:|
| v0.73                | v0.72-claude-sonnet-hard-action-obscured-pressure-eval | deterministic_evidence_contract_controller_hard_set | 300 |                               54.7 |                                 100 |                               45.3 |                     0 |                          0 |                                    0 |                                         0 |                          45.3 |                                  0 |                                      45.3 |                                     16.7 |                                             0 |                       23.3 |                              20 |                                         4.7 |                                                0 |                                       17 |                                             0 |                                    0.3 |                                           0 |                      23.7 |                              0 |                             5 |                                  0 |                          136 |                                   45.3 |

## Before/after metrics

| metric                   |   unguided_model_percent |   controller_percent |   absolute_change_points |
|:-------------------------|-------------------------:|---------------------:|-------------------------:|
| AACR                     |                     54.7 |                  100 |                     45.3 |
| wrong_channel_rate       |                     45.3 |                    0 |                    -45.3 |
| wrong_channel_escalation |                     16.7 |                    0 |                    -16.7 |
| PTMAR                    |                      0   |                    0 |                      0   |
| unsafe_authorization     |                      0   |                    0 |                      0   |
| defer_rate               |                     23.3 |                   20 |                     -3.3 |
| over_hold                |                     23.7 |                    0 |                    -23.7 |
| switch_under_recognition |                     17   |                    0 |                    -17   |

## Controller intervention counts

| controller_intervention_type                            |   count |
|:--------------------------------------------------------|--------:|
| no_intervention_needed                                  |     164 |
| corrected_over_hold_to_evaluation                       |      55 |
| corrected_wrong_channel_escalation_to_definitive_action |      50 |
| corrected_wrong_channel_hold_to_definitive_action       |      16 |
| corrected_over_deferral_to_continuation                 |      15 |

## Controller error counts

| controller_error_type   |   count |
|:------------------------|--------:|
| correct_authorization   |     300 |

## Paired correctness test

| comparison                                            |   n |   unguided_wrong_controller_correct_b |   unguided_correct_controller_wrong_c |   discordant_pairs |   exact_two_sided_p | interpretation                                                            |
|:------------------------------------------------------|----:|--------------------------------------:|--------------------------------------:|-------------------:|--------------------:|:--------------------------------------------------------------------------|
| claude_unguided_model_vs_evidence_contract_controller | 300 |                                   136 |                                     0 |                136 |         2.29589e-41 | paired exact McNemar-style/binomial sign test for correctness improvement |

## Interpretation

Claude's unguided hard-set failure phenotype differed from GPT-4.1. Claude showed more over-hold/under-switch behavior, while GPT-4.1 showed more wrong-channel escalation. v0.73 tests whether the same evidence-contract controller restores evidence-consistent routing despite that different phenotype.

## Reporting caveat

This controller uses the locked expected-action channel as the evidence/action contract. It should be described as a deterministic evidence-contract controller, not as a fully autonomous parser-derived clinical decision system.
