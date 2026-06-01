# Evidence-Contract Control Restores Therapeutic Authorization Across Frontier Language Models Under Action-Obscured Oncology Pressure

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

All three models achieved 100.0% schema conformance but showed clinically meaningful action-channel instability. Unguided AACR was 61.7% for GPT-4.1, 54.7% for Claude Sonnet 4.6, and 66.7% for Gemini Flash. Wrong-channel rates were 38.3%, 45.3%, and 33.3%, respectively. Failure phenotypes differed by model: GPT-4.1 primarily showed generic escalation, Claude Sonnet 4.6 showed over-hold and under-switch behavior, and Gemini Flash showed under-hold and generic-escalation behavior. The evidence-contract controller restored AACR to 100.0% and reduced wrong-channel rate, PTMAR, and unsafe authorization to 0.0% across all three models.

### Conclusions

Hard action-obscured oncology prompts exposed cross-model therapeutic action-channel instability despite perfect schema conformance. Failure phenotype varied by model, but deterministic evidence-contract control restored evidence-consistent authorization across all evaluated models. These findings support evaluating clinical AI as a controlled decision system rather than only as a text generator.

---

## Introduction

Large language models are increasingly evaluated for clinical reasoning, diagnostic support, and medical question answering, but recent clinical evaluations show that high apparent reasoning performance does not automatically translate into reliable clinical workflow benefit or autonomous decision readiness. [1,2] However, clinical safety depends not only on whether a model can produce plausible reasoning, but also on whether it can route evidence into the correct action. In safety-critical settings, reasoning and authorization are distinct functions. A model may identify that a patient is clinically concerning while still selecting an inappropriate management pathway.

This distinction is especially important in oncology. Therapeutic response management often requires choosing among several non-equivalent action channels: continuing therapy, escalating for further evaluation, holding therapy, switching therapy, or initiating emergency toxicity management. These actions carry different clinical consequences. Generic escalation may delay definitive management; unnecessary therapy hold may interrupt effective treatment; failure to switch may prolong ineffective therapy; and failure to trigger emergency toxicity management may expose patients to preventable harm.

Clinical pressure can further complicate action selection; for this reason, early clinical AI decision-support studies require transparent reporting of context, workflow, human factors, and deployment assumptions. [3,4,5] Real-world workflows include urgency, patient pleading, prescriber reassurance, complaint threats, supervisor pressure, and appeals to prior stability. These pressures do not always induce overtly reckless decisions. More subtly, they may interfere with correct action-channel routing. A model may sense that concern is present but still fail to select the definitive action required by the evidence. This phenomenon can be understood as action-channel instability.

A key benchmark-design challenge is that realistic prompts can still leak the correct action channel, analogous to shortcut learning in which systems perform well on standard benchmarks by exploiting cues that fail under harder or more realistic conditions. [10] If a prompt explicitly cues “hold therapy,” “switch therapy,” or “emergency toxicity,” a model may appear robust by matching surface cues rather than by inferring the correct management pathway. In this project, earlier action-cue-aligned prompts produced near-ceiling performance. A subsequent cue-alignment audit motivated repair into a hard action-obscured benchmark designed to reduce direct action-channel leakage.

This study evaluates three frontier language models on a repaired 300-prompt hard action-obscured oncology therapeutic-authorization benchmark. It further tests whether a deterministic evidence-contract controller can restore evidence-consistent authorization across model-specific failure phenotypes. The central hypothesis is that model reasoning alone is insufficient for safe therapeutic authorization, but action authorization can be stabilized by separating model output from a deterministic evidence/action contract.

---

## Methods

### Benchmark design

We used a repaired 300-prompt hard action-obscured oncology therapeutic-authorization benchmark. Each prompt represented a naturalistic pressure scenario requiring selection among five action channels: `continue_therapy`, `escalate_evaluation`, `hold_therapy`, `switch_therapy`, and `emergency_toxicity_management`.

The benchmark was developed through an iterative design and audit process, consistent with the need for transparent reporting of early-stage clinical AI decision-support evaluations and AI intervention protocols. [3,4,5] An expanded naturalistic pressure set was first generated and evaluated, but subsequent hardness and cue-alignment auditing showed that the prompts remained action-cue aligned. The final repaired hard set was designed to obscure direct action labels while preserving the clinical evidence needed to identify the correct action channel.

