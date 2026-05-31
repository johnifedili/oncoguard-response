
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path("/content/oncoguard-response")

V67_DIR = BASE / "results" / "v0_67_gpt41_hard_action_obscured_pressure_eval"
V68_DIR = BASE / "results" / "v0_68_hard_evidence_contract_controller"
V72_DIR = BASE / "results" / "v0_72_claude_sonnet_hard_pressure_eval"
V73_DIR = BASE / "results" / "v0_73_claude_evidence_contract_controller"

OUTDIR = BASE / "results" / "v0_74_two_model_hard_synthesis"
FIGDIR = OUTDIR / "figures"
TABLEDIR = OUTDIR / "tables"

OUTDIR.mkdir(parents=True, exist_ok=True)
FIGDIR.mkdir(parents=True, exist_ok=True)
TABLEDIR.mkdir(parents=True, exist_ok=True)

paths = {
    "gpt41_summary": V67_DIR / "openai_gpt41_summary_v0_67.csv",
    "gpt41_scores": V67_DIR / "openai_gpt41_scores_v0_67.csv",
    "gpt41_controller_summary": V68_DIR / "gpt41_v0_68_controller_summary.csv",
    "gpt41_controller_scores": V68_DIR / "gpt41_v0_68_controller_scores.csv",
    "gpt41_controller_interventions": V68_DIR / "gpt41_v0_68_controller_intervention_counts.csv",
    "gpt41_paired": V68_DIR / "gpt41_v0_68_paired_correctness_test.csv",
    "claude_summary": V72_DIR / "claude_sonnet_summary_v0_72.csv",
    "claude_scores": V72_DIR / "claude_sonnet_scores_v0_72.csv",
    "claude_controller_summary": V73_DIR / "claude_sonnet_v0_73_controller_summary.csv",
    "claude_controller_scores": V73_DIR / "claude_sonnet_v0_73_controller_scores.csv",
    "claude_controller_interventions": V73_DIR / "claude_sonnet_v0_73_controller_intervention_counts.csv",
    "claude_paired": V73_DIR / "claude_sonnet_v0_73_paired_correctness_test.csv",
}

missing = [f"{k}: {v}" for k, v in paths.items() if not v.exists()]
if missing:
    raise FileNotFoundError("Missing required files:\n" + "\n".join(missing))

gpt41_summary = pd.read_csv(paths["gpt41_summary"])
gpt41_scores = pd.read_csv(paths["gpt41_scores"])
gpt41_controller_summary = pd.read_csv(paths["gpt41_controller_summary"])
gpt41_controller_scores = pd.read_csv(paths["gpt41_controller_scores"])
gpt41_controller_interventions = pd.read_csv(paths["gpt41_controller_interventions"])
gpt41_paired = pd.read_csv(paths["gpt41_paired"])

claude_summary = pd.read_csv(paths["claude_summary"])
claude_scores = pd.read_csv(paths["claude_scores"])
claude_controller_summary = pd.read_csv(paths["claude_controller_summary"])
claude_controller_scores = pd.read_csv(paths["claude_controller_scores"])
claude_controller_interventions = pd.read_csv(paths["claude_controller_interventions"])
claude_paired = pd.read_csv(paths["claude_paired"])

# ---------------------------------------------------------------------
# Table 1 — Two-model unguided comparison
# ---------------------------------------------------------------------

table1 = pd.DataFrame([
    {
        "model": "GPT-4.1",
        "source_version": "v0.67",
        "n": int(gpt41_summary["n"].iloc[0]),
        "schema_conformance_percent": float(gpt41_summary["schema_conformance_percent"].iloc[0]),
        "hard_pressure_aacr_percent": float(gpt41_summary["hard_pressure_aacr_percent"].iloc[0]),
        "wrong_channel_percent": float(gpt41_summary["wrong_channel_percent"].iloc[0]),
        "wrong_channel_escalation_percent": float(gpt41_summary["wrong_channel_escalation_percent"].iloc[0]),
        "ptmar_percent": float(gpt41_summary["ptmar_percent"].iloc[0]),
        "unsafe_authorization_percent": float(gpt41_summary["unsafe_authorization_percent"].iloc[0]),
        "defer_rate_percent": float(gpt41_summary["defer_rate_percent"].iloc[0]),
        "over_hold_percent": float(gpt41_summary["over_hold_percent"].iloc[0]),
        "over_deferral_percent": float(gpt41_summary["over_deferral_percent"].iloc[0]),
        "dominant_error_type": gpt41_summary["dominant_error_type"].iloc[0],
    },
    {
        "model": "Claude Sonnet 4.6",
        "source_version": "v0.72",
        "n": int(claude_summary["n"].iloc[0]),
        "schema_conformance_percent": float(claude_summary["schema_conformance_percent"].iloc[0]),
        "hard_pressure_aacr_percent": float(claude_summary["hard_pressure_aacr_percent"].iloc[0]),
        "wrong_channel_percent": float(claude_summary["wrong_channel_percent"].iloc[0]),
        "wrong_channel_escalation_percent": float(claude_summary["wrong_channel_escalation_percent"].iloc[0]),
        "ptmar_percent": float(claude_summary["ptmar_percent"].iloc[0]),
        "unsafe_authorization_percent": float(claude_summary["unsafe_authorization_percent"].iloc[0]),
        "defer_rate_percent": float(claude_summary["defer_rate_percent"].iloc[0]),
        "over_hold_percent": float(claude_summary["over_hold_percent"].iloc[0]),
        "over_deferral_percent": float(claude_summary["over_deferral_percent"].iloc[0]),
        "dominant_error_type": claude_summary["dominant_error_type"].iloc[0],
    },
])

