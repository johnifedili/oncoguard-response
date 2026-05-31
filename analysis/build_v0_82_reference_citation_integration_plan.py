
from pathlib import Path
import pandas as pd

BASE = Path("/content/oncoguard-response")

V81_DIR = BASE / "results" / "v0_81_polished_manuscript_v1"
V80_DIR = BASE / "results" / "v0_80_methods_provenance_supplement"

OUTDIR = BASE / "results" / "v0_82_reference_citation_integration_plan"
OUTDIR.mkdir(parents=True, exist_ok=True)

paths = {
    "manuscript_v1": V81_DIR / "v0_81_polished_manuscript_v1.md",
    "methods_provenance_card": V80_DIR / "onco_guard_response_v0_80_methods_provenance_card.md",
    "endpoint_definitions": V80_DIR / "v0_80_endpoint_definitions.csv",
    "model_registry": V80_DIR / "v0_80_model_registry.csv",
    "protocol_notes": V80_DIR / "v0_80_protocol_notes_and_deviations.csv",
}

missing = [f"{k}: {v}" for k, v in paths.items() if not v.exists()]
if missing:
    raise FileNotFoundError("Missing required source files:\n" + "\n".join(missing))

manuscript_text = paths["manuscript_v1"].read_text()

# ---------------------------------------------------------------------
# Citation domains
# ---------------------------------------------------------------------

citation_domains = pd.DataFrame([
    {
        "domain_id": "D01",
        "domain": "Clinical LLM evaluation and limitations",
        "why_needed": "Supports the claim that clinical LLMs require rigorous evaluation beyond plausible reasoning.",
        "where_to_cite": "Introduction paragraphs 1–2; Discussion principal findings.",
        "example_source_types": "JAMA Network Open clinical reasoning trials; Nature Medicine LLM limitation studies; systematic reviews of LLMs in healthcare.",
        "priority": "high",
    },
    {
        "domain_id": "D02",
        "domain": "Clinical AI reporting guidelines",
        "why_needed": "Supports transparency, protocol reporting, and reviewer-facing reproducibility.",
        "where_to_cite": "Methods; Limitations; Reporting statement.",
        "example_source_types": "DECIDE-AI; CONSORT-AI; SPIRIT-AI; TRIPOD-AI if prediction framing is used.",
        "priority": "high",
    },
    {
        "domain_id": "D03",
        "domain": "AI governance and risk management",
        "why_needed": "Supports the governance framing that clinical AI should be treated as a controlled decision system.",
        "where_to_cite": "Introduction governance paragraph; Discussion evidence-contract control.",
        "example_source_types": "NIST AI RMF; FDA AI/ML SaMD guidance; WHO health AI ethics/governance guidance.",
        "priority": "high",
    },
    {
        "domain_id": "D04",
        "domain": "Clinical decision support and medication/therapy safety",
        "why_needed": "Positions therapeutic authorization as a safety-critical clinical decision-support problem.",
        "where_to_cite": "Introduction oncology therapeutic authorization; Methods benchmark design.",
        "example_source_types": "CDSS safety literature; oncology decision support papers; medication safety AI/CDSS studies.",
        "priority": "high",
    },
    {
        "domain_id": "D05",
        "domain": "Human factors, pressure, and workflow safety",
        "why_needed": "Supports the claim that urgency, authority, social pressure, and workflow pressure can degrade action routing.",
        "where_to_cite": "Introduction naturalistic pressure; Discussion action-channel interference.",
        "example_source_types": "Human factors in medication safety; diagnostic error literature; authority gradient and interruption literature.",
        "priority": "medium-high",
    },
    {
        "domain_id": "D06",
        "domain": "Benchmark validity, leakage, and shortcut learning",
        "why_needed": "Supports the action-cue leakage contribution and the need for hard action-obscured prompts.",
        "where_to_cite": "Introduction action-cue leakage; Discussion benchmark validity.",
        "example_source_types": "Dataset leakage; shortcut learning; benchmark contamination; adversarial evaluation literature.",
        "priority": "high",
    },
    {
        "domain_id": "D07",
        "domain": "Guardrails, controllers, and constrained decision systems",
        "why_needed": "Supports the external controller architecture and separation of model reasoning from authorization.",
        "where_to_cite": "Methods controller; Discussion evidence-contract control.",
        "example_source_types": "AI guardrails; neuro-symbolic systems; constrained decoding; safety controllers; clinical CDS rule systems.",
        "priority": "high",
    },
    {
        "domain_id": "D08",
        "domain": "Oncology treatment response and toxicity management",
        "why_needed": "Supports clinical plausibility of action channels: continue, evaluate, hold, switch, emergency management.",
        "where_to_cite": "Methods benchmark design; Supplementary clinical rationale.",
        "example_source_types": "ASCO/ESMO/NCCN toxicity management guidelines; immune-related adverse event management; RECIST/progression literature.",
        "priority": "medium-high",
    },
])

