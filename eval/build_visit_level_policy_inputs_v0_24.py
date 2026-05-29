
from pathlib import Path
import pandas as pd

BASE = Path("/content/drive/MyDrive/oncoguard-response")

V024 = BASE / "results" / "v0_24_clean_20trajectory_benchmark"
inventory_path = V024 / "trajectory_inventory_v0_24.csv"

inventory = pd.read_csv(inventory_path)

def infer_evidence_state(failure_text, authorization_dependency):
    text = f"{failure_text} {authorization_dependency}".lower()

    if "contradictory" in text:
        return "contradictory_evidence"
    if "missing" in text or "laboratory" in text or "lab" in text:
        return "missing_critical_evidence"
    if "toxicity" in text or "organ function" in text or "safety" in text:
        return "incomplete_toxicity_assessment"
    if "pressure" in text or "hope" in text or "urgency" in text or "family" in text:
        return "narrative_pressure"
    if "benefit" in text or "response" in text:
        return "benefit_overauthorization_risk"

    return "other_authorization_dependency"

def infer_stage_adjusted_status(expected_action):
    if expected_action == "continue_therapy":
        return "authorized_or_resolved"
    if expected_action == "escalate_evaluation":
        return "unresolved_needs_more_evidence"
    if expected_action == "hold_therapy":
        return "active_toxicity_or_safety_hold"
    if expected_action == "switch_therapy":
        return "progression_or_failure_confirmed"
    if expected_action == "emergency_toxicity_management":
        return "emergency_toxicity_confirmed"
    return "other"

rows = []

for _, row in inventory.iterrows():
    actions = [a.strip() for a in str(row["action_path"]).split("->")]

    for i, action in enumerate(actions, start=1):
        evidence_state = infer_evidence_state(
            row["failure_being_tested"],
            row["authorization_dependency"]
        )

        rows.append({
            "trajectory_id": row["trajectory_id"],
            "title": row["title"],
            "visit_number": i,
            "expected_action": action,
            "failure_being_tested": row["failure_being_tested"],
            "authorization_dependency": row["authorization_dependency"],
            "evidence_state_inferred": evidence_state,
            "evidence_status_stage_adjusted": infer_stage_adjusted_status(action),
            "source_json": row["source_json"],
        })

visits = pd.DataFrame(rows)

out = V024 / "visit_level_policy_inputs_v0_24_adjusted.csv"
visits.to_csv(out, index=False)

print("Visit rows:", len(visits))
print("Unique trajectories:", visits["trajectory_id"].nunique())
print(f"Saved: {out}")

print("\nExpected action counts:")
print(visits["expected_action"].value_counts())

print("\nStage-adjusted status counts:")
print(visits["evidence_status_stage_adjusted"].value_counts())
