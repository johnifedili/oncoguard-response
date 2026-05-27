
import json
from pathlib import Path

DEFINITIVE_ACTIONS = {
    "continue_therapy",
    "hold_therapy",
    "switch_therapy",
    "emergency_toxicity_management",
}

def load_trajectories(traj_dir):
    traj_dir = Path(traj_dir)
    trajectories = []
    for path in sorted(traj_dir.glob("OGR_TRJ_*.json")):
        with open(path, "r") as f:
            trajectories.append(json.load(f))
    return trajectories

def iter_visits(trajectories):
    for traj in trajectories:
        for visit in traj.get("visits", []):
            labels = visit.get("labels", {})
            yield {
                "trajectory_id": traj.get("trajectory_id"),
                "visit_index": visit.get("visit_index"),
                "visit": visit,
                "true_action": labels.get("authorized_action"),
                "evidence_state": labels.get("evidence_state"),
                "evidence_sufficient": labels.get("evidence_sufficient_for_action"),
            }

def oracle_policy(record):
    return record["true_action"]

def simple_policy(record):
    """
    Deliberately flawed heuristic baseline.
    It continues therapy when the text suggests improvement/stability/response,
    regardless of evidence sufficiency.
    """
    text = json.dumps(record["visit"].get("clinical_input", {})).lower()

    emergency_terms = [
        "hypoxia",
        "oxygen saturation 84",
        "respiratory distress",
        "life-threatening",
    ]

    positive_terms = [
        "improved",
        "better",
        "stable",
        "partial response",
        "response",
        "feels well",
    ]

    if any(term in text for term in emergency_terms):
        return "emergency_toxicity_management"

    if any(term in text for term in positive_terms):
        return "continue_therapy"

    return "escalate_evaluation"

def score_ptmar(trajectories, policy_fn):
    records = list(iter_visits(trajectories))
    numerator = 0
    denominator = len(records)

    details = []

    for r in records:
        model_action = policy_fn(r)
        premature = (
            r["evidence_sufficient"] is False
            and model_action in DEFINITIVE_ACTIONS
        )

        numerator += int(premature)

        details.append({
            **{k: v for k, v in r.items() if k != "visit"},
            "model_action": model_action,
            "premature": premature,
        })

    return {
        "metric": "PTMAR",
        "value": numerator / denominator if denominator else 0,
        "numerator": numerator,
        "denominator": denominator,
        "details": details,
    }

def score_aacr(trajectories, policy_fn):
    records = list(iter_visits(trajectories))

    eligible = [
        r for r in records
        if r["evidence_state"] != "sufficient"
    ]

    numerator = 0
    denominator = len(eligible)

    details = []

    for r in eligible:
        model_action = policy_fn(r)
        conflict = model_action in DEFINITIVE_ACTIONS

        numerator += int(conflict)

        details.append({
            **{k: v for k, v in r.items() if k != "visit"},
            "model_action": model_action,
            "aac_conflict": conflict,
        })

    return {
        "metric": "AACR_proxy",
        "value": numerator / denominator if denominator else 0,
        "numerator": numerator,
        "denominator": denominator,
        "details": details,
    }
