
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

BASE = Path("/content/drive/MyDrive/oncoguard-response")
RESULTS = BASE / "results" / "v0_30_multi_model_eval"
FIGDIR = RESULTS / "figures_openai_two_model_comparison_v0_30"
FIGDIR.mkdir(parents=True, exist_ok=True)

summary_files = {
    "GPT-4o-mini": RESULTS / "openai_gpt4omini_summary_v0_30.csv",
    "GPT-4.1": RESULTS / "openai_gpt41_summary_v0_30.csv",
}

score_files = {
    "GPT-4o-mini": RESULTS / "openai_gpt4omini_scores_v0_30.csv",
    "GPT-4.1": RESULTS / "openai_gpt41_scores_v0_30.csv",
}

# -----------------------------
# Load summaries
# -----------------------------
summary_rows = []

for display_name, path in summary_files.items():
    if not path.exists():
        raise FileNotFoundError(f"Missing summary file: {path}")
    df = pd.read_csv(path)
    row = df.iloc[0].to_dict()
    row["display_model_name"] = display_name
    summary_rows.append(row)

comparison = pd.DataFrame(summary_rows)

# Put display name first
cols = ["display_model_name"] + [c for c in comparison.columns if c != "display_model_name"]
comparison = comparison[cols]

comparison_out = RESULTS / "openai_model_comparison_summary_v0_30.csv"
comparison.to_csv(comparison_out, index=False)

print(f"Saved: {comparison_out}")
print("\nTwo-model comparison summary:")
print(comparison.to_string(index=False))

# -----------------------------
# Figure 1: Metric comparison
# -----------------------------
metric_cols = [
    "schema_conformance_percent",
    "aacr_percent",
    "ptmar_percent",
    "unsafe_authorization_percent",
    "defer_rate_percent",
    "over_deferral_percent",
    "over_hold_percent",
    "over_emergency_percent",
    "over_switch_percent",
]

metric_labels = [
    "Schema\nconformance",
    "AACR",
    "PTMAR",
    "Unsafe\nauthorization",
    "Defer\nrate",
    "Over-\ndeferral",
    "Over-\nhold",
    "Over-\nemergency",
    "Over-\nswitch",
]

x = np.arange(len(metric_cols))
width = 0.35

plt.figure(figsize=(14, 6))

for i, (_, row) in enumerate(comparison.iterrows()):
    values = [row[col] for col in metric_cols]
    offset = (i - 0.5) * width
    plt.bar(x + offset, values, width, label=row["display_model_name"])

plt.xticks(x, metric_labels)
plt.ylim(0, 110)
plt.ylabel("Rate (%)")
plt.xlabel("Metric")
plt.title("OpenAI Model Comparison on OncoGuard-Response v0.30")
plt.legend()
plt.tight_layout()

out = FIGDIR / "figure_1_openai_model_metric_comparison_v0_30.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")

# -----------------------------
# Load score files
# -----------------------------
score_frames = []

for display_name, path in score_files.items():
    if not path.exists():
        raise FileNotFoundError(f"Missing score file: {path}")
    df = pd.read_csv(path)
    df["display_model_name"] = display_name
    score_frames.append(df)

scores = pd.concat(score_frames, ignore_index=True)

# -----------------------------
# Figure 2: Error taxonomy comparison
# -----------------------------
error_counts = (
    scores
    .groupby(["display_model_name", "error_type"])
    .size()
    .reset_index(name="count")
)

error_pivot = error_counts.pivot(
    index="error_type",
    columns="display_model_name",
    values="count"
).fillna(0)

# Sort by total error burden, keeping correct_authorization visible
error_pivot["total"] = error_pivot.sum(axis=1)
error_pivot = error_pivot.sort_values("total", ascending=False).drop(columns=["total"])

x = np.arange(len(error_pivot.index))
width = 0.35

plt.figure(figsize=(13, 7))

for i, model in enumerate(error_pivot.columns):
    offset = (i - 0.5) * width
    plt.bar(x + offset, error_pivot[model].values, width, label=model)

plt.xticks(x, error_pivot.index, rotation=35, ha="right")
plt.ylabel("Count")
plt.xlabel("Error type")
plt.title("Error Taxonomy Comparison: GPT-4o-mini vs GPT-4.1")
plt.legend()
plt.tight_layout()

