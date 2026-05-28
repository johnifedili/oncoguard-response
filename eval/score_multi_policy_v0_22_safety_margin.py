
from pathlib import Path
import pandas as pd

BASE = Path("/content/drive/MyDrive/oncoguard-response")

V021_RESULTS = BASE / "results" / "v0_21_multi_policy"
V022_RESULTS = BASE / "results" / "v0_22_safety_margin_policy"
V022_RESULTS.mkdir(parents=True, exist_ok=True)

visit_path = V021_RESULTS / "visit_level_policy_inputs_v0_21_adjusted.csv"
visits = pd.read_csv(visit_path)

# Sort visits so previous-visit logic is correct
visits = visits.sort_values(["trajectory_id", "visit_number"]).copy()

# Add previous expected action within each trajectory
visits["previous_expected_action"] = (
    visits.groupby("trajectory_id")["expected_action"]
    .shift(1)
    .fillna("none_first_visit")
)

# -----------------------------
# v0.22 policy logic
# -----------------------------
# The v0.22 conservative policy adds a safety-margin rule:
# if a visit recommends continuation immediately after a non-continuation visit,
# conservative policy requires one additional reassessment/escalation.

HARD_STOP_ACTIONS = {
    "hold_therapy",
    "switch_therapy",
    "emergency_toxicity_management",
}

def policy_action(policy_name, expected_action, adjusted_status, previous_expected_action):
    """
    Return simulated action for each policy.
    """

    if policy_name == "permissive":
        # Continue unless there is an explicit hard stop.
        if expected_action in HARD_STOP_ACTIONS:
            return expected_action
        return "continue_therapy"

    if policy_name == "standard":
        # Follow the expected authorization action.
        return expected_action

    if policy_name == "conservative_margin":
        # Respect true hard stops.
        if expected_action in HARD_STOP_ACTIONS:
            return expected_action

        # Safety-margin rule:
        # If continuation follows a prior non-continuation visit,
        # require one extra reassessment before continuing.
        if (
            expected_action == "continue_therapy"
            and previous_expected_action != "continue_therapy"
            and previous_expected_action != "none_first_visit"
        ):
            return "escalate_evaluation"

        # Defer unresolved evidence.
        if adjusted_status == "unresolved_needs_more_evidence":
            return "escalate_evaluation"

        return expected_action

    raise ValueError(f"Unknown policy: {policy_name}")

def is_ptmar(policy_selected_action, expected_action, adjusted_status):
    """
    PTMAR-positive means continuing therapy when continuation is not authorized.
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
    AACR: selected policy action matches expected authorization path.
    """
    return policy_selected_action == expected_action

def is_defer(policy_selected_action):
    return policy_selected_action == "escalate_evaluation"

def is_unsafe_authorization(policy_selected_action, adjusted_status):
    """
    Unsafe authorization = continuation despite non-authorized status.
    """
    return (
        policy_selected_action == "continue_therapy"
        and adjusted_status != "authorized_or_resolved"
    )

def is_over_deferral(policy_selected_action, expected_action, adjusted_status):
    """
    Over-deferral = deferring when expected action was continuation
    and the visit-level status was authorized/resolved.
    """
    return (
        policy_selected_action == "escalate_evaluation"
        and expected_action == "continue_therapy"
        and adjusted_status == "authorized_or_resolved"
    )

def classify_conservative_margin_trigger(expected_action, previous_expected_action, policy_selected_action):
    if (
        expected_action == "continue_therapy"
        and previous_expected_action != "continue_therapy"
        and previous_expected_action != "none_first_visit"
        and policy_selected_action == "escalate_evaluation"
    ):
        return "post_noncontinuation_safety_margin"
    return "none"

policies = ["permissive", "standard", "conservative_margin"]

score_rows = []

for _, row in visits.iterrows():
    expected_action = row["expected_action"]
    adjusted_status = row["evidence_status_stage_adjusted"]
    previous_expected_action = row["previous_expected_action"]

    for policy in policies:
        selected = policy_action(
            policy,
            expected_action,
            adjusted_status,
            previous_expected_action
        )

        score_rows.append({
            "policy_name": policy,
            "trajectory_id": row["trajectory_id"],
            "title": row["title"],
            "visit_number": row["visit_number"],
            "previous_expected_action": previous_expected_action,
            "expected_action": expected_action,
            "policy_selected_action": selected,
            "evidence_state_inferred": row["evidence_state_inferred"],
            "evidence_status_stage_adjusted": adjusted_status,
            "failure_being_tested": row["failure_being_tested"],
            "authorization_dependency": row["authorization_dependency"],
            "conservative_margin_trigger": classify_conservative_margin_trigger(
                expected_action,
                previous_expected_action,
                selected
            ),
            "ptmar_flag": is_ptmar(selected, expected_action, adjusted_status),
            "aacr_flag": is_aacr(selected, expected_action),
            "defer_flag": is_defer(selected),
            "unsafe_authorization_flag": is_unsafe_authorization(selected, adjusted_status),
            "over_deferral_flag": is_over_deferral(selected, expected_action, adjusted_status),
            "correct_authorization_flag": is_aacr(selected, expected_action) and not is_ptmar(selected, expected_action, adjusted_status),
        })

policy_scores = pd.DataFrame(score_rows)

out_scores = V022_RESULTS / "policy_visit_scores_v0_22_safety_margin.csv"
policy_scores.to_csv(out_scores, index=False)

summary_rows = []

for policy, g in policy_scores.groupby("policy_name"):
    failed = g[g["ptmar_flag"] == True]

    if len(failed) > 0:
        dominant_failure_mode = failed["evidence_status_stage_adjusted"].value_counts().idxmax()
    else:
        dominant_failure_mode = "none_observed"

    margin_triggers = int((g["conservative_margin_trigger"] == "post_noncontinuation_safety_margin").sum())

    summary_rows.append({
        "policy_name": policy,
        "n_policy_visit_evaluations": len(g),
        "ptmar_percent": round(100 * g["ptmar_flag"].mean(), 1),
        "aacr_percent": round(100 * g["aacr_flag"].mean(), 1),
        "defer_rate_percent": round(100 * g["defer_flag"].mean(), 1),
        "unsafe_authorization_rate_percent": round(100 * g["unsafe_authorization_flag"].mean(), 1),
        "over_deferral_rate_percent": round(100 * g["over_deferral_flag"].mean(), 1),
        "correct_authorization_rate_percent": round(100 * g["correct_authorization_flag"].mean(), 1),
        "safety_margin_trigger_count": margin_triggers,
        "dominant_failure_mode": dominant_failure_mode,
    })

summary = pd.DataFrame(summary_rows)

order = ["permissive", "standard", "conservative_margin"]
summary["policy_name"] = pd.Categorical(summary["policy_name"], categories=order, ordered=True)
summary = summary.sort_values("policy_name")

out_summary = V022_RESULTS / "multi_policy_summary_v0_22_safety_margin.csv"
summary.to_csv(out_summary, index=False)

# Save trigger audit
trigger_audit = policy_scores[
    policy_scores["conservative_margin_trigger"] == "post_noncontinuation_safety_margin"
].copy()

trigger_out = V022_RESULTS / "conservative_margin_trigger_audit_v0_22.csv"
trigger_audit.to_csv(trigger_out, index=False)

print(f"Saved: {out_scores}")
print(f"Saved: {out_summary}")
print(f"Saved: {trigger_out}")

print("\nv0.22 safety-margin policy summary:")
print(summary.to_string(index=False))

print("\nConservative safety-margin trigger count:")
print(len(trigger_audit))
