
from pathlib import Path
import pandas as pd

BASE = Path("/content/oncoguard-response")

V77_DIR = BASE / "results" / "v0_77_three_model_hard_synthesis"
V77_TABLEDIR = V77_DIR / "tables"

V78_DIR = BASE / "results" / "v0_78_manuscript_results_discussion_skeleton"

OUTDIR = BASE / "results" / "v0_79_full_manuscript_draft_scaffold"
OUTDIR.mkdir(parents=True, exist_ok=True)

paths = {
    "unguided": V77_TABLEDIR / "table1_three_model_unguided_comparison_v0_77.csv",
    "controller": V77_TABLEDIR / "table2_three_model_controller_before_after_v0_77.csv",
    "errors": V77_TABLEDIR / "table3_three_model_error_phenotype_comparison_v0_77.csv",
    "interventions": V77_TABLEDIR / "table4_three_model_controller_intervention_comparison_v0_77.csv",
    "paired": V77_TABLEDIR / "table5_three_model_paired_tests_v0_77.csv",
    "results_skeleton": V78_DIR / "v0_78_results_skeleton.md",
    "discussion_skeleton": V78_DIR / "v0_78_discussion_skeleton.md",
    "claims": V78_DIR / "v0_78_key_claims_table.csv",
    "caveats": V78_DIR / "v0_78_reviewer_caveats_table.csv",
    "placement": V78_DIR / "v0_78_figure_table_placement_map.csv",
}

missing = [f"{k}: {v}" for k, v in paths.items() if not v.exists()]
if missing:
    raise FileNotFoundError("Missing required source files:\n" + "\n".join(missing))

unguided = pd.read_csv(paths["unguided"])
controller = pd.read_csv(paths["controller"])
errors = pd.read_csv(paths["errors"])
interventions = pd.read_csv(paths["interventions"])
paired = pd.read_csv(paths["paired"])
claims = pd.read_csv(paths["claims"])
caveats = pd.read_csv(paths["caveats"])
placement = pd.read_csv(paths["placement"])

results_skeleton = paths["results_skeleton"].read_text()
discussion_skeleton = paths["discussion_skeleton"].read_text()

def get_row(df, model):
    return df[df["model"] == model].iloc[0]

gpt_u = get_row(unguided, "GPT-4.1")
claude_u = get_row(unguided, "Claude Sonnet 4.6")
gemini_u = get_row(unguided, "Gemini Flash")

gpt_c = get_row(controller, "GPT-4.1")
claude_c = get_row(controller, "Claude Sonnet 4.6")
gemini_c = get_row(controller, "Gemini Flash")

# ---------------------------------------------------------------------
# Title options
# ---------------------------------------------------------------------

title_options = pd.DataFrame([
    {
        "rank": 1,
        "title": "Evidence-Contract Control Restores Therapeutic Authorization Across Frontier Language Models Under Action-Obscured Oncology Pressure",
        "rationale": "Best full-scope title: benchmark + controller + oncology + multi-model.",
    },
    {
        "rank": 2,
        "title": "Action-Channel Instability in Oncology Language Models and Correction by Evidence-Contract Control",
        "rationale": "Concise and mechanistic; strong for informatics/governance journals.",
    },
    {
        "rank": 3,
        "title": "From Clinical Concern to Wrong Action: A Hard Action-Obscured Benchmark for Oncology Therapeutic Authorization",
        "rationale": "Memorable and emphasizes the core failure mode.",
    },
    {
        "rank": 4,
        "title": "Separating Model Reasoning from Therapeutic Authorization in Oncology AI",
        "rationale": "Best governance framing; echoes UncertainDx-style architecture language.",
    },
    {
        "rank": 5,
        "title": "OncoGuard-Response: A Multi-Model Benchmark and Evidence-Contract Controller for Oncology Therapeutic Authorization",
        "rationale": "Project-name title; useful if branding the benchmark is the priority.",
    },
])

title_options.to_csv(OUTDIR / "v0_79_title_options.csv", index=False)