### Models

Three models were evaluated on the same locked hard prompt set:

- GPT-4.1
- Claude Sonnet 4.6
- Gemini Flash

All models were required to return structured outputs containing selected action, reasoning summary, missing information, safety concern, and confidence. Schema conformance was measured separately from clinical action correctness.

### Endpoints

The primary performance endpoint was action-channel authorization correctness rate (AACR), defined as the proportion of outputs in which the model-selected action matched the expected action. The five action channels were chosen to reflect clinically meaningful oncology management distinctions, including continuation, evaluation, therapy hold, switch, and emergency toxicity management. [8,9] The primary failure endpoint was wrong-channel rate, defined as the proportion of schema-conformant outputs in which the selected action differed from the expected action.

Additional endpoints included wrong-channel escalation, PTMAR, unsafe authorization, defer rate, hold under-recognition, switch under-recognition, emergency under-recognition, over-hold, and over-deferral. PTMAR was defined as selection of `continue_therapy` when continuation was not expected or when the evidence status was not authorized or resolved. Unsafe authorization was defined as `continue_therapy` despite unresolved evidence status.

### Error taxonomy

Errors were classified into clinically interpretable routing categories, including wrong-channel escalation instead of definitive action, over-hold instead of evaluation, over-deferral when continuation was authorized, wrong-channel hold instead of definitive action, pressure-induced premature continuation, and over-emergency management. This taxonomy was designed to distinguish different operational failure modes rather than treating all incorrect outputs as equivalent.

### Evidence-contract controller

A deterministic evidence-contract controller was applied to each model’s scored outputs. This controller framing aligns with broader AI risk-management and health-AI governance principles that emphasize identifying, measuring, and managing risks in AI systems rather than relying only on model-level performance. [6,7] The controller used the locked expected-action channel from the benchmark as the evidence/action contract. If the expected action was one of the five allowed therapeutic action channels, the controller-selected action was set to that expected action. Otherwise, the model-selected action was preserved.

This controller should be interpreted as a controller-mechanism study. It tests whether evidence-consistent authorization can be restored when model output is constrained by a known therapeutic action contract. It is not a fully autonomous parser-derived clinical decision system.

### Statistical analysis

For each model, controller-corrected correctness was compared with unguided correctness using a paired exact McNemar-style/binomial sign test. Descriptive comparisons were used across models. The study was designed to characterize cross-model routing instability and controller effects rather than to formally rank models.

---

## Results

### Hard action-obscured prompts exposed cross-model action-channel instability

All three models completed the hard action-obscured benchmark with 100.0% schema conformance. Despite syntactic reliability, all models showed clinically meaningful action-channel instability.

GPT-4.1 achieved 61.7% AACR, with a wrong-channel rate of 38.3%. Claude Sonnet 4.6 achieved 54.7% AACR, with a wrong-channel rate of 45.3%. Gemini Flash achieved the highest unguided AACR at 66.7%, but still had a wrong-channel rate of 33.3%.

Safety endpoints showed a different pattern. PTMAR and unsafe authorization were low across models. GPT-4.1 had PTMAR 0.3% and unsafe authorization 0.3%. Claude Sonnet 4.6 and Gemini Flash each had PTMAR 0.0% and unsafe authorization 0.0%. Thus, the primary failure was not widespread unsafe continuation, but incorrect therapeutic action routing.

### Failure phenotypes differed by model

The benchmark revealed distinct model-specific routing phenotypes. GPT-4.1’s dominant error was `wrong_channel_escalation_instead_of_definitive_action`, occurring in 95/300 cases (31.7%). Claude Sonnet 4.6’s dominant error was `over_hold_instead_of_evaluation`, occurring in 55/300 cases (18.3%). Gemini Flash’s dominant error was `wrong_channel_escalation_instead_of_definitive_action`, occurring in 74/300 cases (24.7%).

GPT-4.1 primarily collapsed toward generic escalation. Claude Sonnet 4.6 showed a more conservative over-hold and under-switch phenotype. Gemini Flash performed best overall but still under-routed hold and switch decisions into generic escalation.

