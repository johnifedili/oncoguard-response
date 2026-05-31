# OncoGuard-Response v0.82 — Reference/Citation Integration Plan

## Purpose

v0.82 defines the citation architecture for the polished v0.81 manuscript.

The goal is to add a scholarly backbone without diluting the paper’s central contribution:

1. Hard action-obscured oncology prompts expose action-channel instability.
2. Failure phenotype differs across GPT-4.1, Claude Sonnet 4.6, and Gemini Flash.
3. A deterministic evidence-contract controller restores evidence-consistent authorization across all three.
4. Action-cue leakage can inflate benchmark performance.
5. Clinical AI should be evaluated as a controlled decision system, not only as a text generator.

## Citation domains

| domain_id   | domain                                                    | why_needed                                                                                                     | where_to_cite                                                               | example_source_types                                                                                                           | priority    |
|:------------|:----------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|:------------|
| D01         | Clinical LLM evaluation and limitations                   | Supports the claim that clinical LLMs require rigorous evaluation beyond plausible reasoning.                  | Introduction paragraphs 1–2; Discussion principal findings.                 | JAMA Network Open clinical reasoning trials; Nature Medicine LLM limitation studies; systematic reviews of LLMs in healthcare. | high        |
| D02         | Clinical AI reporting guidelines                          | Supports transparency, protocol reporting, and reviewer-facing reproducibility.                                | Methods; Limitations; Reporting statement.                                  | DECIDE-AI; CONSORT-AI; SPIRIT-AI; TRIPOD-AI if prediction framing is used.                                                     | high        |
| D03         | AI governance and risk management                         | Supports the governance framing that clinical AI should be treated as a controlled decision system.            | Introduction governance paragraph; Discussion evidence-contract control.    | NIST AI RMF; FDA AI/ML SaMD guidance; WHO health AI ethics/governance guidance.                                                | high        |
| D04         | Clinical decision support and medication/therapy safety   | Positions therapeutic authorization as a safety-critical clinical decision-support problem.                    | Introduction oncology therapeutic authorization; Methods benchmark design.  | CDSS safety literature; oncology decision support papers; medication safety AI/CDSS studies.                                   | high        |
| D05         | Human factors, pressure, and workflow safety              | Supports the claim that urgency, authority, social pressure, and workflow pressure can degrade action routing. | Introduction naturalistic pressure; Discussion action-channel interference. | Human factors in medication safety; diagnostic error literature; authority gradient and interruption literature.               | medium-high |
| D06         | Benchmark validity, leakage, and shortcut learning        | Supports the action-cue leakage contribution and the need for hard action-obscured prompts.                    | Introduction action-cue leakage; Discussion benchmark validity.             | Dataset leakage; shortcut learning; benchmark contamination; adversarial evaluation literature.                                | high        |
| D07         | Guardrails, controllers, and constrained decision systems | Supports the external controller architecture and separation of model reasoning from authorization.            | Methods controller; Discussion evidence-contract control.                   | AI guardrails; neuro-symbolic systems; constrained decoding; safety controllers; clinical CDS rule systems.                    | high        |
| D08         | Oncology treatment response and toxicity management       | Supports clinical plausibility of action channels: continue, evaluate, hold, switch, emergency management.     | Methods benchmark design; Supplementary clinical rationale.                 | ASCO/ESMO/NCCN toxicity management guidelines; immune-related adverse event management; RECIST/progression literature.         | medium-high |

## Seed reference list

| ref_id   | topic                                 | candidate_reference                                                                                                                                               | supports                                                                                                            | use_in_manuscript                                                                   | status                         |
|:---------|:--------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:-------------------------------|
| R01      | Clinical LLM diagnostic reasoning     | Goh et al. Large Language Model Influence on Diagnostic Reasoning. JAMA Network Open. 2024.                                                                       | LLM availability did not significantly improve physician diagnostic reasoning compared with conventional resources. | Introduction and Discussion: LLM reasoning tools need workflow-specific evaluation. | seed_reference_verify_metadata |
| R02      | LLM limitations in clinical diagnosis | Hager et al. Evaluation and mitigation of the limitations of large language models in clinical decision-making. Nature Medicine. 2024.                            | Current models can underperform trained clinicians and need rigorous limitation analysis.                           | Introduction: clinical reasoning ability does not equal safe decision support.      | seed_reference_verify_metadata |
| R03      | Clinical AI reporting guideline       | Vasey et al. DECIDE-AI reporting guideline for early-stage clinical evaluation of AI decision support systems. Nature Medicine/BMJ-linked guideline family. 2022. | Transparent reporting of early-stage clinical AI decision-support studies.                                          | Methods and Supplement: reporting transparency and reproducibility.                 | seed_reference_verify_metadata |
| R04      | AI risk management                    | NIST Artificial Intelligence Risk Management Framework (AI RMF 1.0). 2023.                                                                                        | Risk management framing for trustworthy AI systems.                                                                 | Discussion: governance framing and controlled decision systems.                     | seed_reference_verify_metadata |
| R05      | Health AI governance                  | WHO guidance on ethics and governance of artificial intelligence for health.                                                                                      | High-level health AI governance and safety principles.                                                              | Discussion and limitations.                                                         | needs_web_verification         |
| R06      | CONSORT-AI / SPIRIT-AI                | CONSORT-AI and SPIRIT-AI reporting extensions.                                                                                                                    | Clinical trial/reporting standards for AI interventions.                                                            | Methods caveat: study is preclinical/synthetic, not clinical trial.                 | needs_web_verification         |
| R07      | Human factors / clinical pressure     | Authority gradient, interruption, workload, and medication safety human-factors literature.                                                                       | Clinical pressure can disrupt correct safety-channel execution.                                                     | Discussion: naturalistic pressure as action-channel interference.                   | needs_literature_search        |
| R08      | Benchmark leakage / shortcut learning | Shortcut learning and benchmark leakage literature in machine learning evaluation.                                                                                | Action-cue leakage can inflate benchmark performance.                                                               | Discussion: benchmark validity contribution.                                        | needs_literature_search        |
| R09      | AI guardrails / controllers           | Guardrails, constrained decision systems, and external safety-controller literature.                                                                              | Separation of model reasoning from action authorization.                                                            | Discussion: evidence-contract control as governance architecture.                   | needs_literature_search        |
| R10      | Oncology toxicity/response management | ASCO/ESMO/NCCN immune-related adverse event and oncology response-management guidance.                                                                            | Clinical action channels: hold, switch, evaluate, emergency management.                                             | Methods benchmark rationale and Supplement.                                         | needs_guideline_selection      |