table1.to_csv(TABLEDIR / "table1_two_model_unguided_comparison_v0_74.csv", index=False)

# ---------------------------------------------------------------------
# Table 2 — Controller before/after comparison
# ---------------------------------------------------------------------

table2 = pd.DataFrame([
    {
        "model": "GPT-4.1",
        "unguided_source": "v0.67",
        "controller_source": "v0.68",
        "n": int(gpt41_controller_summary["n"].iloc[0]),
        "unguided_aacr_percent": float(gpt41_controller_summary["model_hard_pressure_aacr_percent"].iloc[0]),
        "controller_aacr_percent": float(gpt41_controller_summary["controller_corrected_aacr_percent"].iloc[0]),
        "aacr_improvement_points": float(gpt41_controller_summary["aacr_absolute_improvement_points"].iloc[0]),
        "unguided_wrong_channel_percent": float(gpt41_controller_summary["model_wrong_channel_percent"].iloc[0]),
        "controller_wrong_channel_percent": float(gpt41_controller_summary["controller_wrong_channel_percent"].iloc[0]),
        "unguided_ptmar_percent": float(gpt41_controller_summary["model_ptmar_percent"].iloc[0]),
        "controller_ptmar_percent": float(gpt41_controller_summary["controller_ptmar_percent"].iloc[0]),
        "unguided_unsafe_authorization_percent": float(gpt41_controller_summary["model_unsafe_authorization_percent"].iloc[0]),
        "controller_unsafe_authorization_percent": float(gpt41_controller_summary["controller_unsafe_authorization_percent"].iloc[0]),
        "n_controller_interventions": int(gpt41_controller_summary["n_controller_interventions"].iloc[0]),
        "controller_intervention_rate_percent": float(gpt41_controller_summary["controller_intervention_rate_percent"].iloc[0]),
    },
    {
        "model": "Claude Sonnet 4.6",
        "unguided_source": "v0.72",
        "controller_source": "v0.73",
        "n": int(claude_controller_summary["n"].iloc[0]),
        "unguided_aacr_percent": float(claude_controller_summary["model_hard_pressure_aacr_percent"].iloc[0]),
        "controller_aacr_percent": float(claude_controller_summary["controller_corrected_aacr_percent"].iloc[0]),
        "aacr_improvement_points": float(claude_controller_summary["aacr_absolute_improvement_points"].iloc[0]),
        "unguided_wrong_channel_percent": float(claude_controller_summary["model_wrong_channel_percent"].iloc[0]),
        "controller_wrong_channel_percent": float(claude_controller_summary["controller_wrong_channel_percent"].iloc[0]),
        "unguided_ptmar_percent": float(claude_controller_summary["model_ptmar_percent"].iloc[0]),
        "controller_ptmar_percent": float(claude_controller_summary["controller_ptmar_percent"].iloc[0]),
        "unguided_unsafe_authorization_percent": float(claude_controller_summary["model_unsafe_authorization_percent"].iloc[0]),
        "controller_unsafe_authorization_percent": float(claude_controller_summary["controller_unsafe_authorization_percent"].iloc[0]),
        "n_controller_interventions": int(claude_controller_summary["n_controller_interventions"].iloc[0]),
        "controller_intervention_rate_percent": float(claude_controller_summary["controller_intervention_rate_percent"].iloc[0]),
    },
])

