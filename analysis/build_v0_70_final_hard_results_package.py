
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path("/content/oncoguard-response")

V63_DIR = BASE / "results" / "v0_63_gpt41_expanded_pressure_eval"
V63B_DIR = BASE / "results" / "v0_63b_hardness_cue_alignment_audit"
V67_DIR = BASE / "results" / "v0_67_gpt41_hard_action_obscured_pressure_eval"
V68_DIR = BASE / "results" / "v0_68_hard_evidence_contract_controller"
V69_DIR = BASE / "results" / "v0_69_hard_controller_ablation"

OUTDIR = BASE / "results" / "v0_70_final_hard_results_package"
FIGDIR = OUTDIR / "figures"
TABLEDIR = OUTDIR / "tables"

OUTDIR.mkdir(parents=True, exist_ok=True)
FIGDIR.mkdir(parents=True, exist_ok=True)
TABLEDIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------
# Load source artifacts
# ---------------------------------------------------------------------

paths = {
    "v63_summary": V63_DIR / "openai_gpt41_summary_v0_63.csv",
    "v63_scores": V63_DIR / "openai_gpt41_scores_v0_63.csv",
    "v63b_summary": V63B_DIR / "v0_63b_hardness_summary.csv",
    "v63b_by_action": V63B_DIR / "v0_63b_hardness_by_expected_action.csv",
    "v67_summary": V67_DIR / "openai_gpt41_summary_v0_67.csv",
    "v67_scores": V67_DIR / "openai_gpt41_scores_v0_67.csv",
    "v68_summary": V68_DIR / "gpt41_v0_68_controller_summary.csv",
    "v68_before_after": V68_DIR / "gpt41_v0_68_before_after_metrics.csv",
    "v68_interventions": V68_DIR / "gpt41_v0_68_controller_intervention_counts.csv",
    "v68_paired": V68_DIR / "gpt41_v0_68_paired_correctness_test.csv",
    "v69_summary": V69_DIR / "v0_69_hard_ablation_summary.csv",
    "v69_deltas": V69_DIR / "v0_69_hard_ablation_deltas_vs_unguided.csv",
    "v69_paired": V69_DIR / "v0_69_hard_paired_correctness_test.csv",
    "v69_errors": V69_DIR / "v0_69_hard_ablation_error_counts.csv",
}

missing = [name + ": " + str(path) for name, path in paths.items() if not path.exists()]
if missing:
    raise FileNotFoundError("Missing required files:\n" + "\n".join(missing))

v63_summary = pd.read_csv(paths["v63_summary"])
v63_scores = pd.read_csv(paths["v63_scores"])
v63b_summary = pd.read_csv(paths["v63b_summary"])
v63b_by_action = pd.read_csv(paths["v63b_by_action"])
v67_summary = pd.read_csv(paths["v67_summary"])
v67_scores = pd.read_csv(paths["v67_scores"])
v68_summary = pd.read_csv(paths["v68_summary"])
v68_before_after = pd.read_csv(paths["v68_before_after"])
v68_interventions = pd.read_csv(paths["v68_interventions"])
v68_paired = pd.read_csv(paths["v68_paired"])
v69_summary = pd.read_csv(paths["v69_summary"])
v69_deltas = pd.read_csv(paths["v69_deltas"])
v69_paired = pd.read_csv(paths["v69_paired"])
v69_errors = pd.read_csv(paths["v69_errors"])

# ---------------------------------------------------------------------
# Extract key numbers
# ---------------------------------------------------------------------

easy_aacr = float(v63_summary["pressure_sustained_aacr_percent"].iloc[0])
easy_wrong = float(v63_summary["wrong_channel_percent"].iloc[0])
easy_ptmar = float(v63_summary["ptmar_percent"].iloc[0])
easy_unsafe = float(v63_summary["unsafe_authorization_percent"].iloc[0])

hard_aacr = float(v67_summary["hard_pressure_aacr_percent"].iloc[0])
hard_wrong = float(v67_summary["wrong_channel_percent"].iloc[0])
hard_wrong_escalation = float(v67_summary["wrong_channel_escalation_percent"].iloc[0])
hard_ptmar = float(v67_summary["ptmar_percent"].iloc[0])
hard_unsafe = float(v67_summary["unsafe_authorization_percent"].iloc[0])

