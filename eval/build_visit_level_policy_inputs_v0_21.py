
from pathlib import Path
import pandas as pd

BASE = Path("/content/drive/MyDrive/oncoguard-response")

V020_RESULTS = BASE / "results" / "freeze_v0_20_pilot"
V021_RESULTS = BASE / "results" / "v0_21_multi_policy"
V021_RESULTS.mkdir(parents=True, exist_ok=True)

inventory_path = V020_RESULTS / "trajectory_inventory_v0_20.csv"
inventory = pd.read_csv(inventory_path)

rows = []

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

for _, row in inventory.iterrows():
    actions = [a.strip() for a in str(row["action_path"]).split("->")]

    for i, action in enumerate(actions, start=1):
        rows.append({
            "trajectory_id": row["trajectory_id"],
            "title": row["title"],
            "visit_number": i,
            "expected_action": action,
            "failure_being_tested": row["failure_being_tested"],
            "authorization_dependency": row["authorization_dependency"],
            "evidence_state_inferred": infer_evidence_state(
                row["failure_being_tested"],
                row["authorization_dependency"]
            ),
        })

visit_level = pd.DataFrame(rows)

out = V021_RESULTS / "visit_level_policy_inputs_v0_21.csv"
visit_level.to_csv(out, index=False)

print("Input trajectories:", inventory.shape)
print("Visit-level rows:", visit_level.shape)
print(f"Saved: {out}")

print("\nExpected action counts:")
print(visit_level["expected_action"].value_counts())

print("\nInferred evidence-state counts:")
print(visit_level["evidence_state_inferred"].value_counts())
