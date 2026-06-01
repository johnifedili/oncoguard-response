
from pathlib import Path
import pandas as pd
import re

BASE = Path("/content/oncoguard-response")

V81_DIR = BASE / "results" / "v0_81_polished_manuscript_v1"
V82_DIR = BASE / "results" / "v0_82_reference_citation_integration_plan"
OUTDIR = BASE / "results" / "v0_83_citation_integrated_manuscript"
OUTDIR.mkdir(parents=True, exist_ok=True)

paths = {
    "manuscript_v1": V81_DIR / "v0_81_polished_manuscript_v1.md",
    "citation_domains": V82_DIR / "v0_82_citation_domains.csv",
    "section_map": V82_DIR / "v0_82_section_citation_map.csv",
    "citation_plan": V82_DIR / "v0_82_reference_citation_integration_plan.md",
}

missing = [f"{k}: {v}" for k, v in paths.items() if not v.exists()]
if missing:
    raise FileNotFoundError("Missing required source files:\n" + "\n".join(missing))

manuscript = paths["manuscript_v1"].read_text()
citation_domains = pd.read_csv(paths["citation_domains"])
section_map = pd.read_csv(paths["section_map"])

# ---------------------------------------------------------------------
# Verified reference registry
# ---------------------------------------------------------------------

verified_refs = pd.DataFrame([
    {
        "ref_num": 1,
        "citation_key": "Goh2024_JAMANetworkOpen",
        "reference": "Goh E, Gallo R, Hom J, et al. Large Language Model Influence on Diagnostic Reasoning: A Randomized Clinical Trial. JAMA Network Open. 2024.",
        "doi_or_url": "https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395",
        "verified_status": "verified_online",
        "supports": "Clinical LLM evaluation; LLM availability did not significantly improve physicians' diagnostic reasoning compared with conventional resources.",
    },
    {
        "ref_num": 2,
        "citation_key": "Hager2024_NatureMedicine",
        "reference": "Hager P, Jungmann F, Holland R, et al. Evaluation and mitigation of the limitations of large language models in clinical decision-making. Nature Medicine. 2024;30:2613-2622.",
        "doi_or_url": "https://doi.org/10.1038/s41591-024-03097-1",
        "verified_status": "verified_online",
        "supports": "LLMs are not ready for autonomous clinical decision-making; models may fail instruction following and workflow integration.",
    },
    {
        "ref_num": 3,
        "citation_key": "Vasey2022_DECIDEAI",
        "reference": "Vasey B, Nagendran M, Campbell B, et al. Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI. Nature Medicine. 2022;28:924-933.",
        "doi_or_url": "https://doi.org/10.1038/s41591-022-01772-9",
        "verified_status": "verified_online",
        "supports": "Reporting guidance for early-stage clinical AI decision-support evaluation.",
    },
    {
        "ref_num": 4,
        "citation_key": "Liu2020_CONSORTAI",
        "reference": "Liu X, Rivera SC, Moher D, Calvert MJ, Denniston AK. Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension. Nature Medicine. 2020;26:1364-1374.",
        "doi_or_url": "https://doi.org/10.1038/s41591-020-1034-x",
        "verified_status": "verified_online",
        "supports": "Transparent reporting for clinical trials involving AI interventions.",
    },
    {
        "ref_num": 5,
        "citation_key": "Rivera2020_SPIRITAI",
        "reference": "Rivera SC, Liu X, Chan AW, Denniston AK, Calvert MJ. Guidelines for clinical trial protocols for interventions involving artificial intelligence: the SPIRIT-AI extension. Nature Medicine. 2020;26:1351-1363.",
        "doi_or_url": "https://doi.org/10.1038/s41591-020-1037-7",
        "verified_status": "verified_online",
        "supports": "Transparent protocol reporting for clinical trials involving AI interventions.",
    },
    {
        "ref_num": 6,
        "citation_key": "NIST2023_AIRMF",
        "reference": "National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 2023.",
        "doi_or_url": "https://www.nist.gov/itl/ai-risk-management-framework",
        "verified_status": "verified_online",
        "supports": "AI risk management and governance framing.",
    },
    {
        "ref_num": 7,
        "citation_key": "WHO2021_HealthAIGovernance",
        "reference": "World Health Organization. Ethics and governance of artificial intelligence for health. 2021.",
        "doi_or_url": "https://www.who.int/publications/i/item/9789240029200",
        "verified_status": "verified_online",
        "supports": "Ethical and governance principles for AI in health.",
    },
    {
        "ref_num": 8,
        "citation_key": "Schneider2021_ASCOirAE",
        "reference": "Schneider BJ, Naidoo J, Santomasso BD, et al. Management of Immune-Related Adverse Events in Patients Treated With Immune Checkpoint Inhibitor Therapy: ASCO Guideline Update. Journal of Clinical Oncology. 2021.",
        "doi_or_url": "https://doi.org/10.1200/JCO.21.01440",
        "verified_status": "verified_online",
        "supports": "Oncology toxicity management; continue/hold/escalate treatment decisions based on toxicity severity.",
    },
    {
        "ref_num": 9,
        "citation_key": "Brahmer2018_ASCOirAE",
        "reference": "Brahmer JR, Lacchetti C, Schneider BJ, et al. Management of Immune-Related Adverse Events in Patients Treated With Immune Checkpoint Inhibitor Therapy: American Society of Clinical Oncology Clinical Practice Guideline. Journal of Clinical Oncology. 2018;36:1714-1768.",
        "doi_or_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6481621/",
        "verified_status": "verified_online",
        "supports": "Clinical action channels for immune-related adverse event management, including suspend/hold and resume decisions.",
    },
    {
        "ref_num": 10,
        "citation_key": "Geirhos2020_ShortcutLearning",
        "reference": "Geirhos R, Jacobsen JH, Michaelis C, et al. Shortcut learning in deep neural networks. Nature Machine Intelligence. 2020;2:665-673.",
        "doi_or_url": "https://doi.org/10.1038/s42256-020-00257-z",
        "verified_status": "verified_online",
        "supports": "Shortcut learning; benchmark performance can fail to transfer to harder or more realistic conditions.",
    },
])

