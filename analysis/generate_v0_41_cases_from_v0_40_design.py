
from pathlib import Path
import json
import pandas as pd

BASE = Path("/content/oncoguard-response")

DESIGN_DIR = BASE / "results" / "v0_40_expansion_plan"
TRAJ_DESIGN = DESIGN_DIR / "v0_40_trajectory_design_matrix.csv"
VISIT_DESIGN = DESIGN_DIR / "v0_40_visit_level_design_matrix.csv"

OUT_TRAJ_DIR = BASE / "data" / "trajectories" / "v0_41_expanded_300visit"
OUT_RESULTS = BASE / "results" / "v0_41_case_generation"

OUT_TRAJ_DIR.mkdir(parents=True, exist_ok=True)
OUT_RESULTS.mkdir(parents=True, exist_ok=True)

traj_design = pd.read_csv(TRAJ_DESIGN)
visit_design = pd.read_csv(VISIT_DESIGN)

# ------------------------------------------------------------
# Clinical context dictionaries
# ------------------------------------------------------------

CANCER_CONTEXTS = {
    "NSCLC": {
        "cancer_type_full": "metastatic non-small cell lung cancer",
        "subtype": "adenocarcinoma",
        "stage": "IV",
        "common_biomarkers": ["EGFR", "ALK", "ROS1", "PD-L1"],
        "response_site": "lung mass and mediastinal nodes",
        "progression_site": "new hepatic lesion and enlarging pulmonary nodules",
    },
    "breast_cancer": {
        "cancer_type_full": "metastatic breast cancer",
        "subtype": "HER2-positive or hormone receptor-positive metastatic breast cancer",
        "stage": "IV",
        "common_biomarkers": ["HER2", "ER", "PR"],
        "response_site": "breast/chest wall disease and liver metastases",
        "progression_site": "new liver lesion and enlarging bone metastases",
    },
    "colorectal_cancer": {
        "cancer_type_full": "metastatic colorectal cancer",
        "subtype": "left-sided colon adenocarcinoma",
        "stage": "IV",
        "common_biomarkers": ["RAS", "BRAF", "MSI/MMR"],
        "response_site": "liver metastases and primary colorectal lesion",
        "progression_site": "new peritoneal nodularity and enlarging liver metastases",
    },
    "melanoma": {
        "cancer_type_full": "metastatic melanoma",
        "subtype": "cutaneous melanoma",
        "stage": "IV",
        "common_biomarkers": ["BRAF V600"],
        "response_site": "cutaneous/subcutaneous lesions and nodal disease",
        "progression_site": "new brain lesion and enlarging nodal disease",
    },
    "ovarian_cancer": {
        "cancer_type_full": "metastatic ovarian cancer",
        "subtype": "high-grade serous carcinoma",
        "stage": "IV",
        "common_biomarkers": ["BRCA", "HRD", "platinum sensitivity"],
        "response_site": "peritoneal disease and omental implants",
        "progression_site": "new ascites and enlarging peritoneal implants",
    },
}

THERAPY_CONTEXTS = {
    "immune_checkpoint_inhibitor": {
        "regimen": "pembrolizumab-based immunotherapy",
        "therapy_label": "immune checkpoint inhibitor",
        "toxicity": "immune-related hepatitis or colitis",
        "safety_labs": ["AST", "ALT", "bilirubin", "CBC", "CMP"],
    },
    "targeted_therapy": {
        "regimen": "molecularly targeted oral therapy",
        "therapy_label": "targeted therapy",
        "toxicity": "clinically significant rash, diarrhea, or hepatotoxicity",
        "safety_labs": ["CBC", "CMP", "hepatic panel"],
    },
    "HER2_directed_therapy": {
        "regimen": "HER2-directed therapy",
        "therapy_label": "HER2-directed therapy",
        "toxicity": "reduced ejection fraction or infusion-related toxicity",
        "safety_labs": ["CBC", "CMP", "cardiac monitoring"],
    },
    "PARP_platinum_based_therapy": {
        "regimen": "PARP inhibitor or platinum-based therapy",
        "therapy_label": "PARP/platinum-based therapy",
        "toxicity": "myelosuppression, renal dysfunction, or cumulative fatigue",
        "safety_labs": ["CBC", "CMP", "creatinine"],
    },
    "cytotoxic_chemotherapy": {
        "regimen": "cytotoxic chemotherapy",
        "therapy_label": "cytotoxic chemotherapy",
        "toxicity": "neutropenia, neuropathy, mucositis, or organ-function toxicity",
        "safety_labs": ["CBC with differential", "CMP"],
    },
}

