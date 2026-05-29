
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

BASE = Path("/content/drive/MyDrive/oncoguard-response")
RESULTS = BASE / "results" / "v0_30_multi_model_eval"
FIGS = RESULTS / "figures_gpt4omini_v0_30"
FIGS.mkdir(parents=True, exist_ok=True)

scores_path = RESULTS / "openai_gpt4omini_scores_v0_30.csv"
summary_path = RESULTS / "openai_gpt4omini_summary_v0_30.csv"

scores = pd.read_csv(scores_path)
summary = pd.read_csv(summary_path)

# -----------------------------
# Figure 1: Metric summary
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

values = [summary[col].iloc[0] for col in metric_cols]

plt.figure(figsize=(12, 6))
plt.bar(metric_labels, values)
plt.ylim(0, 110)
plt.ylabel("Rate (%)")
plt.xlabel("Metric")
plt.title("GPT-4o-mini Performance on OncoGuard-Response v0.30")

for i, value in enumerate(values):
    y = value + 2 if value <= 95 else value - 8
    plt.text(i, y, f"{value:.1f}%", ha="center")

plt.tight_layout()
out = FIGS / "figure_1_gpt4omini_v0_30_metric_summary.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")

# -----------------------------
# Figure 2: Selected action distribution
# -----------------------------
action_counts = scores["selected_action"].value_counts()

plt.figure(figsize=(9, 5))
plt.bar(action_counts.index, action_counts.values)
plt.ylabel("Count")
plt.xlabel("Selected action")
plt.title("GPT-4o-mini Selected Action Distribution")
plt.xticks(rotation=25, ha="right")

for i, value in enumerate(action_counts.values):
    plt.text(i, value + 0.5, str(value), ha="center")

plt.tight_layout()
out = FIGS / "figure_2_gpt4omini_v0_30_selected_action_distribution.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")

# -----------------------------
# Figure 3: Error taxonomy
# -----------------------------
error_counts = scores["error_type"].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(error_counts.index, error_counts.values)
plt.ylabel("Count")
plt.xlabel("Error type")
plt.title("GPT-4o-mini Error Taxonomy on OncoGuard-Response v0.30")
plt.xticks(rotation=35, ha="right")

for i, value in enumerate(error_counts.values):
    plt.text(i, value + 0.5, str(value), ha="center")

plt.tight_layout()
out = FIGS / "figure_3_gpt4omini_v0_30_error_taxonomy.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")

# -----------------------------
# Figure 4: Expected vs selected action heatmap
# -----------------------------
expected_order = [
    "continue_therapy",
    "escalate_evaluation",
    "hold_therapy",
    "switch_therapy",
    "emergency_toxicity_management",
]

selected_order = [
    "continue_therapy",
    "escalate_evaluation",
    "hold_therapy",
    "switch_therapy",
    "emergency_toxicity_management",
]

ct = pd.crosstab(scores["expected_action"], scores["selected_action"])
ct = ct.reindex(index=expected_order, columns=selected_order, fill_value=0)

plt.figure(figsize=(9, 7))
plt.imshow(ct.values, aspect="auto")
plt.xticks(range(len(selected_order)), selected_order, rotation=35, ha="right")
plt.yticks(range(len(expected_order)), expected_order)
plt.xlabel("Model-selected action")
plt.ylabel("Expected benchmark action")
plt.title("GPT-4o-mini Expected vs Selected Action Matrix")

for i in range(ct.shape[0]):
    for j in range(ct.shape[1]):
        plt.text(j, i, str(ct.values[i, j]), ha="center", va="center")

plt.colorbar(label="Count")
plt.tight_layout()
out = FIGS / "figure_4_gpt4omini_v0_30_expected_vs_selected_matrix.png"
plt.savefig(out, dpi=300)
plt.show()
print(f"Saved: {out}")

# -----------------------------
# Figure index
# -----------------------------
figure_index = pd.DataFrame([
    {
        "figure_id": "Figure 1",
        "filename": "figure_1_gpt4omini_v0_30_metric_summary.png",
        "title": "GPT-4o-mini metric summary",
        "description": "Summary of schema conformance, AACR, PTMAR, unsafe authorization, deferral, and over-action metrics."
    },
    {
        "figure_id": "Figure 2",
        "filename": "figure_2_gpt4omini_v0_30_selected_action_distribution.png",
        "title": "Selected action distribution",
        "description": "Distribution of actions selected by GPT-4o-mini across 60 visit-level prompts."
    },
    {
        "figure_id": "Figure 3",
        "filename": "figure_3_gpt4omini_v0_30_error_taxonomy.png",
        "title": "Error taxonomy",
        "description": "Counts of correct authorizations and model error categories."
    },
    {
        "figure_id": "Figure 4",
        "filename": "figure_4_gpt4omini_v0_30_expected_vs_selected_matrix.png",
        "title": "Expected vs selected action matrix",
        "description": "Cross-tabulation of benchmark expected actions against GPT-4o-mini selected actions."
    },
])

index_out = FIGS / "figure_index_gpt4omini_v0_30.csv"
figure_index.to_csv(index_out, index=False)
print(f"Saved: {index_out}")