verified_refs.to_csv(OUTDIR / "v0_83_verified_references.csv", index=False)

# ---------------------------------------------------------------------
# Citation insertion helpers
# ---------------------------------------------------------------------

def replace_once(text, old, new, audit_rows, section, citation_nums, rationale):
    if old not in text:
        audit_rows.append({
            "section": section,
            "status": "not_found",
            "citation_nums": citation_nums,
            "rationale": rationale,
            "target_text": old,
        })
        return text
    text = text.replace(old, new, 1)
    audit_rows.append({
        "section": section,
        "status": "inserted",
        "citation_nums": citation_nums,
        "rationale": rationale,
        "target_text": old,
    })
    return text

audit = []
m = manuscript

# ---------------------------------------------------------------------
# Insert citations into Introduction
# ---------------------------------------------------------------------

m = replace_once(
    m,
    "Large language models are increasingly evaluated for clinical reasoning, diagnostic support, and medical question answering.",
    "Large language models are increasingly evaluated for clinical reasoning, diagnostic support, and medical question answering, but recent clinical evaluations show that high apparent reasoning performance does not automatically translate into reliable clinical workflow benefit or autonomous decision readiness. [1,2]",
    audit,
    "Introduction",
    "1,2",
    "Anchor clinical LLM evaluation and limitation claims.",
)

m = replace_once(
    m,
    "Clinical pressure can further complicate action selection.",
    "Clinical pressure can further complicate action selection; for this reason, early clinical AI decision-support studies require transparent reporting of context, workflow, human factors, and deployment assumptions. [3,4,5]",
    audit,
    "Introduction",
    "3-5",
    "Connect naturalistic pressure framing to clinical AI reporting guidance.",
)

m = replace_once(
    m,
    "A key benchmark-design challenge is that realistic prompts can still leak the correct action channel.",
    "A key benchmark-design challenge is that realistic prompts can still leak the correct action channel, analogous to shortcut learning in which systems perform well on standard benchmarks by exploiting cues that fail under harder or more realistic conditions. [10]",
    audit,
    "Introduction",
    "10",
    "Support action-cue leakage and benchmark validity framing.",
)

# ---------------------------------------------------------------------
# Insert citations into Methods
# ---------------------------------------------------------------------

