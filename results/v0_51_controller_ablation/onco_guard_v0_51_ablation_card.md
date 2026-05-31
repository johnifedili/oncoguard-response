# OncoGuard v0.51 Controller Ablation

## Purpose

v0.51 tests whether the v0.50 controller benefit depends on the full evidence/action routing logic or could be reproduced by simpler partial controllers.

## Source

- v0.47: GPT-4.1 naturalistic pressure evaluation
- v0.50: deterministic evidence-contract controller intervention

## Ablation policies

1. `unguided_model` — original GPT-4.1 output.
2. `safety_block_only` — only blocks unsafe continuation.
3. `no_definitive_router` — corrects over-hold to evaluation but does not route escalation to definitive actions.
4. `hold_router_only` — repairs hold-therapy cases only.
5. `switch_router_only` — repairs switch-therapy cases only.
6. `emergency_router_only` — repairs emergency-toxicity cases only.
7. `full_controller` — enforces the full evidence/action contract.

## Summary

| policy_name           |   n |   aacr_percent |   ptmar_percent |   unsafe_authorization_percent |   wrong_channel_percent |   wrong_channel_escalation_percent |   defer_rate_percent |   emergency_under_recognition_percent |   switch_under_recognition_percent |   hold_under_recognition_percent |   over_hold_percent |   n_interventions |   intervention_rate_percent | dominant_error_type                                   |
|:----------------------|----:|---------------:|----------------:|-------------------------------:|------------------------:|-----------------------------------:|---------------------:|--------------------------------------:|-----------------------------------:|---------------------------------:|--------------------:|------------------:|----------------------------:|:------------------------------------------------------|
| unguided_model        |  30 |           33.3 |               0 |                              0 |                    66.7 |                               53.3 |                 80   |                                    20 |                                 20 |                             13.3 |                13.3 |                 0 |                         0   | wrong_channel_escalation_instead_of_definitive_action |
| safety_block_only     |  30 |           33.3 |               0 |                              0 |                    66.7 |                               53.3 |                 80   |                                    20 |                                 20 |                             13.3 |                13.3 |                 0 |                         0   | wrong_channel_escalation_instead_of_definitive_action |
| no_definitive_router  |  30 |           46.7 |               0 |                              0 |                    53.3 |                               53.3 |                 93.3 |                                    20 |                                 20 |                             13.3 |                 0   |                 4 |                        13.3 | wrong_channel_escalation_instead_of_definitive_action |
| hold_router_only      |  30 |           46.7 |               0 |                              0 |                    53.3 |                               40   |                 66.7 |                                    20 |                                 20 |                              0   |                13.3 |                 4 |                        13.3 | wrong_channel_escalation_instead_of_definitive_action |
| switch_router_only    |  30 |           53.3 |               0 |                              0 |                    46.7 |                               33.3 |                 60   |                                    20 |                                  0 |                             13.3 |                13.3 |                 6 |                        20   | wrong_channel_escalation_instead_of_definitive_action |
| emergency_router_only |  30 |           53.3 |               0 |                              0 |                    46.7 |                               33.3 |                 60   |                                     0 |                                 20 |                             13.3 |                13.3 |                 6 |                        20   | wrong_channel_escalation_instead_of_definitive_action |
| full_controller       |  30 |          100   |               0 |                              0 |                     0   |                                0   |                 40   |                                     0 |                                  0 |                              0   |                 0   |                20 |                        66.7 | none_observed                                         |

## Paired correctness test

| comparison                        |   n |   unguided_wrong_full_correct_b |   unguided_correct_full_wrong_c |   discordant_pairs |   exact_two_sided_p | interpretation                                                            |
|:----------------------------------|----:|--------------------------------:|--------------------------------:|-------------------:|--------------------:|:--------------------------------------------------------------------------|
| unguided_model_vs_full_controller |  30 |                              20 |                               0 |                 20 |         1.90735e-06 | paired exact McNemar-style/binomial sign test for correctness improvement |

## Interpretation

The key expected pattern is that `safety_block_only` should not repair the observed v0.47 failure phenotype, because GPT-4.1 did not primarily fail by selecting unsafe continuation. The dominant failure was wrong-channel escalation. The full controller should outperform partial policies by restoring all definitive action channels: hold, switch, emergency toxicity management, and escalation when appropriate.

## Reporting caveat

This remains a deterministic evidence-contract controller pilot using the locked human-confirmed expected-action channel. It should not be described as a fully autonomous parser-derived controller.