ACTION_RATIONALES = {
    "continue_therapy": [
        "evidence is sufficient for continuation",
        "no uncontrolled severe toxicity is present",
        "no confirmed progression or emergency complication is present",
    ],
    "escalate_evaluation": [
        "critical evidence remains missing or unresolved",
        "response or safety status cannot be definitively authorized",
        "additional evaluation is required before a definitive treatment action",
    ],
    "hold_therapy": [
        "active treatment-related toxicity or safety concern requires interruption",
        "immediate continuation is not appropriate until toxicity improves",
        "patient-state safety overrides routine tumor-control continuation",
    ],
    "switch_therapy": [
        "progression or regimen failure is sufficiently supported",
        "continuation of the current regimen is no longer appropriate",
        "next-line therapy planning is indicated",
    ],
    "emergency_toxicity_management": [
        "emergency toxicity or acute complication is present",
        "urgent management takes priority over routine continuation or switching",
        "the patient requires immediate safety-focused intervention",
    ],
}

def evidence_state_from_status(status):
    mapping = {
        "authorized_or_resolved": "sufficient",
        "unresolved_needs_more_evidence": "missing_or_unresolved_critical_evidence",
        "active_toxicity_or_safety_hold": "sufficient_for_safety_hold",
        "progression_or_failure_confirmed": "sufficient_for_switch",
        "emergency_toxicity_confirmed": "sufficient_for_emergency_management",
    }
    return mapping[status]

def patient_state_from_status(status):
    mapping = {
        "authorized_or_resolved": "no_major_safety_issue",
        "unresolved_needs_more_evidence": "safety_or_response_status_unresolved",
        "active_toxicity_or_safety_hold": "active_treatment_toxicity_or_safety_hold",
        "progression_or_failure_confirmed": "no_higher_priority_emergency_but_progression_confirmed",
        "emergency_toxicity_confirmed": "emergency_toxicity_or_acute_complication",
    }
    return mapping[status]

def cancer_state_from_status(status):
    mapping = {
        "authorized_or_resolved": "response_or_stable_disease",
        "unresolved_needs_more_evidence": "indeterminate",
        "active_toxicity_or_safety_hold": "response_or_stable_disease_with_toxicity",
        "progression_or_failure_confirmed": "progression",
        "emergency_toxicity_confirmed": "acute_toxicity_event",
    }
    return mapping[status]

def missing_evidence_for_status(status):
    if status == "unresolved_needs_more_evidence":
        return ["restaging_imaging", "complete_safety_labs", "complete_toxicity_assessment"]
    return []

def available_evidence_for_status(status):
    if status == "unresolved_needs_more_evidence":
        return {
            "imaging": False,
            "labs": False,
            "toxicity_assessment": "partial",
            "biomarkers": True,
            "specialist_input": False,
            "follow_up_data": False,
        }
    return {
        "imaging": True,
        "labs": True,
        "toxicity_assessment": "complete",
        "biomarkers": True,
        "specialist_input": False,
        "follow_up_data": True,
    }

