
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path("/content/oncoguard-response")

V47_DIR = BASE / "results" / "v0_47_gpt41_naturalistic_pressure_eval"
V50_DIR = BASE / "results" / "v0_50_controller_intervention"
V51_DIR = BASE / "results" / "v0_51_controller_ablation"
V52_DIR = BASE / "results" / "v0_52_pilot_synthesis"

OUTDIR = BASE / "results" / "v0_53_pilot_tables_figures"
FIGDIR = OUTDIR / "figures"
TABLEDIR = OUTDIR / "tables"

OUTDIR.mkdir(parents=True, exist_ok=True)
FIGDIR.mkdir(parents=True, exist_ok=True)
TABLEDIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------
# Load source files
# ---------------------------------------------------------------------

v47_summary_path = V47_DIR / "openai_gpt41_summary_v0_47.csv"
v47_scores_path = V47_DIR / "openai_gpt41_scores_v0_47.csv"

v50_summary_path = V50_DIR / "gpt41_v0_50_controller_summary.csv"
v50_before_after_path = V50_DIR / "gpt41_v0_50_before_after_metrics.csv"
v50_scores_path = V50_DIR / "gpt41_v0_50_controller_scores.csv"
v50_expected_vs_model_path = V50_DIR / "gpt41_v0_50_expected_vs_model_action.csv"
v50_expected_vs_controller_path = V50_DIR / "gpt41_v0_50_expected_vs_controller_action.csv"

v51_summary_path = V51_DIR / "v0_51_ablation_summary.csv"
v51_paired_path = V51_DIR / "v0_51_paired_correctness_test.csv"

required = [
    v47_summary_path,
    v47_scores_path,
    v50_summary_path,
    v50_before_after_path,
    v50_scores_path,
    v50_expected_vs_model_path,
    v50_expected_vs_controller_path,
    v51_summary_path,
    v51_paired_path,
]

missing = [str(p) for p in required if not p.exists()]
if missing:
    raise FileNotFoundError(f"Missing required source files: {missing}")

v47_summary = pd.read_csv(v47_summary_path)
v47_scores = pd.read_csv(v47_scores_path)
v50_summary = pd.read_csv(v50_summary_path)
v50_before_after = pd.read_csv(v50_before_after_path)
v50_scores = pd.read_csv(v50_scores_path)
v50_expected_vs_model = pd.read_csv(v50_expected_vs_model_path, index_col=0)
v50_expected_vs_controller = pd.read_csv(v50_expected_vs_controller_path, index_col=0)
v51_summary = pd.read_csv(v51_summary_path)
v51_paired = pd.read_csv(v51_paired_path)

# ---------------------------------------------------------------------
# Table 1 — Versioned pipeline/provenance
# ---------------------------------------------------------------------

table1 = pd.DataFrame([
    {
        "version": "v0.40",
        "artifact": "Expanded design matrix",
        "purpose": "Defined 100 trajectories / 300 visit-level decisions across cancer types, therapy classes, and action labels.",
        "status": "locked",
    },
    {
        "version": "v0.41",
        "artifact": "Synthetic case generation",
        "purpose": "Generated longitudinal oncology cases from the v0.40 design matrix.",
        "status": "locked",
    },
    {
        "version": "v0.42",
        "artifact": "Integrity audit",
        "purpose": "Confirmed 100 trajectories, 300 visits, schema validity, and design/generation consistency.",
        "status": "locked",
    },
    {
        "version": "v0.43 / v0.43b",
        "artifact": "Clean and blinded prompts",
        "purpose": "Generated model prompt sets; blinded set removed overt metadata cues.",
        "status": "locked",
    },
    {
        "version": "v0.44 / v0.44b",
        "artifact": "Clean/blinded GPT-4.1 pipeline validation",
        "purpose": "Showed ceiling-level 100% AACR; interpreted as pipeline validation and cue-alignment warning.",
        "status": "locked",
    },
    {
        "version": "v0.45",
        "artifact": "Pressure taxonomy and cue-contamination protocol",
        "purpose": "Locked four-layer evaluation architecture and naturalistic pressure framework.",
        "status": "locked",
    },
    {
        "version": "v0.46 / v0.46a-c",
        "artifact": "Naturalistic pressure pilot and confirmation",
        "purpose": "Generated, audited, and author-domain confirmed 30 naturalistic pressure probes.",
        "status": "locked",
    },
    {
        "version": "v0.47",
        "artifact": "GPT-4.1 naturalistic pressure evaluation",
        "purpose": "Identified conservative wrong-channel collapse under naturalistic clinical pressure.",
        "status": "locked",
    },
    {
        "version": "v0.50",
        "artifact": "Evidence-contract controller intervention",
        "purpose": "Corrected wrong-channel model outputs using deterministic evidence/action contract.",
        "status": "locked",
    },
    {
        "version": "v0.51",
        "artifact": "Controller ablation",
        "purpose": "Showed full evidence/action routing was required; safety-block-only did not help.",
        "status": "locked",
    },
    {
        "version": "v0.52",
        "artifact": "Pilot synthesis memo",
        "purpose": "Preserved pilot story, claims, caveats, and next steps.",
        "status": "locked",
    },
])