citation_domains.to_csv(OUTDIR / "v0_82_citation_domains.csv", index=False)

# ---------------------------------------------------------------------
# Candidate reference seed list
# ---------------------------------------------------------------------

reference_seed_list = pd.DataFrame([
    {
        "ref_id": "R01",
        "topic": "Clinical LLM diagnostic reasoning",
        "candidate_reference": "Goh et al. Large Language Model Influence on Diagnostic Reasoning. JAMA Network Open. 2024.",
        "supports": "LLM availability did not significantly improve physician diagnostic reasoning compared with conventional resources.",
        "use_in_manuscript": "Introduction and Discussion: LLM reasoning tools need workflow-specific evaluation.",
        "status": "seed_reference_verify_metadata",
    },
    {
        "ref_id": "R02",
        "topic": "LLM limitations in clinical diagnosis",
        "candidate_reference": "Hager et al. Evaluation and mitigation of the limitations of large language models in clinical decision-making. Nature Medicine. 2024.",
        "supports": "Current models can underperform trained clinicians and need rigorous limitation analysis.",
        "use_in_manuscript": "Introduction: clinical reasoning ability does not equal safe decision support.",
        "status": "seed_reference_verify_metadata",
    },
    {
        "ref_id": "R03",
        "topic": "Clinical AI reporting guideline",
        "candidate_reference": "Vasey et al. DECIDE-AI reporting guideline for early-stage clinical evaluation of AI decision support systems. Nature Medicine/BMJ-linked guideline family. 2022.",
        "supports": "Transparent reporting of early-stage clinical AI decision-support studies.",
        "use_in_manuscript": "Methods and Supplement: reporting transparency and reproducibility.",
        "status": "seed_reference_verify_metadata",
    },
    {
        "ref_id": "R04",
        "topic": "AI risk management",
        "candidate_reference": "NIST Artificial Intelligence Risk Management Framework (AI RMF 1.0). 2023.",
        "supports": "Risk management framing for trustworthy AI systems.",
        "use_in_manuscript": "Discussion: governance framing and controlled decision systems.",
        "status": "seed_reference_verify_metadata",
    },
    {
        "ref_id": "R05",
        "topic": "Health AI governance",
        "candidate_reference": "WHO guidance on ethics and governance of artificial intelligence for health.",
        "supports": "High-level health AI governance and safety principles.",
        "use_in_manuscript": "Discussion and limitations.",
        "status": "needs_web_verification",
    },
    {
        "ref_id": "R06",
        "topic": "CONSORT-AI / SPIRIT-AI",
        "candidate_reference": "CONSORT-AI and SPIRIT-AI reporting extensions.",
        "supports": "Clinical trial/reporting standards for AI interventions.",
        "use_in_manuscript": "Methods caveat: study is preclinical/synthetic, not clinical trial.",
        "status": "needs_web_verification",
    },
    {
        "ref_id": "R07",
        "topic": "Human factors / clinical pressure",
        "candidate_reference": "Authority gradient, interruption, workload, and medication safety human-factors literature.",
        "supports": "Clinical pressure can disrupt correct safety-channel execution.",
        "use_in_manuscript": "Discussion: naturalistic pressure as action-channel interference.",
        "status": "needs_literature_search",
    },
    {
        "ref_id": "R08",
        "topic": "Benchmark leakage / shortcut learning",
        "candidate_reference": "Shortcut learning and benchmark leakage literature in machine learning evaluation.",
        "supports": "Action-cue leakage can inflate benchmark performance.",
        "use_in_manuscript": "Discussion: benchmark validity contribution.",
        "status": "needs_literature_search",
    },
    {
        "ref_id": "R09",
        "topic": "AI guardrails / controllers",
        "candidate_reference": "Guardrails, constrained decision systems, and external safety-controller literature.",
        "supports": "Separation of model reasoning from action authorization.",
        "use_in_manuscript": "Discussion: evidence-contract control as governance architecture.",
        "status": "needs_literature_search",
    },
    {
        "ref_id": "R10",
        "topic": "Oncology toxicity/response management",
        "candidate_reference": "ASCO/ESMO/NCCN immune-related adverse event and oncology response-management guidance.",
        "supports": "Clinical action channels: hold, switch, evaluate, emergency management.",
        "use_in_manuscript": "Methods benchmark rationale and Supplement.",
        "status": "needs_guideline_selection",
    },
])

