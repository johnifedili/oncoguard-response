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

