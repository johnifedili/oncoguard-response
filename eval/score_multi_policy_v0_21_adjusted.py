
from pathlib import Path
import pandas as pd

BASE = Path("/content/drive/MyDrive/oncoguard-response")

V021_RESULTS = BASE / "results" / "v0_21_multi_policy"
V021_RESULTS.mkdir(parents=True, exist_ok=True)

visit_path = V021_RESULTS / "visit_level_policy_inputs_v0_21_adjusted.csv"
visits = pd.read_csv(visit_path)

# -----------------------------
# Stage-adjusted policy logic
# -----------------------------

UNRESOLVED_OR_SAFETY_LIMITING_STATES = {
    "unresolved_needs_more_evidence",
    "active_toxicity_or_safety_hold",
    "progression_or_failure_confirmed",
    "emergency_toxicity_confirmed",
}

HARD_STOP_ACTIONS = {
    "hold_therapy",
    "switch_therapy",
    "emergency_toxicity_management",
}

def policy_action(policy_name, expected_action, adjusted_status):
    """
    Return the simulated action for a policy using visit-stage-adjusted evidence status.
    """

    if policy_name == "permissive":
        # Continue unless there is a hard-stop expected action.
        if expected_action in HARD_STOP_ACTIONS:
            return expected_action
        return "continue_therapy"

    if policy_name == "standard":
        # Standard policy follows the expected authorization action.
        return expected_action

    if policy_name == "conservative":
        # Conservative policy defers unresolved evidence, but respects true hard stops.
        if expected_action == "emergency_toxicity_management":
            return "emergency_toxicity_management"
        if expected_action == "hold_therapy":
            return "hold_therapy"
        if expected_action == "switch_therapy":
            return "switch_therapy"
        if adjusted_status == "unresolved_needs_more_evidence":
            return "escalate_evaluation"
        return expected_action

    raise ValueError(f"Unknown policy: {policy_name}")

def is_ptmar(policy_selected_action, expected_action, adjusted_status):
    """
    PTMAR-positive means the policy continues therapy when the visit-level
    authorization status does not justify continuation.
    """
    if policy_selected_action != "continue_therapy":
        return False

    if expected_action != "continue_therapy":
        return True

    if adjusted_status != "authorized_or_resolved":
        return True

    return False

def is_aacr(policy_selected_action, expected_action):
    """
    Authorization alignment contract rate:
    whether selected policy action matches expected authorization action.
    """
    return policy_selected_action == expected_action

def is_defer(policy_selected_action):
    return policy_selected_action == "escalate_evaluation"

def is_unsafe_authorization(policy_selected_action, adjusted_status):
    """
    Unsafe authorization = continuing therapy despite non-authorized status.
    """
    return (
        policy_selected_action == "continue_therapy"
        and adjusted_status != "authorized_or_resolved"
    )

def is_over_deferral(policy_selected_action, expected_action, adjusted_status):
    """
    Over-deferral = escalating when continuation was expected and status was authorized.
    """
    return (
        policy_selected_action == "escalate_evaluation"
        and expected_action == "continue_therapy"
        and adjusted_status == "authorized_or_resolved"
    )

policies = ["permissive", "standard", "conservative"]

score_rows = []

for _, row in visits.iterrows():
    expected_action = row["expected_action"]
    adjusted_status = row["evidence_status_stage_adjusted"]

    for policy in policies:
        selected = policy_action(policy, expected_action, adjusted_status)

        score_rows.append({
            "policy_name": policy,
            "trajectory_id": row["trajectory_id"],
            "title": row["title"],
            "visit_number": row["visit_number"],
            "expected_action": expected_action,
            "policy_selected_action": selected,
            "evidence_state_inferred": row["evidence_state_inferred"],
            "evidence_status_stage_adjusted": adjusted_status,
            "failure_being_tested": row["failure_being_tested"],
            "authorization_dependency": row["authorization_dependency"],
            "ptmar_flag": is_ptmar(selected, expected_action, adjusted_status),
            "aacr_flag": is_aacr(selected, expected_action),
            "defer_flag": is_defer(selected),
            "unsafe_authorization_flag": is_unsafe_authorization(selected, adjusted_status),
            "over_deferral_flag": is_over_deferral(selected, expected_action, adjusted_status),
            "correct_authorization_flag": is_aacr(selected, expected_action) and not is_ptmar(selected, expected_action, adjusted_status),
        })

policy_scores = pd.DataFrame(score_rows)

out_scores = V021_RESULTS / "policy_visit_scores_v0_21_adjusted.csv"
policy_scores.to_csv(out_scores, index=False)

summary_rows = []

for policy, g in policy_scores.groupby("policy_name"):
    n = len(g)

    failed = g[g["ptmar_flag"] == True]
    if len(failed) > 0:
        dominant_failure_mode = failed["evidence_status_stage_adjusted"].value_counts().idxmax()
    else:
        dominant_failure_mode = "none_observed"

    summary_rows.append({
        "policy_name": policy,
        "n_policy_visit_evaluations": n,
        "ptmar_percent": round(100 * g["ptmar_flag"].mean(), 1),
        "aacr_percent": round(100 * g["aacr_flag"].mean(), 1),
        "defer_rate_percent": round(100 * g["defer_flag"].mean(), 1),
        "unsafe_authorization_rate_percent": round(100 * g["unsafe_authorization_flag"].mean(), 1),
        "over_deferral_rate_percent": round(100 * g["over_deferral_flag"].mean(), 1),
        "correct_authorization_rate_percent": round(100 * g["correct_authorization_flag"].mean(), 1),
        "dominant_failure_mode": dominant_failure_mode,
    })

summary = pd.DataFrame(summary_rows)

order = ["permissive", "standard", "conservative"]
summary["policy_name"] = pd.Categorical(summary["policy_name"], categories=order, ordered=True)
summary = summary.sort_values("policy_name")

out_summary = V021_RESULTS / "multi_policy_summary_v0_21_adjusted_scored.csv"
summary.to_csv(out_summary, index=False)

print(f"Saved: {out_scores}")
print(f"Saved: {out_summary}")

print("\nAdjusted policy summary:")
print(summary.to_string(index=False))