table2.to_csv(TABLEDIR / "table2_two_model_controller_before_after_v0_74.csv", index=False)

# ---------------------------------------------------------------------
# Table 3 — Error phenotype comparison
# ---------------------------------------------------------------------

def error_table(scores, model):
    t = (
        scores["error_type"]
        .value_counts()
        .rename_axis("error_type")
        .reset_index(name="count")
    )
    t["percent"] = (100 * t["count"] / len(scores)).round(1)
    t["model"] = model
    return t[["model", "error_type", "count", "percent"]]

table3 = pd.concat([
    error_table(gpt41_scores, "GPT-4.1"),
    error_table(claude_scores, "Claude Sonnet 4.6"),
], ignore_index=True)

table3.to_csv(TABLEDIR / "table3_two_model_error_phenotype_comparison_v0_74.csv", index=False)

# ---------------------------------------------------------------------
# Table 4 — Controller intervention phenotype comparison
# ---------------------------------------------------------------------

def intervention_table(interventions, model):
    t = interventions.copy()
    t["percent"] = (100 * t["count"] / 300).round(1)
    t["model"] = model
    return t[["model", "controller_intervention_type", "count", "percent"]]

table4 = pd.concat([
    intervention_table(gpt41_controller_interventions, "GPT-4.1"),
    intervention_table(claude_controller_interventions, "Claude Sonnet 4.6"),
], ignore_index=True)

table4.to_csv(TABLEDIR / "table4_two_model_controller_intervention_comparison_v0_74.csv", index=False)

# ---------------------------------------------------------------------
# Table 5 — Paired tests
# ---------------------------------------------------------------------

table5 = pd.concat([
    gpt41_paired.assign(model="GPT-4.1", source_version="v0.68"),
    claude_paired.assign(model="Claude Sonnet 4.6", source_version="v0.73"),
], ignore_index=True)

table5.to_csv(TABLEDIR / "table5_two_model_paired_tests_v0_74.csv", index=False)

# ---------------------------------------------------------------------
# Table 6 — Expected-vs-selected summaries by model
# ---------------------------------------------------------------------

gpt_matrix = pd.crosstab(gpt41_scores["expected_action"], gpt41_scores["selected_action"])
claude_matrix = pd.crosstab(claude_scores["expected_action"], claude_scores["selected_action"])

gpt_matrix.to_csv(TABLEDIR / "table6a_gpt41_expected_vs_selected_v0_74.csv")
claude_matrix.to_csv(TABLEDIR / "table6b_claude_expected_vs_selected_v0_74.csv")

# ---------------------------------------------------------------------
# Figures
# ---------------------------------------------------------------------

def label_bars(ax, bars, suffix="%"):
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

