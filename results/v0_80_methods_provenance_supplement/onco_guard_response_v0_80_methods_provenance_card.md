# OncoGuard-Response v0.80 — Methods/Provenance Supplement Package

## Purpose

v0.80 locks the reviewer-facing methods and provenance supplement for the three-model hard-set benchmark and controller study.

## Included artifacts

- `v0_80_git_provenance.csv`
- `v0_80_version_lineage_map.csv`
- `v0_80_primary_file_manifest_sha256.csv`
- `v0_80_model_registry.csv`
- `v0_80_endpoint_definitions.csv`
- `v0_80_controller_specification.csv`
- `v0_80_controller_logic_specification.md`
- `v0_80_reproducibility_statement.md`
- `v0_80_supplement_outline.md`
- `v0_80_script_registry_sha256.csv`
- `v0_80_protocol_notes_and_deviations.csv`

## Core reproducibility statement

Primary hard prompt set:

`results/v0_66d_targeted_actioncue_repair/v0_66d_model_testing_allowed_hard_prompts.csv`

Primary model evaluations:

- GPT-4.1: v0.67
- Claude Sonnet 4.6: v0.72
- Gemini Flash: v0.75

Controller evaluations:

- GPT-4.1: v0.68
- Claude Sonnet 4.6: v0.73
- Gemini Flash: v0.76

Manuscript synthesis:

- v0.77 three-model hard-set synthesis
- v0.78 Results/Discussion skeleton
- v0.79 full manuscript scaffold

## Required caveat

The controller uses the locked expected-action channel as the deterministic evidence/action contract. It is a controller-mechanism study, not a fully autonomous parser-derived clinical decision system.