table1.to_csv(TABLEDIR / "table1_versioned_pipeline_provenance_v0_53.csv", index=False)

# ---------------------------------------------------------------------
# Table 2 — v0.47 pressure result
# ---------------------------------------------------------------------

table2 = v47_summary.copy()
table2.to_csv(TABLEDIR / "table2_v0_47_gpt41_pressure_results_v0_53.csv", index=False)

# ---------------------------------------------------------------------
# Table 3 — v0.50 controller before/after
# ---------------------------------------------------------------------

table3 = v50_before_after.copy()
table3.to_csv(TABLEDIR / "table3_v0_50_controller_before_after_v0_53.csv", index=False)

# ---------------------------------------------------------------------
# Table 4 — v0.51 ablation
# ---------------------------------------------------------------------

table4 = v51_summary.copy()
table4.to_csv(TABLEDIR / "table4_v0_51_controller_ablation_v0_53.csv", index=False)

# ---------------------------------------------------------------------
# Table 5 — paired correctness test
# ---------------------------------------------------------------------

table5 = v51_paired.copy()
table5.to_csv(TABLEDIR / "table5_v0_51_paired_correctness_test_v0_53.csv", index=False)

# ---------------------------------------------------------------------
# Helper for bar labels
# ---------------------------------------------------------------------

def add_bar_labels(ax, bars, suffix="%"):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            f"{height:.1f}{suffix}",
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=8,
        )

# ---------------------------------------------------------------------
# Figure 1 — Four-layer evaluation architecture schematic
# ---------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 5))
ax.axis("off")

layers = [
    ("Layer 1", "Clean clinical case\nWhat is the correct action?"),
    ("Layer 2", "Naturalistic pressure\nReal workflow / patient / clinician pressure"),
    ("Layer 3", "Cue-contamination audit\nReal clinical message vs obvious safety test"),
    ("Layer 4", "Controller test\nRestore evidence-consistent action channel"),
]

x_positions = [0.08, 0.32, 0.56, 0.80]
for i, (title, body) in enumerate(layers):
    x = x_positions[i]
    rect = plt.Rectangle((x, 0.35), 0.17, 0.32, fill=False, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x + 0.085, 0.58, title, ha="center", va="center", fontsize=11, fontweight="bold")
    ax.text(x + 0.085, 0.47, body, ha="center", va="center", fontsize=9)

    if i < len(layers) - 1:
        ax.annotate(
            "",
            xy=(x_positions[i+1] - 0.015, 0.51),
            xytext=(x + 0.185, 0.51),
            arrowprops=dict(arrowstyle="->", linewidth=1.5),
        )

ax.text(
    0.5,
    0.15,
    "OncoGuard v0.45 four-layer evaluation architecture",
    ha="center",
    va="center",
    fontsize=12,
    fontweight="bold",
)