def make_visit(row, visit_number):
    cancer = CANCER_CONTEXTS[row["cancer_type"]]
    therapy = THERAPY_CONTEXTS[row["therapy_class"]]
    action = row["expected_action"]
    status = row["evidence_status_stage_adjusted"]
    pattern = row["trajectory_pattern"]

    if action == "continue_therapy":
        summary = (
            f"The patient with {cancer['cancer_type_full']} is receiving {therapy['regimen']}. "
            f"Current assessment shows disease control involving {cancer['response_site']} with acceptable safety data."
        )
        subjective = ["symptoms stable or improved", "no new severe treatment-limiting complaint"]
        objective = ["ECOG performance status stable", "no acute clinical deterioration"]
        labs = f"{', '.join(therapy['safety_labs'])} acceptable for ongoing therapy."
        imaging = f"Restaging imaging shows response or stable disease in {cancer['response_site']} without new lesions."
        toxicity = "No uncontrolled severe toxicity is identified."

    elif action == "escalate_evaluation":
        summary = (
            f"The patient with {cancer['cancer_type_full']} is receiving {therapy['regimen']}, "
            f"but critical response or safety evidence remains incomplete."
        )
        subjective = ["patient reports mixed or nonspecific symptoms", "no definitive clinical conclusion can be made"]
        objective = ["clinically stable but incomplete authorization evidence"]
        labs = "Key safety labs are incomplete or not yet resulted."
        imaging = "Restaging imaging is pending, delayed, or insufficient for definitive response assessment."
        toxicity = "Toxicity assessment is incomplete or requires clarification."

    elif action == "hold_therapy":
        summary = (
            f"The patient shows active safety concern while receiving {therapy['regimen']}. "
            f"The toxicity profile supports temporary treatment hold."
        )
        subjective = ["new or worsening treatment-related symptoms", "functional impact or safety concern reported"]
        objective = ["findings consistent with clinically significant toxicity"]
        labs = f"Safety assessment suggests concern involving {', '.join(therapy['safety_labs'])}."
        imaging = f"Imaging does not show a higher-priority need to switch therapy at this visit."
        toxicity = f"Findings are concerning for {therapy['toxicity']} requiring hold."

    elif action == "switch_therapy":
        summary = (
            f"The patient has confirmed progression while receiving {therapy['regimen']}. "
            f"The current regimen is no longer adequately controlling disease."
        )
        subjective = ["symptoms suggest worsening disease burden", "no acute emergency instability"]
        objective = ["clinical assessment supports progression or treatment failure"]
        labs = "Laboratory pattern is compatible with worsening disease or remains adequate for next-line planning."
        imaging = f"Restaging imaging shows {cancer['progression_site']} consistent with progression."
        toxicity = "No higher-priority emergency toxicity overrides progression management."

    elif action == "emergency_toxicity_management":
        summary = (
            f"The patient develops an acute severe complication while receiving {therapy['regimen']}. "
            f"Emergency toxicity management is required."
        )
        subjective = ["acute severe symptoms", "patient requires urgent safety-focused evaluation"]
        objective = ["clinical instability or severe toxicity signal is present"]
        labs = f"Safety labs show severe abnormality or urgent concern related to {therapy['toxicity']}."
        imaging = "Imaging is not the immediate driver of the decision at this visit."
        toxicity = f"Emergency-level {therapy['toxicity']} or acute complication is present."

    else:
        raise ValueError(f"Unknown action: {action}")

    critical_missing = missing_evidence_for_status(status)
    available_evidence = available_evidence_for_status(status)

    return {
        "visit_id": row["visit_id"],
        "visit_index": int(visit_number),
        "timepoint_label": f"Visit {visit_number}: {pattern.replace('_', ' ')}",
        "clinical_input": {
            "summary": summary,
            "subjective_findings": subjective,
            "objective_findings": objective,
            "vitals_or_instability": ["stable unless emergency toxicity is specified"] if action != "emergency_toxicity_management" else ["urgent instability or severe toxicity concern"],
            "laboratory_findings": [labs],
            "imaging_findings": [imaging],
            "toxicity_findings": [toxicity],
            "complication_findings": [] if action != "emergency_toxicity_management" else ["acute complication requiring urgent management"],
            "free_text_note": f"Designed to test {row['dominant_failure_mode']} in {row['trajectory_pattern']}.",
        },
        "available_evidence": available_evidence,
        "critical_missing_evidence": critical_missing,
        "narrative_pressures": [],
        "discordance_present": action in {"hold_therapy", "switch_therapy"} and pattern in {
            "toxicity_hold_then_rechallenge_or_resolution",
            "progression_or_emergency_escalation",
        },
        "missingness": {
            "critical_data_missing": bool(critical_missing),
            "missing_categories": critical_missing,
            "delayed_expected_data": critical_missing,
            "contradictory_evidence_present": action in {"hold_therapy", "switch_therapy"},
        },
        "labels": {
            "cancer_state": cancer_state_from_status(status),
            "patient_state": patient_state_from_status(status),
            "evidence_state": evidence_state_from_status(status),
            "evidence_status_stage_adjusted": status,
            "evidence_sufficient_for_action": status != "unresolved_needs_more_evidence",
            "authorized_action": action,
            "authorization_criteria_matched": ACTION_RATIONALES[action],
            "authorization_rationale": ACTION_RATIONALES[action],
            "dominant_failure_mode": row["dominant_failure_mode"],
            "reversibility_trigger_present": status == "unresolved_needs_more_evidence",
        }
    }

