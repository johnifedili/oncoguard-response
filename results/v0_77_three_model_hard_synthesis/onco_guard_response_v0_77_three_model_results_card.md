# OncoGuard-Response v0.77 — Three-Model Hard-Set Synthesis

## Summary

v0.77 compares GPT-4.1, Claude Sonnet 4.6, and Gemini Flash on the repaired hard action-obscured 300-prompt benchmark and synthesizes controller effects across all three models.

## Three-model unguided comparison

| model             | source_version   |   n |   schema_conformance_percent |   hard_pressure_aacr_percent |   wrong_channel_percent |   wrong_channel_escalation_percent |   ptmar_percent |   unsafe_authorization_percent |   defer_rate_percent |   over_hold_percent |   over_deferral_percent | dominant_error_type                                   | phenotype_label                        |
|:------------------|:-----------------|----:|-----------------------------:|-----------------------------:|------------------------:|-----------------------------------:|----------------:|-------------------------------:|---------------------:|--------------------:|------------------------:|:------------------------------------------------------|:---------------------------------------|
| GPT-4.1           | v0.67            | 300 |                          100 |                         61.7 |                    38.3 |                               31.7 |             0.3 |                            0.3 |                 50.7 |                 5.7 |                     0.7 | wrong_channel_escalation_instead_of_definitive_action | generic_escalation_collapse            |
| Claude Sonnet 4.6 | v0.72            | 300 |                          100 |                         54.7 |                    45.3 |                               16.7 |             0   |                            0   |                 23.3 |                23.7 |                     5   | over_hold_instead_of_evaluation                       | over_hold_under_switch_collapse        |
| Gemini Flash      | v0.75            | 300 |                          100 |                         66.7 |                    33.3 |                               24.7 |             0   |                            0   |                 44.3 |                 4.3 |                     4   | wrong_channel_escalation_instead_of_definitive_action | under_hold_generic_escalation_collapse |

## Three-model controller comparison

| model             | unguided_source   | controller_source   |   n |   unguided_aacr_percent |   controller_aacr_percent |   aacr_improvement_points |   unguided_wrong_channel_percent |   controller_wrong_channel_percent |   unguided_ptmar_percent |   controller_ptmar_percent |   unguided_unsafe_authorization_percent |   controller_unsafe_authorization_percent |   n_controller_interventions |   controller_intervention_rate_percent |
|:------------------|:------------------|:--------------------|----:|------------------------:|--------------------------:|--------------------------:|---------------------------------:|-----------------------------------:|-------------------------:|---------------------------:|----------------------------------------:|------------------------------------------:|-----------------------------:|---------------------------------------:|
| GPT-4.1           | v0.67             | v0.68               | 300 |                    61.7 |                       100 |                      38.3 |                             38.3 |                                  0 |                      0.3 |                          0 |                                     0.3 |                                         0 |                          115 |                                   38.3 |
| Claude Sonnet 4.6 | v0.72             | v0.73               | 300 |                    54.7 |                       100 |                      45.3 |                             45.3 |                                  0 |                      0   |                          0 |                                     0   |                                         0 |                          136 |                                   45.3 |
| Gemini Flash      | v0.75             | v0.76               | 300 |                    66.7 |                       100 |                      33.3 |                             33.3 |                                  0 |                      0   |                          0 |                                     0   |                                         0 |                          100 |                                   33.3 |

## Key interpretation

All three models showed hard-set action-channel instability. Failure phenotype varied by model, while the same deterministic evidence-contract controller restored evidence-consistent action authorization across all three.

## Figures

| figure    | filename                                                   | title                                | purpose                                                                                                   |
|:----------|:-----------------------------------------------------------|:-------------------------------------|:----------------------------------------------------------------------------------------------------------|
| Figure 1  | figure1_three_model_unguided_aacr_v0_77.png                | Unguided AACR by model               | Shows all three models have imperfect action-channel accuracy on the hard benchmark.                      |
| Figure 2  | figure2_three_model_wrong_channel_rate_v0_77.png           | Unguided wrong-channel rate by model | Shows wrong-channel instability across all three models.                                                  |
| Figure 3  | figure3_three_model_controller_before_after_aacr_v0_77.png | Controller before/after AACR         | Shows evidence-contract controller restores AACR across all three models.                                 |
| Figure 4  | figure4_three_model_error_phenotypes_v0_77.png             | Three-model failure phenotypes       | Contrasts GPT-4.1 escalation, Claude over-hold/under-switch, and Gemini under-hold/escalation phenotypes. |
| Figure 5  | figure5_three_model_controller_interventions_v0_77.png     | Controller intervention phenotypes   | Shows which model-specific failures the controller corrected.                                             |
| Figure 6a | figure6_gpt41_expected_vs_selected_heatmap_v0_77.png       | GPT-4.1 expected vs selected action  | Shows GPT-4.1 routing distribution.                                                                       |
| Figure 6b | figure6_claude_expected_vs_selected_heatmap_v0_77.png      | Claude expected vs selected action   | Shows Claude routing distribution.                                                                        |
| Figure 6c | figure6_gemini_expected_vs_selected_heatmap_v0_77.png      | Gemini expected vs selected action   | Shows Gemini routing distribution.                                                                        |

## Tables

| table    | filename                                                        | title                                          |
|:---------|:----------------------------------------------------------------|:-----------------------------------------------|
| Table 1  | table1_three_model_unguided_comparison_v0_77.csv                | Three-model unguided comparison                |
| Table 2  | table2_three_model_controller_before_after_v0_77.csv            | Three-model controller before/after comparison |
| Table 3  | table3_three_model_error_phenotype_comparison_v0_77.csv         | Three-model error phenotype comparison         |
| Table 4  | table4_three_model_controller_intervention_comparison_v0_77.csv | Three-model controller intervention comparison |
| Table 5  | table5_three_model_paired_tests_v0_77.csv                       | Three-model paired correctness tests           |
| Table 6a | table6a_gpt41_expected_vs_selected_v0_77.csv                    | GPT-4.1 expected vs selected matrix            |
| Table 6b | table6b_claude_expected_vs_selected_v0_77.csv                   | Claude expected vs selected matrix             |
| Table 6c | table6c_gemini_expected_vs_selected_v0_77.csv                   | Gemini expected vs selected matrix             |