out = FIGDIR / "figure_2_openai_model_error_comparison_v0_30.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")

error_out = RESULTS / "openai_model_error_comparison_v0_30.csv"
error_pivot.to_csv(error_out)
print(f"Saved: {error_out}")

# -----------------------------
# Figure 3: Selected action distribution comparison
# -----------------------------
action_order = [
    "continue_therapy",
    "escalate_evaluation",
    "hold_therapy",
    "switch_therapy",
    "emergency_toxicity_management",
]

action_counts = (
    scores
    .groupby(["display_model_name", "selected_action"])
    .size()
    .reset_index(name="count")
)

action_pivot = action_counts.pivot(
    index="selected_action",
    columns="display_model_name",
    values="count"
).fillna(0)

action_pivot = action_pivot.reindex(action_order).fillna(0)

x = np.arange(len(action_pivot.index))
width = 0.35

plt.figure(figsize=(11, 6))

for i, model in enumerate(action_pivot.columns):
    offset = (i - 0.5) * width
    plt.bar(x + offset, action_pivot[model].values, width, label=model)

plt.xticks(x, action_pivot.index, rotation=25, ha="right")
plt.ylabel("Count")
plt.xlabel("Selected action")
plt.title("Selected Action Distribution: GPT-4o-mini vs GPT-4.1")
plt.legend()
plt.tight_layout()

out = FIGDIR / "figure_3_openai_model_selected_action_comparison_v0_30.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")

action_out = RESULTS / "openai_model_selected_action_comparison_v0_30.csv"
action_pivot.to_csv(action_out)
print(f"Saved: {action_out}")

# -----------------------------
# Figure 4: Expected continue therapy behavior
# -----------------------------
continue_subset = scores[scores["expected_action"] == "continue_therapy"].copy()

continue_counts = (
    continue_subset
    .groupby(["display_model_name", "selected_action"])
    .size()
    .reset_index(name="count")
)

continue_pivot = continue_counts.pivot(
    index="selected_action",
    columns="display_model_name",
    values="count"
).fillna(0)

continue_pivot = continue_pivot.reindex(action_order).fillna(0)

x = np.arange(len(continue_pivot.index))
width = 0.35

plt.figure(figsize=(11, 6))

for i, model in enumerate(continue_pivot.columns):
    offset = (i - 0.5) * width
    plt.bar(x + offset, continue_pivot[model].values, width, label=model)

plt.xticks(x, continue_pivot.index, rotation=25, ha="right")
plt.ylabel("Count")
plt.xlabel("Selected action when continuation was expected")
plt.title("Model Behavior on Continuation-Authorized Visits")
plt.legend()
plt.tight_layout()

out = FIGDIR / "figure_4_openai_model_continuation_authorized_behavior_v0_30.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")

continue_out = RESULTS / "openai_model_continuation_authorized_behavior_v0_30.csv"
continue_pivot.to_csv(continue_out)
print(f"Saved: {continue_out}")

# -----------------------------
# Create manuscript-ready markdown
# -----------------------------
mini = comparison[comparison["display_model_name"] == "GPT-4o-mini"].iloc[0]
gpt41 = comparison[comparison["display_model_name"] == "GPT-4.1"].iloc[0]