fig.tight_layout()
fig.savefig(FIGDIR / "figure1_four_layer_evaluation_architecture_v0_53.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------
# Figure 2 — Clean vs pressure vs controller AACR
# ---------------------------------------------------------------------

clean_aacr = 100.0
pressure_aacr = float(v47_summary["pressure_sustained_aacr_percent"].iloc[0])
controller_aacr = float(v50_summary["controller_corrected_aacr_percent"].iloc[0])

fig, ax = plt.subplots(figsize=(8, 5))
labels = ["Clean/blinded\nbenchmark", "Naturalistic\npressure", "Controller\ncorrected"]
values = [clean_aacr, pressure_aacr, controller_aacr]
bars = ax.bar(labels, values)
ax.set_ylim(0, 110)
ax.set_ylabel("AACR (%)")
ax.set_title("Action-channel accuracy across benchmark stages")
add_bar_labels(ax, bars)
fig.tight_layout()
fig.savefig(FIGDIR / "figure2_clean_pressure_controller_aacr_v0_53.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------
# Figure 3 — Expected vs selected action heatmap v0.47
# ---------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 6))
matrix = v50_expected_vs_model.copy()
im = ax.imshow(matrix.values)

ax.set_xticks(range(len(matrix.columns)))
ax.set_yticks(range(len(matrix.index)))
ax.set_xticklabels(matrix.columns, rotation=45, ha="right")
ax.set_yticklabels(matrix.index)

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        ax.text(j, i, str(matrix.iloc[i, j]), ha="center", va="center")

ax.set_xlabel("GPT-4.1 selected action")
ax.set_ylabel("Expected action")
ax.set_title("v0.47 GPT-4.1 naturalistic pressure: expected vs selected")
fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
fig.tight_layout()
fig.savefig(FIGDIR / "figure3_v0_47_expected_vs_selected_heatmap_v0_53.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------
# Figure 4 — Expected vs controller action heatmap v0.50
# ---------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 6))
matrix = v50_expected_vs_controller.copy()
im = ax.imshow(matrix.values)

ax.set_xticks(range(len(matrix.columns)))
ax.set_yticks(range(len(matrix.index)))
ax.set_xticklabels(matrix.columns, rotation=45, ha="right")
ax.set_yticklabels(matrix.index)

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        ax.text(j, i, str(matrix.iloc[i, j]), ha="center", va="center")

ax.set_xlabel("Controller-selected action")
ax.set_ylabel("Expected action")
ax.set_title("v0.50 controller: expected vs selected")
fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
fig.tight_layout()
fig.savefig(FIGDIR / "figure4_v0_50_expected_vs_controller_heatmap_v0_53.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------
# Figure 5 — Ablation AACR bar plot
# ---------------------------------------------------------------------

policy_order = [
    "unguided_model",
    "safety_block_only",
    "no_definitive_router",
    "hold_router_only",
    "switch_router_only",
    "emergency_router_only",
    "full_controller",
]

plot_df = v51_summary.copy()
plot_df["policy_order"] = plot_df["policy_name"].map({p: i for i, p in enumerate(policy_order)})
plot_df = plot_df.sort_values("policy_order")

fig, ax = plt.subplots(figsize=(11, 5))
bars = ax.bar(plot_df["policy_name"], plot_df["aacr_percent"])
ax.set_ylim(0, 110)
ax.set_ylabel("AACR (%)")
ax.set_title("v0.51 controller ablation: action-channel accuracy")
ax.set_xticklabels(plot_df["policy_name"], rotation=45, ha="right")
add_bar_labels(ax, bars)
fig.tight_layout()
fig.savefig(FIGDIR / "figure5_v0_51_ablation_aacr_v0_53.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------
# Figure 6 — Wrong-channel collapse schematic
# ---------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 5))
ax.axis("off")

ax.text(0.5, 0.90, "Conservative wrong-channel collapse under naturalistic pressure", ha="center", fontsize=13, fontweight="bold")

boxes = [
    (0.05, 0.55, "Naturalistic\nclinical pressure"),
    (0.30, 0.55, "Model recognizes\nconcern"),
    (0.55, 0.55, "Generic lower-acuity\nescalation"),
    (0.80, 0.55, "Definitive action\nmissed"),
]

for x, y, text in boxes:
    rect = plt.Rectangle((x, y), 0.16, 0.18, fill=False, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x + 0.08, y + 0.09, text, ha="center", va="center", fontsize=9)

for i in range(len(boxes) - 1):
    x = boxes[i][0]
    ax.annotate(
        "",
        xy=(boxes[i+1][0] - 0.015, 0.64),
        xytext=(x + 0.175, 0.64),
        arrowprops=dict(arrowstyle="->", linewidth=1.5),
    )

ax.text(
    0.5,
    0.30,
    "Clinical analogy: recognizing that a patient is unwell but calling a family member rather than emergency responders.",
    ha="center",
    va="center",
    fontsize=10,
)

ax.text(
    0.5,
    0.18,
    "Controller role: restore the evidence-consistent action channel.",
    ha="center",
    va="center",
    fontsize=10,
    fontweight="bold",
)

fig.tight_layout()
fig.savefig(FIGDIR / "figure6_wrong_channel_collapse_schematic_v0_53.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------
# Figure index and table index
# ---------------------------------------------------------------------

figure_index = pd.DataFrame([
    {
        "figure": "Figure 1",
        "filename": "figure1_four_layer_evaluation_architecture_v0_53.png",
        "title": "Four-layer evaluation architecture",
        "purpose": "Shows Layer 1 clean case, Layer 2 naturalistic pressure, Layer 3 cue audit, Layer 4 controller test.",
    },
    {
        "figure": "Figure 2",
        "filename": "figure2_clean_pressure_controller_aacr_v0_53.png",
        "title": "Clean vs pressure vs controller AACR",
        "purpose": "Shows ceiling clean performance, pressure collapse, and controller correction.",
    },
    {
        "figure": "Figure 3",
        "filename": "figure3_v0_47_expected_vs_selected_heatmap_v0_53.png",
        "title": "v0.47 expected vs selected action heatmap",
        "purpose": "Shows GPT-4.1 wrong-channel collapse into escalation/hold.",
    },
    {
        "figure": "Figure 4",
        "filename": "figure4_v0_50_expected_vs_controller_heatmap_v0_53.png",
        "title": "v0.50 expected vs controller-selected action heatmap",
        "purpose": "Shows controller restoration of action-channel alignment.",
    },
    {
        "figure": "Figure 5",
        "filename": "figure5_v0_51_ablation_aacr_v0_53.png",
        "title": "v0.51 ablation AACR",
        "purpose": "Shows full controller outperforms safety-block and partial-router ablations.",
    },
    {
        "figure": "Figure 6",
        "filename": "figure6_wrong_channel_collapse_schematic_v0_53.png",
        "title": "Wrong-channel collapse schematic",
        "purpose": "Explains the severity-action mismatch / action-channel interference phenotype.",
    },
])

figure_index.to_csv(OUTDIR / "figure_index_v0_53.csv", index=False)

table_index = pd.DataFrame([
    {
        "table": "Table 1",
        "filename": "table1_versioned_pipeline_provenance_v0_53.csv",
        "title": "Versioned pipeline provenance",
    },
    {
        "table": "Table 2",
        "filename": "table2_v0_47_gpt41_pressure_results_v0_53.csv",
        "title": "v0.47 GPT-4.1 pressure results",
    },
    {
        "table": "Table 3",
        "filename": "table3_v0_50_controller_before_after_v0_53.csv",
        "title": "v0.50 controller before/after results",
    },
    {
        "table": "Table 4",
        "filename": "table4_v0_51_controller_ablation_v0_53.csv",
        "title": "v0.51 controller ablation results",
    },
    {
        "table": "Table 5",
        "filename": "table5_v0_51_paired_correctness_test_v0_53.csv",
        "title": "v0.51 paired correctness test",
    },
])

table_index.to_csv(OUTDIR / "table_index_v0_53.csv", index=False)

# ---------------------------------------------------------------------
# Results card
# ---------------------------------------------------------------------

card = f"""# OncoGuard-Response v0.53 Pilot Tables and Figures

## Purpose

v0.53 creates manuscript-ready pilot tables and figures from the v0.47, v0.50, v0.51, and v0.52 pilot results.

## Main pilot story

Clean/blinded benchmark performance reached ceiling, but naturalistic pressure exposed conservative wrong-channel collapse. The deterministic evidence-contract controller restored evidence-consistent action-channel routing, and ablation showed that full routing—not simple safety blocking—was required.

## Key metrics

| Metric | Unguided GPT-4.1 under pressure | Controller |
|---|---:|---:|
| AACR | {pressure_aacr:.1f}% | {controller_aacr:.1f}% |
| Wrong-channel rate | {float(v50_summary["model_wrong_channel_percent"].iloc[0]):.1f}% | {float(v50_summary["controller_wrong_channel_percent"].iloc[0]):.1f}% |
| Wrong-channel escalation | {float(v50_summary["model_wrong_channel_escalation_percent"].iloc[0]):.1f}% | {float(v50_summary["controller_wrong_channel_escalation_percent"].iloc[0]):.1f}% |
| PTMAR | {float(v47_summary["ptmar_percent"].iloc[0]):.1f}% | {float(v50_summary["controller_ptmar_percent"].iloc[0]):.1f}% |
| Unsafe authorization | {float(v47_summary["unsafe_authorization_percent"].iloc[0]):.1f}% | {float(v50_summary["controller_unsafe_authorization_percent"].iloc[0]):.1f}% |

## Figures

{figure_index.to_markdown(index=False)}

## Tables

{table_index.to_markdown(index=False)}

## Reporting caveat

This remains a 30-probe pilot with author-domain confirmation and a deterministic evidence-contract controller. It should not be described as independent multi-rater clinical validation or a fully autonomous parser-derived controller.
"""

(OUTDIR / "onco_guard_response_v0_53_tables_figures_card.md").write_text(card)

print("Saved v0.53 tables and figures to:", OUTDIR)

print("\nTables:")
for p in sorted(TABLEDIR.glob("*.csv")):
    print(p.name)

print("\nFigures:")
for p in sorted(FIGDIR.glob("*.png")):
    print(p.name)

print("\nIndexes:")
print((OUTDIR / "figure_index_v0_53.csv").name)
print((OUTDIR / "table_index_v0_53.csv").name)
print((OUTDIR / "onco_guard_response_v0_53_tables_figures_card.md").name)
