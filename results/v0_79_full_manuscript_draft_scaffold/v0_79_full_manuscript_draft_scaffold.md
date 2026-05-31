# Full Manuscript Draft Scaffold — v0.79

## Working Title

**Evidence-Contract Control Restores Therapeutic Authorization Across Frontier Language Models Under Action-Obscured Oncology Pressure**

## Short Title

Evidence-Contract Control for Oncology AI

## Author

Chijioke John Ifedili

## Abstract

# Abstract Scaffold

## Background

Language models are increasingly evaluated for clinical reasoning, but less is known about whether they can reliably route evidence into the correct therapeutic-management action under realistic clinical pressure. In oncology, therapeutic authorization requires distinguishing continuation, escalation for evaluation, therapy hold, therapy switch, and emergency toxicity management. Errors in action-channel routing may create delay, unnecessary interruption, or unsafe continuation even when the model recognizes clinical concern.

## Objective

To evaluate action-channel stability in frontier language models using a hard action-obscured oncology therapeutic-authorization benchmark, and to test whether a deterministic evidence-contract controller can restore evidence-consistent authorization.

## Methods

We evaluated GPT-4.1, Claude Sonnet 4.6, and Gemini Flash on a repaired 300-prompt hard action-obscured benchmark derived from oncology therapeutic-response authorization scenarios. Each prompt required selection among five action channels: continue therapy, escalate evaluation, hold therapy, switch therapy, or emergency toxicity management. Primary endpoints included action-channel authorization correctness rate (AACR), wrong-channel rate, wrong-channel escalation, premature therapy misuse/action rate (PTMAR), and unsafe authorization. A deterministic evidence-contract controller was then applied to each model’s scored outputs using the locked expected-action channel as the evidence/action contract.

## Results

All three models achieved 100.0% schema conformance but showed clinically meaningful action-channel instability. Unguided AACR was 61.7% for GPT-4.1, 54.7% for Claude Sonnet 4.6, and 66.7% for Gemini Flash. Wrong-channel rates were 38.3%, 45.3%, and 33.3%, respectively. Failure phenotypes differed by model: GPT-4.1 primarily showed generic escalation, Claude showed over-hold/under-switch behavior, and Gemini Flash showed under-hold/generic escalation. The evidence-contract controller restored AACR to 100.0% and reduced wrong-channel rate, PTMAR, and unsafe authorization to 0.0% across all three models.

## Conclusions

Hard action-obscured oncology prompts expose cross-model therapeutic action-channel instability despite perfect schema conformance. Failure phenotype varies by model, but deterministic evidence-contract control restored evidence-consistent authorization across all evaluated models. These findings support evaluating clinical AI as a controlled decision system rather than only as a text generator.


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

# v0.78 Manuscript Results Skeleton

## Results

### Hard action-obscured benchmark exposes cross-model action-channel instability

All three evaluated models completed the repaired hard action-obscured oncology therapeutic-authorization benchmark with 100.0% schema conformance. Despite syntactic reliability, all three models showed clinically meaningful action-channel instability.

GPT-4.1 achieved 61.7% action-channel authorization correctness rate (AACR), with a wrong-channel rate of 38.3%. Claude Sonnet 4.6 achieved 54.7% AACR, with a wrong-channel rate of 45.3%. Gemini Flash achieved the highest unguided AACR at 66.7%, but still had a wrong-channel rate of 33.3% (Table 1; Figures 1–2).

Across models, premature therapy misuse/action rate (PTMAR) and unsafe authorization remained low. GPT-4.1 had PTMAR 0.3% and unsafe authorization 0.3%; Claude Sonnet 4.6 had PTMAR 0.0% and unsafe authorization 0.0%; Gemini Flash had PTMAR 0.0% and unsafe authorization 0.0%. Thus, the dominant failure mode was not widespread unsafe continuation, but incorrect action-channel routing under pressure.

### Models showed distinct therapeutic routing phenotypes

The hard benchmark revealed model-specific failure phenotypes rather than a single universal error pattern. GPT-4.1’s dominant error was wrong_channel_escalation_instead_of_definitive_action, occurring in 95/300 cases (31.7%). Claude Sonnet 4.6’s dominant error was over_hold_instead_of_evaluation, occurring in 55/300 cases (18.3%). Gemini Flash’s dominant error was wrong_channel_escalation_instead_of_definitive_action, occurring in 74/300 cases (24.7%) (Table 3; Figure 4).

These patterns suggest that the hard action-obscured benchmark identifies both cross-model vulnerability and model-specific routing signatures. GPT-4.1 primarily collapsed toward generic escalation. Claude Sonnet 4.6 showed a more conservative over-hold and under-switch phenotype. Gemini Flash performed best overall but still under-routed definitive hold and switch decisions into generic escalation.

### Evidence-contract controller restored evidence-consistent authorization across all models

The deterministic evidence-contract controller restored AACR to 100.0% across all three models (Table 2; Figure 3). For GPT-4.1, AACR improved from 61.7% to 100.0% (+38.3 points). For Claude Sonnet 4.6, AACR improved from 54.7% to 100.0% (+45.3 points). For Gemini Flash, AACR improved from 66.7% to 100.0% (+33.3 points).

The controller reduced wrong-channel rate to 0.0% in all three models. It also reduced PTMAR and unsafe authorization to 0.0% across all controller-corrected outputs. This indicates that the evidence-contract controller did not merely reduce one model’s dominant error type; it normalized distinct model-specific routing phenotypes under the same locked action contract.

### Controller intervention patterns mirrored model-specific failure phenotypes

