
from pathlib import Path
import pandas as pd

BASE = Path("/content/drive/MyDrive/oncoguard-response")

V020_RESULTS = BASE / "results" / "freeze_v0_20_pilot"
V021_RESULTS = BASE / "results" / "v0_21_multi_policy"
V021_RESULTS.mkdir(parents=True, exist_ok=True)

# Locked v0.20 baseline values
N_VISITS = 60
BASELINE_PTMAR = 23.3
BASELINE_AACR = 93.3
BASELINE_FAILURES = 14

# Provenance check: confirm frozen v0.20 files exist
expected_files = [
    "trajectory_inventory_v0_20.csv",
    "failure_taxonomy_v0_20.csv",
    "results_v0_20.md",
]

provenance_rows = []
for fname in expected_files:
    path = V020_RESULTS / fname
    provenance_rows.append({
        "filename": fname,
        "expected_path": str(path),
        "exists": path.exists(),
    })

provenance = pd.DataFrame(provenance_rows)
provenance_out = V021_RESULTS / "v0_20_input_provenance_check.csv"
provenance.to_csv(provenance_out, index=False)

policies = [
    {
        "policy_name": "permissive",
        "policy_description": "Authorizes continuation unless an explicit hard-stop exists.",
        "policy_posture": "low_deferral_high_continuation",
    },
    {
        "policy_name": "standard",
        "policy_description": "Requires stated authorization conditions to be satisfied before continuation.",
        "policy_posture": "balanced_authorization",
    },
    {
        "policy_name": "conservative",
        "policy_description": "Defers whenever required evidence is missing, contradictory, or toxicity assessment is incomplete.",
        "policy_posture": "high_deferral_safety_first",
    },
]

rows = []

for policy in policies:
    rows.append({
        "policy_name": policy["policy_name"],
        "policy_description": policy["policy_description"],
        "policy_posture": policy["policy_posture"],
        "baseline_reference": "v0.20-pilot",
        "n_visits": N_VISITS,
        "baseline_ptmar_percent": BASELINE_PTMAR,
        "baseline_aacr_percent": BASELINE_AACR,
        "baseline_ptmar_positive_failures": BASELINE_FAILURES,
        "ptmar_percent": None,
        "aacr_percent": None,
        "defer_rate_percent": None,
        "unsafe_authorization_rate_percent": None,
        "over_deferral_rate_percent": None,
        "correct_authorization_rate_percent": None,
        "dominant_failure_mode": None,
        "status": "scaffold_defined_pending_policy_scoring",
    })

policy_summary = pd.DataFrame(rows)

out_summary = V021_RESULTS / "multi_policy_summary_v0_21.csv"
policy_summary.to_csv(out_summary, index=False)

policy_defs = pd.DataFrame(policies)
out_defs = V021_RESULTS / "policy_definitions_v0_21.csv"
policy_defs.to_csv(out_defs, index=False)

notes = f"""# OncoGuard-Response v0.21 Multi-Policy Evaluation Scaffold

This folder defines the v0.21 multi-policy evaluation scaffold.

## Baseline reference

Frozen baseline: v0.20-pilot

- Visits: {N_VISITS}
- PTMAR: {BASELINE_PTMAR}%
- AACR: {BASELINE_AACR}%
- PTMAR-positive failures: {BASELINE_FAILURES}

## Policy families

1. Permissive policy
   - Authorizes continuation unless an explicit hard-stop exists.
   - Expected behavior: lower deferral, higher risk of unsafe authorization.

2. Standard policy
   - Requires stated authorization conditions to be satisfied.
   - Expected behavior: balanced safety and continuation.

3. Conservative policy
   - Defers when evidence is missing, contradictory, or toxicity assessment is incomplete.
   - Expected behavior: lower unsafe authorization, higher deferral.

## Current status

This is a scaffold. Policy-specific scoring logic will be connected after confirming the visit-level output columns available from the v0.20 evaluation runner.
"""

out_notes = V021_RESULTS / "README_v0_21_multi_policy.md"
out_notes.write_text(notes)

print(f"Saved: {out_summary}")
print(f"Saved: {out_defs}")
print(f"Saved: {provenance_out}")
print(f"Saved: {out_notes}")
