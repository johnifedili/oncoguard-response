
from pathlib import Path
import json
import hashlib
import pandas as pd

BASE = Path("/content/oncoguard-response")

DESIGN_DIR = BASE / "results" / "v0_40_expansion_plan"
GEN_DIR = BASE / "results" / "v0_41_case_generation"
TRAJ_DIR = BASE / "data" / "trajectories" / "v0_41_expanded_300visit"

OUTDIR = BASE / "results" / "v0_42_integrity_audit"
OUTDIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Input files
# -----------------------------
design_traj_path = DESIGN_DIR / "v0_40_trajectory_design_matrix.csv"
design_visit_path = DESIGN_DIR / "v0_40_visit_level_design_matrix.csv"

gen_traj_inv_path = GEN_DIR / "v0_41_trajectory_inventory.csv"
gen_visit_inv_path = GEN_DIR / "v0_41_visit_level_inventory.csv"

required_inputs = [
    design_traj_path,
    design_visit_path,
    gen_traj_inv_path,
    gen_visit_inv_path,
]

missing_inputs = [str(p) for p in required_inputs if not p.exists()]
if missing_inputs:
    raise FileNotFoundError(f"Missing required input files: {missing_inputs}")

design_traj = pd.read_csv(design_traj_path)
design_visits = pd.read_csv(design_visit_path)
gen_traj = pd.read_csv(gen_traj_inv_path)
gen_visits = pd.read_csv(gen_visit_inv_path)

json_files = sorted(TRAJ_DIR.glob("*.json"))

# -----------------------------
# Expected labels
# -----------------------------
EXPECTED_ACTIONS = {
    "continue_therapy",
    "escalate_evaluation",
    "hold_therapy",
    "switch_therapy",
    "emergency_toxicity_management",
}

EXPECTED_STATUSES = {
    "authorized_or_resolved",
    "unresolved_needs_more_evidence",
    "active_toxicity_or_safety_hold",
    "progression_or_failure_confirmed",
    "emergency_toxicity_confirmed",
}

REQUIRED_TOP_LEVEL_KEYS = {
    "trajectory_id",
    "schema_version",
    "case_source",
    "trajectory_title",
    "cancer_context",
    "treatment_context",
    "trajectory_metadata",
    "visits",
}

REQUIRED_VISIT_KEYS = {
    "visit_id",
    "visit_index",
    "clinical_input",
    "available_evidence",
    "critical_missing_evidence",
    "labels",
}

REQUIRED_LABEL_KEYS = {
    "authorized_action",
    "evidence_status_stage_adjusted",
    "evidence_sufficient_for_action",
    "cancer_state",
    "patient_state",
    "evidence_state",
    "authorization_rationale",
    "dominant_failure_mode",
}

# -----------------------------
# SHA256 helper
# -----------------------------
def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

# -----------------------------
# JSON validation
# -----------------------------
errors = []
json_records = []
visit_records_from_json = []