m = replace_once(
    m,
    "The benchmark was developed through an iterative design and audit process.",
    "The benchmark was developed through an iterative design and audit process, consistent with the need for transparent reporting of early-stage clinical AI decision-support evaluations and AI intervention protocols. [3,4,5]",
    audit,
    "Methods",
    "3-5",
    "Support benchmark construction and reporting transparency.",
)

m = replace_once(
    m,
    "The primary performance endpoint was action-channel authorization correctness rate (AACR), defined as the proportion of outputs in which the model-selected action matched the expected action.",
    "The primary performance endpoint was action-channel authorization correctness rate (AACR), defined as the proportion of outputs in which the model-selected action matched the expected action. The five action channels were chosen to reflect clinically meaningful oncology management distinctions, including continuation, evaluation, therapy hold, switch, and emergency toxicity management. [8,9]",
    audit,
    "Methods",
    "8,9",
    "Support clinical relevance of oncology therapeutic action channels.",
)

m = replace_once(
    m,
    "A deterministic evidence-contract controller was applied to each model’s scored outputs.",
    "A deterministic evidence-contract controller was applied to each model’s scored outputs. This controller framing aligns with broader AI risk-management and health-AI governance principles that emphasize identifying, measuring, and managing risks in AI systems rather than relying only on model-level performance. [6,7]",
    audit,
    "Methods",
    "6,7",
    "Support controller/risk-management framing.",
)

# ---------------------------------------------------------------------
# Insert citations into Discussion
# ---------------------------------------------------------------------

m = replace_once(
    m,
    "This study demonstrates that hard action-obscured oncology therapeutic-authorization prompts expose clinically meaningful action-channel instability across multiple frontier models.",
    "This study demonstrates that hard action-obscured oncology therapeutic-authorization prompts expose clinically meaningful action-channel instability across multiple frontier models. This extends prior clinical LLM evaluations by focusing not on general diagnostic reasoning alone, but on whether model outputs can be routed into the correct therapeutic action channel. [1,2]",
    audit,
    "Discussion",
    "1,2",
    "Place contribution relative to clinical LLM evaluation literature.",
)

m = replace_once(
    m,
    "This framing is important because not all unsafe clinical AI behavior appears as reckless continuation.",
    "This framing is important because not all unsafe clinical AI behavior appears as reckless continuation, and oncology toxicity guidance itself distinguishes monitoring, holding therapy, resuming therapy, switching therapy, and urgent management depending on clinical severity. [8,9]",
    audit,
    "Discussion",
    "8,9",
    "Support clinical relevance of multiple action channels.",
)

m = replace_once(
    m,
    "The pressure templates used in this benchmark were designed to reflect real workflow pressures rather than artificial jailbreaks.",
    "The pressure templates used in this benchmark were designed to reflect real workflow pressures rather than artificial jailbreaks. This emphasis is consistent with early clinical AI evaluation guidance, which highlights the importance of reporting clinical context and human-system interaction assumptions. [3]",
    audit,
    "Discussion",
    "3",
    "Support workflow/clinical evaluation framing.",
)

m = replace_once(
    m,
    "This supports a governance architecture in which clinical AI systems are evaluated as controlled decision systems, not merely as text generators.",
    "This supports a governance architecture in which clinical AI systems are evaluated as controlled decision systems, not merely as text generators. This framing is consistent with AI risk-management approaches that emphasize mapped risks, measurement, governance controls, and accountable system behavior. [6,7]",
    audit,
    "Discussion",
    "6,7",
    "Support governance architecture framing.",
)

m = replace_once(
    m,
    "This work also contributes a benchmark-design lesson.",
    "This work also contributes a benchmark-design lesson. Shortcut-learning literature shows that systems may perform well on standard benchmarks by using decision rules that fail under more challenging or realistic conditions, which parallels the action-cue leakage observed before hard-set repair. [10]",
    audit,
    "Discussion",
    "10",
    "Support benchmark validity and leakage contribution.",
)

m = replace_once(
    m,
    "This study has several limitations.",
    "This study has several limitations. The reporting and validation caveats are consistent with clinical AI reporting guidance, especially because this study is a synthetic benchmark and controller-mechanism evaluation rather than a deployed clinical trial. [3,4,5]",
    audit,
    "Limitations",
    "3-5",
    "Support reporting and validation caveats.",
)

# ---------------------------------------------------------------------
# Add references section
# ---------------------------------------------------------------------