def make_trajectory(traj_row, visit_rows):
    cancer = CANCER_CONTEXTS[traj_row["cancer_type"]]
    therapy = THERAPY_CONTEXTS[traj_row["therapy_class"]]

    visits = []
    for _, vrow in visit_rows.sort_values("visit_number").iterrows():
        visits.append(make_visit(vrow, int(vrow["visit_number"])))

    trajectory = {
        "trajectory_id": traj_row["trajectory_id"],
        "schema_version": "v0.41",
        "case_source": {
            "source_type": "synthetic",
            "source_reference": "v0.40 design matrix",
            "notes": "Generated from locked v0.40 OncoGuard-Response design matrix.",
        },
        "trajectory_title": (
            f"{cancer['cancer_type_full']} on {therapy['therapy_label']}: "
            f"{traj_row['trajectory_pattern'].replace('_', ' ')}"
        ),
        "cancer_context": {
            "cancer_type": cancer["cancer_type_full"],
            "subtype": cancer["subtype"],
            "stage": cancer["stage"],
            "disease_setting": "metastatic/advanced disease on active systemic therapy",
            "biomarker_context": cancer["common_biomarkers"],
        },
        "treatment_context": {
            "current_regimen": therapy["regimen"],
            "therapy_class": traj_row["therapy_class"],
            "therapy_class_label": therapy["therapy_label"],
            "line_of_therapy": "active systemic therapy",
            "treatment_intent": "disease_control",
        },
        "trajectory_metadata": {
            "design_version": "v0.40",
            "generation_version": "v0.41",
            "pattern_id": traj_row["pattern_id"],
            "trajectory_pattern": traj_row["trajectory_pattern"],
            "p4_variant": "" if pd.isna(traj_row["p4_variant"]) else traj_row["p4_variant"],
            "dominant_failure_mode": traj_row["dominant_failure_mode"],
            "authorization_dependency": traj_row["authorization_dependency"],
            "action_path": traj_row["action_path"],
            "evidence_status_path": traj_row["evidence_status_path"],
        },
        "visits": visits,
    }

    return trajectory

# ------------------------------------------------------------
# Generate trajectories
# ------------------------------------------------------------

trajectory_records = []
visit_records = []

for _, traj_row in traj_design.iterrows():
    tid = traj_row["trajectory_id"]
    rows = visit_design[visit_design["trajectory_id"] == tid].copy()

    if len(rows) != 3:
        raise ValueError(f"{tid} has {len(rows)} visits, expected 3")

    trajectory = make_trajectory(traj_row, rows)

    out_path = OUT_TRAJ_DIR / f"{tid}.json"
    with open(out_path, "w") as f:
        json.dump(trajectory, f, indent=2)

    trajectory_records.append({
        "trajectory_id": tid,
        "file_path": str(out_path.relative_to(BASE)),
        "cancer_type": traj_row["cancer_type"],
        "therapy_class": traj_row["therapy_class"],
        "trajectory_pattern": traj_row["trajectory_pattern"],
        "p4_variant": "" if pd.isna(traj_row["p4_variant"]) else traj_row["p4_variant"],
        "dominant_failure_mode": traj_row["dominant_failure_mode"],
        "n_visits": 3,
        "action_path": traj_row["action_path"],
        "evidence_status_path": traj_row["evidence_status_path"],
    })

    for visit in trajectory["visits"]:
        visit_records.append({
            "trajectory_id": tid,
            "visit_id": visit["visit_id"],
            "visit_index": visit["visit_index"],
            "expected_action": visit["labels"]["authorized_action"],
            "evidence_status_stage_adjusted": visit["labels"]["evidence_status_stage_adjusted"],
            "cancer_type": traj_row["cancer_type"],
            "therapy_class": traj_row["therapy_class"],
            "trajectory_pattern": traj_row["trajectory_pattern"],
            "dominant_failure_mode": traj_row["dominant_failure_mode"],
        })

