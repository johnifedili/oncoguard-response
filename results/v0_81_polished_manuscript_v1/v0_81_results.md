## Results

All three models achieved 100.0% schema conformance but showed clinically meaningful action-channel instability. Unguided AACR was 61.7% for GPT-4.1, 54.7% for Claude Sonnet 4.6, and 66.7% for Gemini Flash. Wrong-channel rates were 38.3%, 45.3%, and 33.3%, respectively. Failure phenotypes differed by model: GPT-4.1 primarily showed generic escalation, Claude Sonnet 4.6 showed over-hold and under-switch behavior, and Gemini Flash showed under-hold and generic-escalation behavior. The evidence-contract controller restored AACR to 100.0% and reduced wrong-channel rate, PTMAR, and unsafe authorization to 0.0% across all three models.

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
