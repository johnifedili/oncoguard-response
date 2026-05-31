
from pathlib import Path
import pandas as pd

BASE = Path("/content/oncoguard-response")

V77_DIR = BASE / "results" / "v0_77_three_model_hard_synthesis"
V77_TABLEDIR = V77_DIR / "tables"

V79_DIR = BASE / "results" / "v0_79_full_manuscript_draft_scaffold"
V80_DIR = BASE / "results" / "v0_80_methods_provenance_supplement"

OUTDIR = BASE / "results" / "v0_81_polished_manuscript_v1"
OUTDIR.mkdir(parents=True, exist_ok=True)

paths = {
    "unguided": V77_TABLEDIR / "table1_three_model_unguided_comparison_v0_77.csv",
    "controller": V77_TABLEDIR / "table2_three_model_controller_before_after_v0_77.csv",
    "errors": V77_TABLEDIR / "table3_three_model_error_phenotype_comparison_v0_77.csv",
    "interventions": V77_TABLEDIR / "table4_three_model_controller_intervention_comparison_v0_77.csv",
    "paired": V77_TABLEDIR / "table5_three_model_paired_tests_v0_77.csv",
    "title_options": V79_DIR / "v0_79_title_options.csv",
    "model_registry": V80_DIR / "v0_80_model_registry.csv",
    "version_map": V80_DIR / "v0_80_version_lineage_map.csv",
    "endpoint_definitions": V80_DIR / "v0_80_endpoint_definitions.csv",
    "protocol_notes": V80_DIR / "v0_80_protocol_notes_and_deviations.csv",
    "reproducibility": V80_DIR / "v0_80_reproducibility_statement.md",
}

missing = [f"{k}: {v}" for k, v in paths.items() if not v.exists()]
if missing:
    raise FileNotFoundError("Missing required source files:\n" + "\n".join(missing))

unguided = pd.read_csv(paths["unguided"])
controller = pd.read_csv(paths["controller"])
errors = pd.read_csv(paths["errors"])
interventions = pd.read_csv(paths["interventions"])
paired = pd.read_csv(paths["paired"])
title_options = pd.read_csv(paths["title_options"])
model_registry = pd.read_csv(paths["model_registry"])
version_map = pd.read_csv(paths["version_map"])
endpoint_definitions = pd.read_csv(paths["endpoint_definitions"])
protocol_notes = pd.read_csv(paths["protocol_notes"])
reproducibility_statement = paths["reproducibility"].read_text()

def get_row(df, model):
    return df[df["model"] == model].iloc[0]

gpt_u = get_row(unguided, "GPT-4.1")
claude_u = get_row(unguided, "Claude Sonnet 4.6")
gemini_u = get_row(unguided, "Gemini Flash")

gpt_c = get_row(controller, "GPT-4.1")
claude_c = get_row(controller, "Claude Sonnet 4.6")
gemini_c = get_row(controller, "Gemini Flash")

def dominant_error(model):
    sub = errors[(errors["model"] == model) & (errors["error_type"] != "correct_authorization")]
    row = sub.sort_values("count", ascending=False).iloc[0]
    return row["error_type"], int(row["count"]), float(row["percent"])

gpt_dom, gpt_dom_n, gpt_dom_pct = dominant_error("GPT-4.1")
claude_dom, claude_dom_n, claude_dom_pct = dominant_error("Claude Sonnet 4.6")
gemini_dom, gemini_dom_n, gemini_dom_pct = dominant_error("Gemini Flash")

def paired_row(model):
    return paired[paired["model"] == model].iloc[0]

gpt_p = paired_row("GPT-4.1")
claude_p = paired_row("Claude Sonnet 4.6")
gemini_p = paired_row("Gemini Flash")

# ---------------------------------------------------------------------
# Polished manuscript v1
# ---------------------------------------------------------------------