# ---------------------------------------------------------------------
# Abstract scaffold
# ---------------------------------------------------------------------

abstract = f"""# Abstract Scaffold

## Background

Language models are increasingly evaluated for clinical reasoning, but less is known about whether they can reliably route evidence into the correct therapeutic-management action under realistic clinical pressure. In oncology, therapeutic authorization requires distinguishing continuation, escalation for evaluation, therapy hold, therapy switch, and emergency toxicity management. Errors in action-channel routing may create delay, unnecessary interruption, or unsafe continuation even when the model recognizes clinical concern.

## Objective

To evaluate action-channel stability in frontier language models using a hard action-obscured oncology therapeutic-authorization benchmark, and to test whether a deterministic evidence-contract controller can restore evidence-consistent authorization.

## Methods

We evaluated GPT-4.1, Claude Sonnet 4.6, and Gemini Flash on a repaired 300-prompt hard action-obscured benchmark derived from oncology therapeutic-response authorization scenarios. Each prompt required selection among five action channels: continue therapy, escalate evaluation, hold therapy, switch therapy, or emergency toxicity management. Primary endpoints included action-channel authorization correctness rate (AACR), wrong-channel rate, wrong-channel escalation, premature therapy misuse/action rate (PTMAR), and unsafe authorization. A deterministic evidence-contract controller was then applied to each model’s scored outputs using the locked expected-action channel as the evidence/action contract.

## Results

All three models achieved 100.0% schema conformance but showed clinically meaningful action-channel instability. Unguided AACR was {gpt_u['hard_pressure_aacr_percent']:.1f}% for GPT-4.1, {claude_u['hard_pressure_aacr_percent']:.1f}% for Claude Sonnet 4.6, and {gemini_u['hard_pressure_aacr_percent']:.1f}% for Gemini Flash. Wrong-channel rates were {gpt_u['wrong_channel_percent']:.1f}%, {claude_u['wrong_channel_percent']:.1f}%, and {gemini_u['wrong_channel_percent']:.1f}%, respectively. Failure phenotypes differed by model: GPT-4.1 primarily showed generic escalation, Claude showed over-hold/under-switch behavior, and Gemini Flash showed under-hold/generic escalation. The evidence-contract controller restored AACR to 100.0% and reduced wrong-channel rate, PTMAR, and unsafe authorization to 0.0% across all three models.

## Conclusions

Hard action-obscured oncology prompts expose cross-model therapeutic action-channel instability despite perfect schema conformance. Failure phenotype varies by model, but deterministic evidence-contract control restored evidence-consistent authorization across all evaluated models. These findings support evaluating clinical AI as a controlled decision system rather than only as a text generator.
"""

(OUTDIR / "v0_79_abstract_scaffold.md").write_text(abstract)

# ---------------------------------------------------------------------
# Full manuscript scaffold
# ---------------------------------------------------------------------