reference_seed_list.to_csv(OUTDIR / "v0_82_reference_seed_list.csv", index=False)

# ---------------------------------------------------------------------
# Manuscript section citation map
# ---------------------------------------------------------------------

section_citation_map = pd.DataFrame([
    {
        "section": "Abstract",
        "citation_need": "Usually no citations unless journal permits; keep evidence internal to study.",
        "recommended_refs": "",
        "priority": "low",
    },
    {
        "section": "Introduction paragraph 1",
        "citation_need": "Clinical LLMs increasingly evaluated for clinical reasoning and decision support.",
        "recommended_refs": "R01; R02; systematic reviews",
        "priority": "high",
    },
    {
        "section": "Introduction paragraph 2",
        "citation_need": "Oncology therapeutic management requires distinct action channels and safety-sensitive decisions.",
        "recommended_refs": "R10; oncology toxicity/response guidance",
        "priority": "high",
    },
    {
        "section": "Introduction paragraph 3",
        "citation_need": "Clinical pressure, interruptions, and authority/workflow pressure can affect safety behavior.",
        "recommended_refs": "R07",
        "priority": "medium-high",
    },
    {
        "section": "Introduction paragraph 4",
        "citation_need": "Benchmark cue leakage and shortcut learning can inflate model performance.",
        "recommended_refs": "R08",
        "priority": "high",
    },
    {
        "section": "Methods benchmark design",
        "citation_need": "Reporting guidance and benchmark transparency.",
        "recommended_refs": "R03; R06",
        "priority": "high",
    },
    {
        "section": "Methods endpoints",
        "citation_need": "Endpoint definitions mostly internal; cite reporting/clinical safety where needed.",
        "recommended_refs": "R03; R10",
        "priority": "medium",
    },
    {
        "section": "Methods controller",
        "citation_need": "Guardrail/controller/constrained decision system framing.",
        "recommended_refs": "R04; R09",
        "priority": "high",
    },
    {
        "section": "Discussion principal findings",
        "citation_need": "Compare with prior LLM clinical reasoning limitations.",
        "recommended_refs": "R01; R02",
        "priority": "high",
    },
    {
        "section": "Discussion naturalistic pressure",
        "citation_need": "Support pressure as workflow/human-factors risk.",
        "recommended_refs": "R07",
        "priority": "medium-high",
    },
    {
        "section": "Discussion evidence-contract control",
        "citation_need": "AI governance, risk management, controller/guardrail framing.",
        "recommended_refs": "R04; R05; R09",
        "priority": "high",
    },
    {
        "section": "Discussion benchmark validity",
        "citation_need": "Support action-cue leakage as benchmark validity issue.",
        "recommended_refs": "R08",
        "priority": "high",
    },
    {
        "section": "Limitations",
        "citation_need": "Synthetic benchmark, reporting limitations, external validation requirements.",
        "recommended_refs": "R03; R06",
        "priority": "medium-high",
    },
])

section_citation_map.to_csv(OUTDIR / "v0_82_section_citation_map.csv", index=False)

# ---------------------------------------------------------------------
# Citation insertion todo list
# ---------------------------------------------------------------------

todo = pd.DataFrame([
    {
        "task_order": 1,
        "task": "Verify metadata for seed references R01-R06",
        "output": "Confirmed citation strings with DOI/PMID/URL where available.",
    },
    {
        "task_order": 2,
        "task": "Search human-factors/clinical pressure literature for R07",
        "output": "3–5 references on authority gradient, interruption, workload, and medication/clinical safety.",
    },
    {
        "task_order": 3,
        "task": "Search benchmark leakage/shortcut learning literature for R08",
        "output": "3–5 ML benchmark validity references.",
    },
    {
        "task_order": 4,
        "task": "Search guardrail/controller literature for R09",
        "output": "3–5 references on external controllers, constrained decision systems, guardrails.",
    },
    {
        "task_order": 5,
        "task": "Select oncology guideline citations for R10",
        "output": "ASCO/ESMO/NCCN or equivalent guideline sources for therapy hold/switch/emergency toxicity actions.",
    },
    {
        "task_order": 6,
        "task": "Insert citations into v0.81 manuscript",
        "output": "v0.83 cited manuscript draft.",
    },
    {
        "task_order": 7,
        "task": "Generate reference list in target journal style",
        "output": "v0.83 reference list and citation-integrated manuscript.",
    },
])

todo.to_csv(OUTDIR / "v0_82_citation_integration_todo.csv", index=False)

# ---------------------------------------------------------------------
# Search query plan for next web/literature pass
# ---------------------------------------------------------------------

