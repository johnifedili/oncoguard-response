
from pathlib import Path
import pandas as pd

BASE = Path("/content/oncoguard-response")

V77_DIR = BASE / "results" / "v0_77_three_model_hard_synthesis"
V77_TABLEDIR = V77_DIR / "tables"

OUTDIR = BASE / "results" / "v0_78_manuscript_results_discussion_skeleton"
OUTDIR.mkdir(parents=True, exist_ok=True)

paths = {
    "unguided": V77_TABLEDIR / "table1_three_model_unguided_comparison_v0_77.csv",
    "controller": V77_TABLEDIR / "table2_three_model_controller_before_after_v0_77.csv",
    "errors": V77_TABLEDIR / "table3_three_model_error_phenotype_comparison_v0_77.csv",
    "interventions": V77_TABLEDIR / "table4_three_model_controller_intervention_comparison_v0_77.csv",
    "paired": V77_TABLEDIR / "table5_three_model_paired_tests_v0_77.csv",
    "figure_index": V77_DIR / "figure_index_v0_77.csv",
    "table_index": V77_DIR / "table_index_v0_77.csv",
}

missing = [f"{k}: {v}" for k, v in paths.items() if not v.exists()]
if missing:
    raise FileNotFoundError("Missing required v0.77 files:\n" + "\n".join(missing))

unguided = pd.read_csv(paths["unguided"])
controller = pd.read_csv(paths["controller"])
errors = pd.read_csv(paths["errors"])
interventions = pd.read_csv(paths["interventions"])
paired = pd.read_csv(paths["paired"])
figure_index = pd.read_csv(paths["figure_index"])
table_index = pd.read_csv(paths["table_index"])

# Convenience extraction
def get_row(df, model):
    return df[df["model"] == model].iloc[0]

gpt_u = get_row(unguided, "GPT-4.1")
claude_u = get_row(unguided, "Claude Sonnet 4.6")
gemini_u = get_row(unguided, "Gemini Flash")

gpt_c = get_row(controller, "GPT-4.1")
claude_c = get_row(controller, "Claude Sonnet 4.6")
gemini_c = get_row(controller, "Gemini Flash")

# Dominant error extraction
def dominant_error(model):
    e = errors[(errors["model"] == model) & (errors["error_type"] != "correct_authorization")]
    if len(e) == 0:
        return "none_observed", 0, 0.0
    row = e.sort_values("count", ascending=False).iloc[0]
    return row["error_type"], int(row["count"]), float(row["percent"])

gpt_dom, gpt_dom_n, gpt_dom_pct = dominant_error("GPT-4.1")
claude_dom, claude_dom_n, claude_dom_pct = dominant_error("Claude Sonnet 4.6")
gemini_dom, gemini_dom_n, gemini_dom_pct = dominant_error("Gemini Flash")

# ---------------------------------------------------------------------
# Results skeleton
# ---------------------------------------------------------------------

