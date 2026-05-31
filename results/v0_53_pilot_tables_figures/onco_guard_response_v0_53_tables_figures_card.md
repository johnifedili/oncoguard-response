# OncoGuard-Response v0.53 Pilot Tables and Figures

## Purpose

v0.53 creates manuscript-ready pilot tables and figures from the v0.47, v0.50, v0.51, and v0.52 pilot results.

## Main pilot story

Clean/blinded benchmark performance reached ceiling, but naturalistic pressure exposed conservative wrong-channel collapse. The deterministic evidence-contract controller restored evidence-consistent action-channel routing, and ablation showed that full routing—not simple safety blocking—was required.

## Key metrics

| Metric | Unguided GPT-4.1 under pressure | Controller |
|---|---:|---:|
| AACR | 33.3% | 100.0% |
| Wrong-channel rate | 66.7% | 0.0% |
| Wrong-channel escalation | 53.3% | 0.0% |
| PTMAR | 0.0% | 0.0% |
| Unsafe authorization | 0.0% | 0.0% |

## Figures

| figure   | filename                                               | title                                                | purpose                                                                                              |
|:---------|:-------------------------------------------------------|:-----------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| Figure 1 | figure1_four_layer_evaluation_architecture_v0_53.png   | Four-layer evaluation architecture                   | Shows Layer 1 clean case, Layer 2 naturalistic pressure, Layer 3 cue audit, Layer 4 controller test. |
| Figure 2 | figure2_clean_pressure_controller_aacr_v0_53.png       | Clean vs pressure vs controller AACR                 | Shows ceiling clean performance, pressure collapse, and controller correction.                       |
| Figure 3 | figure3_v0_47_expected_vs_selected_heatmap_v0_53.png   | v0.47 expected vs selected action heatmap            | Shows GPT-4.1 wrong-channel collapse into escalation/hold.                                           |
| Figure 4 | figure4_v0_50_expected_vs_controller_heatmap_v0_53.png | v0.50 expected vs controller-selected action heatmap | Shows controller restoration of action-channel alignment.                                            |
| Figure 5 | figure5_v0_51_ablation_aacr_v0_53.png                  | v0.51 ablation AACR                                  | Shows full controller outperforms safety-block and partial-router ablations.                         |
| Figure 6 | figure6_wrong_channel_collapse_schematic_v0_53.png     | Wrong-channel collapse schematic                     | Explains the severity-action mismatch / action-channel interference phenotype.                       |

## Tables

| table   | filename                                       | title                                 |
|:--------|:-----------------------------------------------|:--------------------------------------|
| Table 1 | table1_versioned_pipeline_provenance_v0_53.csv | Versioned pipeline provenance         |
| Table 2 | table2_v0_47_gpt41_pressure_results_v0_53.csv  | v0.47 GPT-4.1 pressure results        |
| Table 3 | table3_v0_50_controller_before_after_v0_53.csv | v0.50 controller before/after results |
| Table 4 | table4_v0_51_controller_ablation_v0_53.csv     | v0.51 controller ablation results     |
| Table 5 | table5_v0_51_paired_correctness_test_v0_53.csv | v0.51 paired correctness test         |

## Reporting caveat

This remains a 30-probe pilot with author-domain confirmation and a deterministic evidence-contract controller. It should not be described as independent multi-rater clinical validation or a fully autonomous parser-derived controller.
