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

