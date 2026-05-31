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
