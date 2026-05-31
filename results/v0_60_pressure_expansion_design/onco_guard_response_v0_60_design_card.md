# OncoGuard-Response v0.60 — 300-Probe Naturalistic Pressure Expansion Design

## Purpose

v0.60 defines the design matrix for the expanded 300-probe naturalistic pressure benchmark.

This is a design artifact only. It does not generate prompts, run models, or apply a controller.

## Rationale

The v0.46–v0.53 pilot established that naturalistic clinical pressure can expose conservative wrong-channel collapse in GPT-4.1 and that an evidence-contract controller can correct the observed failure. The v0.60 design expands the pilot in a more reviewer-proof way by balancing across:

- pressure templates,
- expected action channels,
- cancer types,
- therapy classes,
- evidence states.

## Design summary

| design_version   |   n_total_probes |   n_pressure_templates |   n_expected_actions |   n_cancer_types |   n_therapy_classes |   probes_per_template |   probes_per_expected_action |   model_testing_allowed_count | status                             |
|:-----------------|-----------------:|-----------------------:|---------------------:|-----------------:|--------------------:|----------------------:|-----------------------------:|------------------------------:|:-----------------------------------|
| v0.60            |              300 |                     10 |                    5 |                5 |                   5 |                    30 |                           60 |                             0 | design_locked_not_prompt_generated |

## Pressure templates

The design uses 10 pressure templates:

- 6 validated pilot backbone templates from v0.46
- 4 additional oncology-specific naturalistic templates

| pressure_template_id                | template_name                                  | template_status             | taxonomy_mapping                                 |
|:------------------------------------|:-----------------------------------------------|:----------------------------|:-------------------------------------------------|
| T01_travel_urgency                  | Travel / treatment-timing urgency              | validated_pilot_backbone    | F01_plea;F02_tempo;F13_premise                   |
| T02_reported_team_reassurance       | Reported team reassurance                      | validated_pilot_backbone    | F03_whitecoat;F04_shadow;F13_premise;F02_tempo   |
| T03_weaponized_complaint_channel    | Weaponized complaint channel                   | validated_pilot_backbone    | F11_coerce;F06_empath;F02_tempo;F13_premise      |
| T04_prescriber_familiarity          | Clinician familiarity pressure                 | validated_pilot_backbone    | F03_whitecoat;F10_persona;F04_shadow;F13_premise |
| T05_social_consensus                | Social consensus pressure                      | validated_pilot_backbone    | F11_coerce;F03_whitecoat;F13_premise;F04_shadow  |
| T06_supervisor_workflow_pressure    | Supervisor / workflow pressure                 | validated_pilot_backbone    | F03_whitecoat;F13_premise;F04_shadow;F02_tempo   |
| T07_infusion_chair_compounding      | Infusion-chair / compounding deadline pressure | new_v0_60_oncology_template | F02_tempo;F01_plea;F04_shadow                    |
| T08_toxicity_minimization           | Toxicity minimization                          | new_v0_60_oncology_template | F04_shadow;F05_anchor;F13_premise                |
| T09_progression_minimization        | Progression minimization                       | new_v0_60_oncology_template | F13_premise;F04_shadow;F05_anchor                |
| T10_protocol_waiver_prior_stability | Protocol-waiver / prior-stability pressure     | new_v0_60_oncology_template | F03_whitecoat;F13_premise;F04_shadow;F02_tempo   |

## Expected action balance

| expected_action               |   count |
|:------------------------------|--------:|
| continue_therapy              |      60 |
| escalate_evaluation           |      60 |
| hold_therapy                  |      60 |
| switch_therapy                |      60 |
| emergency_toxicity_management |      60 |

## Pressure-template balance

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

## Template × expected-action matrix

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

## Cancer distribution

| cancer_type       |   count |
|:------------------|--------:|
| NSCLC             |      60 |
| breast_cancer     |      60 |
| colorectal_cancer |      60 |
| melanoma          |      60 |
| ovarian_cancer    |      60 |

## Therapy distribution

| therapy_class               |   count |
|:----------------------------|--------:|
| immune_checkpoint_inhibitor |      60 |
| targeted_therapy            |      60 |
| cytotoxic_chemotherapy      |      60 |
| HER2_directed_therapy       |      60 |
| PARP_platinum_based_therapy |      60 |

## Binding rule

No model testing should occur from v0.60. The next steps are:

1. v0.61 prompt generation from the locked v0.60 design matrix.
2. v0.62 Layer 1–3 audit and independent/human confirmation.
3. v0.63 model evaluation.
4. v0.64 controller intervention and ablation.

## Reporting caveat

v0.60 is a prospective design matrix for expansion, not an empirical result.
