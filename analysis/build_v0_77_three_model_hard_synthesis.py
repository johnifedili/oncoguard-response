
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path("/content/oncoguard-response")

V67_DIR = BASE / "results" / "v0_67_gpt41_hard_action_obscured_pressure_eval"
V68_DIR = BASE / "results" / "v0_68_hard_evidence_contract_controller"

V72_DIR = BASE / "results" / "v0_72_claude_sonnet_hard_pressure_eval"
V73_DIR = BASE / "results" / "v0_73_claude_evidence_contract_controller"

V75_DIR = BASE / "results" / "v0_75_gemini_flash_hard_pressure_eval"
V76_DIR = BASE / "results" / "v0_76_gemini_evidence_contract_controller"

OUTDIR = BASE / "results" / "v0_77_three_model_hard_synthesis"
FIGDIR = OUTDIR / "figures"
TABLEDIR = OUTDIR / "tables"

OUTDIR.mkdir(parents=True, exist_ok=True)
FIGDIR.mkdir(parents=True, exist_ok=True)
TABLEDIR.mkdir(parents=True, exist_ok=True)

paths = {
    "gpt41_summary": V67_DIR / "openai_gpt41_summary_v0_67.csv",
    "gpt41_scores": V67_DIR / "openai_gpt41_scores_v0_67.csv",
    "gpt41_controller_summary": V68_DIR / "gpt41_v0_68_controller_summary.csv",
    "gpt41_controller_interventions": V68_DIR / "gpt41_v0_68_controller_intervention_counts.csv",
    "gpt41_paired": V68_DIR / "gpt41_v0_68_paired_correctness_test.csv",

    "claude_summary": V72_DIR / "claude_sonnet_summary_v0_72.csv",
    "claude_scores": V72_DIR / "claude_sonnet_scores_v0_72.csv",
    "claude_controller_summary": V73_DIR / "claude_sonnet_v0_73_controller_summary.csv",
    "claude_controller_interventions": V73_DIR / "claude_sonnet_v0_73_controller_intervention_counts.csv",
    "claude_paired": V73_DIR / "claude_sonnet_v0_73_paired_correctness_test.csv",

    "gemini_summary": V75_DIR / "gemini_flash_summary_v0_75.csv",
    "gemini_scores": V75_DIR / "gemini_flash_scores_v0_75.csv",
    "gemini_controller_summary": V76_DIR / "gemini_flash_v0_76_controller_summary.csv",
    "gemini_controller_interventions": V76_DIR / "gemini_flash_v0_76_controller_intervention_counts.csv",
    "gemini_paired": V76_DIR / "gemini_flash_v0_76_paired_correctness_test.csv",
}

missing = [f"{k}: {v}" for k, v in paths.items() if not v.exists()]
if missing:
    raise FileNotFoundError("Missing required files:\n" + "\n".join(missing))

gpt41_summary = pd.read_csv(paths["gpt41_summary"])
gpt41_scores = pd.read_csv(paths["gpt41_scores"])
gpt41_controller_summary = pd.read_csv(paths["gpt41_controller_summary"])
gpt41_controller_interventions = pd.read_csv(paths["gpt41_controller_interventions"])
gpt41_paired = pd.read_csv(paths["gpt41_paired"])

claude_summary = pd.read_csv(paths["claude_summary"])
claude_scores = pd.read_csv(paths["claude_scores"])
claude_controller_summary = pd.read_csv(paths["claude_controller_summary"])
claude_controller_interventions = pd.read_csv(paths["claude_controller_interventions"])
claude_paired = pd.read_csv(paths["claude_paired"])

gemini_summary = pd.read_csv(paths["gemini_summary"])
gemini_scores = pd.read_csv(paths["gemini_scores"])
gemini_controller_summary = pd.read_csv(paths["gemini_controller_summary"])
gemini_controller_interventions = pd.read_csv(paths["gemini_controller_interventions"])
gemini_paired = pd.read_csv(paths["gemini_paired"])