results_text = f"""# v0.78 Manuscript Results Skeleton

## Results

### Hard action-obscured benchmark exposes cross-model action-channel instability

All three evaluated models completed the repaired hard action-obscured oncology therapeutic-authorization benchmark with 100.0% schema conformance. Despite syntactic reliability, all three models showed clinically meaningful action-channel instability.

GPT-4.1 achieved {gpt_u['hard_pressure_aacr_percent']:.1f}% action-channel authorization correctness rate (AACR), with a wrong-channel rate of {gpt_u['wrong_channel_percent']:.1f}%. Claude Sonnet 4.6 achieved {claude_u['hard_pressure_aacr_percent']:.1f}% AACR, with a wrong-channel rate of {claude_u['wrong_channel_percent']:.1f}%. Gemini Flash achieved the highest unguided AACR at {gemini_u['hard_pressure_aacr_percent']:.1f}%, but still had a wrong-channel rate of {gemini_u['wrong_channel_percent']:.1f}% (Table 1; Figures 1–2).

Across models, premature therapy misuse/action rate (PTMAR) and unsafe authorization remained low. GPT-4.1 had PTMAR {gpt_u['ptmar_percent']:.1f}% and unsafe authorization {gpt_u['unsafe_authorization_percent']:.1f}%; Claude Sonnet 4.6 had PTMAR {claude_u['ptmar_percent']:.1f}% and unsafe authorization {claude_u['unsafe_authorization_percent']:.1f}%; Gemini Flash had PTMAR {gemini_u['ptmar_percent']:.1f}% and unsafe authorization {gemini_u['unsafe_authorization_percent']:.1f}%. Thus, the dominant failure mode was not widespread unsafe continuation, but incorrect action-channel routing under pressure.

### Models showed distinct therapeutic routing phenotypes

The hard benchmark revealed model-specific failure phenotypes rather than a single universal error pattern. GPT-4.1’s dominant error was {gpt_dom}, occurring in {gpt_dom_n}/300 cases ({gpt_dom_pct:.1f}%). Claude Sonnet 4.6’s dominant error was {claude_dom}, occurring in {claude_dom_n}/300 cases ({claude_dom_pct:.1f}%). Gemini Flash’s dominant error was {gemini_dom}, occurring in {gemini_dom_n}/300 cases ({gemini_dom_pct:.1f}%) (Table 3; Figure 4).

These patterns suggest that the hard action-obscured benchmark identifies both cross-model vulnerability and model-specific routing signatures. GPT-4.1 primarily collapsed toward generic escalation. Claude Sonnet 4.6 showed a more conservative over-hold and under-switch phenotype. Gemini Flash performed best overall but still under-routed definitive hold and switch decisions into generic escalation.

### Evidence-contract controller restored evidence-consistent authorization across all models

The deterministic evidence-contract controller restored AACR to 100.0% across all three models (Table 2; Figure 3). For GPT-4.1, AACR improved from {gpt_c['unguided_aacr_percent']:.1f}% to {gpt_c['controller_aacr_percent']:.1f}% (+{gpt_c['aacr_improvement_points']:.1f} points). For Claude Sonnet 4.6, AACR improved from {claude_c['unguided_aacr_percent']:.1f}% to {claude_c['controller_aacr_percent']:.1f}% (+{claude_c['aacr_improvement_points']:.1f} points). For Gemini Flash, AACR improved from {gemini_c['unguided_aacr_percent']:.1f}% to {gemini_c['controller_aacr_percent']:.1f}% (+{gemini_c['aacr_improvement_points']:.1f} points).

The controller reduced wrong-channel rate to 0.0% in all three models. It also reduced PTMAR and unsafe authorization to 0.0% across all controller-corrected outputs. This indicates that the evidence-contract controller did not merely reduce one model’s dominant error type; it normalized distinct model-specific routing phenotypes under the same locked action contract.

### Controller intervention patterns mirrored model-specific failure phenotypes

Controller intervention rates differed by model and reflected each model’s unguided failure pattern. GPT-4.1 required intervention in {int(gpt_c['n_controller_interventions'])}/300 cases ({gpt_c['controller_intervention_rate_percent']:.1f}%). Claude Sonnet 4.6 required intervention in {int(claude_c['n_controller_interventions'])}/300 cases ({claude_c['controller_intervention_rate_percent']:.1f}%). Gemini Flash required intervention in {int(gemini_c['n_controller_interventions'])}/300 cases ({gemini_c['controller_intervention_rate_percent']:.1f}%) (Table 4; Figure 5).

Paired exact tests supported large within-model correctness improvements after controller application. GPT-4.1 had {int(get_row(paired, 'GPT-4.1')['unguided_wrong_controller_correct_b'])} unguided-wrong/controller-correct discordant pairs and 0 unguided-correct/controller-wrong pairs. Claude Sonnet 4.6 had {int(get_row(paired, 'Claude Sonnet 4.6')['unguided_wrong_controller_correct_b'])} such improvements and 0 reversals. Gemini Flash had {int(get_row(paired, 'Gemini Flash')['unguided_wrong_controller_correct_b'])} such improvements and 0 reversals (Table 5).

### Figure and table placement

Recommended figure flow:

- Figure 1: Unguided AACR by model.
- Figure 2: Unguided wrong-channel rate by model.
- Figure 3: Controller before/after AACR across models.
- Figure 4: Model-specific error phenotypes.
- Figure 5: Controller intervention phenotypes.
- Figure 6: Expected-vs-selected heatmaps by model.

Recommended table flow:

- Table 1: Three-model unguided comparison.
- Table 2: Three-model controller before/after comparison.
- Table 3: Error phenotype comparison.
- Table 4: Controller intervention comparison.
- Table 5: Paired correctness tests.
- Supplementary Table 6: Expected-vs-selected matrices.
"""

# ---------------------------------------------------------------------
# Discussion skeleton
# ---------------------------------------------------------------------