Controller intervention rates differed by model and reflected each model’s unguided failure pattern. GPT-4.1 required intervention in 115/300 cases (38.3%). Claude Sonnet 4.6 required intervention in 136/300 cases (45.3%). Gemini Flash required intervention in 100/300 cases (33.3%) (Table 4; Figure 5).

Paired exact tests supported large within-model correctness improvements after controller application. GPT-4.1 had 115 unguided-wrong/controller-correct discordant pairs and 0 unguided-correct/controller-wrong pairs. Claude Sonnet 4.6 had 136 such improvements and 0 reversals. Gemini Flash had 100 such improvements and 0 reversals (Table 5).

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


---

# 4. Discussion

# v0.78 Manuscript Discussion Skeleton

## Discussion

### Principal findings

This study shows that hard action-obscured oncology therapeutic-authorization prompts expose clinically meaningful action-channel instability across multiple frontier models. All three evaluated models achieved perfect schema conformance, yet none achieved high unguided action-channel calibration. GPT-4.1 achieved 61.7% AACR, Claude Sonnet 4.6 achieved 54.7% AACR, and Gemini Flash achieved 66.7% AACR.

The key finding is not simply that models made errors. Rather, the benchmark revealed that under naturalistic pressure and action-obscured evidence, models often recognized clinical concern but routed the case to the wrong therapeutic-management channel. This supports the concept of action-channel instability: the model may identify that something is wrong while still failing to authorize the correct operational action.

### Model-specific failure phenotypes

The results demonstrate that action-channel instability is cross-model, but not uniform. GPT-4.1 primarily failed through generic escalation, suggesting a tendency to route definitive treatment-management decisions into noncommittal evaluation pathways. Claude Sonnet 4.6 showed a different phenotype, dominated by over-hold and under-switch behavior. Gemini Flash performed best overall but still under-routed hold and switch decisions into escalation.

This model-specific pattern is important for AI governance. It suggests that model safety cannot be inferred from a single aggregate accuracy metric. Two models can have similar wrong-channel rates while producing clinically different operational burdens. Generic escalation may delay definitive management; over-holding may interrupt therapy unnecessarily; under-switch behavior may delay transition away from ineffective or unsafe therapy. Governance benchmarks should therefore measure not only whether models are wrong, but how they are wrong.

### Naturalistic pressure as action-channel interference

The findings support the framing that clinical pressure does not always cause models to make overtly reckless decisions. Instead, pressure may interfere with routing to the correct action channel. In this benchmark, errors were dominated by wrong-channel routing rather than rampant unsafe continuation. This mirrors real clinical workflow risk: urgency, reassurance, complaint threats, prescriber familiarity, social consensus, and workflow pressure may not always cause a clinician or model to directly choose the most unsafe option, but they can divert attention away from the correct safety channel.

This provides a stronger and more realistic governance thesis than a simple adversarial-safety frame. The benchmark captures how pressure can create action-channel interference: the model senses concern but does not execute the correct therapeutic authorization pathway.

### Evidence-contract control as a governance mechanism

The deterministic evidence-contract controller restored evidence-consistent authorization across all three models. The controller improved GPT-4.1 from 61.7% to 100.0% AACR, Claude Sonnet 4.6 from 54.7% to 100.0% AACR, and Gemini Flash from 66.7% to 100.0% AACR. Wrong-channel rate, PTMAR, and unsafe authorization were reduced to 0.0% across controller-corrected outputs.

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

| caveat              | wording                                                                                                                                                                         |
|:--------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Synthetic benchmark | This benchmark is synthetic and should not be interpreted as patient-care deployment evidence.                                                                                  |
| Controller contract | The controller uses the locked expected-action channel as the deterministic evidence/action contract and is not yet a fully autonomous parser-derived clinical decision system. |
| Human confirmation  | Human/expert confirmation was author-domain confirmation rather than independent blinded multi-rater adjudication.                                                              |
| Model snapshots     | Provider model behavior may change; exact model IDs, dates, and output artifacts should be reported.                                                                            |
| Domain scope        | The benchmark focuses on oncology therapeutic authorization and requires domain-specific adaptation before extension to other clinical settings.                                |

---

# 10. Key Claims

| claim_type                | claim                                                                                                              | supporting_result                                                                                         | recommended_location                                               |
|:--------------------------|:-------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------|
| primary empirical finding | Hard action-obscured prompts exposed action-channel instability across all three models.                           | Unguided AACR ranged from 54.7% to 66.7%; wrong-channel rate ranged from 33.3% to 45.3%.                  | Results opening paragraph and Discussion principal findings.       |
| phenotype finding         | Failure phenotype was model-specific.                                                                              | GPT-4.1: generic escalation; Claude: over-hold/under-switch; Gemini: under-hold/generic escalation.       | Results model-specific phenotype subsection.                       |
| controller finding        | The deterministic evidence-contract controller restored evidence-consistent authorization across all three models. | Controller-corrected AACR 100.0% and wrong-channel/PTMAR/unsafe authorization 0.0% across all three.      | Results controller subsection and Discussion governance mechanism. |
| benchmark-design finding  | Action-cue-aligned prompts can overestimate model robustness.                                                      | v0.63 near-ceiling GPT-4.1 result followed by v0.63b cue-alignment audit and v0.67 hard-set degradation.  | Discussion benchmark validity contribution.                        |
| governance interpretation | Safety-critical clinical AI should be evaluated as a controlled decision system, not only as a text generator.     | Controller corrected distinct model-specific routing phenotypes without relying on model self-correction. | Discussion evidence-contract control and conclusion.               |

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