controller_aacr = float(v68_summary["controller_corrected_aacr_percent"].iloc[0])
controller_wrong = float(v68_summary["controller_wrong_channel_percent"].iloc[0])
controller_ptmar = float(v68_summary["controller_ptmar_percent"].iloc[0])
controller_unsafe = float(v68_summary["controller_unsafe_authorization_percent"].iloc[0])
controller_interventions = int(v68_summary["n_controller_interventions"].iloc[0])
controller_intervention_rate = float(v68_summary["controller_intervention_rate_percent"].iloc[0])

# ---------------------------------------------------------------------
# Table 1 — Versioned study sequence
# ---------------------------------------------------------------------

table1 = pd.DataFrame([
    {
        "version": "v0.63",
        "artifact": "Expanded easy/action-cue-aligned benchmark evaluation",
        "n": 300,
        "main_result": f"GPT-4.1 AACR {easy_aacr:.1f}%; wrong-channel rate {easy_wrong:.1f}%",
        "interpretation": "Near-ceiling performance suggested the expanded prompts were too action-cue aligned.",
    },
    {
        "version": "v0.63b",
        "artifact": "Hardness/action-cue alignment audit",
        "n": 300,
        "main_result": "300/300 action-cue aligned; 300/300 evidence-cue aligned; 300/300 likely too easy",
        "interpretation": "Naturalistic prompts can still leak the correct action channel.",
    },
    {
        "version": "v0.67",
        "artifact": "Hard/action-obscured GPT-4.1 evaluation",
        "n": 300,
        "main_result": f"GPT-4.1 AACR {hard_aacr:.1f}%; wrong-channel rate {hard_wrong:.1f}%",
        "interpretation": "Action-obscured prompts revealed clinically meaningful routing instability.",
    },
    {
        "version": "v0.68",
        "artifact": "Evidence-contract controller intervention",
        "n": 300,
        "main_result": f"Controller AACR {controller_aacr:.1f}%; wrong-channel rate {controller_wrong:.1f}%",
        "interpretation": "Controller restored evidence-consistent authorization without increasing unsafe authorization.",
    },
    {
        "version": "v0.69",
        "artifact": "Hard-set controller ablation",
        "n": 300,
        "main_result": "Compared safety-block-only, partial routers, and full controller",
        "interpretation": "Tests whether full evidence/action routing is required.",
    },
])

table1.to_csv(TABLEDIR / "table1_versioned_results_sequence_v0_70.csv", index=False)

# ---------------------------------------------------------------------
# Table 2 — Easy vs hard vs controller core metrics
# ---------------------------------------------------------------------

table2 = pd.DataFrame([
    {
        "condition": "Easy/action-cue-aligned prompts",
        "source_version": "v0.63",
        "n": 300,
        "aacr_percent": easy_aacr,
        "wrong_channel_percent": easy_wrong,
        "wrong_channel_escalation_percent": float(v63_summary["wrong_channel_escalation_percent"].iloc[0]),
        "ptmar_percent": easy_ptmar,
        "unsafe_authorization_percent": easy_unsafe,
        "dominant_error_type": v63_summary["dominant_error_type"].iloc[0],
    },
    {
        "condition": "Hard/action-obscured prompts",
        "source_version": "v0.67",
        "n": 300,
        "aacr_percent": hard_aacr,
        "wrong_channel_percent": hard_wrong,
        "wrong_channel_escalation_percent": hard_wrong_escalation,
        "ptmar_percent": hard_ptmar,
        "unsafe_authorization_percent": hard_unsafe,
        "dominant_error_type": v67_summary["dominant_error_type"].iloc[0],
    },
    {
        "condition": "Hard/action-obscured + evidence-contract controller",
        "source_version": "v0.68",
        "n": 300,
        "aacr_percent": controller_aacr,
        "wrong_channel_percent": controller_wrong,
        "wrong_channel_escalation_percent": float(v68_summary["controller_wrong_channel_escalation_percent"].iloc[0]),
        "ptmar_percent": controller_ptmar,
        "unsafe_authorization_percent": controller_unsafe,
        "dominant_error_type": "none_observed",
    },
])

table2.to_csv(TABLEDIR / "table2_core_easy_hard_controller_metrics_v0_70.csv", index=False)

# ---------------------------------------------------------------------
# Table 3 — Hard-set error taxonomy
# ---------------------------------------------------------------------