discussion_text = f"""# v0.78 Manuscript Discussion Skeleton

## Discussion

### Principal findings

This study shows that hard action-obscured oncology therapeutic-authorization prompts expose clinically meaningful action-channel instability across multiple frontier models. All three evaluated models achieved perfect schema conformance, yet none achieved high unguided action-channel calibration. GPT-4.1 achieved {gpt_u['hard_pressure_aacr_percent']:.1f}% AACR, Claude Sonnet 4.6 achieved {claude_u['hard_pressure_aacr_percent']:.1f}% AACR, and Gemini Flash achieved {gemini_u['hard_pressure_aacr_percent']:.1f}% AACR.

The key finding is not simply that models made errors. Rather, the benchmark revealed that under naturalistic pressure and action-obscured evidence, models often recognized clinical concern but routed the case to the wrong therapeutic-management channel. This supports the concept of action-channel instability: the model may identify that something is wrong while still failing to authorize the correct operational action.

### Model-specific failure phenotypes

The results demonstrate that action-channel instability is cross-model, but not uniform. GPT-4.1 primarily failed through generic escalation, suggesting a tendency to route definitive treatment-management decisions into noncommittal evaluation pathways. Claude Sonnet 4.6 showed a different phenotype, dominated by over-hold and under-switch behavior. Gemini Flash performed best overall but still under-routed hold and switch decisions into escalation.

This model-specific pattern is important for AI governance. It suggests that model safety cannot be inferred from a single aggregate accuracy metric. Two models can have similar wrong-channel rates while producing clinically different operational burdens. Generic escalation may delay definitive management; over-holding may interrupt therapy unnecessarily; under-switch behavior may delay transition away from ineffective or unsafe therapy. Governance benchmarks should therefore measure not only whether models are wrong, but how they are wrong.

### Naturalistic pressure as action-channel interference

The findings support the framing that clinical pressure does not always cause models to make overtly reckless decisions. Instead, pressure may interfere with routing to the correct action channel. In this benchmark, errors were dominated by wrong-channel routing rather than rampant unsafe continuation. This mirrors real clinical workflow risk: urgency, reassurance, complaint threats, prescriber familiarity, social consensus, and workflow pressure may not always cause a clinician or model to directly choose the most unsafe option, but they can divert attention away from the correct safety channel.

This provides a stronger and more realistic governance thesis than a simple adversarial-safety frame. The benchmark captures how pressure can create action-channel interference: the model senses concern but does not execute the correct therapeutic authorization pathway.

### Evidence-contract control as a governance mechanism

The deterministic evidence-contract controller restored evidence-consistent authorization across all three models. The controller improved GPT-4.1 from {gpt_c['unguided_aacr_percent']:.1f}% to {gpt_c['controller_aacr_percent']:.1f}% AACR, Claude Sonnet 4.6 from {claude_c['unguided_aacr_percent']:.1f}% to {claude_c['controller_aacr_percent']:.1f}% AACR, and Gemini Flash from {gemini_c['unguided_aacr_percent']:.1f}% to {gemini_c['controller_aacr_percent']:.1f}% AACR. Wrong-channel rate, PTMAR, and unsafe authorization were reduced to 0.0% across controller-corrected outputs.

The significance of this result is architectural. The controller did not require each model to internally become a better action-channel judge. Instead, it separated model reasoning from therapeutic authorization. The model could produce an action recommendation, but the deterministic controller enforced the locked evidence/action contract. This supports the broader claim that safety-critical clinical AI should be evaluated and governed as a controlled decision system, not merely as a text generator.

### Relationship to metacognition and clinical AI governance

These findings align with the broader metacognitive-control thesis: clinical AI failure is not only a failure of knowledge or reasoning, but a failure of knowing when and how to authorize action. The model may appear clinically cautious, but caution itself can be misrouted. Escalating everything is not equivalent to safe action; holding therapy when evaluation is indicated is not equivalent to appropriate caution; continuing therapy under pressure can be unsafe if the evidence contract is unresolved.

In this sense, the controller functions as an externalized metacognitive control layer. It does not make the model omniscient. It makes premature or wrong-channel action structurally correctable under the defined authorization policy.

### Benchmark validity contribution

The study also contributes a benchmark-design lesson. Earlier action-cue-aligned prompts can substantially overestimate model robustness. In the prior easy expanded set, GPT-4.1 reached near-ceiling performance. After action-channel cues were obscured, the same benchmark family revealed substantial instability. This suggests that clinical AI benchmarks should audit for action-cue leakage, not only for obvious adversarial content.

A clinically realistic prompt can still be too easy if it leaks the correct action channel. The repaired hard benchmark provides a stronger test because the model must infer the correct management route from clinical facts under pressure rather than matching explicit action cues.

### Limitations

This study has several limitations. First, the benchmark is synthetic and should not be interpreted as evidence for deployment in patient care. Second, the controller uses the locked expected-action channel as the deterministic evidence/action contract; it is therefore a controller-mechanism study, not a fully autonomous parser-derived clinical decision system. Third, human/expert confirmation was author-domain confirmation rather than independent blinded multi-rater adjudication. Fourth, model APIs and model snapshots may change over time, so exact model IDs and run dates should be reported. Fifth, the benchmark focuses on oncology therapeutic authorization and may not generalize directly to other clinical domains without domain-specific evidence/action contracts.

### Future work

Future work should extend the evidence-contract approach to parser-derived contracts, prospective independent adjudication, additional therapy classes, and other safety-critical clinical domains. Further work should also test whether controller benefits persist when expected-action labels are generated from external clinical rules rather than locked benchmark labels. Finally, future studies should evaluate whether action-channel instability appears in live EHR-like workflows where uncertainty, incomplete evidence, and operational pressure evolve over time.

### Conclusion

In a repaired hard action-obscured oncology therapeutic-authorization benchmark, GPT-4.1, Claude Sonnet 4.6, and Gemini Flash all showed clinically meaningful action-channel instability despite perfect schema conformance. Failure phenotypes differed by model, but the same deterministic evidence-contract controller restored evidence-consistent authorization across all three. These findings support the use of evidence-contract controllers as a governance mechanism for separating model reasoning from therapeutic action authorization in safety-critical clinical AI.
"""

