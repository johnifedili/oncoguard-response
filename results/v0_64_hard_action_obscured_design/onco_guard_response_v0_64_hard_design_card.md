# OncoGuard-Response v0.64 — Hard Action-Obscured 300-Probe Design

## Purpose

v0.64 creates a hard 300-probe action-obscured challenge-set design in response to the v0.63b hardness/action-cue alignment audit.

v0.63b showed that the v0.61 expanded set was likely too action-cue aligned:

- all 300 prompts were action-cue aligned,
- all 300 were evidence-cue aligned,
- all 300 were likely too easy by the heuristic audit,
- GPT-4.1 achieved 98.3% AACR.

v0.64 preserves the same balanced design structure but replaces label-revealing wording with clinical fact patterns that require inference.

## Design summary

| design_version   | design_type                        | source_versions   |   n_total_probes |   n_pressure_templates |   n_expected_actions |   n_cancer_types |   n_therapy_classes |   probes_per_template |   probes_per_expected_action |   n_rows_with_prohibited_direct_cue_hits |   model_testing_allowed_count | status                                  |
|:-----------------|:-----------------------------------|:------------------|-----------------:|-----------------------:|---------------------:|-----------------:|--------------------:|----------------------:|-----------------------------:|-----------------------------------------:|------------------------------:|:----------------------------------------|
| v0.64            | hard_action_obscured_challenge_set | v0.60-v0.63b      |              300 |                     10 |                    5 |                5 |                   5 |                    30 |                           60 |                                        0 |                             0 | hard_design_locked_not_prompt_generated |

## Balance

### Expected action distribution

| expected_action               |   count |
|:------------------------------|--------:|
| continue_therapy              |      60 |
| escalate_evaluation           |      60 |
| hold_therapy                  |      60 |
| switch_therapy                |      60 |
| emergency_toxicity_management |      60 |

### Template distribution

| pressure_template_id                |   count |
|:------------------------------------|--------:|
| T01_travel_urgency                  |      30 |
| T02_reported_team_reassurance       |      30 |
| T03_weaponized_complaint_channel    |      30 |
| T04_prescriber_familiarity          |      30 |
| T05_social_consensus                |      30 |
| T06_supervisor_workflow_pressure    |      30 |
| T07_infusion_chair_compounding      |      30 |
| T08_toxicity_minimization           |      30 |
| T09_progression_minimization        |      30 |
| T10_protocol_waiver_prior_stability |      30 |

### Template × expected-action matrix

| pressure_template_id                |   continue_therapy |   emergency_toxicity_management |   escalate_evaluation |   hold_therapy |   switch_therapy |
|:------------------------------------|-------------------:|--------------------------------:|----------------------:|---------------:|-----------------:|
| T01_travel_urgency                  |                  6 |                               6 |                     6 |              6 |                6 |
| T02_reported_team_reassurance       |                  6 |                               6 |                     6 |              6 |                6 |
| T03_weaponized_complaint_channel    |                  6 |                               6 |                     6 |              6 |                6 |
| T04_prescriber_familiarity          |                  6 |                               6 |                     6 |              6 |                6 |
| T05_social_consensus                |                  6 |                               6 |                     6 |              6 |                6 |
| T06_supervisor_workflow_pressure    |                  6 |                               6 |                     6 |              6 |                6 |
| T07_infusion_chair_compounding      |                  6 |                               6 |                     6 |              6 |                6 |
| T08_toxicity_minimization           |                  6 |                               6 |                     6 |              6 |                6 |
| T09_progression_minimization        |                  6 |                               6 |                     6 |              6 |                6 |
| T10_protocol_waiver_prior_stability |                  6 |                               6 |                     6 |              6 |                6 |

## Obscuring strategy

Direct phrases such as “confirmed progression,” “urgent toxicity,” “active treatment hold,” and “not enough verified information” are avoided. Instead, the design uses clinical facts such as lesion measurements, symptom descriptions, missing lab values, and workflow context.

## Binding rule

v0.64 is a design artifact only. No prompts are generated and no model testing is allowed from this artifact.

Next steps:

1. v0.65 — Generate hard action-obscured prompts.
2. v0.66 — Layer 1–3 plus action-cue audit.
3. v0.67 — GPT-4.1 hard-set evaluation.
4. v0.68 — Controller intervention.
5. v0.69 — Ablation.

## Caveat

This is a designed challenge set, not an empirical result.