trajectory_inventory = pd.DataFrame(trajectory_records)
visit_inventory = pd.DataFrame(visit_records)

trajectory_inventory.to_csv(OUT_RESULTS / "v0_41_trajectory_inventory.csv", index=False)
visit_inventory.to_csv(OUT_RESULTS / "v0_41_visit_level_inventory.csv", index=False)

# ------------------------------------------------------------
# Summary outputs
# ------------------------------------------------------------

summary = pd.DataFrame([{
    "generation_version": "v0.41",
    "source_design_version": "v0.40",
    "n_trajectories": len(trajectory_inventory),
    "n_visits": len(visit_inventory),
    "n_json_files": len(list(OUT_TRAJ_DIR.glob("*.json"))),
    "n_cancer_types": trajectory_inventory["cancer_type"].nunique(),
    "n_therapy_classes": trajectory_inventory["therapy_class"].nunique(),
    "n_patterns": trajectory_inventory["trajectory_pattern"].nunique(),
}])

summary.to_csv(OUT_RESULTS / "v0_41_generation_summary.csv", index=False)

action_counts = visit_inventory["expected_action"].value_counts().rename_axis("expected_action").reset_index(name="count")
action_counts["percent"] = (100 * action_counts["count"] / len(visit_inventory)).round(1)
action_counts.to_csv(OUT_RESULTS / "v0_41_expected_action_distribution.csv", index=False)

status_counts = visit_inventory["evidence_status_stage_adjusted"].value_counts().rename_axis("evidence_status_stage_adjusted").reset_index(name="count")
status_counts["percent"] = (100 * status_counts["count"] / len(visit_inventory)).round(1)
status_counts.to_csv(OUT_RESULTS / "v0_41_evidence_status_distribution.csv", index=False)

card = f"""# OncoGuard-Response v0.41 Case Generation Card

## Purpose

v0.41 generates synthetic oncology trajectory JSON files from the locked v0.40 expanded benchmark design matrix.

## Source design

- Source: v0.40 design matrix
- Design: 100 trajectories × 3 visits
- Visit-level decisions: 300

## Generated artifacts

- JSON trajectory directory: `data/trajectories/v0_41_expanded_300visit/`
- Trajectory inventory: `results/v0_41_case_generation/v0_41_trajectory_inventory.csv`
- Visit-level inventory: `results/v0_41_case_generation/v0_41_visit_level_inventory.csv`

## Summary

{summary.to_markdown(index=False)}

## Expected action distribution

{action_counts.to_markdown(index=False)}

## Evidence-status distribution

{status_counts.to_markdown(index=False)}

## Notes

These cases are synthetic and are intended for benchmark/controller evaluation, not clinical decision-making. The cases preserve the locked v0.40 design matrix and generate structured longitudinal oncology visits with labels for therapeutic authorization.
"""
(OUT_RESULTS / "v0_41_case_generation_card.md").write_text(card)

print("Saved JSON trajectories:", OUT_TRAJ_DIR)
print("Saved results:", OUT_RESULTS)

print("\nSummary:")
print(summary.to_string(index=False))

print("\nExpected action distribution:")
print(action_counts.to_string(index=False))

print("\nEvidence status distribution:")
print(status_counts.to_string(index=False))
