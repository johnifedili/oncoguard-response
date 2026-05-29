
from pathlib import Path
import pandas as pd

BASE = Path("/content/drive/MyDrive/oncoguard-response")
V021_RESULTS = BASE / "results" / "v0_21_multi_policy"

visit_path = V021_RESULTS / "visit_level_policy_inputs_v0_21.csv"
visits = pd.read_csv(visit_path)

UNSAFE_CONTINUATION_STATES = {
    "missing_critical_evidence",
    "incomplete_toxicity_assessment",
    "contradictory_evidence",
    "benefit_overauthorization_risk",
}

conflicts = visits[
    (visits["expected_action"] == "continue_therapy") &
    (visits["evidence_state_inferred"].isin(UNSAFE_CONTINUATION_STATES))
].copy()

conflicts["conflict_type"] = "continue_expected_despite_unresolved_evidence"

out = V021_RESULTS / "action_evidence_conflict_audit_v0_21.csv"
conflicts.to_csv(out, index=False)

summary = (
    conflicts["evidence_state_inferred"]
    .value_counts()
    .reset_index()
)
summary.columns = ["evidence_state_inferred", "conflict_count"]

summary_out = V021_RESULTS / "action_evidence_conflict_summary_v0_21.csv"
summary.to_csv(summary_out, index=False)

print("Total visits:", len(visits))
print("Conflict visits:", len(conflicts))
print("\nConflict summary:")
print(summary.to_string(index=False))

print(f"\nSaved: {out}")
print(f"Saved: {summary_out}")