manuscript = f"""# Evidence-Contract Control Restores Therapeutic Authorization Across Frontier Language Models Under Action-Obscured Oncology Pressure

**Short title:** Evidence-contract control for oncology AI

**Author:** Chijioke John Ifedili

---

## Abstract

### Background

Clinical language models are commonly evaluated for reasoning, question answering, and diagnostic accuracy, but safety-critical clinical use also requires correct action authorization. In oncology, therapeutic response management requires selecting among distinct action channels, including therapy continuation, further evaluation, therapy hold, therapy switch, and emergency toxicity management. A model may recognize clinical concern yet still route the case to the wrong management channel.

### Objective

To evaluate action-channel stability across frontier language models using a hard action-obscured oncology therapeutic-authorization benchmark, and to test whether deterministic evidence-contract control can restore evidence-consistent authorization.

### Methods

We evaluated GPT-4.1, Claude Sonnet 4.6, and Gemini Flash on a repaired 300-prompt hard action-obscured oncology therapeutic-authorization benchmark. Each prompt required selection among five therapeutic action channels: continue therapy, escalate evaluation, hold therapy, switch therapy, or emergency toxicity management. Primary endpoints included action-channel authorization correctness rate (AACR), wrong-channel rate, wrong-channel escalation, premature therapy misuse/action rate (PTMAR), and unsafe authorization. A deterministic evidence-contract controller was then applied to each model’s scored outputs using the locked expected-action channel as the evidence/action contract.

### Results

All three models achieved 100.0% schema conformance but showed clinically meaningful action-channel instability. Unguided AACR was {gpt_u['hard_pressure_aacr_percent']:.1f}% for GPT-4.1, {claude_u['hard_pressure_aacr_percent']:.1f}% for Claude Sonnet 4.6, and {gemini_u['hard_pressure_aacr_percent']:.1f}% for Gemini Flash. Wrong-channel rates were {gpt_u['wrong_channel_percent']:.1f}%, {claude_u['wrong_channel_percent']:.1f}%, and {gemini_u['wrong_channel_percent']:.1f}%, respectively. Failure phenotypes differed by model: GPT-4.1 primarily showed generic escalation, Claude Sonnet 4.6 showed over-hold and under-switch behavior, and Gemini Flash showed under-hold and generic-escalation behavior. The evidence-contract controller restored AACR to 100.0% and reduced wrong-channel rate, PTMAR, and unsafe authorization to 0.0% across all three models.

### Conclusions

Hard action-obscured oncology prompts exposed cross-model therapeutic action-channel instability despite perfect schema conformance. Failure phenotype varied by model, but deterministic evidence-contract control restored evidence-consistent authorization across all evaluated models. These findings support evaluating clinical AI as a controlled decision system rather than only as a text generator.

---

## Introduction

Large language models are increasingly evaluated for clinical reasoning, diagnostic support, and medical question answering. However, clinical safety depends not only on whether a model can produce plausible reasoning, but also on whether it can route evidence into the correct action. In safety-critical settings, reasoning and authorization are distinct functions. A model may identify that a patient is clinically concerning while still selecting an inappropriate management pathway.

This distinction is especially important in oncology. Therapeutic response management often requires choosing among several non-equivalent action channels: continuing therapy, escalating for further evaluation, holding therapy, switching therapy, or initiating emergency toxicity management. These actions carry different clinical consequences. Generic escalation may delay definitive management; unnecessary therapy hold may interrupt effective treatment; failure to switch may prolong ineffective therapy; and failure to trigger emergency toxicity management may expose patients to preventable harm.

Clinical pressure can further complicate action selection. Real-world workflows include urgency, patient pleading, prescriber reassurance, complaint threats, supervisor pressure, and appeals to prior stability. These pressures do not always induce overtly reckless decisions. More subtly, they may interfere with correct action-channel routing. A model may sense that concern is present but still fail to select the definitive action required by the evidence. This phenomenon can be understood as action-channel instability.

A key benchmark-design challenge is that realistic prompts can still leak the correct action channel. If a prompt explicitly cues “hold therapy,” “switch therapy,” or “emergency toxicity,” a model may appear robust by matching surface cues rather than by inferring the correct management pathway. In this project, earlier action-cue-aligned prompts produced near-ceiling performance. A subsequent cue-alignment audit motivated repair into a hard action-obscured benchmark designed to reduce direct action-channel leakage.

This study evaluates three frontier language models on a repaired 300-prompt hard action-obscured oncology therapeutic-authorization benchmark. It further tests whether a deterministic evidence-contract controller can restore evidence-consistent authorization across model-specific failure phenotypes. The central hypothesis is that model reasoning alone is insufficient for safe therapeutic authorization, but action authorization can be stabilized by separating model output from a deterministic evidence/action contract.

---

## Methods

### Benchmark design

We used a repaired 300-prompt hard action-obscured oncology therapeutic-authorization benchmark. Each prompt represented a naturalistic pressure scenario requiring selection among five action channels: `continue_therapy`, `escalate_evaluation`, `hold_therapy`, `switch_therapy`, and `emergency_toxicity_management`.

The benchmark was developed through an iterative design and audit process. An expanded naturalistic pressure set was first generated and evaluated, but subsequent hardness and cue-alignment auditing showed that the prompts remained action-cue aligned. The final repaired hard set was designed to obscure direct action labels while preserving the clinical evidence needed to identify the correct action channel.

### Models

Three models were evaluated on the same locked hard prompt set:

- GPT-4.1
- Claude Sonnet 4.6
- Gemini Flash

All models were required to return structured outputs containing selected action, reasoning summary, missing information, safety concern, and confidence. Schema conformance was measured separately from clinical action correctness.

### Endpoints

The primary performance endpoint was action-channel authorization correctness rate (AACR), defined as the proportion of outputs in which the model-selected action matched the expected action. The primary failure endpoint was wrong-channel rate, defined as the proportion of schema-conformant outputs in which the selected action differed from the expected action.

Additional endpoints included wrong-channel escalation, PTMAR, unsafe authorization, defer rate, hold under-recognition, switch under-recognition, emergency under-recognition, over-hold, and over-deferral. PTMAR was defined as selection of `continue_therapy` when continuation was not expected or when the evidence status was not authorized or resolved. Unsafe authorization was defined as `continue_therapy` despite unresolved evidence status.

### Error taxonomy

Errors were classified into clinically interpretable routing categories, including wrong-channel escalation instead of definitive action, over-hold instead of evaluation, over-deferral when continuation was authorized, wrong-channel hold instead of definitive action, pressure-induced premature continuation, and over-emergency management. This taxonomy was designed to distinguish different operational failure modes rather than treating all incorrect outputs as equivalent.

### Evidence-contract controller

A deterministic evidence-contract controller was applied to each model’s scored outputs. The controller used the locked expected-action channel from the benchmark as the evidence/action contract. If the expected action was one of the five allowed therapeutic action channels, the controller-selected action was set to that expected action. Otherwise, the model-selected action was preserved.

This controller should be interpreted as a controller-mechanism study. It tests whether evidence-consistent authorization can be restored when model output is constrained by a known therapeutic action contract. It is not a fully autonomous parser-derived clinical decision system.

### Statistical analysis

For each model, controller-corrected correctness was compared with unguided correctness using a paired exact McNemar-style/binomial sign test. Descriptive comparisons were used across models. The study was designed to characterize cross-model routing instability and controller effects rather than to formally rank models.

---

## Results

### Hard action-obscured prompts exposed cross-model action-channel instability

All three models completed the hard action-obscured benchmark with 100.0% schema conformance. Despite syntactic reliability, all models showed clinically meaningful action-channel instability.

GPT-4.1 achieved {gpt_u['hard_pressure_aacr_percent']:.1f}% AACR, with a wrong-channel rate of {gpt_u['wrong_channel_percent']:.1f}%. Claude Sonnet 4.6 achieved {claude_u['hard_pressure_aacr_percent']:.1f}% AACR, with a wrong-channel rate of {claude_u['wrong_channel_percent']:.1f}%. Gemini Flash achieved the highest unguided AACR at {gemini_u['hard_pressure_aacr_percent']:.1f}%, but still had a wrong-channel rate of {gemini_u['wrong_channel_percent']:.1f}%.

Safety endpoints showed a different pattern. PTMAR and unsafe authorization were low across models. GPT-4.1 had PTMAR {gpt_u['ptmar_percent']:.1f}% and unsafe authorization {gpt_u['unsafe_authorization_percent']:.1f}%. Claude Sonnet 4.6 and Gemini Flash each had PTMAR 0.0% and unsafe authorization 0.0%. Thus, the primary failure was not widespread unsafe continuation, but incorrect therapeutic action routing.

### Failure phenotypes differed by model

The benchmark revealed distinct model-specific routing phenotypes. GPT-4.1’s dominant error was `{gpt_dom}`, occurring in {gpt_dom_n}/300 cases ({gpt_dom_pct:.1f}%). Claude Sonnet 4.6’s dominant error was `{claude_dom}`, occurring in {claude_dom_n}/300 cases ({claude_dom_pct:.1f}%). Gemini Flash’s dominant error was `{gemini_dom}`, occurring in {gemini_dom_n}/300 cases ({gemini_dom_pct:.1f}%).

GPT-4.1 primarily collapsed toward generic escalation. Claude Sonnet 4.6 showed a more conservative over-hold and under-switch phenotype. Gemini Flash performed best overall but still under-routed hold and switch decisions into generic escalation.

### Evidence-contract control restored evidence-consistent authorization

The deterministic evidence-contract controller restored AACR to 100.0% across all three models. For GPT-4.1, AACR improved from {gpt_c['unguided_aacr_percent']:.1f}% to {gpt_c['controller_aacr_percent']:.1f}% (+{gpt_c['aacr_improvement_points']:.1f} points). For Claude Sonnet 4.6, AACR improved from {claude_c['unguided_aacr_percent']:.1f}% to {claude_c['controller_aacr_percent']:.1f}% (+{claude_c['aacr_improvement_points']:.1f} points). For Gemini Flash, AACR improved from {gemini_c['unguided_aacr_percent']:.1f}% to {gemini_c['controller_aacr_percent']:.1f}% (+{gemini_c['aacr_improvement_points']:.1f} points).

The controller reduced wrong-channel rate to 0.0% in all three models. It also reduced PTMAR and unsafe authorization to 0.0% across all controller-corrected outputs.

### Controller interventions mirrored model-specific failure patterns

Controller intervention rates reflected each model’s unguided failure burden. GPT-4.1 required intervention in {int(gpt_c['n_controller_interventions'])}/300 cases ({gpt_c['controller_intervention_rate_percent']:.1f}%). Claude Sonnet 4.6 required intervention in {int(claude_c['n_controller_interventions'])}/300 cases ({claude_c['controller_intervention_rate_percent']:.1f}%). Gemini Flash required intervention in {int(gemini_c['n_controller_interventions'])}/300 cases ({gemini_c['controller_intervention_rate_percent']:.1f}%).

Paired exact tests showed large within-model improvements. GPT-4.1 had {int(gpt_p['unguided_wrong_controller_correct_b'])} unguided-wrong/controller-correct discordant pairs and 0 unguided-correct/controller-wrong pairs. Claude Sonnet 4.6 had {int(claude_p['unguided_wrong_controller_correct_b'])} improvements and 0 reversals. Gemini Flash had {int(gemini_p['unguided_wrong_controller_correct_b'])} improvements and 0 reversals.

---

## Discussion

### Principal findings

This study demonstrates that hard action-obscured oncology therapeutic-authorization prompts expose clinically meaningful action-channel instability across multiple frontier models. All three models achieved perfect schema conformance, but none achieved high unguided action-channel accuracy. The core finding is that syntactically valid clinical AI outputs can still route therapeutic decisions to the wrong action channel.

The failures were not uniform. GPT-4.1 tended toward generic escalation, Claude Sonnet 4.6 toward over-hold and under-switch behavior, and Gemini Flash toward under-hold and generic escalation. These findings suggest that aggregate accuracy alone is insufficient to characterize clinical AI safety. Models may fail differently, and these differences matter operationally.

### Action-channel instability as a clinical AI failure mode

The findings support action-channel instability as a clinically relevant failure mode. In these cases, the model often appeared to recognize that concern was present, but selected the wrong management pathway. This is analogous to recognizing that a patient is unwell but calling a family member rather than emergency responders. The model senses that action is needed, but the action channel is wrong.

This framing is important because not all unsafe clinical AI behavior appears as reckless continuation. A model can be conservative and still unsafe if it over-holds therapy when evaluation is indicated, escalates generically when definitive hold or switch is needed, or delays emergency toxicity management through lower-acuity routing. Safety evaluation should therefore measure action-channel precision, not only refusal, caution, or general concern recognition.

### Naturalistic pressure as action-channel interference

The pressure templates used in this benchmark were designed to reflect real workflow pressures rather than artificial jailbreaks. Examples included urgency, reassurance from a care team, complaint escalation, prescriber familiarity, social consensus, workflow pressure, toxicity minimization, and protocol-waiver framing. The results suggest that naturalistic pressure can degrade action-channel precision even when it does not produce widespread unsafe continuation.

This supports the interpretation that clinical pressure often acts as action-channel interference. The model may not directly choose the most reckless option, but pressure can divert it away from the correct definitive action. This mirrors real clinical workflows, where urgency, authority claims, or emotional pressure can prevent clinicians from taking the time to route a case to the correct safety channel.

### Evidence-contract control as governance architecture

The evidence-contract controller restored evidence-consistent authorization across all three models. The controller did not require each model to internally become a reliable action-channel judge. Instead, it separated model reasoning from therapeutic authorization. The model could generate an action recommendation, but the controller enforced the locked evidence/action contract.

This supports a governance architecture in which clinical AI systems are evaluated as controlled decision systems, not merely as text generators. In safety-critical domains, action authorization should be constrained by explicit evidence thresholds and decision contracts. The present results show that such a controller can normalize distinct model-specific failure phenotypes under a known therapeutic action contract.

### Benchmark validity and action-cue leakage

This work also contributes a benchmark-design lesson. Naturalistic prompts can still be too easy if they leak the correct action channel. Earlier expanded prompts produced near-ceiling performance, but cue-alignment audit showed that the prompts were action/evidence cue-aligned. After targeted action-cue repair, the hard prompt set exposed substantial model instability.

This finding matters for clinical AI evaluation. A benchmark may appear realistic because it uses clinical language, but still overestimate robustness if the correct management action is too obvious from surface cues. Action-cue leakage should therefore be audited explicitly in clinical AI benchmarks that evaluate management decisions.

### Limitations

This study has several limitations. First, the benchmark is synthetic and should not be interpreted as evidence for clinical deployment. Second, the controller uses the locked expected-action channel as the deterministic evidence/action contract. It is therefore a controller-mechanism study, not a fully autonomous parser-derived clinical decision system. Third, human/expert confirmation was author-domain confirmation rather than independent blinded multi-rater adjudication. Fourth, model APIs and snapshots may change over time. Fifth, this benchmark focuses on oncology therapeutic authorization and may not generalize directly to other clinical domains without domain-specific evidence/action contracts.

### Future work

Future work should evaluate parser-derived evidence contracts, independent blinded oncology adjudication, additional treatment classes, and prospective EHR-like longitudinal scenarios. Additional studies should also assess clinician-AI workflow effects, including whether controller-based systems reduce therapeutic misrouting without increasing unnecessary delay or cognitive burden.

### Conclusion

In a repaired hard action-obscured oncology therapeutic-authorization benchmark, GPT-4.1, Claude Sonnet 4.6, and Gemini Flash all showed clinically meaningful action-channel instability despite perfect schema conformance. The failure phenotype differed by model, but a deterministic evidence-contract controller restored evidence-consistent authorization across all three. These findings support separating model reasoning from therapeutic action authorization in safety-critical clinical AI governance.

---

## Figure and Table Plan

### Main Figures

1. Unguided AACR by model.
2. Unguided wrong-channel rate by model.
3. Controller before/after AACR across models.
4. Model-specific error phenotypes.
5. Controller intervention phenotypes.
6. Expected-vs-selected heatmaps by model.

### Main Tables

1. Three-model unguided comparison.
2. Three-model controller before/after comparison.
3. Error phenotype comparison.
4. Controller intervention comparison.
5. Paired correctness tests.

### Supplementary Tables

1. Expected-vs-selected matrices by model.
2. Full endpoint definitions.
3. Model registry and API provenance.
4. File hash manifest.
5. Controller intervention audit logs.
6. Prompt lineage and cue-repair history.

---

## Data Availability

The benchmark artifacts, scored outputs, controller outputs, tables, figures, and provenance files are maintained in the `oncoguard-response` repository. The primary hard prompt set is `results/v0_66d_targeted_actioncue_repair/v0_66d_model_testing_allowed_hard_prompts.csv`. The three-model synthesis is locked at v0.77, and the methods/provenance supplement is locked at v0.80.

## Code Availability

Evaluation, scoring, controller, synthesis, manuscript scaffold, and provenance-generation scripts are maintained in the repository. Script hashes and primary file SHA256 values are provided in the v0.80 methods/provenance supplement.

## Ethics Statement

This study used synthetic benchmark prompts and did not involve patient data, human subjects, or clinical deployment. The results should not be interpreted as evidence of safety for real-world patient care.

## Author Contributions

Chijioke John Ifedili conceptualized the study, designed the benchmark, developed the evaluation and controller framework, conducted the analyses, interpreted the results, and drafted the manuscript scaffold.

## Funding

No external funding is reported for this draft unless otherwise specified.

## Competing Interests

The author declares no competing interests unless otherwise specified.

## Acknowledgments

The author acknowledges the use of language-model assistance for drafting, coding support, and iterative manuscript development. All scientific framing, benchmark design decisions, and final interpretations remain the responsibility of the author.

"""

