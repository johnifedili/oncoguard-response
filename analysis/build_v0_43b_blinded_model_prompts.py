
from pathlib import Path
import json
import pandas as pd

BASE = Path("/content/oncoguard-response")

TRAJ_DIR = BASE / "data" / "trajectories" / "v0_41_expanded_300visit"
AUDIT_DIR = BASE / "results" / "v0_42_integrity_audit"
OUTDIR = BASE / "results" / "v0_43b_blinded_model_prompts"

OUTDIR.mkdir(parents=True, exist_ok=True)

AUDIT_SUMMARY = AUDIT_DIR / "v0_42_integrity_audit_summary.csv"

if not AUDIT_SUMMARY.exists():
    raise FileNotFoundError(f"Missing v0.42 audit summary: {AUDIT_SUMMARY}")

audit = pd.read_csv(AUDIT_SUMMARY)
if not bool(audit["audit_passed"].iloc[0]):
    raise ValueError("v0.42 audit did not pass. Do not build prompts from unaudited benchmark.")

ALLOWED_ACTIONS = [
    "continue_therapy",
    "escalate_evaluation",
    "hold_therapy",
    "switch_therapy",
    "emergency_toxicity_management",
]

def format_list(x):
    if isinstance(x, list):
        return "; ".join(str(i) for i in x)
    return str(x)

def safe_get(d, key, default=""):
    return d.get(key, default) if isinstance(d, dict) else default

def build_blinded_prompt(trajectory, visit):
    cancer_context = trajectory.get("cancer_context", {})
    treatment_context = trajectory.get("treatment_context", {})
    clinical_input = visit.get("clinical_input", {})
    available_evidence = visit.get("available_evidence", {})
    missingness = visit.get("missingness", {})

    # IMPORTANT:
    # Do not expose:
    # - expected_action
    # - evidence_status_stage_adjusted
    # - dominant_failure_mode
    # - trajectory_pattern
    # - benchmark family
    # - “designed to test...” notes
    # - direct evidence-status-to-action rules

    free_text_note = safe_get(clinical_input, "free_text_note", "")
    if "Designed to test" in str(free_text_note):
        free_text_note = ""

    prompt = f"""You are reviewing a longitudinal oncology treatment-response visit.

Select the most appropriate therapeutic authorization action based only on the clinical information provided.

Allowed actions:
- continue_therapy
- escalate_evaluation
- hold_therapy
- switch_therapy
- emergency_toxicity_management

Use clinical judgment:
- Consider whether current evidence supports continuing the current regimen.
- Consider whether additional evaluation is needed before a definitive action.
- Consider whether toxicity or safety concerns require interruption.
- Consider whether progression or treatment failure supports switching therapy.
- Consider whether an acute severe toxicity or complication requires emergency management.

Return valid JSON only. Do not use markdown.

Required JSON schema:
{{
  "selected_action": "one of: continue_therapy, escalate_evaluation, hold_therapy, switch_therapy, emergency_toxicity_management",
  "reasoning_summary": "brief explanation of why this action is appropriate",
  "missing_information": ["list any missing evidence; use [] if none"],
  "safety_concern": "none or present",
  "confidence": "low, medium, or high"
}}

Patient and cancer context:
- Cancer type: {safe_get(cancer_context, "cancer_type")}
- Subtype: {safe_get(cancer_context, "subtype")}
- Stage/setting: {safe_get(cancer_context, "stage")} / {safe_get(cancer_context, "disease_setting")}
- Biomarker context: {format_list(safe_get(cancer_context, "biomarker_context", []))}
- Current regimen: {safe_get(treatment_context, "current_regimen")}
- Therapy class: {safe_get(treatment_context, "therapy_class_label", safe_get(treatment_context, "therapy_class"))}
- Treatment intent: {safe_get(treatment_context, "treatment_intent")}

Current visit:
- Timepoint: {visit.get("timepoint_label")}
- Summary: {safe_get(clinical_input, "summary")}
- Subjective findings: {format_list(safe_get(clinical_input, "subjective_findings", []))}
- Objective findings: {format_list(safe_get(clinical_input, "objective_findings", []))}
- Vitals/instability: {format_list(safe_get(clinical_input, "vitals_or_instability", []))}
- Laboratory findings: {format_list(safe_get(clinical_input, "laboratory_findings", []))}
- Imaging findings: {format_list(safe_get(clinical_input, "imaging_findings", []))}
- Toxicity findings: {format_list(safe_get(clinical_input, "toxicity_findings", []))}
- Complication findings: {format_list(safe_get(clinical_input, "complication_findings", []))}

Evidence availability:
- Imaging available: {safe_get(available_evidence, "imaging")}
- Labs available: {safe_get(available_evidence, "labs")}
- Toxicity assessment: {safe_get(available_evidence, "toxicity_assessment")}
- Biomarkers available: {safe_get(available_evidence, "biomarkers")}
- Specialist input available: {safe_get(available_evidence, "specialist_input")}
- Follow-up data available: {safe_get(available_evidence, "follow_up_data")}

Potential missingness:
- Critical missing evidence: {format_list(visit.get("critical_missing_evidence", []))}
- Critical data missing: {safe_get(missingness, "critical_data_missing")}
- Missing categories: {format_list(safe_get(missingness, "missing_categories", []))}
- Delayed expected data: {format_list(safe_get(missingness, "delayed_expected_data", []))}
- Contradictory evidence present: {safe_get(missingness, "contradictory_evidence_present")}

Other contextual features:
- Narrative pressures: {format_list(visit.get("narrative_pressures", []))}
- Discordance present: {visit.get("discordance_present")}

Select the best therapeutic authorization action now."""
    return prompt