# ---------------------------------------------------------------------
# Table 1 — Three-model unguided comparison
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
        "phenotype_label": "generic_escalation_collapse",
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
        "phenotype_label": "over_hold_under_switch_collapse",
    },
    {
        "model": "Gemini Flash",
        "source_version": "v0.75",
        "n": int(gemini_summary["n"].iloc[0]),
        "schema_conformance_percent": float(gemini_summary["schema_conformance_percent"].iloc[0]),
        "hard_pressure_aacr_percent": float(gemini_summary["hard_pressure_aacr_percent"].iloc[0]),
        "wrong_channel_percent": float(gemini_summary["wrong_channel_percent"].iloc[0]),
        "wrong_channel_escalation_percent": float(gemini_summary["wrong_channel_escalation_percent"].iloc[0]),
        "ptmar_percent": float(gemini_summary["ptmar_percent"].iloc[0]),
        "unsafe_authorization_percent": float(gemini_summary["unsafe_authorization_percent"].iloc[0]),
        "defer_rate_percent": float(gemini_summary["defer_rate_percent"].iloc[0]),
        "over_hold_percent": float(gemini_summary["over_hold_percent"].iloc[0]),
        "over_deferral_percent": float(gemini_summary["over_deferral_percent"].iloc[0]),
        "dominant_error_type": gemini_summary["dominant_error_type"].iloc[0],
        "phenotype_label": "under_hold_generic_escalation_collapse",
    },
])

table1.to_csv(TABLEDIR / "table1_three_model_unguided_comparison_v0_77.csv", index=False)

# ---------------------------------------------------------------------
# Table 2 — Three-model controller before/after
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
    {
        "model": "Gemini Flash",
        "unguided_source": "v0.75",
        "controller_source": "v0.76",
        "n": int(gemini_controller_summary["n"].iloc[0]),
        "unguided_aacr_percent": float(gemini_controller_summary["model_hard_pressure_aacr_percent"].iloc[0]),
        "controller_aacr_percent": float(gemini_controller_summary["controller_corrected_aacr_percent"].iloc[0]),
        "aacr_improvement_points": float(gemini_controller_summary["aacr_absolute_improvement_points"].iloc[0]),
        "unguided_wrong_channel_percent": float(gemini_controller_summary["model_wrong_channel_percent"].iloc[0]),
        "controller_wrong_channel_percent": float(gemini_controller_summary["controller_wrong_channel_percent"].iloc[0]),
        "unguided_ptmar_percent": float(gemini_controller_summary["model_ptmar_percent"].iloc[0]),
        "controller_ptmar_percent": float(gemini_controller_summary["controller_ptmar_percent"].iloc[0]),
        "unguided_unsafe_authorization_percent": float(gemini_controller_summary["model_unsafe_authorization_percent"].iloc[0]),
        "controller_unsafe_authorization_percent": float(gemini_controller_summary["controller_unsafe_authorization_percent"].iloc[0]),
        "n_controller_interventions": int(gemini_controller_summary["n_controller_interventions"].iloc[0]),
        "controller_intervention_rate_percent": float(gemini_controller_summary["controller_intervention_rate_percent"].iloc[0]),
    },
])

table2.to_csv(TABLEDIR / "table2_three_model_controller_before_after_v0_77.csv", index=False)

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
    error_table(gemini_scores, "Gemini Flash"),
], ignore_index=True)

table3.to_csv(TABLEDIR / "table3_three_model_error_phenotype_comparison_v0_77.csv", index=False)

# ---------------------------------------------------------------------
# Table 4 — Controller intervention comparison
# ---------------------------------------------------------------------

def intervention_table(interventions, model):
    t = interventions.copy()
    t["percent"] = (100 * t["count"] / 300).round(1)
    t["model"] = model
    return t[["model", "controller_intervention_type", "count", "percent"]]

table4 = pd.concat([
    intervention_table(gpt41_controller_interventions, "GPT-4.1"),
    intervention_table(claude_controller_interventions, "Claude Sonnet 4.6"),
    intervention_table(gemini_controller_interventions, "Gemini Flash"),
], ignore_index=True)

table4.to_csv(TABLEDIR / "table4_three_model_controller_intervention_comparison_v0_77.csv", index=False)

# ---------------------------------------------------------------------
# Table 5 — Paired tests
# ---------------------------------------------------------------------

