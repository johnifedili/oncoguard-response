# OncoGuard-Response v0.43b Blinded Model Prompt Set

## Purpose

v0.43b creates a blinded, less scaffolded prompt set from the audited v0.42 expanded benchmark.

This version removes benchmark-specific cues that may have produced ceiling performance in the scaffolded v0.43 prompt set.

## Removed cue types

The v0.43b prompt excludes:

- expected action labels
- evidence-status labels
- trajectory pattern
- dominant failure mode being tested
- benchmark-family language
- “designed to test...” notes
- direct evidence-status-to-action mapping rules

## Retained clinical information

The prompt retains:

- cancer context
- treatment context
- current visit clinical findings
- symptoms
- objective findings
- labs
- imaging
- toxicity findings
- complication findings
- evidence availability
- missingness
- narrative pressure / discordance features
- allowed action list
- required JSON schema

## Output file

`results/v0_43b_blinded_model_prompts/model_prompts_v0_43b.csv`

## Summary

| prompt_version   | prompt_variant                          | source_design_version   | source_generation_version   | source_audit_version   |   n_prompts |   n_trajectories |   n_expected_actions |   n_evidence_statuses | first_prompt_id   | last_prompt_id   |
|:-----------------|:----------------------------------------|:------------------------|:----------------------------|:-----------------------|------------:|-----------------:|---------------------:|----------------------:|:------------------|:-----------------|
| v0.43b           | blinded_no_failure_mode_or_pattern_cues | v0.40-design-matrix     | v0.41-case-generation       | v0.42-integrity-audit  |         300 |              100 |                    5 |                     5 | OGR_V043B_001     | OGR_V043B_300    |

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

## Intended use

This prompt set is intended for v0.44b blinded unguided model evaluation.