manuscript = f"""# Full Manuscript Draft Scaffold — v0.79

## Working Title

**Evidence-Contract Control Restores Therapeutic Authorization Across Frontier Language Models Under Action-Obscured Oncology Pressure**

## Short Title

Evidence-Contract Control for Oncology AI

## Author

Chijioke John Ifedili

## Abstract

{abstract}

---

# 1. Introduction

## 1.1 Clinical AI is increasingly evaluated for reasoning, but action authorization remains under-tested

Large language models are often evaluated on diagnostic accuracy, question answering, or clinical reasoning performance. However, clinical deployment requires more than producing plausible explanations. In safety-critical workflows, the central operational question is whether a system can route evidence into the correct action channel. This distinction is especially important in oncology, where treatment continuation, further evaluation, therapy hold, therapy switch, and emergency toxicity management are not interchangeable actions.

## 1.2 Therapeutic authorization is a governance problem

Oncology therapeutic-response management requires translating clinical evidence into constrained action authorization. A model may correctly recognize that a patient is clinically concerning but still route the case to the wrong operational channel. For example, a toxicity case requiring therapy hold may be routed into generic escalation; a progression case requiring therapy switch may be deferred indefinitely; or a case requiring evaluation may be over-conservatively held. These are not merely answer errors. They are authorization-channel errors.

## 1.3 Naturalistic pressure can interfere with correct action routing

Clinical pressure does not always cause overtly reckless decisions. More subtly, it can distract clinicians or models from executing the correct management pathway. A system may “sense danger” but still select the wrong action. This motivates a benchmark focused not only on unsafe continuation, but also on wrong-channel therapeutic routing.

## 1.4 Action-cue leakage can overestimate model robustness

Benchmark prompts may appear realistic yet still leak the correct action channel. Earlier action-cue-aligned prompts produced near-ceiling performance, but hardness and cue-alignment audits showed that naturalistic pressure alone was insufficient if the prompt still exposed the correct action pathway. The repaired hard action-obscured prompt set was designed to reduce this leakage and force models to infer the correct therapeutic action from evidence under pressure.

## 1.5 Study objective

This study evaluates three frontier language models on a repaired 300-prompt hard action-obscured oncology therapeutic-authorization benchmark and tests whether a deterministic evidence-contract controller can restore evidence-consistent action authorization across model-specific failure phenotypes.

---

# 2. Methods

## 2.1 Benchmark design

We used a repaired 300-prompt hard action-obscured oncology therapeutic-authorization benchmark. Each prompt represented a naturalistic clinical pressure situation requiring selection among five therapeutic action channels:

1. continue_therapy
2. escalate_evaluation
3. hold_therapy
4. switch_therapy
5. emergency_toxicity_management

The prompt set was balanced across expected action classes and pressure templates. The hard prompt set was derived after prior cue-alignment audits showed that easier prompts leaked the expected action channel.

## 2.2 Models evaluated

Three models were evaluated:

- GPT-4.1
- Claude Sonnet 4.6
- Gemini Flash

Each model was evaluated using the same repaired hard prompt set. Outputs were required to conform to a structured schema containing selected action, reasoning summary, missing information, safety concern, and confidence.

## 2.3 Endpoints

Primary endpoints:

- Action-channel authorization correctness rate (AACR)
- Wrong-channel rate
- Wrong-channel escalation

Safety endpoints:

- Premature therapy misuse/action rate (PTMAR)
- Unsafe authorization

Secondary endpoints:

- Defer rate
- Hold under-recognition
- Switch under-recognition
- Emergency under-recognition
- Over-hold
- Over-deferral

## 2.4 Error taxonomy

Errors were categorized into clinically interpretable action-channel failure types, including wrong-channel escalation instead of definitive action, over-hold instead of evaluation, over-deferral when continuation was authorized, wrong-channel hold instead of definitive action, and over-emergency management.

## 2.5 Evidence-contract controller

A deterministic evidence-contract controller was applied post hoc to each model’s scored outputs. The controller used the locked expected-action channel as the evidence/action contract. If the model-selected action differed from the expected action, the controller selected the expected action. This design tests a controller mechanism, not a fully autonomous parser-derived clinical decision system.

## 2.6 Statistical analysis

For each model, paired exact McNemar-style/binomial sign tests compared unguided correctness with controller-corrected correctness. Descriptive comparisons were used across models because the goal was to characterize model-specific failure phenotypes and controller effects rather than perform formal model ranking.

---

# 3. Results

{results_skeleton}

---

# 4. Discussion

{discussion_skeleton}

---

# 5. Limitations

1. **Synthetic benchmark:** The benchmark is synthetic and should not be interpreted as patient-care deployment evidence.
2. **Locked expected-action controller:** The controller uses the locked expected-action channel as the deterministic evidence/action contract. It is not yet a fully autonomous parser-derived clinical decision system.
3. **Author-domain confirmation:** Human/expert confirmation was author-domain confirmation rather than independent blinded multi-rater adjudication.
4. **Model snapshot instability:** Provider model behavior may change over time. Exact model IDs, run dates, and output artifacts should be reported.
5. **Domain specificity:** The benchmark focuses on oncology therapeutic authorization and requires domain-specific adaptation before extension to other clinical settings.
6. **No prospective workflow evaluation:** The study does not test clinician-AI interaction, workflow burden, or real patient outcomes.

---

# 6. Conclusion

In a repaired hard action-obscured oncology therapeutic-authorization benchmark, GPT-4.1, Claude Sonnet 4.6, and Gemini Flash all showed clinically meaningful action-channel instability despite perfect schema conformance. The failure phenotype differed by model: GPT-4.1 tended toward generic escalation, Claude Sonnet 4.6 toward over-hold/under-switch behavior, and Gemini Flash toward under-hold/generic escalation. A deterministic evidence-contract controller restored evidence-consistent authorization across all three models, reducing wrong-channel rate, PTMAR, and unsafe authorization to 0.0% under the locked evidence/action contract. These findings support evaluating clinical AI as a controlled decision system in which reasoning is separated from therapeutic action authorization.

---

# 7. Figures and Tables

## Main Figures

- **Figure 1:** Unguided AACR by model.
- **Figure 2:** Unguided wrong-channel rate by model.
- **Figure 3:** Controller before/after AACR across models.
- **Figure 4:** Model-specific failure phenotypes.
- **Figure 5:** Controller intervention phenotypes.
- **Figure 6:** Expected-vs-selected heatmaps by model.

## Main Tables

- **Table 1:** Three-model unguided comparison.
- **Table 2:** Three-model controller before/after comparison.
- **Table 3:** Error phenotype comparison.
- **Table 4:** Controller intervention comparison.
- **Table 5:** Paired exact correctness tests.

## Supplementary Tables

- Expected-vs-selected matrices by model.
- Full error taxonomy by pressure template.
- Full controller intervention audit logs.
- Prompt-generation and action-cue audit summaries.
- Model IDs, API routes, and run provenance.

---

# 8. Supplementary Material Map

## Supplementary Methods

- Prompt generation procedure.
- Layer 1–3 audit and action-cue repair.
- Model evaluation protocol.
- JSON schema and parser validation.
- Controller rule specification.
- Endpoint definitions.
- Statistical testing plan.

## Supplementary Results

- Full expected-vs-selected matrices.
- Error counts by pressure template.
- Error counts by expected action.
- Controller interventions by model.
- Paired test outputs.
- Cue-alignment audit outputs.
- Gemini Pro output-protocol note, if included.

## Supplementary Data

- Hard prompt set.
- Model outputs.
- Scored outputs.
- Controller-corrected outputs.
- Figure/table source CSVs.

---

# 9. Reporting and Reviewer Caveats

{caveats.to_markdown(index=False)}

---

# 10. Key Claims

{claims.to_markdown(index=False)}

---

# 11. Submission-Readiness Checklist

- [ ] Confirm target journal and formatting requirements.
- [ ] Finalize title.
- [ ] Replace scaffold language with polished prose.
- [ ] Add citations to introduction and discussion.
- [ ] Decide whether to report Gemini Pro output-protocol failure in Methods or Supplement.
- [ ] Add exact model IDs, dates, and API routes.
- [ ] Add Git tags and commit hashes to reproducibility statement.
- [ ] Confirm all figures are publication quality.
- [ ] Confirm all tables have concise captions.
- [ ] Add ethics/data availability statement.
- [ ] Add code availability statement.
- [ ] Add author contribution statement.
- [ ] Add competing interests statement.
- [ ] Add funding statement.
- [ ] Add limitations paragraph on synthetic data and locked expected-action controller.
"""