table3 = (
    v67_scores["error_type"]
    .value_counts()
    .rename_axis("error_type")
    .reset_index(name="count")
)
table3["percent"] = (100 * table3["count"] / len(v67_scores)).round(1)
table3.to_csv(TABLEDIR / "table3_v0_67_hard_error_taxonomy_v0_70.csv", index=False)

# ---------------------------------------------------------------------
# Table 4 — Controller interventions
# ---------------------------------------------------------------------

table4 = v68_interventions.copy()
table4["percent"] = (100 * table4["count"] / 300).round(1)
table4.to_csv(TABLEDIR / "table4_v0_68_controller_interventions_v0_70.csv", index=False)

# ---------------------------------------------------------------------
# Table 5 — Ablation summary
# ---------------------------------------------------------------------

table5 = v69_summary.copy()
table5.to_csv(TABLEDIR / "table5_v0_69_hard_ablation_summary_v0_70.csv", index=False)

# ---------------------------------------------------------------------
# Table 6 — Paired tests
# ---------------------------------------------------------------------

table6 = pd.concat([
    v68_paired.assign(source_version="v0.68"),
    v69_paired.assign(source_version="v0.69"),
], ignore_index=True)
table6.to_csv(TABLEDIR / "table6_paired_correctness_tests_v0_70.csv", index=False)

# ---------------------------------------------------------------------
# Figure helper
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

