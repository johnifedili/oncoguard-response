
from pathlib import Path
import json
import pandas as pd

BASE = Path("/content/drive/MyDrive/oncoguard-response")

TRAJ_DIR = BASE / "data" / "trajectories" / "v0_pilot"
OUTDIR = BASE / "results" / "v0_24_clean_20trajectory_benchmark"
OUTDIR.mkdir(parents=True, exist_ok=True)

rows = []

for path in sorted(TRAJ_DIR.glob("OGR_TRJ_*.json")):
    with open(path) as f:
        d = json.load(f)

    visits = d.get("visits", [])
    actions = [v["labels"]["authorized_action"] for v in visits]

    title = (
        d.get("trajectory_title")
        or d.get("title")
        or d.get("case_source", {}).get("notes")
        or d.get("trajectory_id")
    )

    auth_dep = d.get("authorization_dependency", "")
    if isinstance(auth_dep, list):
        auth_dep = "; ".join(auth_dep)

    rows.append({
        "trajectory_id": d.get("trajectory_id"),
        "title": title,
        "n_visits": len(visits),
        "action_path": " -> ".join(actions),
        "failure_being_tested": d.get("failure_being_tested"),
        "authorization_dependency": auth_dep,
        "source_json": str(path.relative_to(BASE)),
    })

inventory = pd.DataFrame(rows).sort_values("trajectory_id")

out = OUTDIR / "trajectory_inventory_v0_24.csv"
inventory.to_csv(out, index=False)

print("Trajectories:", len(inventory))
print("Total visits:", inventory["n_visits"].sum())
print(f"Saved: {out}")

print("\nTrajectory IDs:")
print(inventory["trajectory_id"].to_list())

print("\nAction counts from action paths:")
all_actions = []
for path in inventory["action_path"]:
    all_actions.extend([a.strip() for a in path.split("->")])
print(pd.Series(all_actions).value_counts())