## Section citation map

| section                              | citation_need                                                                                     | recommended_refs                         | priority    |
|:-------------------------------------|:--------------------------------------------------------------------------------------------------|:-----------------------------------------|:------------|
| Abstract                             | Usually no citations unless journal permits; keep evidence internal to study.                     |                                          | low         |
| Introduction paragraph 1             | Clinical LLMs increasingly evaluated for clinical reasoning and decision support.                 | R01; R02; systematic reviews             | high        |
| Introduction paragraph 2             | Oncology therapeutic management requires distinct action channels and safety-sensitive decisions. | R10; oncology toxicity/response guidance | high        |
| Introduction paragraph 3             | Clinical pressure, interruptions, and authority/workflow pressure can affect safety behavior.     | R07                                      | medium-high |
| Introduction paragraph 4             | Benchmark cue leakage and shortcut learning can inflate model performance.                        | R08                                      | high        |
| Methods benchmark design             | Reporting guidance and benchmark transparency.                                                    | R03; R06                                 | high        |
| Methods endpoints                    | Endpoint definitions mostly internal; cite reporting/clinical safety where needed.                | R03; R10                                 | medium      |
| Methods controller                   | Guardrail/controller/constrained decision system framing.                                         | R04; R09                                 | high        |
| Discussion principal findings        | Compare with prior LLM clinical reasoning limitations.                                            | R01; R02                                 | high        |
| Discussion naturalistic pressure     | Support pressure as workflow/human-factors risk.                                                  | R07                                      | medium-high |
| Discussion evidence-contract control | AI governance, risk management, controller/guardrail framing.                                     | R04; R05; R09                            | high        |
| Discussion benchmark validity        | Support action-cue leakage as benchmark validity issue.                                           | R08                                      | high        |
| Limitations                          | Synthetic benchmark, reporting limitations, external validation requirements.                     | R03; R06                                 | medium-high |

## Citation integration todo

|   task_order | task                                                          | output                                                                                             |
|-------------:|:--------------------------------------------------------------|:---------------------------------------------------------------------------------------------------|
|            1 | Verify metadata for seed references R01-R06                   | Confirmed citation strings with DOI/PMID/URL where available.                                      |
|            2 | Search human-factors/clinical pressure literature for R07     | 3–5 references on authority gradient, interruption, workload, and medication/clinical safety.      |
|            3 | Search benchmark leakage/shortcut learning literature for R08 | 3–5 ML benchmark validity references.                                                              |
|            4 | Search guardrail/controller literature for R09                | 3–5 references on external controllers, constrained decision systems, guardrails.                  |
|            5 | Select oncology guideline citations for R10                   | ASCO/ESMO/NCCN or equivalent guideline sources for therapy hold/switch/emergency toxicity actions. |
|            6 | Insert citations into v0.81 manuscript                        | v0.83 cited manuscript draft.                                                                      |
|            7 | Generate reference list in target journal style               | v0.83 reference list and citation-integrated manuscript.                                           |

## Literature search query plan

| query_group              | query                                                                                                 | target                                        |
|:-------------------------|:------------------------------------------------------------------------------------------------------|:----------------------------------------------|
| clinical_llm_evaluation  | large language models clinical reasoning diagnostic reasoning evaluation JAMA Network Open 2024       | Clinical LLM evaluation studies.              |
| clinical_llm_limitations | large language models clinical decision making limitations Nature Medicine 2024 Hager                 | Nature Medicine LLM limitation study.         |
| reporting_guidelines     | DECIDE-AI CONSORT-AI SPIRIT-AI reporting guidelines artificial intelligence clinical decision support | Clinical AI reporting standards.              |
| governance               | NIST AI Risk Management Framework healthcare AI governance WHO ethics governance AI health            | AI governance frameworks.                     |
| human_factors_pressure   | clinical pressure authority gradient interruption workload medication safety human factors            | Human factors / clinical pressure literature. |
| benchmark_leakage        | benchmark leakage shortcut learning machine learning evaluation dataset artifacts                     | Benchmark validity literature.                |
| guardrails_controllers   | AI guardrails external controller constrained decision system safety critical AI                      | Controller/guardrail literature.              |
| oncology_guidelines      | ASCO guideline immune-related adverse events hold therapy emergency toxicity management oncology      | Oncology therapeutic action guidance.         |

## Notes for v0.83

v0.83 should become the citation-integrated manuscript draft. It should not over-cite the empirical result sections, because the empirical results are original. Citations should primarily support:

- why clinical LLM evaluation needs more than reasoning accuracy;
- why reporting/provenance matters;
- why governance/controller framing is appropriate;
- why action-cue leakage is a benchmark validity problem;
- why oncology therapeutic action channels are clinically meaningful.

## Citation placement rule

Avoid citation stacking at the end of paragraphs. Use citations to support claims, not to decorate every sentence. The Results section should cite internal tables/figures, while the Introduction and Discussion should carry most external citations.