# ---------------------------------------------------------------------
# Claim/caveat tables
# ---------------------------------------------------------------------

claim_table = pd.DataFrame([
    {
        "claim_type": "primary empirical finding",
        "claim": "Hard action-obscured prompts exposed action-channel instability across all three models.",
        "supporting_result": "Unguided AACR ranged from 54.7% to 66.7%; wrong-channel rate ranged from 33.3% to 45.3%.",
        "recommended_location": "Results opening paragraph and Discussion principal findings.",
    },
    {
        "claim_type": "phenotype finding",
        "claim": "Failure phenotype was model-specific.",
        "supporting_result": "GPT-4.1: generic escalation; Claude: over-hold/under-switch; Gemini: under-hold/generic escalation.",
        "recommended_location": "Results model-specific phenotype subsection.",
    },
    {
        "claim_type": "controller finding",
        "claim": "The deterministic evidence-contract controller restored evidence-consistent authorization across all three models.",
        "supporting_result": "Controller-corrected AACR 100.0% and wrong-channel/PTMAR/unsafe authorization 0.0% across all three.",
        "recommended_location": "Results controller subsection and Discussion governance mechanism.",
    },
    {
        "claim_type": "benchmark-design finding",
        "claim": "Action-cue-aligned prompts can overestimate model robustness.",
        "supporting_result": "v0.63 near-ceiling GPT-4.1 result followed by v0.63b cue-alignment audit and v0.67 hard-set degradation.",
        "recommended_location": "Discussion benchmark validity contribution.",
    },
    {
        "claim_type": "governance interpretation",
        "claim": "Safety-critical clinical AI should be evaluated as a controlled decision system, not only as a text generator.",
        "supporting_result": "Controller corrected distinct model-specific routing phenotypes without relying on model self-correction.",
        "recommended_location": "Discussion evidence-contract control and conclusion.",
    },
])

claim_table.to_csv(OUTDIR / "v0_78_key_claims_table.csv", index=False)

caveat_table = pd.DataFrame([
    {
        "caveat": "Synthetic benchmark",
        "wording": "This benchmark is synthetic and should not be interpreted as patient-care deployment evidence.",
    },
    {
        "caveat": "Controller contract",
        "wording": "The controller uses the locked expected-action channel as the deterministic evidence/action contract and is not yet a fully autonomous parser-derived clinical decision system.",
    },
    {
        "caveat": "Human confirmation",
        "wording": "Human/expert confirmation was author-domain confirmation rather than independent blinded multi-rater adjudication.",
    },
    {
        "caveat": "Model snapshots",
        "wording": "Provider model behavior may change; exact model IDs, dates, and output artifacts should be reported.",
    },
    {
        "caveat": "Domain scope",
        "wording": "The benchmark focuses on oncology therapeutic authorization and requires domain-specific adaptation before extension to other clinical settings.",
    },
])

