# OncoGuard-Response v0.74 — Two-Model Hard-Set Synthesis

## Summary

v0.74 compares GPT-4.1 and Claude Sonnet 4.6 on the repaired hard action-obscured 300-prompt benchmark and synthesizes controller effects across both models.

## Two-model unguided comparison

| model             | source_version   |   n |   schema_conformance_percent |   hard_pressure_aacr_percent |   wrong_channel_percent |   wrong_channel_escalation_percent |   ptmar_percent |   unsafe_authorization_percent |   defer_rate_percent |   over_hold_percent |   over_deferral_percent | dominant_error_type                                   |
|:------------------|:-----------------|----:|-----------------------------:|-----------------------------:|------------------------:|-----------------------------------:|----------------:|-------------------------------:|---------------------:|--------------------:|------------------------:|:------------------------------------------------------|
| GPT-4.1           | v0.67            | 300 |                          100 |                         61.7 |                    38.3 |                               31.7 |             0.3 |                            0.3 |                 50.7 |                 5.7 |                     0.7 | wrong_channel_escalation_instead_of_definitive_action |
| Claude Sonnet 4.6 | v0.72            | 300 |                          100 |                         54.7 |                    45.3 |                               16.7 |             0   |                            0   |                 23.3 |                23.7 |                     5   | over_hold_instead_of_evaluation                       |

## Two-model controller comparison

| model             | unguided_source   | controller_source   |   n |   unguided_aacr_percent |   controller_aacr_percent |   aacr_improvement_points |   unguided_wrong_channel_percent |   controller_wrong_channel_percent |   unguided_ptmar_percent |   controller_ptmar_percent |   unguided_unsafe_authorization_percent |   controller_unsafe_authorization_percent |   n_controller_interventions |   controller_intervention_rate_percent |
|:------------------|:------------------|:--------------------|----:|------------------------:|--------------------------:|--------------------------:|---------------------------------:|-----------------------------------:|-------------------------:|---------------------------:|----------------------------------------:|------------------------------------------:|-----------------------------:|---------------------------------------:|
| GPT-4.1           | v0.67             | v0.68               | 300 |                    61.7 |                       100 |                      38.3 |                             38.3 |                                  0 |                      0.3 |                          0 |                                     0.3 |                                         0 |                          115 |                                   38.3 |
| Claude Sonnet 4.6 | v0.72             | v0.73               | 300 |                    54.7 |                       100 |                      45.3 |                             45.3 |                                  0 |                      0   |                          0 |                                     0   |                                         0 |                          136 |                                   45.3 |

## Key interpretation

Both models showed substantial action-channel instability on the hard set. GPT-4.1 primarily failed through generic escalation, while Claude primarily failed through over-hold and under-switch behavior. The same evidence-contract controller corrected both phenotypes.

## Figures

| figure    | filename                                                 | title                                | purpose                                                                              |
|:----------|:---------------------------------------------------------|:-------------------------------------|:-------------------------------------------------------------------------------------|
| Figure 1  | figure1_two_model_unguided_aacr_v0_74.png                | Unguided AACR by model               | Shows both GPT-4.1 and Claude fail the hard action-obscured benchmark.               |
| Figure 2  | figure2_two_model_wrong_channel_rate_v0_74.png           | Unguided wrong-channel rate by model | Shows wrong-channel instability in both models.                                      |
| Figure 3  | figure3_two_model_controller_before_after_aacr_v0_74.png | Controller before/after AACR         | Shows evidence-contract controller restores AACR across both models.                 |
| Figure 4  | figure4_two_model_error_phenotypes_v0_74.png             | Model-specific failure phenotypes    | Contrasts GPT-4.1 escalation phenotype with Claude over-hold/under-switch phenotype. |
| Figure 5a | figure5_gpt41_expected_vs_selected_heatmap_v0_74.png     | GPT-4.1 expected vs selected action  | Shows GPT-4.1 routing distribution.                                                  |
| Figure 5b | figure5_claude_expected_vs_selected_heatmap_v0_74.png    | Claude expected vs selected action   | Shows Claude routing distribution.                                                   |

## Tables

| table    | filename                                                      | title                                        |
|:---------|:--------------------------------------------------------------|:---------------------------------------------|
| Table 1  | table1_two_model_unguided_comparison_v0_74.csv                | Two-model unguided comparison                |
| Table 2  | table2_two_model_controller_before_after_v0_74.csv            | Two-model controller before/after comparison |
| Table 3  | table3_two_model_error_phenotype_comparison_v0_74.csv         | Two-model error phenotype comparison         |
| Table 4  | table4_two_model_controller_intervention_comparison_v0_74.csv | Two-model controller intervention comparison |
| Table 5  | table5_two_model_paired_tests_v0_74.csv                       | Two-model paired correctness tests           |
| Table 6a | table6a_gpt41_expected_vs_selected_v0_74.csv                  | GPT-4.1 expected vs selected matrix          |
| Table 6b | table6b_claude_expected_vs_selected_v0_74.csv                 | Claude expected vs selected matrix           |