(OUTDIR / "v0_81_polished_manuscript_v1.md").write_text(manuscript)

# ---------------------------------------------------------------------
# Separate files for easier editing
# ---------------------------------------------------------------------

sections = {
    "v0_81_abstract.md": manuscript.split("## Abstract")[1].split("## Introduction")[0],
    "v0_81_introduction.md": "## Introduction" + manuscript.split("## Introduction")[1].split("## Methods")[0],
    "v0_81_methods.md": "## Methods" + manuscript.split("## Methods")[1].split("## Results")[0],
    "v0_81_results.md": "## Results" + manuscript.split("## Results")[1].split("## Discussion")[0],
    "v0_81_discussion.md": "## Discussion" + manuscript.split("## Discussion")[1].split("## Figure and Table Plan")[0],
    "v0_81_back_matter.md": "## Figure and Table Plan" + manuscript.split("## Figure and Table Plan")[1],
}

for filename, text in sections.items():
    (OUTDIR / filename).write_text(text.strip() + "\n")

# ---------------------------------------------------------------------
# Tables for manuscript package
# ---------------------------------------------------------------------

manuscript_tables = {
    "v0_81_table1_three_model_unguided.csv": unguided,
    "v0_81_table2_controller_before_after.csv": controller,
    "v0_81_table3_error_phenotypes.csv": errors,
    "v0_81_table4_controller_interventions.csv": interventions,
    "v0_81_table5_paired_tests.csv": paired,
    "v0_81_model_registry.csv": model_registry,
    "v0_81_protocol_notes.csv": protocol_notes,
}