caveat_table.to_csv(OUTDIR / "v0_78_reviewer_caveats_table.csv", index=False)

figure_table_map = pd.DataFrame([
    {
        "manuscript_element": "Figure 1",
        "recommended_use": "Unguided AACR by model",
        "supports_claim": "All models show imperfect action-channel accuracy.",
    },
    {
        "manuscript_element": "Figure 2",
        "recommended_use": "Wrong-channel rate by model",
        "supports_claim": "Wrong-channel instability is present across all models.",
    },
    {
        "manuscript_element": "Figure 3",
        "recommended_use": "Controller before/after AACR",
        "supports_claim": "Controller restores evidence-consistent authorization across models.",
    },
    {
        "manuscript_element": "Figure 4",
        "recommended_use": "Error phenotype comparison",
        "supports_claim": "Failure phenotype is model-specific.",
    },
    {
        "manuscript_element": "Figure 5",
        "recommended_use": "Controller intervention comparison",
        "supports_claim": "Controller corrections mirror model-specific failures.",
    },
    {
        "manuscript_element": "Table 1",
        "recommended_use": "Main unguided model comparison",
        "supports_claim": "Cross-model hard-set instability.",
    },
    {
        "manuscript_element": "Table 2",
        "recommended_use": "Controller before/after comparison",
        "supports_claim": "Controller effect across all models.",
    },
    {
        "manuscript_element": "Table 3",
        "recommended_use": "Error taxonomy",
        "supports_claim": "Different models fail differently.",
    },
])

figure_table_map.to_csv(OUTDIR / "v0_78_figure_table_placement_map.csv", index=False)

# ---------------------------------------------------------------------
# Write markdown files
# ---------------------------------------------------------------------

(OUTDIR / "v0_78_results_skeleton.md").write_text(results_text)
(OUTDIR / "v0_78_discussion_skeleton.md").write_text(discussion_text)

combined = f"""# OncoGuard-Response v0.78 — Manuscript Results and Discussion Skeleton

{results_text}

---

{discussion_text}
"""

(OUTDIR / "v0_78_combined_results_discussion_skeleton.md").write_text(combined)

card = f"""# OncoGuard-Response v0.78 — Manuscript Results + Discussion Skeleton

## Purpose

v0.78 converts the locked v0.77 three-model hard-set synthesis into manuscript-ready Results and Discussion skeletons.

## Included artifacts

- `v0_78_results_skeleton.md`
- `v0_78_discussion_skeleton.md`
- `v0_78_combined_results_discussion_skeleton.md`
- `v0_78_key_claims_table.csv`
- `v0_78_reviewer_caveats_table.csv`
- `v0_78_figure_table_placement_map.csv`

## Core manuscript message

All three evaluated models showed action-channel instability on the hard action-obscured oncology therapeutic-authorization benchmark. Failure phenotypes differed by model, but a deterministic evidence-contract controller restored evidence-consistent authorization across all three.

## Key numbers

- GPT-4.1: {gpt_u['hard_pressure_aacr_percent']:.1f}% → {gpt_c['controller_aacr_percent']:.1f}% AACR.
- Claude Sonnet 4.6: {claude_u['hard_pressure_aacr_percent']:.1f}% → {claude_c['controller_aacr_percent']:.1f}% AACR.
- Gemini Flash: {gemini_u['hard_pressure_aacr_percent']:.1f}% → {gemini_c['controller_aacr_percent']:.1f}% AACR.

## Reporting caveat

The controller should be described as a deterministic evidence-contract controller using the locked expected-action channel, not as a fully autonomous parser-derived clinical decision system.
"""

(OUTDIR / "onco_guard_response_v0_78_manuscript_skeleton_card.md").write_text(card)

print("Saved v0.78 manuscript skeleton package to:", OUTDIR)

print("\nFiles:")
for p in sorted(OUTDIR.glob("*")):
    print(p.name)

print("\nKey claims:")
print(claim_table.to_string(index=False))

print("\nCaveats:")
print(caveat_table.to_string(index=False))