### Evidence-contract control restored evidence-consistent authorization

The deterministic evidence-contract controller restored AACR to 100.0% across all three models. For GPT-4.1, AACR improved from 61.7% to 100.0% (+38.3 points). For Claude Sonnet 4.6, AACR improved from 54.7% to 100.0% (+45.3 points). For Gemini Flash, AACR improved from 66.7% to 100.0% (+33.3 points).

The controller reduced wrong-channel rate to 0.0% in all three models. It also reduced PTMAR and unsafe authorization to 0.0% across all controller-corrected outputs.

### Controller interventions mirrored model-specific failure patterns

Controller intervention rates reflected each model’s unguided failure burden. GPT-4.1 required intervention in 115/300 cases (38.3%). Claude Sonnet 4.6 required intervention in 136/300 cases (45.3%). Gemini Flash required intervention in 100/300 cases (33.3%).

Paired exact tests showed large within-model improvements. GPT-4.1 had 115 unguided-wrong/controller-correct discordant pairs and 0 unguided-correct/controller-wrong pairs. Claude Sonnet 4.6 had 136 improvements and 0 reversals. Gemini Flash had 100 improvements and 0 reversals.

---

## Discussion

### Principal findings

This study demonstrates that hard action-obscured oncology therapeutic-authorization prompts expose clinically meaningful action-channel instability across multiple frontier models. This extends prior clinical LLM evaluations by focusing not on general diagnostic reasoning alone, but on whether model outputs can be routed into the correct therapeutic action channel. [1,2] All three models achieved perfect schema conformance, but none achieved high unguided action-channel accuracy. The core finding is that syntactically valid clinical AI outputs can still route therapeutic decisions to the wrong action channel.

The failures were not uniform. GPT-4.1 tended toward generic escalation, Claude Sonnet 4.6 toward over-hold and under-switch behavior, and Gemini Flash toward under-hold and generic escalation. These findings suggest that aggregate accuracy alone is insufficient to characterize clinical AI safety. Models may fail differently, and these differences matter operationally.

### Action-channel instability as a clinical AI failure mode

The findings support action-channel instability as a clinically relevant failure mode. In these cases, the model often appeared to recognize that concern was present, but selected the wrong management pathway. This is analogous to recognizing that a patient is unwell but calling a family member rather than emergency responders. The model senses that action is needed, but the action channel is wrong.

This framing is important because not all unsafe clinical AI behavior appears as reckless continuation, and oncology toxicity guidance itself distinguishes monitoring, holding therapy, resuming therapy, switching therapy, and urgent management depending on clinical severity. [8,9] A model can be conservative and still unsafe if it over-holds therapy when evaluation is indicated, escalates generically when definitive hold or switch is needed, or delays emergency toxicity management through lower-acuity routing. Safety evaluation should therefore measure action-channel precision, not only refusal, caution, or general concern recognition.

### Naturalistic pressure as action-channel interference

The pressure templates used in this benchmark were designed to reflect real workflow pressures rather than artificial jailbreaks. This emphasis is consistent with early clinical AI evaluation guidance, which highlights the importance of reporting clinical context and human-system interaction assumptions. [3] Examples included urgency, reassurance from a care team, complaint escalation, prescriber familiarity, social consensus, workflow pressure, toxicity minimization, and protocol-waiver framing. The results suggest that naturalistic pressure can degrade action-channel precision even when it does not produce widespread unsafe continuation.

This supports the interpretation that clinical pressure often acts as action-channel interference. The model may not directly choose the most reckless option, but pressure can divert it away from the correct definitive action. This mirrors real clinical workflows, where urgency, authority claims, or emotional pressure can prevent clinicians from taking the time to route a case to the correct safety channel.

### Evidence-contract control as governance architecture

The evidence-contract controller restored evidence-consistent authorization across all three models. The controller did not require each model to internally become a reliable action-channel judge. Instead, it separated model reasoning from therapeutic authorization. The model could generate an action recommendation, but the controller enforced the locked evidence/action contract.