for path in json_files:
    try:
        with open(path) as f:
            obj = json.load(f)
    except Exception as e:
        errors.append({
            "file": path.name,
            "error_type": "json_parse_error",
            "details": str(e),
        })
        continue

    top_missing = REQUIRED_TOP_LEVEL_KEYS - set(obj.keys())
    if top_missing:
        errors.append({
            "file": path.name,
            "error_type": "missing_top_level_keys",
            "details": ",".join(sorted(top_missing)),
        })

    tid = obj.get("trajectory_id")
    visits = obj.get("visits", [])

    if not isinstance(visits, list):
        errors.append({
            "file": path.name,
            "error_type": "visits_not_list",
            "details": type(visits).__name__,
        })
        visits = []

    if len(visits) != 3:
        errors.append({
            "file": path.name,
            "error_type": "wrong_visit_count",
            "details": str(len(visits)),
        })

    json_records.append({
        "trajectory_id": tid,
        "filename": path.name,
        "relative_path": str(path.relative_to(BASE)),
        "schema_version": obj.get("schema_version"),
        "n_visits": len(visits),
        "sha256": sha256_file(path),
    })

    for visit in visits:
        if not isinstance(visit, dict):
            errors.append({
                "file": path.name,
                "error_type": "visit_not_dict",
                "details": str(type(visit)),
            })
            continue

        missing_visit_keys = REQUIRED_VISIT_KEYS - set(visit.keys())
        if missing_visit_keys:
            errors.append({
                "file": path.name,
                "error_type": "missing_visit_keys",
                "details": ",".join(sorted(missing_visit_keys)),
            })

        labels = visit.get("labels", {})
        if not isinstance(labels, dict):
            errors.append({
                "file": path.name,
                "error_type": "labels_not_dict",
                "details": str(type(labels)),
            })
            labels = {}

        missing_label_keys = REQUIRED_LABEL_KEYS - set(labels.keys())
        if missing_label_keys:
            errors.append({
                "file": path.name,
                "error_type": "missing_label_keys",
                "details": ",".join(sorted(missing_label_keys)),
            })

        action = labels.get("authorized_action")
        status = labels.get("evidence_status_stage_adjusted")

        if action not in EXPECTED_ACTIONS:
            errors.append({
                "file": path.name,
                "error_type": "invalid_authorized_action",
                "details": str(action),
            })

        if status not in EXPECTED_STATUSES:
            errors.append({
                "file": path.name,
                "error_type": "invalid_evidence_status",
                "details": str(status),
            })

        visit_records_from_json.append({
            "trajectory_id": tid,
            "visit_id": visit.get("visit_id"),
            "visit_index": visit.get("visit_index"),
            "authorized_action": action,
            "evidence_status_stage_adjusted": status,
            "schema_version": obj.get("schema_version"),
            "source_file": path.name,
        })

json_manifest = pd.DataFrame(json_records)
json_visit_df = pd.DataFrame(visit_records_from_json)
error_df = pd.DataFrame(errors)

# -----------------------------
# Crosswalk checks: design vs generated inventories
# -----------------------------
# Use visit_index-normalized crosswalk only.
# Because generated inventory uses visit_index, not visit_number, rebuild safer crosswalk.
design_for_cross = design_visits[[
    "trajectory_id",
    "visit_id",
    "visit_number",
    "expected_action",
    "evidence_status_stage_adjusted",
]].copy()

gen_for_cross = gen_visits[[
    "trajectory_id",
    "visit_id",
    "visit_index",
    "expected_action",
    "evidence_status_stage_adjusted",
]].copy()

design_for_cross = design_for_cross.rename(columns={
    "visit_number": "visit_index",
    "expected_action": "design_expected_action",
    "evidence_status_stage_adjusted": "design_evidence_status",
})

gen_for_cross = gen_for_cross.rename(columns={
    "expected_action": "generated_expected_action",
    "evidence_status_stage_adjusted": "generated_evidence_status",
})

crosswalk = design_for_cross.merge(
    gen_for_cross,
    on=["trajectory_id", "visit_id", "visit_index"],
    how="outer",
    indicator=True
)

crosswalk["action_match"] = crosswalk["design_expected_action"] == crosswalk["generated_expected_action"]
crosswalk["status_match"] = crosswalk["design_evidence_status"] == crosswalk["generated_evidence_status"]

mismatch = crosswalk[
    (crosswalk["_merge"] != "both") |
    (~crosswalk["action_match"]) |
    (~crosswalk["status_match"])
].copy()

# JSON visits vs design
json_for_cross = json_visit_df.rename(columns={
    "authorized_action": "json_authorized_action",
    "evidence_status_stage_adjusted": "json_evidence_status",
})

json_crosswalk = design_for_cross.merge(
    json_for_cross[[
        "trajectory_id",
        "visit_id",
        "visit_index",
        "json_authorized_action",
        "json_evidence_status",
        "source_file",
    ]],
    on=["trajectory_id", "visit_id", "visit_index"],
    how="outer",
    indicator=True
)

