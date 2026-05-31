# OncoGuard v0.46 Naturalistic Pressure Probe Pilot

## Purpose

v0.46 creates a 30-probe naturalistic pressure pilot from the v0.45 pressure taxonomy and cue-contamination protocol.

These probes are **not model-ready** until they pass Layers 1–3 review:

1. Clean clinical case validity
2. Naturalistic pressure realism
3. Cue-contamination audit

## Design

- 6 high-yield pressure templates
- 5 source oncology visits per template
- 30 total draft probes
- F07 ratchet excluded from this pilot because it is multi-turn

## Selected pressure templates

| pressure_template_id             |   count |
|:---------------------------------|--------:|
| T01_travel_urgency               |       5 |
| T02_reported_team_reassurance    |       5 |
| T03_weaponized_complaint_channel |       5 |
| T04_prescriber_familiarity       |       5 |
| T05_social_consensus             |       5 |
| T06_supervisor_workflow_pressure |       5 |

## Expected action distribution

| source_expected_action        |   count |
|:------------------------------|--------:|
| escalate_evaluation           |      12 |
| hold_therapy                  |       6 |
| switch_therapy                |       6 |
| emergency_toxicity_management |       6 |

## Files

- `naturalistic_pressure_probes_v0_46.csv`
- `v0_46_layer123_scoring_sheet.csv`
- `v0_46_pilot_summary.csv`
- `v0_46_template_distribution.csv`
- `v0_46_expected_action_distribution.csv`
- `v0_46_taxonomy_mapping_distribution.csv`
- `v0_46_basic_cue_scan.csv`

## Binding rule

No model or controller testing should be performed on these probes until each probe passes:

- Layer 1 clinical validity
- Layer 2 pressure realism score threshold
- Layer 3 cue-contamination threshold

## Current status

Draft probe pilot generated. Human/LLM audit required before v0.47 model testing.
