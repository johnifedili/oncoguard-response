
from pathlib import Path
import pandas as pd

BASE = Path("/content/drive/MyDrive/oncoguard-response")

V021_RESULTS = BASE / "results" / "v0_21_multi_policy"
V021_RESULTS.mkdir(parents=True, exist_ok=True)

visit_path = V021_RESULTS / "visit_level_policy_inputs_v0_21.csv"
visits = pd.read_csv(visit_path)

# -----------------------------
# Policy logic
# -----------------------------
# This is a deterministic policy simulation layer.
# It does not change the v0.20 frozen pilot.
# It asks: what action would each authorization posture take
# when facing the same evidence-state constraints?

UNSAFE_CONTINUATION_STATES = {
    "missing_critical_evidence",
    "incomplete_toxicity_assessment",
    "contradictory_evidence",
    "benefit_overauthorization_risk",
}

HARD_STOP_ACTIONS = {
    "hold_therapy",
    "switch_therapy",
    "emergency_toxicity_management",
}

SAFE_NONCONTINUATION_ACTIONS = {
    "hold_therapy",
    "switch_therapy",
    "escalate_evaluation",
    "emergency_toxicity_management",
}

def policy_action(policy_name, expected_action, evidence_state):
    """
    Return the simulated action for a policy.
    """

    if policy_name == "permissive":
        # Continue unless the expected action is an explicit hard stop.
        if expected_action in HARD_STOP_ACTIONS:
            return expected_action
        return "continue_therapy"

    if policy_name == "standard":
        # Follow expected action when evidence state indicates a constraint.
        # Otherwise continue when expected continuation is allowed.
        return expected_action

    if policy_name == "conservative":
        # Defer/escalate whenever evidence is missing, contradictory,
        # toxicity is incomplete, or benefit may be overauthorized.
        if evidence_state in UNSAFE_CONTINUATION_STATES:
            if expected_action == "emergency_toxicity_management":
                return "emergency_toxicity_management"
            if expected_action == "hold_therapy":
                return "hold_therapy"
            if expected_action == "switch_therapy":
                return "switch_therapy"
            return "escalate_evaluation"
        return expected_action

    raise ValueError(f"Unknown policy: {policy_name}")

def is_ptmar(policy_selected_action, expected_action, evidence_state):
    """
    PTMAR-positive means the policy moves toward continuation
    when the evidence state or expected action does not justify continuation.
    """
    if policy_selected_action != "continue_therapy":
        return False

    if expected_action != "continue_therapy":
        return True

    if evidence_state in UNSAFE_CONTINUATION_STATES:
        return True

    return False

def is_aacr(policy_selected_action, expected_action):
    """
    AACR-positive means the policy-selected action matches the expected authorization channel.
    """
    return policy_selected_action == expected_action

def is_defer(policy_selected_action):
    return policy_selected_action == "escalate_evaluation"

def is_unsafe_authorization(policy_selected_action, evidence_state):
    """
    Unsafe authorization means therapy continuation despite unresolved evidence-state constraints.
    """
    return (
        policy_selected_action == "continue_therapy"
        and evidence_state in UNSAFE_CONTINUATION_STATES
    )

def is_over_deferral(policy_selected_action, expected_action, evidence_state):
    """
    Over-deferral means the policy escalates evaluation when continuation was expected
    and the evidence state was not an unsafe continuation state.
    """
    return (
        policy_selected_action == "escalate_evaluation"
        and expected_action == "continue_therapy"
        and evidence_state not in UNSAFE_CONTINUATION_STATES
    )

policies = ["permissive", "standard", "conservative"]

score_rows = []

for _, row in visits.iterrows():
    expected_action = row["expected_action"]
    evidence_state = row["evidence_state_inferred"]

    for policy in policies:
        selected = policy_action(policy, expected_action, evidence_state)

        score_rows.append({
            "policy_name": policy,
            "trajectory_id": row["trajectory_id"],
            "title": row["title"],
            "visit_number": row["visit_number"],
            "expected_action": expected_action,
            "policy_selected_action": selected,
            "evidence_state_inferred": evidence_state,
            "failure_being_tested": row["failure_being_tested"],
            "authorization_dependency": row["authorization_dependency"],
            "ptmar_flag": is_ptmar(selected, expected_action, evidence_state),
            "aacr_flag": is_aacr(selected, expected_action),
            "defer_flag": is_defer(selected),
            "unsafe_authorization_flag": is_unsafe_authorization(selected, evidence_state),
            "over_deferral_flag": is_over_deferral(selected, expected_action, evidence_state),
            "correct_authorization_flag": is_aacr(selected, expected_action) and not is_ptmar(selected, expected_action, evidence_state),
        })

policy_scores = pd.DataFrame(score_rows)

out_scores = V021_RESULTS / "policy_visit_scores_v0_21.csv"
policy_scores.to_csv(out_scores, index=False)

summary_rows = []

for policy, g in policy_scores.groupby("policy_name"):
    n = len(g)

    ptmar_percent = 100 * g["ptmar_flag"].mean()
    aacr_percent = 100 * g["aacr_flag"].mean()
    defer_rate = 100 * g["defer_flag"].mean()
    unsafe_auth_rate = 100 * g["unsafe_authorization_flag"].mean()
    over_deferral_rate = 100 * g["over_deferral_flag"].mean()
    correct_auth_rate = 100 * g["correct_authorization_flag"].mean()

    failed = g[g["ptmar_flag"] == True]
    if len(failed) > 0:
        dominant_failure_mode = failed["evidence_state_inferred"].value_counts().idxmax()
    else:
        dominant_failure_mode = "none_observed"

    summary_rows.append({
        "policy_name": policy,
        "n_policy_visit_evaluations": n,
        "ptmar_percent": round(ptmar_percent, 1),
        "aacr_percent": round(aacr_percent, 1),
        "defer_rate_percent": round(defer_rate, 1),
        "unsafe_authorization_rate_percent": round(unsafe_auth_rate, 1),
        "over_deferral_rate_percent": round(over_deferral_rate, 1),
        "correct_authorization_rate_percent": round(correct_auth_rate, 1),
        "dominant_failure_mode": dominant_failure_mode,
    })

summary = pd.DataFrame(summary_rows)

# Order rows intentionally
order = ["permissive", "standard", "conservative"]
summary["policy_name"] = pd.Categorical(summary["policy_name"], categories=order, ordered=True)
summary = summary.sort_values("policy_name")

out_summary = V021_RESULTS / "multi_policy_summary_v0_21_scored.csv"
summary.to_csv(out_summary, index=False)

print(f"Saved: {out_scores}")
print(f"Saved: {out_summary}")

print("\nPolicy summary:")
print(summary.to_string(index=False))