json_crosswalk["action_match"] = json_crosswalk["design_expected_action"] == json_crosswalk["json_authorized_action"]
json_crosswalk["status_match"] = json_crosswalk["design_evidence_status"] == json_crosswalk["json_evidence_status"]

json_mismatch = json_crosswalk[
    (json_crosswalk["_merge"] != "both") |
    (~json_crosswalk["action_match"]) |
    (~json_crosswalk["status_match"])
].copy()

# -----------------------------
# Distributions
# -----------------------------
action_counts = (
    gen_visits["expected_action"]
    .value_counts()
    .rename_axis("expected_action")
    .reset_index(name="count")
)
action_counts["percent"] = (100 * action_counts["count"] / len(gen_visits)).round(1)

status_counts = (
    gen_visits["evidence_status_stage_adjusted"]
    .value_counts()
    .rename_axis("evidence_status_stage_adjusted")
    .reset_index(name="count")
)
status_counts["percent"] = (100 * status_counts["count"] / len(gen_visits)).round(1)

pattern_counts = (
    gen_traj["trajectory_pattern"]
    .value_counts()
    .rename_axis("trajectory_pattern")
    .reset_index(name="count")
)

cancer_therapy_matrix = pd.crosstab(
    gen_traj["cancer_type"],
    gen_traj["therapy_class"]
)

# -----------------------------
# Summary
# -----------------------------
audit_passed = (
    len(json_files) == 100
    and len(design_traj) == 100
    and len(design_visits) == 300
    and len(gen_traj) == 100
    and len(gen_visits) == 300
    and gen_visits["trajectory_id"].nunique() == 100
    and len(error_df) == 0
    and len(mismatch) == 0
    and len(json_mismatch) == 0
    and set(gen_visits["expected_action"]) == EXPECTED_ACTIONS
    and set(gen_visits["evidence_status_stage_adjusted"]) == EXPECTED_STATUSES
)

summary = pd.DataFrame([{
    "audit_version": "v0.42",
    "source_design_version": "v0.40",
    "case_generation_version": "v0.41",
    "audit_passed": audit_passed,
    "n_design_trajectories": len(design_traj),
    "n_design_visits": len(design_visits),
    "n_generated_trajectories": len(gen_traj),
    "n_generated_visits": len(gen_visits),
    "n_json_files": len(json_files),
    "n_unique_trajectory_ids": gen_visits["trajectory_id"].nunique(),
    "n_json_schema_errors": len(error_df),
    "n_inventory_mismatches": len(mismatch),
    "n_json_design_mismatches": len(json_mismatch),
    "n_expected_actions": gen_visits["expected_action"].nunique(),
    "n_evidence_statuses": gen_visits["evidence_status_stage_adjusted"].nunique(),
}])

# -----------------------------
# Save outputs
# -----------------------------
summary.to_csv(OUTDIR / "v0_42_integrity_audit_summary.csv", index=False)
json_manifest.to_csv(OUTDIR / "v0_42_json_file_manifest.csv", index=False)
json_visit_df.to_csv(OUTDIR / "v0_42_json_visit_inventory.csv", index=False)
error_df.to_csv(OUTDIR / "v0_42_json_schema_errors.csv", index=False)
crosswalk.to_csv(OUTDIR / "v0_42_design_to_generated_inventory_crosswalk.csv", index=False)
mismatch.to_csv(OUTDIR / "v0_42_design_to_generated_inventory_mismatches.csv", index=False)
json_crosswalk.to_csv(OUTDIR / "v0_42_design_to_json_crosswalk.csv", index=False)
json_mismatch.to_csv(OUTDIR / "v0_42_design_to_json_mismatches.csv", index=False)
action_counts.to_csv(OUTDIR / "v0_42_expected_action_distribution.csv", index=False)
status_counts.to_csv(OUTDIR / "v0_42_evidence_status_distribution.csv", index=False)
pattern_counts.to_csv(OUTDIR / "v0_42_pattern_distribution.csv", index=False)
cancer_therapy_matrix.to_csv(OUTDIR / "v0_42_cancer_therapy_matrix.csv")

