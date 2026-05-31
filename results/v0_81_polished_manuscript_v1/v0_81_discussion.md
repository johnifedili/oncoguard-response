## Discussion

### Principal findings

This study demonstrates that hard action-obscured oncology therapeutic-authorization prompts expose clinically meaningful action-channel instability across multiple frontier models. All three models achieved perfect schema conformance, but none achieved high unguided action-channel accuracy. The core finding is that syntactically valid clinical AI outputs can still route therapeutic decisions to the wrong action channel.

The failures were not uniform. GPT-4.1 tended toward generic escalation, Claude Sonnet 4.6 toward over-hold and under-switch behavior, and Gemini Flash toward under-hold and generic escalation. These findings suggest that aggregate accuracy alone is insufficient to characterize clinical AI safety. Models may fail differently, and these differences matter operationally.

### Action-channel instability as a clinical AI failure mode

The findings support action-channel instability as a clinically relevant failure mode. In these cases, the model often appeared to recognize that concern was present, but selected the wrong management pathway. This is analogous to recognizing that a patient is unwell but calling a family member rather than emergency responders. The model senses that action is needed, but the action channel is wrong.

This framing is important because not all unsafe clinical AI behavior appears as reckless continuation. A model can be conservative and still unsafe if it over-holds therapy when evaluation is indicated, escalates generically when definitive hold or switch is needed, or delays emergency toxicity management through lower-acuity routing. Safety evaluation should therefore measure action-channel precision, not only refusal, caution, or general concern recognition.

### Naturalistic pressure as action-channel interference

The pressure templates used in this benchmark were designed to reflect real workflow pressures rather than artificial jailbreaks. Examples included urgency, reassurance from a care team, complaint escalation, prescriber familiarity, social consensus, workflow pressure, toxicity minimization, and protocol-waiver framing. The results suggest that naturalistic pressure can degrade action-channel precision even when it does not produce widespread unsafe continuation.

This supports the interpretation that clinical pressure often acts as action-channel interference. The model may not directly choose the most reckless option, but pressure can divert it away from the correct definitive action. This mirrors real clinical workflows, where urgency, authority claims, or emotional pressure can prevent clinicians from taking the time to route a case to the correct safety channel.

### Evidence-contract control as governance architecture

The evidence-contract controller restored evidence-consistent authorization across all three models. The controller did not require each model to internally become a reliable action-channel judge. Instead, it separated model reasoning from therapeutic authorization. The model could generate an action recommendation, but the controller enforced the locked evidence/action contract.

This supports a governance architecture in which clinical AI systems are evaluated as controlled decision systems, not merely as text generators. In safety-critical domains, action authorization should be constrained by explicit evidence thresholds and decision contracts. The present results show that such a controller can normalize distinct model-specific failure phenotypes under a known therapeutic action contract.

### Benchmark validity and action-cue leakage

This work also contributes a benchmark-design lesson. Naturalistic prompts can still be too easy if they leak the correct action channel. Earlier expanded prompts produced near-ceiling performance, but cue-alignment audit showed that the prompts were action/evidence cue-aligned. After targeted action-cue repair, the hard prompt set exposed substantial model instability.

This finding matters for clinical AI evaluation. A benchmark may appear realistic because it uses clinical language, but still overestimate robustness if the correct management action is too obvious from surface cues. Action-cue leakage should therefore be audited explicitly in clinical AI benchmarks that evaluate management decisions.

### Limitations

This study has several limitations. First, the benchmark is synthetic and should not be interpreted as evidence for clinical deployment. Second, the controller uses the locked expected-action channel as the deterministic evidence/action contract. It is therefore a controller-mechanism study, not a fully autonomous parser-derived clinical decision system. Third, human/expert confirmation was author-domain confirmation rather than independent blinded multi-rater adjudication. Fourth, model APIs and snapshots may change over time. Fifth, this benchmark focuses on oncology therapeutic authorization and may not generalize directly to other clinical domains without domain-specific evidence/action contracts.

### Future work

Future work should evaluate parser-derived evidence contracts, independent blinded oncology adjudication, additional treatment classes, and prospective EHR-like longitudinal scenarios. Additional studies should also assess clinician-AI workflow effects, including whether controller-based systems reduce therapeutic misrouting without increasing unnecessary delay or cognitive burden.

### Conclusion

In a repaired hard action-obscured oncology therapeutic-authorization benchmark, GPT-4.1, Claude Sonnet 4.6, and Gemini Flash all showed clinically meaningful action-channel instability despite perfect schema conformance. The failure phenotype differed by model, but a deterministic evidence-contract controller restored evidence-consistent authorization across all three. These findings support separating model reasoning from therapeutic action authorization in safety-critical clinical AI governance.

---
