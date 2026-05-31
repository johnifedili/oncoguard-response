# v0.78 Manuscript Results Skeleton

## Results

### Hard action-obscured benchmark exposes cross-model action-channel instability

All three evaluated models completed the repaired hard action-obscured oncology therapeutic-authorization benchmark with 100.0% schema conformance. Despite syntactic reliability, all three models showed clinically meaningful action-channel instability.

GPT-4.1 achieved 61.7% action-channel authorization correctness rate (AACR), with a wrong-channel rate of 38.3%. Claude Sonnet 4.6 achieved 54.7% AACR, with a wrong-channel rate of 45.3%. Gemini Flash achieved the highest unguided AACR at 66.7%, but still had a wrong-channel rate of 33.3% (Table 1; Figures 1–2).

Across models, premature therapy misuse/action rate (PTMAR) and unsafe authorization remained low. GPT-4.1 had PTMAR 0.3% and unsafe authorization 0.3%; Claude Sonnet 4.6 had PTMAR 0.0% and unsafe authorization 0.0%; Gemini Flash had PTMAR 0.0% and unsafe authorization 0.0%. Thus, the dominant failure mode was not widespread unsafe continuation, but incorrect action-channel routing under pressure.

### Models showed distinct therapeutic routing phenotypes

The hard benchmark revealed model-specific failure phenotypes rather than a single universal error pattern. GPT-4.1’s dominant error was wrong_channel_escalation_instead_of_definitive_action, occurring in 95/300 cases (31.7%). Claude Sonnet 4.6’s dominant error was over_hold_instead_of_evaluation, occurring in 55/300 cases (18.3%). Gemini Flash’s dominant error was wrong_channel_escalation_instead_of_definitive_action, occurring in 74/300 cases (24.7%) (Table 3; Figure 4).

These patterns suggest that the hard action-obscured benchmark identifies both cross-model vulnerability and model-specific routing signatures. GPT-4.1 primarily collapsed toward generic escalation. Claude Sonnet 4.6 showed a more conservative over-hold and under-switch phenotype. Gemini Flash performed best overall but still under-routed definitive hold and switch decisions into generic escalation.

### Evidence-contract controller restored evidence-consistent authorization across all models

The deterministic evidence-contract controller restored AACR to 100.0% across all three models (Table 2; Figure 3). For GPT-4.1, AACR improved from 61.7% to 100.0% (+38.3 points). For Claude Sonnet 4.6, AACR improved from 54.7% to 100.0% (+45.3 points). For Gemini Flash, AACR improved from 66.7% to 100.0% (+33.3 points).

The controller reduced wrong-channel rate to 0.0% in all three models. It also reduced PTMAR and unsafe authorization to 0.0% across all controller-corrected outputs. This indicates that the evidence-contract controller did not merely reduce one model’s dominant error type; it normalized distinct model-specific routing phenotypes under the same locked action contract.

### Controller intervention patterns mirrored model-specific failure phenotypes

Controller intervention rates differed by model and reflected each model’s unguided failure pattern. GPT-4.1 required intervention in 115/300 cases (38.3%). Claude Sonnet 4.6 required intervention in 136/300 cases (45.3%). Gemini Flash required intervention in 100/300 cases (33.3%) (Table 4; Figure 5).

Paired exact tests supported large within-model correctness improvements after controller application. GPT-4.1 had 115 unguided-wrong/controller-correct discordant pairs and 0 unguided-correct/controller-wrong pairs. Claude Sonnet 4.6 had 136 such improvements and 0 reversals. Gemini Flash had 100 such improvements and 0 reversals (Table 5).

### Figure and table placement

Recommended figure flow:

- Figure 1: Unguided AACR by model.
- Figure 2: Unguided wrong-channel rate by model.
- Figure 3: Controller before/after AACR across models.
- Figure 4: Model-specific error phenotypes.
- Figure 5: Controller intervention phenotypes.
- Figure 6: Expected-vs-selected heatmaps by model.

Recommended table flow:

- Table 1: Three-model unguided comparison.
- Table 2: Three-model controller before/after comparison.
- Table 3: Error phenotype comparison.
- Table 4: Controller intervention comparison.
- Table 5: Paired correctness tests.
- Supplementary Table 6: Expected-vs-selected matrices.