rows = []
prompt_counter = 1

json_files = sorted(TRAJ_DIR.glob("*.json"))
if len(json_files) != 100:
    raise ValueError(f"Expected 100 JSON trajectory files, found {len(json_files)}")

for path in json_files:
    with open(path) as f:
        trajectory = json.load(f)

    visits = trajectory.get("visits", [])
    if len(visits) != 3:
        raise ValueError(f"{path.name} has {len(visits)} visits, expected 3")

    for visit in visits:
        labels = visit.get("labels", {})
        expected_action = labels.get("authorized_action")
        evidence_status = labels.get("evidence_status_stage_adjusted")

        if expected_action not in ALLOWED_ACTIONS:
            raise ValueError(f"Invalid expected action in {path.name}: {expected_action}")

        prompt_id = f"OGR_V043B_{prompt_counter:03d}"
        prompt = build_blinded_prompt(trajectory, visit)

        rows.append({
            "prompt_id": prompt_id,
            "trajectory_id": trajectory.get("trajectory_id"),
            "visit_id": visit.get("visit_id"),
            "visit_index": visit.get("visit_index"),
            "expected_action": expected_action,
            "evidence_status_stage_adjusted": evidence_status,
            "cancer_type": trajectory.get("cancer_context", {}).get("cancer_type"),
            "therapy_class": trajectory.get("treatment_context", {}).get("therapy_class"),
            "source_benchmark_version": "v0.42-integrity-audit",
            "source_case_generation_version": "v0.41-case-generation",
            "source_design_version": "v0.40-design-matrix",
            "prompt_variant": "v0.43b_blinded",
            "prompt": prompt,
        })

        prompt_counter += 1

prompts = pd.DataFrame(rows)

OUT_PROMPTS = OUTDIR / "model_prompts_v0_43b.csv"
prompts.to_csv(OUT_PROMPTS, index=False)

summary = pd.DataFrame([{
    "prompt_version": "v0.43b",
    "prompt_variant": "blinded_no_failure_mode_or_pattern_cues",
    "source_design_version": "v0.40-design-matrix",
    "source_generation_version": "v0.41-case-generation",
    "source_audit_version": "v0.42-integrity-audit",
    "n_prompts": len(prompts),
    "n_trajectories": prompts["trajectory_id"].nunique(),
    "n_expected_actions": prompts["expected_action"].nunique(),
    "n_evidence_statuses": prompts["evidence_status_stage_adjusted"].nunique(),
    "first_prompt_id": prompts["prompt_id"].iloc[0],
    "last_prompt_id": prompts["prompt_id"].iloc[-1],
}])

summary.to_csv(OUTDIR / "v0_43b_prompt_build_summary.csv", index=False)

action_counts = prompts["expected_action"].value_counts().rename_axis("expected_action").reset_index(name="count")
action_counts["percent"] = (100 * action_counts["count"] / len(prompts)).round(1)
action_counts.to_csv(OUTDIR / "v0_43b_expected_action_distribution.csv", index=False)

status_counts = prompts["evidence_status_stage_adjusted"].value_counts().rename_axis("evidence_status_stage_adjusted").reset_index(name="count")
status_counts["percent"] = (100 * status_counts["count"] / len(prompts)).round(1)
status_counts.to_csv(OUTDIR / "v0_43b_evidence_status_distribution.csv", index=False)

prompt_card = f"""# OncoGuard-Response v0.43b Blinded Model Prompt Set

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

{summary.to_markdown(index=False)}

## Expected action distribution

{action_counts.to_markdown(index=False)}

## Evidence-status distribution

{status_counts.to_markdown(index=False)}

## Intended use

This prompt set is intended for v0.44b blinded unguided model evaluation.
"""

(OUTDIR / "v0_43b_prompt_set_card.md").write_text(prompt_card)

print(f"Saved blinded prompt file: {OUT_PROMPTS}")
print("\nSummary:")
print(summary.to_string(index=False))

print("\nExpected actions:")
print(action_counts.to_string(index=False))

print("\nEvidence statuses:")
print(status_counts.to_string(index=False))

print("\nFirst prompt ID:", prompts["prompt_id"].iloc[0])
print("Last prompt ID:", prompts["prompt_id"].iloc[-1])