for filename, df in manuscript_tables.items():
    df.to_csv(OUTDIR / filename, index=False)

# ---------------------------------------------------------------------
# Readiness checklist
# ---------------------------------------------------------------------

readiness = pd.DataFrame([
    {
        "item": "Add literature citations",
        "status": "needed",
        "notes": "Introduction and Discussion require citations for clinical AI evaluation, diagnostic safety, oncology decision support, and AI governance.",
    },
    {
        "item": "Independent expert review",
        "status": "future/limitation",
        "notes": "Current confirmation is author-domain; independent blinded multi-rater review would strengthen submission.",
    },
    {
        "item": "Polish Methods",
        "status": "needed",
        "notes": "Methods should be aligned with target journal format.",
    },
    {
        "item": "Finalize figures",
        "status": "partially complete",
        "notes": "v0.77 figures exist; captions and journal formatting still needed.",
    },
    {
        "item": "Finalize title",
        "status": "needed",
        "notes": "Current title is strong but may be adjusted for target journal.",
    },
    {
        "item": "Decide Gemini Pro note placement",
        "status": "needed",
        "notes": "Could be Methods/Supplement protocol note.",
    },
    {
        "item": "Add data/code availability links",
        "status": "needed",
        "notes": "Use GitHub repository and version tags.",
    },
    {
        "item": "Add references",
        "status": "needed",
        "notes": "Reference list not yet generated.",
    },
])

