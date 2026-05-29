
from pathlib import Path
import pandas as pd

BASE = Path("/content/drive/MyDrive/oncoguard-response")

# Corrected clean benchmark source of truth
INPUT = BASE / "results" / "v0_24_clean_20trajectory_benchmark" / "visit_level_policy_inputs_v0_24_adjusted.csv"

OUTDIR = BASE / "results" / "v0_30_multi_model_eval"
OUTDIR.mkdir(parents=True, exist_ok=True)

PROMPT_TEMPLATE_PATH = OUTDIR / "model_prompt_template_v0_30.md"

visits = pd.read_csv(INPUT)
template = PROMPT_TEMPLATE_PATH.read_text()

required_cols = [
    "trajectory_id",
    "title",
    "visit_number",
    "expected_action",
    "failure_being_tested",
    "authorization_dependency",
    "evidence_state_inferred",
    "evidence_status_stage_adjusted",
]

missing = [c for c in required_cols if c not in visits.columns]
if missing:
    raise ValueError(f"Missing required columns: {missing}")

if len(visits) != 60:
    raise ValueError(f"Expected 60 visit rows from v0.24, found {len(visits)}")

prompt_rows = []

for idx, row in visits.iterrows():
    prompt = template.format(
        trajectory_id=row["trajectory_id"],
        title=row["title"],
        visit_number=row["visit_number"],
        failure_being_tested=row["failure_being_tested"],
        authorization_dependency=row["authorization_dependency"],
        evidence_state_inferred=row["evidence_state_inferred"],
        evidence_status_stage_adjusted=row["evidence_status_stage_adjusted"],
    )

    prompt_rows.append({
        "prompt_id": f"OGR_V030_{idx+1:03d}",
        "trajectory_id": row["trajectory_id"],
        "visit_number": row["visit_number"],
        "expected_action": row["expected_action"],
        "evidence_state_inferred": row["evidence_state_inferred"],
        "evidence_status_stage_adjusted": row["evidence_status_stage_adjusted"],
        "source_benchmark_version": "v0.24-clean-20trajectory-benchmark",
        "prompt": prompt,
    })

prompts = pd.DataFrame(prompt_rows)

out = OUTDIR / "model_prompts_v0_30.csv"
prompts.to_csv(out, index=False)

print("Source input:", INPUT)
print("Input visits:", visits.shape)
print("Prompt rows:", prompts.shape)
print(f"Saved: {out}")

print("\nExpected action counts:")
print(prompts["expected_action"].value_counts())

print("\nAdjusted evidence status counts:")
print(prompts["evidence_status_stage_adjusted"].value_counts())

print("\nFirst prompt ID:", prompts["prompt_id"].iloc[0])
print("Last prompt ID:", prompts["prompt_id"].iloc[-1])
print("First trajectory:", prompts["trajectory_id"].iloc[0])
print("Last trajectory:", prompts["trajectory_id"].iloc[-1])
