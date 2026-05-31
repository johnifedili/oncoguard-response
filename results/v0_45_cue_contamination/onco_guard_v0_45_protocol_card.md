# OncoGuard v0.45 Protocol Card

## Purpose

v0.45 formalizes the pressure taxonomy, naturalistic rewrite rules, cue-contamination audit rubric, and pilot design for evaluating clinical LLM robustness under realistic workflow pressure.

## Source architecture

Four-layer architecture:

1. Clean clinical case
2. Naturalistic pressure
3. Cue-contamination audit
4. Controller test

## Generated files

- `onco_response_pressure_taxonomy_v0_45.csv`
- `naturalistic_pressure_templates_v0_45.csv`
- `cue_contamination_rubric_v0_45.md`
- `naturalistic_rewrite_rules_v0_45.md`
- `pilot_design_v0_45.md`

## Pressure family count

| Type | Count |
|---|---:|
| Single-turn families | 12 |
| Multi-turn families | 1 |
| Total families | 13 |

## Naturalistic pressure templates

| Template count | 9 |
|---|---:|

## Binding rule

No model/controller testing should occur until probes pass:

- Layer 1 clinical validity
- Layer 2 pressure realism
- Layer 3 cue-contamination audit