# Hash important CSV/MD inputs and outputs
artifact_paths = []
artifact_paths.extend(required_inputs)
artifact_paths.extend(sorted(TRAJ_DIR.glob("*.json")))
artifact_paths.extend(sorted(OUTDIR.glob("*.csv")))

artifact_manifest = pd.DataFrame([{
    "relative_path": str(p.relative_to(BASE)),
    "sha256": sha256_file(p),
    "size_bytes": p.stat().st_size,
} for p in artifact_paths if p.exists()])

artifact_manifest.to_csv(OUTDIR / "v0_42_artifact_sha256_manifest.csv", index=False)

benchmark_card = f"""# OncoGuard-Response v0.42 Expanded Benchmark Card

## Purpose

v0.42 audits the expanded OncoGuard-Response benchmark generated in v0.41 from the locked v0.40 design matrix.

## Version lineage

- v0.40: expanded benchmark design matrix
- v0.41: synthetic case generation from v0.40
- v0.42: integrity audit, benchmark card, and manifest

## Benchmark size

| Item | Count |
|---|---:|
| Design trajectories | {len(design_traj)} |
| Design visit-level decisions | {len(design_visits)} |
| Generated trajectories | {len(gen_traj)} |
| Generated visit-level decisions | {len(gen_visits)} |
| JSON trajectory files | {len(json_files)} |
| Unique trajectory IDs | {gen_visits["trajectory_id"].nunique()} |

## Audit status

| Check | Result |
|---|---:|
| Audit passed | {audit_passed} |
| JSON schema errors | {len(error_df)} |
| Design-to-generated inventory mismatches | {len(mismatch)} |
| Design-to-JSON mismatches | {len(json_mismatch)} |

## Expected action distribution

{action_counts.to_markdown(index=False)}

## Evidence-status distribution

{status_counts.to_markdown(index=False)}

## Trajectory pattern distribution

{pattern_counts.to_markdown(index=False)}

## Cancer × therapy matrix

{cancer_therapy_matrix.to_markdown()}

## Intended use

This expanded benchmark is intended for evaluating oncology therapeutic authorization behavior in large language models and for testing evidence-gated controller interventions. It is not intended for clinical decision-making.

## Key governance endpoints supported

- PTMAR
- unsafe authorization rate
- AACR
- over-deferral
- over-holding
- over-emergency management
- over-switching / premature switching
- wrong-channel escalation
- schema conformance
- controller-mediated action correction
- treatment-delay risk

## Notes

The benchmark intentionally includes a high proportion of continuation-authorized visits because the v0.30 four-model pilot identified under-continuation and over-deferral as dominant governance failure modes.
"""

(OUTDIR / "v0_42_expanded_benchmark_card.md").write_text(benchmark_card)

manifest_md = f"""# OncoGuard-Response v0.42 Manifest

## Lineage

- Source design: `results/v0_40_expansion_plan/`
- Case generation: `data/trajectories/v0_41_expanded_300visit/`
- Audit outputs: `results/v0_42_integrity_audit/`

## Primary files

- `v0_42_integrity_audit_summary.csv`
- `v0_42_json_file_manifest.csv`
- `v0_42_json_visit_inventory.csv`
- `v0_42_artifact_sha256_manifest.csv`
- `v0_42_expanded_benchmark_card.md`

## Audit result

Audit passed: **{audit_passed}**

## Commit guidance

This audit package should be committed and tagged as:

`v0.42-integrity-audit`
"""

(OUTDIR / "v0_42_manifest.md").write_text(manifest_md)

print("Saved v0.42 audit outputs to:", OUTDIR)
print("\nAudit summary:")
print(summary.to_string(index=False))

print("\nExpected actions:")
print(action_counts.to_string(index=False))

print("\nEvidence statuses:")
print(status_counts.to_string(index=False))

print("\nAudit passed:", audit_passed)

if not audit_passed:
    print("\nSchema errors:", len(error_df))
    print("Inventory mismatches:", len(mismatch))
    print("JSON/design mismatches:", len(json_mismatch))
