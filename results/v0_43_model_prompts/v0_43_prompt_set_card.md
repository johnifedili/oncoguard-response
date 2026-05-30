# OncoGuard-Response v0.43 Model Prompt Set

## Purpose

v0.43 converts the audited v0.42 expanded benchmark into a model-ready prompt set for unguided LLM evaluation.

## Source lineage

- v0.40: expanded 100-trajectory / 300-visit design matrix
- v0.41: synthetic trajectory JSON case generation
- v0.42: integrity audit, benchmark card, and manifest
- v0.43: model prompt construction

## Output file

`results/v0_43_model_prompts/model_prompts_v0_43.csv`

## Summary

| prompt_version   | source_design_version   | source_generation_version   | source_audit_version   |   n_prompts |   n_trajectories |   n_expected_actions |   n_evidence_statuses | first_prompt_id   | last_prompt_id   |
|:-----------------|:------------------------|:----------------------------|:-----------------------|------------:|-----------------:|---------------------:|----------------------:|:------------------|:-----------------|
| v0.43            | v0.40-design-matrix     | v0.41-case-generation       | v0.42-integrity-audit  |         300 |              100 |                    5 |                     5 | OGR_V043_001      | OGR_V043_300     |

## Expected action distribution

| expected_action               |   count |   percent |
|:------------------------------|--------:|----------:|
| continue_therapy              |     175 |      58.3 |
| escalate_evaluation           |      63 |      21   |
| hold_therapy                  |      37 |      12.3 |
| switch_therapy                |      13 |       4.3 |
| emergency_toxicity_management |      12 |       4   |

## Evidence-status distribution

| evidence_status_stage_adjusted   |   count |   percent |
|:---------------------------------|--------:|----------:|
| authorized_or_resolved           |     175 |      58.3 |
| unresolved_needs_more_evidence   |      63 |      21   |
| active_toxicity_or_safety_hold   |      37 |      12.3 |
| progression_or_failure_confirmed |      13 |       4.3 |
| emergency_toxicity_confirmed     |      12 |       4   |

## Prompt schema

Each prompt asks the model to select exactly one of five actions:

- continue_therapy
- escalate_evaluation
- hold_therapy
- switch_therapy
- emergency_toxicity_management

Each model response is required to return valid JSON with:

- selected_action
- reasoning_summary
- missing_information
- safety_concern
- confidence

## Intended use

This prompt set is intended for v0.44 unguided model evaluation and later v0.50 controller/ablation testing.
