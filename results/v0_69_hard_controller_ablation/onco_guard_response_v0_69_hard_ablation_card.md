# OncoGuard-Response v0.69 — Hard-Set Controller Ablation

## Purpose

v0.69 tests whether the v0.68 controller benefit on the hard action-obscured benchmark requires full evidence/action routing.

The ablation compares:

1. unguided_model
2. safety_block_only
3. no_definitive_router
4. hold_router_only
5. switch_router_only
6. emergency_router_only
7. full_controller

## Summary

| policy_name           |   n |   aacr_percent |   ptmar_percent |   unsafe_authorization_percent |   wrong_channel_percent |   wrong_channel_escalation_percent |   defer_rate_percent |   emergency_under_recognition_percent |   switch_under_recognition_percent |   hold_under_recognition_percent |   over_hold_percent |   over_deferral_percent |   n_interventions |   intervention_rate_percent | dominant_error_type                                   |
|:----------------------|----:|---------------:|----------------:|-------------------------------:|------------------------:|-----------------------------------:|---------------------:|--------------------------------------:|-----------------------------------:|---------------------------------:|--------------------:|------------------------:|------------------:|----------------------------:|:------------------------------------------------------|
| unguided_model        | 300 |           61.7 |             0.3 |                            0.3 |                    38.3 |                               31.7 |                 50.7 |                                  13.7 |                               11.3 |                               11 |                 5.7 |                     0.7 |                 0 |                         0   | wrong_channel_escalation_instead_of_definitive_action |
| safety_block_only     | 300 |           62   |             0   |                            0   |                    38   |                               31.7 |                 51   |                                  13.7 |                               11.3 |                               11 |                 5.7 |                     0.7 |                 1 |                         0.3 | wrong_channel_escalation_instead_of_definitive_action |
| no_definitive_router  | 300 |           64   |             0   |                            0   |                    36   |                               31.7 |                 51.7 |                                  13.7 |                               11.3 |                               11 |                 4.3 |                     0   |                 7 |                         2.3 | wrong_channel_escalation_instead_of_definitive_action |
| hold_router_only      | 300 |           73   |             0   |                            0   |                    27   |                               20.7 |                 40   |                                  13.7 |                               11.3 |                                0 |                 5.7 |                     0.7 |                34 |                        11.3 | wrong_channel_escalation_instead_of_definitive_action |
| switch_router_only    | 300 |           73.3 |             0   |                            0   |                    26.7 |                               20.3 |                 39.7 |                                  13.7 |                                0   |                               11 |                 5.7 |                     0.7 |                35 |                        11.7 | wrong_channel_escalation_instead_of_definitive_action |
| emergency_router_only | 300 |           75.7 |             0   |                            0   |                    24.3 |                               22.3 |                 41.7 |                                   0   |                               11.3 |                               11 |                 1.3 |                     0.7 |                42 |                        14   | wrong_channel_escalation_instead_of_definitive_action |
| full_controller       | 300 |          100   |             0   |                            0   |                     0   |                                0   |                 20   |                                   0   |                                0   |                                0 |                 0   |                     0   |               115 |                        38.3 | none_observed                                         |

## Deltas vs unguided

| policy_name           |   aacr_delta_vs_unguided_points |   wrong_channel_delta_vs_unguided_points |   wrong_channel_escalation_delta_vs_unguided_points |   ptmar_delta_vs_unguided_points |   unsafe_authorization_delta_vs_unguided_points |
|:----------------------|--------------------------------:|-----------------------------------------:|----------------------------------------------------:|---------------------------------:|------------------------------------------------:|
| safety_block_only     |                             0.3 |                                     -0.3 |                                                 0   |                             -0.3 |                                            -0.3 |
| no_definitive_router  |                             2.3 |                                     -2.3 |                                                 0   |                             -0.3 |                                            -0.3 |
| hold_router_only      |                            11.3 |                                    -11.3 |                                               -11   |                             -0.3 |                                            -0.3 |
| switch_router_only    |                            11.6 |                                    -11.6 |                                               -11.4 |                             -0.3 |                                            -0.3 |
| emergency_router_only |                            14   |                                    -14   |                                                -9.4 |                             -0.3 |                                            -0.3 |
| full_controller       |                            38.3 |                                    -38.3 |                                               -31.7 |                             -0.3 |                                            -0.3 |

## Paired correctness test

| comparison                        |   n |   unguided_wrong_full_correct_b |   unguided_correct_full_wrong_c |   discordant_pairs |   exact_two_sided_p | interpretation                                                            |
|:----------------------------------|----:|--------------------------------:|--------------------------------:|-------------------:|--------------------:|:--------------------------------------------------------------------------|
| unguided_model_vs_full_controller | 300 |                             115 |                               0 |                115 |         4.81482e-35 | paired exact McNemar-style/binomial sign test for correctness improvement |

## Interpretation

If safety_block_only fails to substantially improve AACR, this supports the claim that the dominant failure was not unsafe continuation. If partial routers improve only their covered channels, while the full controller restores all action channels, this supports the mechanism-specific value of full evidence/action routing.

## Reporting caveat

The full controller uses the locked expected-action channel as the deterministic evidence/action contract. This remains a controller-mechanism study, not a fully autonomous parser-derived clinical decision system.