refs_text = "\n\n## References\n\n"
for _, row in verified_refs.iterrows():
    refs_text += f"{int(row['ref_num'])}. {row['reference']} {row['doi_or_url']}\n"

# Remove existing references if any, then append
m = re.sub(r"\n## References\n.*$", "", m, flags=re.DOTALL)
m = m.rstrip() + refs_text

# ---------------------------------------------------------------------
# Write outputs
# ---------------------------------------------------------------------

(OUTDIR / "v0_83_citation_integrated_manuscript.md").write_text(m)

audit_df = pd.DataFrame(audit)
audit_df.to_csv(OUTDIR / "v0_83_citation_insertion_audit.csv", index=False)

unresolved = audit_df[audit_df["status"] != "inserted"].copy()
unresolved.to_csv(OUTDIR / "v0_83_unresolved_citation_insertions.csv", index=False)

# Count reference use
citation_use = []
for _, ref in verified_refs.iterrows():
    num = int(ref["ref_num"])
    pattern = rf"(?<!\d){num}(?!\d)"
    bracket_mentions = len(re.findall(rf"\[[^\]]*\b{num}\b[^\]]*\]", m))
    citation_use.append({
        "ref_num": num,
        "citation_key": ref["citation_key"],
        "bracket_citation_mentions": bracket_mentions,
        "used_in_manuscript": bracket_mentions > 0,
    })

citation_use_df = pd.DataFrame(citation_use)
citation_use_df.to_csv(OUTDIR / "v0_83_reference_usage_audit.csv", index=False)

# Create manuscript citation map
citation_map = pd.DataFrame([
    {
        "manuscript_section": "Introduction",
        "citation_nums": "1,2,3,4,5,10",
        "purpose": "Clinical LLM limitations; reporting guidance; benchmark shortcut/action-cue leakage.",
    },
    {
        "manuscript_section": "Methods",
        "citation_nums": "3,4,5,6,7,8,9",
        "purpose": "Clinical AI reporting; governance; oncology action-channel clinical rationale.",
    },
    {
        "manuscript_section": "Discussion",
        "citation_nums": "1,2,3,6,7,8,9,10",
        "purpose": "Positioning, governance interpretation, action-channel clinical relevance, benchmark validity.",
    },
    {
        "manuscript_section": "Limitations",
        "citation_nums": "3,4,5",
        "purpose": "Reporting and validation caveats.",
    },
])

citation_map.to_csv(OUTDIR / "v0_83_manuscript_citation_map.csv", index=False)

# Create card
card = f"""# OncoGuard-Response v0.83 — Citation-Integrated Manuscript Draft

## Purpose

v0.83 integrates verified references into the polished v0.81 manuscript.

## Source artifacts

- Manuscript source: `results/v0_81_polished_manuscript_v1/v0_81_polished_manuscript_v1.md`
- Citation plan source: `results/v0_82_reference_citation_integration_plan`

## Included artifacts

- `v0_83_citation_integrated_manuscript.md`
- `v0_83_verified_references.csv`
- `v0_83_citation_insertion_audit.csv`
- `v0_83_unresolved_citation_insertions.csv`
- `v0_83_reference_usage_audit.csv`
- `v0_83_manuscript_citation_map.csv`

## Verified reference domains

1. Clinical LLM evaluation and limitations.
2. Clinical AI reporting guidelines.
3. AI risk management and health AI governance.
4. Oncology toxicity/action-channel management.
5. Shortcut learning and benchmark validity.

## Important note

This draft uses numbered bracket citations. Final formatting should be adjusted to the target journal style.
"""

(OUTDIR / "onco_guard_response_v0_83_citation_integrated_card.md").write_text(card)

print("Saved v0.83 citation-integrated manuscript package to:", OUTDIR)

print("\nFiles:")
for p in sorted(OUTDIR.glob("*")):
    print(p.name)

print("\nVerified references:")
print(verified_refs[["ref_num", "citation_key", "reference"]].to_string(index=False))

print("\nCitation insertion audit:")
print(audit_df.to_string(index=False))

print("\nReference usage:")
print(citation_use_df.to_string(index=False))

if len(unresolved):
    print("\nWARNING: unresolved citation insertions:")
    print(unresolved.to_string(index=False))
else:
    print("\nAll citation insertions resolved.")