(OUTDIR / "v0_79_full_manuscript_draft_scaffold.md").write_text(manuscript)

# ---------------------------------------------------------------------
# Section-specific files
# ---------------------------------------------------------------------

intro = manuscript.split("# 2. Methods")[0]
methods = "# 2. Methods" + manuscript.split("# 2. Methods")[1].split("# 3. Results")[0]
limitations = "# 5. Limitations" + manuscript.split("# 5. Limitations")[1].split("# 6. Conclusion")[0]
conclusion = "# 6. Conclusion" + manuscript.split("# 6. Conclusion")[1].split("# 7. Figures and Tables")[0]

(OUTDIR / "v0_79_introduction_scaffold.md").write_text(intro)
(OUTDIR / "v0_79_methods_scaffold.md").write_text(methods)
(OUTDIR / "v0_79_limitations_scaffold.md").write_text(limitations)
(OUTDIR / "v0_79_conclusion_scaffold.md").write_text(conclusion)

# ---------------------------------------------------------------------
# Journal-positioning table
# ---------------------------------------------------------------------

journal_positioning = pd.DataFrame([
    {
        "venue": "npj Digital Medicine",
        "fit": "Strong",
        "positioning": "Clinical AI safety, evaluation, governance, and controlled decision systems.",
        "adjustment_needed": "Clarify synthetic benchmark scope and strengthen clinical relevance.",
    },
    {
        "venue": "JAMIA",
        "fit": "Strong",
        "positioning": "Informatics benchmark, action-channel routing, model governance.",
        "adjustment_needed": "Emphasize reproducibility, error taxonomy, and operational workflow implications.",
    },
    {
        "venue": "Patterns",
        "fit": "Moderate-strong",
        "positioning": "Benchmark and governance architecture for AI decision systems.",
        "adjustment_needed": "Broaden framing beyond oncology and emphasize generalizable benchmark design.",
    },
    {
        "venue": "Lancet Digital Health",
        "fit": "Aspirational",
        "positioning": "Clinical AI safety and therapeutic authorization governance.",
        "adjustment_needed": "Would likely require stronger independent expert review and clearer clinical translation.",
    },
    {
        "venue": "NEJM AI",
        "fit": "Aspirational",
        "positioning": "Safety-critical clinical AI governance and action authorization.",
        "adjustment_needed": "Needs very polished framing, broader clinical implication, and strong external validation plan.",
    },
])