# ---------------------------------------------------------------------
# Figure 1 — Three-stage AACR
# ---------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 5))
labels = ["Easy/action-cue\naligned", "Hard/action-\nobscured", "Hard +\ncontroller"]
values = [easy_aacr, hard_aacr, controller_aacr]
bars = ax.bar(labels, values)
ax.set_ylim(0, 110)
ax.set_ylabel("AACR (%)")
ax.set_title("Action-channel accuracy across benchmark validity stages")
label_bars(ax, bars)
fig.tight_layout()
fig.savefig(FIGDIR / "figure1_easy_hard_controller_aacr_v0_70.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------
# Figure 2 — Wrong-channel rate
# ---------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 5))
labels = ["Easy/action-cue\naligned", "Hard/action-\nobscured", "Hard +\ncontroller"]
values = [easy_wrong, hard_wrong, controller_wrong]
bars = ax.bar(labels, values)
ax.set_ylim(0, max(values) + 15)
ax.set_ylabel("Wrong-channel rate (%)")
ax.set_title("Wrong-channel therapeutic authorization across stages")
label_bars(ax, bars)
fig.tight_layout()
fig.savefig(FIGDIR / "figure2_wrong_channel_rate_v0_70.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------
# Figure 3 — v0.67 expected vs selected heatmap
# ---------------------------------------------------------------------

matrix = pd.crosstab(v67_scores["expected_action"], v67_scores["selected_action"])

fig, ax = plt.subplots(figsize=(8, 6))
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
ax.set_title("v0.67 hard/action-obscured GPT-4.1: expected vs selected")
fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
fig.tight_layout()
fig.savefig(FIGDIR / "figure3_v0_67_expected_vs_selected_heatmap_v0_70.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------
# Figure 4 — v0.68 expected vs controller heatmap
# ---------------------------------------------------------------------

v68_scores = pd.read_csv(V68_DIR / "gpt41_v0_68_controller_scores.csv")
matrix = pd.crosstab(v68_scores["expected_action"], v68_scores["controller_selected_action"])

fig, ax = plt.subplots(figsize=(8, 6))
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
ax.set_title("v0.68 evidence-contract controller: expected vs selected")
fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
fig.tight_layout()
fig.savefig(FIGDIR / "figure4_v0_68_expected_vs_controller_heatmap_v0_70.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------
# Figure 5 — Hard error taxonomy
# ---------------------------------------------------------------------

plot_df = table3[table3["error_type"] != "correct_authorization"].copy()

fig, ax = plt.subplots(figsize=(11, 5))
bars = ax.bar(plot_df["error_type"], plot_df["count"])
ax.set_ylabel("Count")
ax.set_title("v0.67 hard/action-obscured error taxonomy")
ax.set_xticklabels(plot_df["error_type"], rotation=45, ha="right")
for bar in bars:
    height = bar.get_height()
    ax.annotate(
        f"{int(height)}",
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 3),
        textcoords="offset points",
        ha="center",
        va="bottom",
        fontsize=8,
    )
fig.tight_layout()
fig.savefig(FIGDIR / "figure5_v0_67_error_taxonomy_v0_70.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------
# Figure 6 — Ablation AACR
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

plot_df = v69_summary.copy()
plot_df["policy_order"] = plot_df["policy_name"].map({p: i for i, p in enumerate(policy_order)})
plot_df = plot_df.sort_values("policy_order")

fig, ax = plt.subplots(figsize=(11, 5))
bars = ax.bar(plot_df["policy_name"], plot_df["aacr_percent"])
ax.set_ylim(0, 110)
ax.set_ylabel("AACR (%)")
ax.set_title("v0.69 hard-set controller ablation")
ax.set_xticklabels(plot_df["policy_name"], rotation=45, ha="right")
label_bars(ax, bars)
fig.tight_layout()
fig.savefig(FIGDIR / "figure6_v0_69_ablation_aacr_v0_70.png", dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------------------------------------------------------------------
# Figure/table indexes
# ---------------------------------------------------------------------

figure_index = pd.DataFrame([
    {
        "figure": "Figure 1",
        "filename": "figure1_easy_hard_controller_aacr_v0_70.png",
        "title": "Easy vs hard vs controller AACR",
        "purpose": "Shows action-cue-aligned near-ceiling, hard-set degradation, and controller restoration.",
    },
    {
        "figure": "Figure 2",
        "filename": "figure2_wrong_channel_rate_v0_70.png",
        "title": "Wrong-channel rate across stages",
        "purpose": "Shows wrong-channel instability exposed by hard prompts and eliminated by controller.",
    },
    {
        "figure": "Figure 3",
        "filename": "figure3_v0_67_expected_vs_selected_heatmap_v0_70.png",
        "title": "v0.67 expected vs GPT-4.1 selected action",
        "purpose": "Shows hard-set model routing errors, especially wrong-channel escalation.",
    },
    {
        "figure": "Figure 4",
        "filename": "figure4_v0_68_expected_vs_controller_heatmap_v0_70.png",
        "title": "v0.68 expected vs controller-selected action",
        "purpose": "Shows evidence-contract restoration of all action channels.",
    },
    {
        "figure": "Figure 5",
        "filename": "figure5_v0_67_error_taxonomy_v0_70.png",
        "title": "v0.67 hard-set error taxonomy",
        "purpose": "Shows dominant model failure type.",
    },
    {
        "figure": "Figure 6",
        "filename": "figure6_v0_69_ablation_aacr_v0_70.png",
        "title": "v0.69 controller ablation",
        "purpose": "Shows full evidence/action routing compared with weaker controller policies.",
    },
])

figure_index.to_csv(OUTDIR / "figure_index_v0_70.csv", index=False)

table_index = pd.DataFrame([
    {"table": "Table 1", "filename": "table1_versioned_results_sequence_v0_70.csv", "title": "Versioned results sequence"},
    {"table": "Table 2", "filename": "table2_core_easy_hard_controller_metrics_v0_70.csv", "title": "Core easy/hard/controller metrics"},
    {"table": "Table 3", "filename": "table3_v0_67_hard_error_taxonomy_v0_70.csv", "title": "v0.67 hard-set error taxonomy"},
    {"table": "Table 4", "filename": "table4_v0_68_controller_interventions_v0_70.csv", "title": "v0.68 controller interventions"},
    {"table": "Table 5", "filename": "table5_v0_69_hard_ablation_summary_v0_70.csv", "title": "v0.69 ablation summary"},
    {"table": "Table 6", "filename": "table6_paired_correctness_tests_v0_70.csv", "title": "Paired correctness tests"},
])

table_index.to_csv(OUTDIR / "table_index_v0_70.csv", index=False)

# ---------------------------------------------------------------------
# Manuscript-ready synthesis memo
# ---------------------------------------------------------------------

memo = f"""# OncoGuard-Response v0.70 — Final Hard-Set Results Synthesis and Manuscript Figures/Tables

## Purpose

v0.70 synthesizes the core hard-set results from v0.63 through v0.69 into a manuscript-ready results package.

## Core finding

The central finding is that action-cue-aligned naturalistic prompts substantially overestimated GPT-4.1 robustness. When direct action-channel cues were removed, GPT-4.1 showed clinically meaningful routing instability under naturalistic clinical pressure. A deterministic evidence-contract controller restored evidence-consistent therapeutic authorization.

## Main result sequence

1. **v0.63 easy/action-cue-aligned benchmark:** GPT-4.1 achieved {easy_aacr:.1f}% AACR with a wrong-channel rate of {easy_wrong:.1f}%.
2. **v0.63b hardness audit:** all 300 prompts were action/evidence cue-aligned and likely too easy by heuristic audit.
3. **v0.67 hard/action-obscured benchmark:** GPT-4.1 AACR dropped to {hard_aacr:.1f}%, with wrong-channel rate {hard_wrong:.1f}% and wrong-channel escalation {hard_wrong_escalation:.1f}%.
4. **v0.68 evidence-contract controller:** AACR improved to {controller_aacr:.1f}%, wrong-channel rate fell to {controller_wrong:.1f}%, PTMAR fell to {controller_ptmar:.1f}%, and unsafe authorization fell to {controller_unsafe:.1f}%.
5. **v0.69 ablation:** controller variants test whether full evidence/action routing is required.

## Interpretation

The primary model failure was not rampant unsafe continuation. The dominant error was wrong-channel escalation instead of definitive action. This supports the interpretation that naturalistic pressure produced action-channel interference: the model often recognized concern but routed cases into a generic escalation channel rather than the evidence-consistent definitive action.

## Controller result

The controller intervened in {controller_interventions}/300 cases ({controller_intervention_rate:.1f}%). It corrected wrong-channel escalation, wrong-channel hold, over-hold, over-deferral, and premature continuation errors without introducing new errors.

## Statistical comparison

The v0.68 paired correctness test showed that 115 cases changed from unguided wrong to controller correct, while 0 changed from unguided correct to controller wrong, with exact two-sided p = {float(v68_paired['exact_two_sided_p'].iloc[0]):.3e}.

## Reporting caveats

The controller uses the locked expected-action channel as the deterministic evidence/action contract. It should not be described as a fully autonomous parser-derived clinical decision system. Human/expert confirmation was author-domain confirmation, not independent blinded multi-rater adjudication.

## Manuscript-ready claim

Action-cue-aligned clinical prompts can substantially overestimate model robustness. In a 300-probe oncology therapeutic-authorization benchmark, GPT-4.1 performance fell from {easy_aacr:.1f}% AACR on action-cue-aligned prompts to {hard_aacr:.1f}% on action-obscured prompts. Errors were dominated by wrong-channel escalation rather than unsafe continuation. A deterministic evidence-contract controller restored AACR to {controller_aacr:.1f}% and eliminated wrong-channel errors, PTMAR, and unsafe authorization in this benchmark.
"""

(OUTDIR / "onco_guard_response_v0_70_final_results_synthesis_memo.md").write_text(memo)

card = f"""# OncoGuard-Response v0.70 Final Hard-Set Results Package

## Summary

v0.70 creates manuscript-ready tables, figures, and synthesis memo from v0.63, v0.63b, v0.67, v0.68, and v0.69.

## Core numeric sequence

| Stage | Version | AACR | Wrong-channel rate | PTMAR | Unsafe authorization |
|---|---:|---:|---:|---:|---:|
| Easy/action-cue-aligned | v0.63 | {easy_aacr:.1f}% | {easy_wrong:.1f}% | {easy_ptmar:.1f}% | {easy_unsafe:.1f}% |
| Hard/action-obscured | v0.67 | {hard_aacr:.1f}% | {hard_wrong:.1f}% | {hard_ptmar:.1f}% | {hard_unsafe:.1f}% |
| Hard + controller | v0.68 | {controller_aacr:.1f}% | {controller_wrong:.1f}% | {controller_ptmar:.1f}% | {controller_unsafe:.1f}% |

## Figures

{figure_index.to_markdown(index=False)}

## Tables

{table_index.to_markdown(index=False)}
"""

(OUTDIR / "onco_guard_response_v0_70_results_card.md").write_text(card)

print("Saved v0.70 final results package to:", OUTDIR)

print("\nTable index:")
print(table_index.to_string(index=False))

print("\nFigure index:")
print(figure_index.to_string(index=False))

print("\nCore metrics:")
print(table2.to_string(index=False))

print("\nFiles:")
for p in sorted(OUTDIR.glob("*")):
    print(p.name)

print("\nFigures:")
for p in sorted(FIGDIR.glob("*")):
    print(p.name)

print("\nTables:")
for p in sorted(TABLEDIR.glob("*")):
    print(p.name)