search_queries = pd.DataFrame([
    {
        "query_group": "clinical_llm_evaluation",
        "query": "large language models clinical reasoning diagnostic reasoning evaluation JAMA Network Open 2024",
        "target": "Clinical LLM evaluation studies.",
    },
    {
        "query_group": "clinical_llm_limitations",
        "query": "large language models clinical decision making limitations Nature Medicine 2024 Hager",
        "target": "Nature Medicine LLM limitation study.",
    },
    {
        "query_group": "reporting_guidelines",
        "query": "DECIDE-AI CONSORT-AI SPIRIT-AI reporting guidelines artificial intelligence clinical decision support",
        "target": "Clinical AI reporting standards.",
    },
    {
        "query_group": "governance",
        "query": "NIST AI Risk Management Framework healthcare AI governance WHO ethics governance AI health",
        "target": "AI governance frameworks.",
    },
    {
        "query_group": "human_factors_pressure",
        "query": "clinical pressure authority gradient interruption workload medication safety human factors",
        "target": "Human factors / clinical pressure literature.",
    },
    {
        "query_group": "benchmark_leakage",
        "query": "benchmark leakage shortcut learning machine learning evaluation dataset artifacts",
        "target": "Benchmark validity literature.",
    },
    {
        "query_group": "guardrails_controllers",
        "query": "AI guardrails external controller constrained decision system safety critical AI",
        "target": "Controller/guardrail literature.",
    },
    {
        "query_group": "oncology_guidelines",
        "query": "ASCO guideline immune-related adverse events hold therapy emergency toxicity management oncology",
        "target": "Oncology therapeutic action guidance.",
    },
])

search_queries.to_csv(OUTDIR / "v0_82_literature_search_query_plan.csv", index=False)

# ---------------------------------------------------------------------
# Markdown citation plan
# ---------------------------------------------------------------------

citation_plan_md = f"""# OncoGuard-Response v0.82 — Reference/Citation Integration Plan

## Purpose

v0.82 defines the citation architecture for the polished v0.81 manuscript.

The goal is to add a scholarly backbone without diluting the paper’s central contribution:

1. Hard action-obscured oncology prompts expose action-channel instability.
2. Failure phenotype differs across GPT-4.1, Claude Sonnet 4.6, and Gemini Flash.
3. A deterministic evidence-contract controller restores evidence-consistent authorization across all three.
4. Action-cue leakage can inflate benchmark performance.
5. Clinical AI should be evaluated as a controlled decision system, not only as a text generator.

## Citation domains

{citation_domains.to_markdown(index=False)}

## Seed reference list

{reference_seed_list.to_markdown(index=False)}

## Section citation map

{section_citation_map.to_markdown(index=False)}

## Citation integration todo

{todo.to_markdown(index=False)}

## Literature search query plan

{search_queries.to_markdown(index=False)}

## Notes for v0.83

v0.83 should become the citation-integrated manuscript draft. It should not over-cite the empirical result sections, because the empirical results are original. Citations should primarily support:

- why clinical LLM evaluation needs more than reasoning accuracy;
- why reporting/provenance matters;
- why governance/controller framing is appropriate;
- why action-cue leakage is a benchmark validity problem;
- why oncology therapeutic action channels are clinically meaningful.

## Citation placement rule

Avoid citation stacking at the end of paragraphs. Use citations to support claims, not to decorate every sentence. The Results section should cite internal tables/figures, while the Introduction and Discussion should carry most external citations.
"""

(OUTDIR / "v0_82_reference_citation_integration_plan.md").write_text(citation_plan_md)

# ---------------------------------------------------------------------
# Package card
# ---------------------------------------------------------------------

card = """# OncoGuard-Response v0.82 — Reference/Citation Integration Plan

## Purpose

v0.82 creates the citation architecture for the polished v0.81 manuscript.

## Included artifacts

- `v0_82_citation_domains.csv`
- `v0_82_reference_seed_list.csv`
- `v0_82_section_citation_map.csv`
- `v0_82_citation_integration_todo.csv`
- `v0_82_literature_search_query_plan.csv`
- `v0_82_reference_citation_integration_plan.md`

## Next recommended artifact

v0.83 = citation-integrated manuscript draft with verified references.
"""

(OUTDIR / "onco_guard_response_v0_82_citation_plan_card.md").write_text(card)

print("Saved v0.82 reference/citation integration plan to:", OUTDIR)

print("\nFiles:")
for p in sorted(OUTDIR.glob("*")):
    print(p.name)

print("\nCitation domains:")
print(citation_domains.to_string(index=False))

print("\nReference seed list:")
print(reference_seed_list.to_string(index=False))

print("\nSection citation map:")
print(section_citation_map.to_string(index=False))
