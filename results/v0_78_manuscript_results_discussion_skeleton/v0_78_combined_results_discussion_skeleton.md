# OncoGuard-Response v0.78 — Manuscript Results and Discussion Skeleton

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

