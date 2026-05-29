
from pathlib import Path
import pandas as pd

BASE = Path("/content/drive/MyDrive/oncoguard-response")

V021_RESULTS = BASE / "results" / "v0_21_multi_policy"
V021_RESULTS.mkdir(parents=True, exist_ok=True)

input_path = V021_RESULTS / "visit_level_policy_inputs_v0_21.csv"
visits = pd.read_csv(input_path)

def infer_stage_adjusted_status(expected_action, original_evidence_state):
    """
    Convert trajectory-level evidence-state labels into visit-stage-adjusted
    evidence status using the expected action path.

    This prevents late authorized continuation visits from being falsely
    labeled as unresolved just because the overall trajectory tested
    missing evidence or toxicity.
    """

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

    return original_evidence_state

visits["evidence_status_stage_adjusted"] = visits.apply(
    lambda r: infer_stage_adjusted_status(
        r["expected_action"],
        r["evidence_state_inferred"]
    ),
    axis=1
)

out = V021_RESULTS / "visit_level_policy_inputs_v0_21_adjusted.csv"
visits.to_csv(out, index=False)

print("Saved:", out)
print("\nAdjusted evidence status counts:")
print(visits["evidence_status_stage_adjusted"].value_counts())

print("\nCross-tab: expected_action x adjusted evidence status")
print(pd.crosstab(visits["expected_action"], visits["evidence_status_stage_adjusted"]))
