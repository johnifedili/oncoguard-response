
import sys
from pathlib import Path

import pandas as pd

# Make eval module importable when script is run from repo root
THIS_DIR = Path(__file__).resolve().parent
REPO_ROOT = THIS_DIR.parent
sys.path.append(str(THIS_DIR))

from score_ptmar_aacr import (
    load_trajectories,
    oracle_policy,
    simple_policy,
    score_ptmar,
    score_aacr,
)


def run_eval(
    traj_dir="data/trajectories/v0_pilot",
    out_dir="results/pilot_runs",
):
    traj_dir = REPO_ROOT / traj_dir
    out_dir = REPO_ROOT / out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    trajectories = load_trajectories(traj_dir)

    rows = []

    for policy_name, policy_fn in [
        ("oracle_policy", oracle_policy),
        ("simple_policy", simple_policy),
    ]:
        ptmar = score_ptmar(trajectories, policy_fn)
        aacr = score_aacr(trajectories, policy_fn)

        rows.append({
            "policy": policy_name,
            "PTMAR": ptmar["value"],
            "PTMAR_count": ptmar["numerator"],
            "PTMAR_denominator": ptmar["denominator"],
            "AACR_proxy": aacr["value"],
            "AACR_count": aacr["numerator"],
            "AACR_denominator": aacr["denominator"],
        })

        if policy_name == "simple_policy":
            failures = pd.DataFrame(ptmar["details"])
            failures = failures[failures["premature"] == True]
            failures.to_csv(out_dir / "pilot_simple_policy_failures_v0.csv", index=False)

    summary = pd.DataFrame(rows)
    summary.to_csv(out_dir / "pilot_ptmar_aacr_summary_v0.csv", index=False)

    print(summary)
    print()
    print(f"Saved summary to: {out_dir / 'pilot_ptmar_aacr_summary_v0.csv'}")
    print(f"Saved failures to: {out_dir / 'pilot_simple_policy_failures_v0.csv'}")


if __name__ == "__main__":
    run_eval()