md = f"""# OncoGuard-Response v0.30 — OpenAI Two-Model Comparison

## Overview

This analysis compares GPT-4o-mini and GPT-4.1 on the corrected OncoGuard-Response v0.24 clean 20-trajectory / 60-visit benchmark.

Both models were evaluated on the same 60 visit-level therapeutic authorization prompts derived from the v0.24 benchmark.

## Benchmark

Benchmark version:

`v0.24-clean-20trajectory-benchmark`

Prompt file:

`results/v0_30_multi_model_eval/model_prompts_v0_30.csv`

## Summary results

| Metric | GPT-4o-mini | GPT-4.1 |
|---|---:|---:|
| n | {int(mini["n"])} | {int(gpt41["n"])} |
| Schema conformance | {mini["schema_conformance_percent"]:.1f}% | {gpt41["schema_conformance_percent"]:.1f}% |
| AACR | {mini["aacr_percent"]:.1f}% | {gpt41["aacr_percent"]:.1f}% |
| PTMAR | {mini["ptmar_percent"]:.1f}% | {gpt41["ptmar_percent"]:.1f}% |
| Unsafe authorization | {mini["unsafe_authorization_percent"]:.1f}% | {gpt41["unsafe_authorization_percent"]:.1f}% |
| Defer rate | {mini["defer_rate_percent"]:.1f}% | {gpt41["defer_rate_percent"]:.1f}% |
| Over-deferral | {mini["over_deferral_percent"]:.1f}% | {gpt41["over_deferral_percent"]:.1f}% |
| Over-hold | {mini["over_hold_percent"]:.1f}% | {gpt41["over_hold_percent"]:.1f}% |
| Over-emergency management | {mini["over_emergency_percent"]:.1f}% | {gpt41["over_emergency_percent"]:.1f}% |
| Over-switch / premature switch | {mini["over_switch_percent"]:.1f}% | {gpt41["over_switch_percent"]:.1f}% |

## Key findings

Both models achieved 100.0% schema conformance and 0.0% PTMAR / unsafe authorization, indicating that neither model prematurely continued therapy in the benchmark.

GPT-4.1 achieved higher AACR than GPT-4o-mini:

- GPT-4o-mini AACR: {mini["aacr_percent"]:.1f}%
- GPT-4.1 AACR: {gpt41["aacr_percent"]:.1f}%

However, GPT-4.1 was more defer-heavy:

- GPT-4o-mini defer rate: {mini["defer_rate_percent"]:.1f}%
- GPT-4.1 defer rate: {gpt41["defer_rate_percent"]:.1f}%

GPT-4.1 also showed higher over-deferral:

- GPT-4o-mini over-deferral: {mini["over_deferral_percent"]:.1f}%
- GPT-4.1 over-deferral: {gpt41["over_deferral_percent"]:.1f}%

## Governance phenotype

GPT-4o-mini demonstrated a schema-perfect conservative over-deferral / over-holding phenotype.

GPT-4.1 demonstrated a schema-perfect conservative escalation phenotype, with higher AACR but more frequent escalation rather than continuation.

## Interpretation

The comparison shows that larger model capacity did not eliminate authorization calibration failure. GPT-4.1 improved overall authorization alignment but remained highly conservative, frequently escalating evaluation when continuation was expected.

This supports the central OncoGuard-Response claim: oncology AI systems should not be evaluated only for avoidance of unsafe continuation. They should also be evaluated for treatment-delay risk, over-deferral, over-holding, premature switching, and wrong-channel escalation.

## Main takeaway

Both models avoided unsafe continuation, but both showed conservative authorization bias. GPT-4.1 improved AACR relative to GPT-4o-mini while increasing defer-heavy behavior. OncoGuard-Response therefore reveals a clinically meaningful governance tradeoff: safety against premature continuation may coexist with unnecessary treatment delay or interruption.
"""

md_out = RESULTS / "results_openai_two_model_comparison_v0_30.md"
md_out.write_text(md)
print(f"Saved: {md_out}")

# -----------------------------
# Figure index
# -----------------------------
figure_index = pd.DataFrame([
    {
        "figure_id": "Figure 1",
        "filename": "figure_1_openai_model_metric_comparison_v0_30.png",
        "title": "OpenAI model metric comparison",
        "description": "Side-by-side comparison of schema conformance, AACR, PTMAR, unsafe authorization, deferral, and over-action metrics."
    },
    {
        "figure_id": "Figure 2",
        "filename": "figure_2_openai_model_error_comparison_v0_30.png",
        "title": "OpenAI model error taxonomy comparison",
        "description": "Comparison of error-type counts between GPT-4o-mini and GPT-4.1."
    },
    {
        "figure_id": "Figure 3",
        "filename": "figure_3_openai_model_selected_action_comparison_v0_30.png",
        "title": "Selected action distribution comparison",
        "description": "Comparison of selected therapeutic authorization actions across models."
    },
    {
        "figure_id": "Figure 4",
        "filename": "figure_4_openai_model_continuation_authorized_behavior_v0_30.png",
        "title": "Continuation-authorized behavior comparison",
        "description": "Comparison of model-selected actions specifically on visits where continuation was expected."
    },
])

fig_index_out = FIGDIR / "figure_index_openai_two_model_comparison_v0_30.csv"
figure_index.to_csv(fig_index_out, index=False)
print(f"Saved: {fig_index_out}")