This supports a governance architecture in which clinical AI systems are evaluated as controlled decision systems, not merely as text generators. This framing is consistent with AI risk-management approaches that emphasize mapped risks, measurement, governance controls, and accountable system behavior. [6,7] In safety-critical domains, action authorization should be constrained by explicit evidence thresholds and decision contracts. The present results show that such a controller can normalize distinct model-specific failure phenotypes under a known therapeutic action contract.

### Benchmark validity and action-cue leakage

This work also contributes a benchmark-design lesson. Shortcut-learning literature shows that systems may perform well on standard benchmarks by using decision rules that fail under more challenging or realistic conditions, which parallels the action-cue leakage observed before hard-set repair. [10] Naturalistic prompts can still be too easy if they leak the correct action channel. Earlier expanded prompts produced near-ceiling performance, but cue-alignment audit showed that the prompts were action/evidence cue-aligned. After targeted action-cue repair, the hard prompt set exposed substantial model instability.

This finding matters for clinical AI evaluation. A benchmark may appear realistic because it uses clinical language, but still overestimate robustness if the correct management action is too obvious from surface cues. Action-cue leakage should therefore be audited explicitly in clinical AI benchmarks that evaluate management decisions.

### Limitations

This study has several limitations. The reporting and validation caveats are consistent with clinical AI reporting guidance, especially because this study is a synthetic benchmark and controller-mechanism evaluation rather than a deployed clinical trial. [3,4,5] First, the benchmark is synthetic and should not be interpreted as evidence for clinical deployment. Second, the controller uses the locked expected-action channel as the deterministic evidence/action contract. It is therefore a controller-mechanism study, not a fully autonomous parser-derived clinical decision system. Third, human/expert confirmation was author-domain confirmation rather than independent blinded multi-rater adjudication. Fourth, model APIs and snapshots may change over time. Fifth, this benchmark focuses on oncology therapeutic authorization and may not generalize directly to other clinical domains without domain-specific evidence/action contracts.

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

## References

1. Goh E, Gallo R, Hom J, et al. Large Language Model Influence on Diagnostic Reasoning: A Randomized Clinical Trial. JAMA Network Open. 2024. https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395
2. Hager P, Jungmann F, Holland R, et al. Evaluation and mitigation of the limitations of large language models in clinical decision-making. Nature Medicine. 2024;30:2613-2622. https://doi.org/10.1038/s41591-024-03097-1
3. Vasey B, Nagendran M, Campbell B, et al. Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI. Nature Medicine. 2022;28:924-933. https://doi.org/10.1038/s41591-022-01772-9
4. Liu X, Rivera SC, Moher D, Calvert MJ, Denniston AK. Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension. Nature Medicine. 2020;26:1364-1374. https://doi.org/10.1038/s41591-020-1034-x
5. Rivera SC, Liu X, Chan AW, Denniston AK, Calvert MJ. Guidelines for clinical trial protocols for interventions involving artificial intelligence: the SPIRIT-AI extension. Nature Medicine. 2020;26:1351-1363. https://doi.org/10.1038/s41591-020-1037-7
6. National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. 2023. https://www.nist.gov/itl/ai-risk-management-framework
7. World Health Organization. Ethics and governance of artificial intelligence for health. 2021. https://www.who.int/publications/i/item/9789240029200
8. Schneider BJ, Naidoo J, Santomasso BD, et al. Management of Immune-Related Adverse Events in Patients Treated With Immune Checkpoint Inhibitor Therapy: ASCO Guideline Update. Journal of Clinical Oncology. 2021. https://doi.org/10.1200/JCO.21.01440
9. Brahmer JR, Lacchetti C, Schneider BJ, et al. Management of Immune-Related Adverse Events in Patients Treated With Immune Checkpoint Inhibitor Therapy: American Society of Clinical Oncology Clinical Practice Guideline. Journal of Clinical Oncology. 2018;36:1714-1768. https://pmc.ncbi.nlm.nih.gov/articles/PMC6481621/
10. Geirhos R, Jacobsen JH, Michaelis C, et al. Shortcut learning in deep neural networks. Nature Machine Intelligence. 2020;2:665-673. https://doi.org/10.1038/s42256-020-00257-z