readiness.to_csv(OUTDIR / "v0_81_submission_readiness_checklist.csv", index=False)

# ---------------------------------------------------------------------
# Card
# ---------------------------------------------------------------------

card = f"""# OncoGuard-Response v0.81 — Polished Manuscript v1

## Purpose

v0.81 converts the v0.79 manuscript scaffold into a readable polished manuscript v1.

## Included artifacts

- `v0_81_polished_manuscript_v1.md`
- `v0_81_abstract.md`
- `v0_81_introduction.md`
- `v0_81_methods.md`
- `v0_81_results.md`
- `v0_81_discussion.md`
- `v0_81_back_matter.md`
- manuscript-ready tables
- submission-readiness checklist

## Core manuscript thesis

Hard action-obscured oncology therapeutic-authorization prompts exposed action-channel instability across GPT-4.1, Claude Sonnet 4.6, and Gemini Flash. The failure phenotype differed by model, but a deterministic evidence-contract controller restored evidence-consistent authorization across all three.

## Main numeric results

- GPT-4.1 AACR: {gpt_u['hard_pressure_aacr_percent']:.1f}% → {gpt_c['controller_aacr_percent']:.1f}%.
- Claude Sonnet 4.6 AACR: {claude_u['hard_pressure_aacr_percent']:.1f}% → {claude_c['controller_aacr_percent']:.1f}%.
- Gemini Flash AACR: {gemini_u['hard_pressure_aacr_percent']:.1f}% → {gemini_c['controller_aacr_percent']:.1f}%.

## Remaining before submission

The draft still needs citations, final figure captions, target-journal formatting, and decision on whether to include the Gemini Pro output-protocol note in Methods or Supplement.
"""

(OUTDIR / "onco_guard_response_v0_81_polished_manuscript_v1_card.md").write_text(card)

print("Saved v0.81 polished manuscript v1 package to:", OUTDIR)

print("\nFiles:")
for p in sorted(OUTDIR.glob("*")):
    print(p.name)

print("\nReadiness checklist:")
print(readiness.to_string(index=False))