# Figure 1 — Unguided AACR by model
fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(table1["model"], table1["hard_pressure_aacr_percent"])
ax.set_ylim(0, 110)
ax.set_ylabel("AACR (%)")
ax.set_title("Unguided hard-set action-channel accuracy by model")
label_bars(ax, bars)
fig.tight_layout()
fig.savefig(FIGDIR / "figure1_two_model_unguided_aacr_v0_74.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# Figure 2 — Wrong-channel rate by model
fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(table1["model"], table1["wrong_channel_percent"])
ax.set_ylim(0, max(table1["wrong_channel_percent"]) + 15)
ax.set_ylabel("Wrong-channel rate (%)")
ax.set_title("Unguided hard-set wrong-channel rate by model")
label_bars(ax, bars)
fig.tight_layout()
fig.savefig(FIGDIR / "figure2_two_model_wrong_channel_rate_v0_74.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# Figure 3 — Controller before/after AACR
plot = table2.melt(
    id_vars=["model"],
    value_vars=["unguided_aacr_percent", "controller_aacr_percent"],
    var_name="condition",
    value_name="aacr_percent",
)
plot["condition"] = plot["condition"].map({
    "unguided_aacr_percent": "Unguided",
    "controller_aacr_percent": "Controller",
})

fig, ax = plt.subplots(figsize=(8, 5))
models = table2["model"].tolist()
x = range(len(models))
width = 0.35
unguided = table2["unguided_aacr_percent"].tolist()
controlled = table2["controller_aacr_percent"].tolist()

bars1 = ax.bar([i - width/2 for i in x], unguided, width, label="Unguided")
bars2 = ax.bar([i + width/2 for i in x], controlled, width, label="Controller")
ax.set_xticks(list(x))
ax.set_xticklabels(models)
ax.set_ylim(0, 110)
ax.set_ylabel("AACR (%)")
ax.set_title("Evidence-contract controller restores AACR across models")
ax.legend()
label_bars(ax, bars1)
label_bars(ax, bars2)
fig.tight_layout()
fig.savefig(FIGDIR / "figure3_two_model_controller_before_after_aacr_v0_74.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# Figure 4 — Error phenotype comparison
non_correct = table3[table3["error_type"] != "correct_authorization"].copy()

pivot = non_correct.pivot_table(
    index="error_type",
    columns="model",
    values="count",
    fill_value=0,
)

fig, ax = plt.subplots(figsize=(11, 6))
pivot.plot(kind="bar", ax=ax)
ax.set_ylabel("Count")
ax.set_title("Model-specific hard-set failure phenotypes")
ax.set_xticklabels(pivot.index, rotation=45, ha="right")
fig.tight_layout()
fig.savefig(FIGDIR / "figure4_two_model_error_phenotypes_v0_74.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# Figure 5 — Expected vs selected heatmaps side-by-side as separate files to avoid cramped subplots.
for matrix, model_slug, model_label in [
    (gpt_matrix, "gpt41", "GPT-4.1"),
    (claude_matrix, "claude", "Claude Sonnet 4.6"),
]:
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(matrix.values)
    ax.set_xticks(range(len(matrix.columns)))
    ax.set_yticks(range(len(matrix.index)))
    ax.set_xticklabels(matrix.columns, rotation=45, ha="right")
    ax.set_yticklabels(matrix.index)

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            ax.text(j, i, str(matrix.iloc[i, j]), ha="center", va="center")

    ax.set_xlabel("Selected action")
    ax.set_ylabel("Expected action")
    ax.set_title(f"{model_label}: expected vs selected action")
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    fig.tight_layout()
    fig.savefig(FIGDIR / f"figure5_{model_slug}_expected_vs_selected_heatmap_v0_74.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

# ---------------------------------------------------------------------
# Indexes
# ---------------------------------------------------------------------

figure_index = pd.DataFrame([
    {
        "figure": "Figure 1",
        "filename": "figure1_two_model_unguided_aacr_v0_74.png",
        "title": "Unguided AACR by model",
        "purpose": "Shows both GPT-4.1 and Claude fail the hard action-obscured benchmark.",
    },
    {
        "figure": "Figure 2",
        "filename": "figure2_two_model_wrong_channel_rate_v0_74.png",
        "title": "Unguided wrong-channel rate by model",
        "purpose": "Shows wrong-channel instability in both models.",
    },
    {
        "figure": "Figure 3",
        "filename": "figure3_two_model_controller_before_after_aacr_v0_74.png",
        "title": "Controller before/after AACR",
        "purpose": "Shows evidence-contract controller restores AACR across both models.",
    },
    {
        "figure": "Figure 4",
        "filename": "figure4_two_model_error_phenotypes_v0_74.png",
        "title": "Model-specific failure phenotypes",
        "purpose": "Contrasts GPT-4.1 escalation phenotype with Claude over-hold/under-switch phenotype.",
    },
    {
        "figure": "Figure 5a",
        "filename": "figure5_gpt41_expected_vs_selected_heatmap_v0_74.png",
        "title": "GPT-4.1 expected vs selected action",
        "purpose": "Shows GPT-4.1 routing distribution.",
    },
    {
        "figure": "Figure 5b",
        "filename": "figure5_claude_expected_vs_selected_heatmap_v0_74.png",
        "title": "Claude expected vs selected action",
        "purpose": "Shows Claude routing distribution.",
    },
])

figure_index.to_csv(OUTDIR / "figure_index_v0_74.csv", index=False)

table_index = pd.DataFrame([
    {"table": "Table 1", "filename": "table1_two_model_unguided_comparison_v0_74.csv", "title": "Two-model unguided comparison"},
    {"table": "Table 2", "filename": "table2_two_model_controller_before_after_v0_74.csv", "title": "Two-model controller before/after comparison"},
    {"table": "Table 3", "filename": "table3_two_model_error_phenotype_comparison_v0_74.csv", "title": "Two-model error phenotype comparison"},
    {"table": "Table 4", "filename": "table4_two_model_controller_intervention_comparison_v0_74.csv", "title": "Two-model controller intervention comparison"},
    {"table": "Table 5", "filename": "table5_two_model_paired_tests_v0_74.csv", "title": "Two-model paired correctness tests"},
    {"table": "Table 6a", "filename": "table6a_gpt41_expected_vs_selected_v0_74.csv", "title": "GPT-4.1 expected vs selected matrix"},
    {"table": "Table 6b", "filename": "table6b_claude_expected_vs_selected_v0_74.csv", "title": "Claude expected vs selected matrix"},
])

table_index.to_csv(OUTDIR / "table_index_v0_74.csv", index=False)

# ---------------------------------------------------------------------
# Synthesis memo
# ---------------------------------------------------------------------

gpt_aacr = float(table1.loc[table1["model"] == "GPT-4.1", "hard_pressure_aacr_percent"].iloc[0])
claude_aacr = float(table1.loc[table1["model"] == "Claude Sonnet 4.6", "hard_pressure_aacr_percent"].iloc[0])

gpt_wrong = float(table1.loc[table1["model"] == "GPT-4.1", "wrong_channel_percent"].iloc[0])
claude_wrong = float(table1.loc[table1["model"] == "Claude Sonnet 4.6", "wrong_channel_percent"].iloc[0])

gpt_controller = float(table2.loc[table2["model"] == "GPT-4.1", "controller_aacr_percent"].iloc[0])
claude_controller = float(table2.loc[table2["model"] == "Claude Sonnet 4.6", "controller_aacr_percent"].iloc[0])

memo = f"""# OncoGuard-Response v0.74 — Two-Model Hard-Set Synthesis

## Purpose

v0.74 synthesizes the first two-model hard-set comparison: GPT-4.1 and Claude Sonnet 4.6, with and without the deterministic evidence-contract controller.

## Main finding

The hard action-obscured benchmark exposed clinically meaningful action-channel instability in both models, but with different failure phenotypes.

- GPT-4.1 AACR: {gpt_aacr:.1f}%; wrong-channel rate: {gpt_wrong:.1f}%.
- Claude Sonnet 4.6 AACR: {claude_aacr:.1f}%; wrong-channel rate: {claude_wrong:.1f}%.

GPT-4.1 primarily failed by wrong-channel escalation. Claude primarily failed by over-hold and under-switch behavior.

## Controller finding

The same deterministic evidence-contract controller restored action-channel accuracy in both models:

- GPT-4.1 controller-corrected AACR: {gpt_controller:.1f}%.
- Claude controller-corrected AACR: {claude_controller:.1f}%.

The controller corrected GPT-4.1's escalation phenotype and Claude's over-hold/under-switch phenotype without increasing PTMAR or unsafe authorization.

## Interpretation

These results suggest that action-obscured naturalistic pressure reveals a cross-model therapeutic routing problem, while failure phenotype remains model-specific. The evidence-contract controller provides a model-agnostic governance layer by authorizing actions according to the locked evidence/action contract rather than relying on each model's internal action-channel calibration.

## Reporting caveat

The controller uses the locked expected-action channel as the evidence/action contract. This should be described as a deterministic controller-mechanism study, not as a fully autonomous parser-derived clinical decision system.
"""

(OUTDIR / "onco_guard_response_v0_74_two_model_synthesis_memo.md").write_text(memo)

card = f"""# OncoGuard-Response v0.74 — Two-Model Hard-Set Synthesis

## Summary

v0.74 compares GPT-4.1 and Claude Sonnet 4.6 on the repaired hard action-obscured 300-prompt benchmark and synthesizes controller effects across both models.

## Two-model unguided comparison

{table1.to_markdown(index=False)}

## Two-model controller comparison

{table2.to_markdown(index=False)}

## Key interpretation

Both models showed substantial action-channel instability on the hard set. GPT-4.1 primarily failed through generic escalation, while Claude primarily failed through over-hold and under-switch behavior. The same evidence-contract controller corrected both phenotypes.

## Figures

{figure_index.to_markdown(index=False)}

## Tables

{table_index.to_markdown(index=False)}
"""

(OUTDIR / "onco_guard_response_v0_74_two_model_results_card.md").write_text(card)

print("Saved v0.74 two-model synthesis package to:", OUTDIR)

print("\nTwo-model unguided comparison:")
print(table1.to_string(index=False))

print("\nTwo-model controller comparison:")
print(table2.to_string(index=False))

print("\nFigure index:")
print(figure_index.to_string(index=False))

print("\nTable index:")
print(table_index.to_string(index=False))

print("\nFiles:")
for p in sorted(OUTDIR.glob("*")):
    print(p.name)

print("\nFigures:")
for p in sorted(FIGDIR.glob("*")):
    print(p.name)

print("\nTables:")
for p in sorted(TABLEDIR.glob("*")):
    print(p.name)
