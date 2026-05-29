
"""
OncoGuard-Response v0.21 Multi-Policy Evaluation Scaffold

Purpose:
Compare different therapeutic-response authorization policies against the frozen v0.20 pilot outputs.

This script does NOT modify the frozen v0.20 files.
It creates new v0.21 policy-comparison outputs.
"""

from pathlib import Path
import pandas as pd


BASE = Path("/content/drive/MyDrive/oncoguard-response")

V0_20_RESULTS = BASE / "results" / "freeze_v0_20_pilot"
V0_21_RESULTS = BASE / "results" / "policy_eval_v0_21"
V0_21_RESULTS.mkdir(parents=True, exist_ok=True)

SUMMARY_PATH = V0_20_RESULTS / "pilot_ptmar_aacr_summary_v0.csv"
TAXONOMY_PATH = V0_20_RESULTS / "failure_taxonomy_v0_20.csv"


# ---------------------------------------------------------------------
# Policy definitions
# ---------------------------------------------------------------------

POLICIES = {
    "permissive": {
        "description": "Authorizes continuation unless a hard-stop evidence-state failure is present.",
        "deferral_posture": "low",
        "expected_behavior": "More willing to continue therapy when benefit signal exists.",
    },
    "standard": {
        "description": "Requires core authorization conditions to be satisfied before continuation.",
        "deferral_posture": "moderate",
        "expected_behavior": "Balances response benefit against toxicity and evidence sufficiency.",
    },
    "conservative": {
        "description": "Defers whenever critical evidence is missing, contradictory, or toxicity assessment is incomplete.",
        "deferral_posture": "high",
        "expected_behavior": "Prioritizes safety and evidence sufficiency over early continuation.",
    },
}


# ---------------------------------------------------------------------
# Load frozen v0.20 results
# ---------------------------------------------------------------------

def load_v0_20_results():
    if not SUMMARY_PATH.exists():
        raise FileNotFoundError(f"Missing summary file: {SUMMARY_PATH}")

    if not TAXONOMY_PATH.exists():
        raise FileNotFoundError(f"Missing taxonomy file: {TAXONOMY_PATH}")

    summary = pd.read_csv(SUMMARY_PATH)
    taxonomy = pd.read_csv(TAXONOMY_PATH)

    return summary, taxonomy


# ---------------------------------------------------------------------
# Extract baseline frozen metrics
# ---------------------------------------------------------------------

def extract_baseline_metrics(summary, taxonomy):
    """
    This function assumes the known frozen v0.20 pilot values.
    If future summary files contain standardized columns, replace this
    with direct parsing from summary.
    """

    n_visits = 60
    ptmar_rate = 23.3
    aacr_rate = 93.3
    ptmar_events = int(taxonomy["failure_count"].sum())

    return {
        "n_visits": n_visits,
        "ptmar_rate": ptmar_rate,
        "aacr_rate": aacr_rate,
        "ptmar_events": ptmar_events,
    }


# ---------------------------------------------------------------------
# Policy simulation scaffold
# ---------------------------------------------------------------------

def simulate_policy_outputs(baseline):
    """
    Placeholder scaffold for v0.21.

    These are NOT final empirical results.
    They are scaffold values to establish the output contract.

    Later, replace these heuristic adjustments with visit-level policy logic.
    """

    rows = []

    for policy_name, policy_info in POLICIES.items():
        if policy_name == "permissive":
            simulated_ptmar = baseline["ptmar_rate"] + 5.0
            simulated_aacr = baseline["aacr_rate"] - 3.0
            simulated_defer_rate = 10.0
            simulated_over_deferral_rate = 2.0
            simulated_unsafe_authorization_rate = simulated_ptmar

        elif policy_name == "standard":
            simulated_ptmar = baseline["ptmar_rate"]
            simulated_aacr = baseline["aacr_rate"]
            simulated_defer_rate = 20.0
            simulated_over_deferral_rate = 5.0
            simulated_unsafe_authorization_rate = simulated_ptmar

        elif policy_name == "conservative":
            simulated_ptmar = max(0.0, baseline["ptmar_rate"] - 10.0)
            simulated_aacr = baseline["aacr_rate"] - 1.5
            simulated_defer_rate = 35.0
            simulated_over_deferral_rate = 12.0
            simulated_unsafe_authorization_rate = simulated_ptmar

        else:
            raise ValueError(f"Unknown policy: {policy_name}")

        rows.append({
            "policy_name": policy_name,
            "policy_description": policy_info["description"],
            "deferral_posture": policy_info["deferral_posture"],
            "n_visits": baseline["n_visits"],
            "ptmar_rate": round(simulated_ptmar, 1),
            "aacr_rate": round(simulated_aacr, 1),
            "defer_rate": round(simulated_defer_rate, 1),
            "over_deferral_rate": round(simulated_over_deferral_rate, 1),
            "unsafe_authorization_rate": round(simulated_unsafe_authorization_rate, 1),
            "status": "scaffold_placeholder_not_final_result",
        })

    return pd.DataFrame(rows)


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main():
    summary, taxonomy = load_v0_20_results()
    baseline = extract_baseline_metrics(summary, taxonomy)

    policy_df = simulate_policy_outputs(baseline)

    out_csv = V0_21_RESULTS / "policy_comparison_v0_21_scaffold.csv"
    policy_df.to_csv(out_csv, index=False)

    policy_notes = V0_21_RESULTS / "policy_eval_v0_21_notes.md"
    policy_notes.write_text(
        """# OncoGuard-Response v0.21 Multi-Policy Evaluation Scaffold

This directory contains the initial multi-policy evaluation scaffold.

Important: `policy_comparison_v0_21_scaffold.csv` is a scaffold output only.  
The values are placeholders designed to lock the output schema before implementing visit-level policy logic.

## Policies

1. Permissive policy  
   Authorizes continuation unless a hard-stop evidence-state failure is present.

2. Standard policy  
   Requires core authorization conditions to be satisfied before continuation.

3. Conservative policy  
   Defers whenever critical evidence is missing, contradictory, or toxicity assessment is incomplete.

## Intended v0.21 metrics

- PTMAR
- AACR
- defer rate
- over-deferral rate
- unsafe authorization rate
- correct authorization rate
- dominant failure mode

## Next implementation step

Replace scaffold placeholder values with visit-level policy adjudication logic using the trajectory inventory and candidate response evaluations.
"""
    )

    print(f"Saved policy scaffold: {out_csv}")
    print(f"Saved notes: {policy_notes}")
    print()
    print(policy_df)


if __name__ == "__main__":
    main()