table5 = pd.concat([
    gpt41_paired.assign(model="GPT-4.1", source_version="v0.68"),
    claude_paired.assign(model="Claude Sonnet 4.6", source_version="v0.73"),
    gemini_paired.assign(model="Gemini Flash", source_version="v0.76"),
], ignore_index=True)

table5.to_csv(TABLEDIR / "table5_three_model_paired_tests_v0_77.csv", index=False)

# ---------------------------------------------------------------------
# Table 6 — Expected-vs-selected matrices
# ---------------------------------------------------------------------

gpt_matrix = pd.crosstab(gpt41_scores["expected_action"], gpt41_scores["selected_action"])
claude_matrix = pd.crosstab(claude_scores["expected_action"], claude_scores["selected_action"])
gemini_matrix = pd.crosstab(gemini_scores["expected_action"], gemini_scores["selected_action"])

gpt_matrix.to_csv(TABLEDIR / "table6a_gpt41_expected_vs_selected_v0_77.csv")
claude_matrix.to_csv(TABLEDIR / "table6b_claude_expected_vs_selected_v0_77.csv")
gemini_matrix.to_csv(TABLEDIR / "table6c_gemini_expected_vs_selected_v0_77.csv")

# ---------------------------------------------------------------------
# Figure helpers
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

# Figure 1 — Unguided AACR
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(table1["model"], table1["hard_pressure_aacr_percent"])
ax.set_ylim(0, 110)
ax.set_ylabel("AACR (%)")
ax.set_title("Unguided hard-set action-channel accuracy by model")
label_bars(ax, bars)
fig.tight_layout()
fig.savefig(FIGDIR / "figure1_three_model_unguided_aacr_v0_77.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# Figure 2 — Wrong-channel rate
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(table1["model"], table1["wrong_channel_percent"])
ax.set_ylim(0, max(table1["wrong_channel_percent"]) + 15)
ax.set_ylabel("Wrong-channel rate (%)")
ax.set_title("Unguided hard-set wrong-channel rate by model")
label_bars(ax, bars)
fig.tight_layout()
fig.savefig(FIGDIR / "figure2_three_model_wrong_channel_rate_v0_77.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# Figure 3 — Controller before/after AACR
fig, ax = plt.subplots(figsize=(9, 5))
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
ax.set_title("Evidence-contract controller restores AACR across three models")
ax.legend()
label_bars(ax, bars1)
label_bars(ax, bars2)
fig.tight_layout()
fig.savefig(FIGDIR / "figure3_three_model_controller_before_after_aacr_v0_77.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# Figure 4 — Error phenotype comparison
non_correct = table3[table3["error_type"] != "correct_authorization"].copy()

pivot = non_correct.pivot_table(
    index="error_type",
    columns="model",
    values="count",
    fill_value=0,
)

fig, ax = plt.subplots(figsize=(12, 6))
pivot.plot(kind="bar", ax=ax)
ax.set_ylabel("Count")
ax.set_title("Three-model hard-set failure phenotypes")
ax.set_xticklabels(pivot.index, rotation=45, ha="right")
fig.tight_layout()
fig.savefig(FIGDIR / "figure4_three_model_error_phenotypes_v0_77.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# Figure 5 — Controller intervention comparison
pivot2 = table4[table4["controller_intervention_type"] != "no_intervention_needed"].pivot_table(
    index="controller_intervention_type",
    columns="model",
    values="count",
    fill_value=0,
)

fig, ax = plt.subplots(figsize=(12, 6))
pivot2.plot(kind="bar", ax=ax)
ax.set_ylabel("Count")
ax.set_title("Controller intervention phenotypes across models")
ax.set_xticklabels(pivot2.index, rotation=45, ha="right")
fig.tight_layout()
fig.savefig(FIGDIR / "figure5_three_model_controller_interventions_v0_77.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# Figure 6 — Expected vs selected heatmaps
for matrix, model_slug, model_label in [
    (gpt_matrix, "gpt41", "GPT-4.1"),
    (claude_matrix, "claude", "Claude Sonnet 4.6"),
    (gemini_matrix, "gemini", "Gemini Flash"),
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
    fig.savefig(FIGDIR / f"figure6_{model_slug}_expected_vs_selected_heatmap_v0_77.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

# ---------------------------------------------------------------------
# Indexes
# ---------------------------------------------------------------------

figure_index = pd.DataFrame([
    {
        "figure": "Figure 1",
        "filename": "figure1_three_model_unguided_aacr_v0_77.png",
        "title": "Unguided AACR by model",
        "purpose": "Shows all three models have imperfect action-channel accuracy on the hard benchmark.",
    },
    {
        "figure": "Figure 2",
        "filename": "figure2_three_model_wrong_channel_rate_v0_77.png",
        "title": "Unguided wrong-channel rate by model",
        "purpose": "Shows wrong-channel instability across all three models.",
    },
    {
        "figure": "Figure 3",
        "filename": "figure3_three_model_controller_before_after_aacr_v0_77.png",
        "title": "Controller before/after AACR",
        "purpose": "Shows evidence-contract controller restores AACR across all three models.",
    },
    {
        "figure": "Figure 4",
        "filename": "figure4_three_model_error_phenotypes_v0_77.png",
        "title": "Three-model failure phenotypes",
        "purpose": "Contrasts GPT-4.1 escalation, Claude over-hold/under-switch, and Gemini under-hold/escalation phenotypes.",
    },
    {
        "figure": "Figure 5",
        "filename": "figure5_three_model_controller_interventions_v0_77.png",
        "title": "Controller intervention phenotypes",
        "purpose": "Shows which model-specific failures the controller corrected.",
    },
    {
        "figure": "Figure 6a",
        "filename": "figure6_gpt41_expected_vs_selected_heatmap_v0_77.png",
        "title": "GPT-4.1 expected vs selected action",
        "purpose": "Shows GPT-4.1 routing distribution.",
    },
    {
        "figure": "Figure 6b",
        "filename": "figure6_claude_expected_vs_selected_heatmap_v0_77.png",
        "title": "Claude expected vs selected action",
        "purpose": "Shows Claude routing distribution.",
    },
    {
        "figure": "Figure 6c",
        "filename": "figure6_gemini_expected_vs_selected_heatmap_v0_77.png",
        "title": "Gemini expected vs selected action",
        "purpose": "Shows Gemini routing distribution.",
    },
])

figure_index.to_csv(OUTDIR / "figure_index_v0_77.csv", index=False)

table_index = pd.DataFrame([
    {"table": "Table 1", "filename": "table1_three_model_unguided_comparison_v0_77.csv", "title": "Three-model unguided comparison"},
    {"table": "Table 2", "filename": "table2_three_model_controller_before_after_v0_77.csv", "title": "Three-model controller before/after comparison"},
    {"table": "Table 3", "filename": "table3_three_model_error_phenotype_comparison_v0_77.csv", "title": "Three-model error phenotype comparison"},
    {"table": "Table 4", "filename": "table4_three_model_controller_intervention_comparison_v0_77.csv", "title": "Three-model controller intervention comparison"},
    {"table": "Table 5", "filename": "table5_three_model_paired_tests_v0_77.csv", "title": "Three-model paired correctness tests"},
    {"table": "Table 6a", "filename": "table6a_gpt41_expected_vs_selected_v0_77.csv", "title": "GPT-4.1 expected vs selected matrix"},
    {"table": "Table 6b", "filename": "table6b_claude_expected_vs_selected_v0_77.csv", "title": "Claude expected vs selected matrix"},
    {"table": "Table 6c", "filename": "table6c_gemini_expected_vs_selected_v0_77.csv", "title": "Gemini expected vs selected matrix"},
])

table_index.to_csv(OUTDIR / "table_index_v0_77.csv", index=False)

# ---------------------------------------------------------------------
# Synthesis memo and card
# ---------------------------------------------------------------------

memo = f"""# OncoGuard-Response v0.77 — Three-Model Hard-Set Synthesis and Controller Comparison

## Purpose

v0.77 synthesizes the three-model hard action-obscured benchmark results and controller effects across GPT-4.1, Claude Sonnet 4.6, and Gemini Flash.

## Core finding

All three models showed clinically meaningful action-channel instability under the repaired hard action-obscured oncology therapeutic-authorization benchmark.

Unguided AACR:

- GPT-4.1: {table1.loc[table1['model']=='GPT-4.1','hard_pressure_aacr_percent'].iloc[0]:.1f}%.
- Claude Sonnet 4.6: {table1.loc[table1['model']=='Claude Sonnet 4.6','hard_pressure_aacr_percent'].iloc[0]:.1f}%.
- Gemini Flash: {table1.loc[table1['model']=='Gemini Flash','hard_pressure_aacr_percent'].iloc[0]:.1f}%.

Wrong-channel rate:

- GPT-4.1: {table1.loc[table1['model']=='GPT-4.1','wrong_channel_percent'].iloc[0]:.1f}%.
- Claude Sonnet 4.6: {table1.loc[table1['model']=='Claude Sonnet 4.6','wrong_channel_percent'].iloc[0]:.1f}%.
- Gemini Flash: {table1.loc[table1['model']=='Gemini Flash','wrong_channel_percent'].iloc[0]:.1f}%.

## Model-specific failure phenotypes

The hard benchmark revealed distinct model-specific routing phenotypes:

- GPT-4.1 primarily failed through generic wrong-channel escalation.
- Claude Sonnet 4.6 primarily failed through over-hold and under-switch behavior.
- Gemini Flash performed best overall but still showed under-hold and generic-escalation routing failures.

## Controller result

The deterministic evidence-contract controller restored evidence-consistent authorization across all three models:

- GPT-4.1: {table2.loc[table2['model']=='GPT-4.1','unguided_aacr_percent'].iloc[0]:.1f}% → {table2.loc[table2['model']=='GPT-4.1','controller_aacr_percent'].iloc[0]:.1f}%.
- Claude Sonnet 4.6: {table2.loc[table2['model']=='Claude Sonnet 4.6','unguided_aacr_percent'].iloc[0]:.1f}% → {table2.loc[table2['model']=='Claude Sonnet 4.6','controller_aacr_percent'].iloc[0]:.1f}%.
- Gemini Flash: {table2.loc[table2['model']=='Gemini Flash','unguided_aacr_percent'].iloc[0]:.1f}% → {table2.loc[table2['model']=='Gemini Flash','controller_aacr_percent'].iloc[0]:.1f}%.

Across all three controller runs, wrong-channel rate, PTMAR, and unsafe authorization were reduced to 0.0% under the locked deterministic evidence/action contract.

## Interpretation

The results support a cross-model governance thesis: action-obscured naturalistic clinical pressure can expose therapeutic routing instability even when schema conformance is perfect. The specific failure phenotype varies by model, but a deterministic evidence-contract controller can normalize these failures by separating model reasoning from action authorization.

## Reporting caveat

The controller uses the locked expected-action channel as the evidence/action contract. It should be reported as a deterministic controller-mechanism study, not as a fully autonomous parser-derived clinical decision system.
"""

(OUTDIR / "onco_guard_response_v0_77_three_model_synthesis_memo.md").write_text(memo)

card = f"""# OncoGuard-Response v0.77 — Three-Model Hard-Set Synthesis

## Summary

v0.77 compares GPT-4.1, Claude Sonnet 4.6, and Gemini Flash on the repaired hard action-obscured 300-prompt benchmark and synthesizes controller effects across all three models.

## Three-model unguided comparison

{table1.to_markdown(index=False)}

## Three-model controller comparison

{table2.to_markdown(index=False)}

## Key interpretation

All three models showed hard-set action-channel instability. Failure phenotype varied by model, while the same deterministic evidence-contract controller restored evidence-consistent action authorization across all three.

## Figures

{figure_index.to_markdown(index=False)}

## Tables

{table_index.to_markdown(index=False)}
"""

(OUTDIR / "onco_guard_response_v0_77_three_model_results_card.md").write_text(card)

print("Saved v0.77 three-model synthesis package to:", OUTDIR)

print("\nThree-model unguided comparison:")
print(table1.to_string(index=False))

print("\nThree-model controller comparison:")
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