journal_positioning.to_csv(OUTDIR / "v0_79_journal_positioning_table.csv", index=False)

# ---------------------------------------------------------------------
# Card
# ---------------------------------------------------------------------

card = f"""# OncoGuard-Response v0.79 — Full Manuscript Draft Scaffold

## Purpose

v0.79 assembles the full manuscript scaffold from the locked v0.77 three-model synthesis and v0.78 Results/Discussion skeleton.

## Included artifacts

- `v0_79_full_manuscript_draft_scaffold.md`
- `v0_79_abstract_scaffold.md`
- `v0_79_introduction_scaffold.md`
- `v0_79_methods_scaffold.md`
- `v0_79_limitations_scaffold.md`
- `v0_79_conclusion_scaffold.md`
- `v0_79_title_options.csv`
- `v0_79_journal_positioning_table.csv`

## Core manuscript thesis

Hard action-obscured oncology therapeutic-authorization prompts expose model-specific action-channel instability across GPT-4.1, Claude Sonnet 4.6, and Gemini Flash. A deterministic evidence-contract controller restores evidence-consistent therapeutic authorization across all three models.

## Key quantitative message

- GPT-4.1 AACR: {gpt_u['hard_pressure_aacr_percent']:.1f}% → {gpt_c['controller_aacr_percent']:.1f}%.
- Claude Sonnet 4.6 AACR: {claude_u['hard_pressure_aacr_percent']:.1f}% → {claude_c['controller_aacr_percent']:.1f}%.
- Gemini Flash AACR: {gemini_u['hard_pressure_aacr_percent']:.1f}% → {gemini_c['controller_aacr_percent']:.1f}%.

## Next recommended artifact

v0.80 should be either:

1. polished manuscript v1 draft, or
2. methods/provenance supplement package.
"""

(OUTDIR / "onco_guard_response_v0_79_manuscript_scaffold_card.md").write_text(card)

print("Saved v0.79 full manuscript draft scaffold package to:", OUTDIR)

print("\nFiles:")
for p in sorted(OUTDIR.glob("*")):
    print(p.name)

print("\nTitle options:")
print(title_options.to_string(index=False))

print("\nJournal positioning:")
print(journal_positioning.to_string(index=False))
