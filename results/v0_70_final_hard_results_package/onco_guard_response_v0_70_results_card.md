# OncoGuard-Response v0.70 Final Hard-Set Results Package

## Summary

v0.70 creates manuscript-ready tables, figures, and synthesis memo from v0.63, v0.63b, v0.67, v0.68, and v0.69.

## Core numeric sequence

| Stage | Version | AACR | Wrong-channel rate | PTMAR | Unsafe authorization |
|---|---:|---:|---:|---:|---:|
| Easy/action-cue-aligned | v0.63 | 98.3% | 1.7% | 0.0% | 0.0% |
| Hard/action-obscured | v0.67 | 61.7% | 38.3% | 0.3% | 0.3% |
| Hard + controller | v0.68 | 100.0% | 0.0% | 0.0% | 0.0% |

## Figures

| figure   | filename                                               | title                                        | purpose                                                                                  |
|:---------|:-------------------------------------------------------|:---------------------------------------------|:-----------------------------------------------------------------------------------------|
| Figure 1 | figure1_easy_hard_controller_aacr_v0_70.png            | Easy vs hard vs controller AACR              | Shows action-cue-aligned near-ceiling, hard-set degradation, and controller restoration. |
| Figure 2 | figure2_wrong_channel_rate_v0_70.png                   | Wrong-channel rate across stages             | Shows wrong-channel instability exposed by hard prompts and eliminated by controller.    |
| Figure 3 | figure3_v0_67_expected_vs_selected_heatmap_v0_70.png   | v0.67 expected vs GPT-4.1 selected action    | Shows hard-set model routing errors, especially wrong-channel escalation.                |
| Figure 4 | figure4_v0_68_expected_vs_controller_heatmap_v0_70.png | v0.68 expected vs controller-selected action | Shows evidence-contract restoration of all action channels.                              |
| Figure 5 | figure5_v0_67_error_taxonomy_v0_70.png                 | v0.67 hard-set error taxonomy                | Shows dominant model failure type.                                                       |
| Figure 6 | figure6_v0_69_ablation_aacr_v0_70.png                  | v0.69 controller ablation                    | Shows full evidence/action routing compared with weaker controller policies.             |

## Tables

| table   | filename                                           | title                             |
|:--------|:---------------------------------------------------|:----------------------------------|
| Table 1 | table1_versioned_results_sequence_v0_70.csv        | Versioned results sequence        |
| Table 2 | table2_core_easy_hard_controller_metrics_v0_70.csv | Core easy/hard/controller metrics |
| Table 3 | table3_v0_67_hard_error_taxonomy_v0_70.csv         | v0.67 hard-set error taxonomy     |
| Table 4 | table4_v0_68_controller_interventions_v0_70.csv    | v0.68 controller interventions    |
| Table 5 | table5_v0_69_hard_ablation_summary_v0_70.csv       | v0.69 ablation summary            |
| Table 6 | table6_paired_correctness_tests_v0_70.csv          | Paired correctness tests          |
