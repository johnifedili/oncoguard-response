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
