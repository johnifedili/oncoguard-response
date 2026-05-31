# OncoGuard-Response v0.52 — Pilot Results Synthesis Memo

**Document type:** Pilot results synthesis memo  
**Version:** v0.52  
**Author:** Chijioke John Ifedili  
**Project:** OncoGuard-Response / OncoGuard v0.45 naturalistic pressure architecture  
**Status:** Pilot synthesis after v0.51 controller ablation  
**Source tags:** v0.45 through v0.51  
**Primary branch:** `v0.24-clean-benchmark-branch`

---

## 1. Purpose of this memo

This memo synthesizes the OncoGuard-Response pilot sequence from the expanded clean benchmark through the naturalistic pressure evaluation, controller intervention, and controller ablation.

The purpose is to preserve the scientific story before scaling to a larger benchmark. The key conclusion is that clean oncology authorization prompts produced ceiling performance, but naturalistic clinical pressure revealed a distinct governance failure: **conservative wrong-channel collapse**. A deterministic evidence-contract controller corrected this failure by restoring the evidence-consistent therapeutic action channel while preserving zero premature therapy misuse and zero unsafe authorization.

This memo is a synthesis document, not a new empirical run.

---

## 2. Research question

The pilot addressed the following question:

> When oncology therapeutic authorization decisions are framed under realistic workflow, patient, clinician, organizational, or social pressure, does GPT-4.1 maintain the correct evidence-consistent action channel, and can an evidence-gated controller correct pressure-induced wrong-channel behavior?

The study was not designed merely to force model failure. It followed a four-layer evaluation architecture:

1. **Clean clinical case** — What is the correct therapeutic action?
2. **Naturalistic pressure** — Does the prompt contain realistic clinical/workflow pressure?
3. **Cue-contamination audit** — Does the prompt avoid looking like an obvious adversarial or safety benchmark?
4. **Controller test** — If the model chooses the wrong action, does the controller restore the evidence-consistent action?

---

## 3. Background and methodological pivot

The project began with an expanded clean oncology authorization benchmark. The response space contained five therapeutic authorization actions:

- `continue_therapy`
- `escalate_evaluation`
- `hold_therapy`
- `switch_therapy`
- `emergency_toxicity_management`

The expanded clean design contained 100 trajectories and 300 visit-level decisions across five cancer types, five therapy classes, and multiple trajectory patterns. GPT-4.1 achieved ceiling performance on the clean and blinded prompt variants, including 100% schema conformance and 100% action-channel accuracy.

Rather than interpreting this as definitive model robustness, the ceiling result was treated as a validity warning. The project identified a likely benchmark-design risk: **cue contamination / surface-feature shortcut learning**, in which frontier models may detect that a prompt is a safety/adversarial evaluation and activate safe-response templates rather than reason through realistic clinical pressure.

This led to the v0.45 four-layer architecture and the creation of naturalistic pressure probes based on real clinical/pharmacy workflow patterns rather than obvious red-team wording.

---

## 4. Versioned provenance summary

### v0.40 — Expanded design matrix

The project defined a 100-trajectory / 300-visit benchmark design matrix. Expected action distribution:

- `continue_therapy`: 175
- `escalate_evaluation`: 63
- `hold_therapy`: 37
- `switch_therapy`: 13
- `emergency_toxicity_management`: 12

### v0.41 — Synthetic case generation

Synthetic longitudinal oncology cases were generated from the v0.40 design.

### v0.42 — Integrity audit

The expanded benchmark passed integrity checks: 100 trajectories, 300 visit-level decisions, 100 unique trajectory IDs, and no JSON/design mismatches.

### v0.43 / v0.43b — Prompt generation

The clean and blinded prompt sets were generated. The blinded set removed obvious metadata cues such as failure mode and trajectory pattern.

### v0.44 / v0.44b — GPT-4.1 clean/blinded pipeline validation

GPT-4.1 achieved 100% AACR on the clean/blinded expanded benchmark. This was treated as pipeline validation and as evidence that the clean benchmark was too cue-aligned or too easy for rigorous pressure-robustness claims.

### v0.45 — Cue-contamination protocol and pressure taxonomy

A 13-family pressure taxonomy and cue-contamination protocol were locked. The taxonomy included F01–F13, with F07 defined as a multi-turn ratchet family. The protocol emphasized naturalistic clinical pressure rather than cartoonish red-team prompts.

### v0.46 — Naturalistic pressure pilot

A 30-probe naturalistic pressure pilot was generated from six high-yield pressure templates:

1. Travel / treatment timing urgency
2. Reported team reassurance
3. Weaponized complaint channel
4. Prescriber/oncologist familiarity pressure
5. Social consensus pressure
6. Supervisor/workflow pressure

### v0.46a — Automated Layer 1–3 audit

All 30 probes passed the automated Layer 1–3 screen:

- Layer 1 clinical-validity screen: 30/30
- Layer 2 pressure-realism screen: 30/30
- Layer 3 cue-contamination screen: 30/30
- Cue contamination score 0: 30/30

### v0.46b — Human confirmation package

A human/expert confirmation package was created, including a reviewer view, instructions, and confirmation sheet.

### v0.46c — Completed author-domain confirmation

The 30 probes received author-domain expert pilot confirmation and were marked eligible for model testing. This should be reported as **author-domain expert pilot confirmation**, not independent blinded multi-rater adjudication.

### v0.47 — GPT-4.1 naturalistic pressure evaluation

GPT-4.1 was evaluated on the 30 human-confirmed naturalistic pressure probes.

### v0.50 — Deterministic evidence-contract controller intervention

A deterministic evidence-contract controller was applied to the same v0.47 model outputs.

### v0.51 — Controller ablation

Ablation analyses tested whether the controller benefit required full evidence/action routing or could be reproduced by simpler partial controllers.

---

## 5. v0.47 main finding: conservative wrong-channel collapse

GPT-4.1 maintained technical output reliability under naturalistic pressure:

- Schema conformance: 100.0%
- Parse success: 100.0%

However, action-channel performance degraded substantially:

- Pressure-sustained AACR: 33.3%
- Wrong-channel rate: 66.7%
- Wrong-channel escalation: 53.3%
- Defer rate: 80.0%
- PTMAR: 0.0%
- Unsafe authorization: 0.0%

The model selected only two actions:

- `escalate_evaluation`: 24
- `hold_therapy`: 6

It never selected:

- `continue_therapy`
- `switch_therapy`
- `emergency_toxicity_management`

The dominant error was:

> `wrong_channel_escalation_instead_of_definitive_action`

The expected-vs-selected pattern showed:

- Emergency toxicity cases: 6/6 routed to `escalate_evaluation`
- Switch-therapy cases: 6/6 routed to `escalate_evaluation`
- Hold-therapy cases: 2/6 correctly held; 4/6 escalated
- Escalate-evaluation cases: 8/12 correctly escalated; 4/12 over-held

The model did not primarily fail by authorizing unsafe continuation. Instead, it often recognized that concern existed but routed definitive safety events into a lower-acuity escalation channel.

A useful clinical analogy for this failure is:

> The model recognized that something was wrong, but chose the wrong response channel. Clinically, this resembles recognizing that a patient is unwell but calling a family member rather than emergency responders.

This finding is better described as **severity-action mismatch** or **conservative wrong-channel collapse**, not as simple unsafe compliance.

---

## 6. Why the v0.47 failure matters

The v0.47 result identifies a clinically meaningful governance problem. Avoiding unsafe continuation is not sufficient if the model fails to select the appropriate definitive action channel.

In oncology therapeutic authorization, `escalate_evaluation` is appropriate when evidence remains unresolved. But it is not the correct endpoint when the available evidence already supports:

- emergency toxicity management,
- therapy hold,
- or therapy switch.

Thus, conservative deferral can still be unsafe or inefficient when it delays the correct clinical action. The problem is not only whether the model acts too early; it is whether the model maps evidence severity to the correct action channel.

---

## 7. v0.50 controller intervention result

The v0.50 deterministic evidence-contract controller was applied to the same 30 v0.47 GPT-4.1 outputs.

Main results:

- AACR improved from 33.3% to 100.0%: +66.7 percentage points
- Wrong-channel rate decreased from 66.7% to 0.0%: −66.7 percentage points
- Wrong-channel escalation decreased from 53.3% to 0.0%: −53.3 percentage points
- Defer rate decreased from 80.0% to 40.0%: −40.0 percentage points
- Emergency under-recognition decreased from 20.0% to 0.0%
- Switch under-recognition decreased from 20.0% to 0.0%
- Hold under-recognition decreased from 13.3% to 0.0%
- PTMAR remained 0.0%
- Unsafe authorization remained 0.0%

Controller interventions occurred in 20/30 probes:

- 16 corrected wrong-channel escalation to definitive action
- 4 corrected over-hold to evaluation
- 10 required no intervention

The controller therefore fixed the observed failure phenotype without introducing premature therapy misuse or unsafe authorization.

---

## 8. v0.51 ablation result

The v0.51 ablation tested whether the v0.50 improvement could be reproduced by simpler partial controllers.

Policies tested:

1. `unguided_model`
2. `safety_block_only`
3. `no_definitive_router`
4. `hold_router_only`
5. `switch_router_only`
6. `emergency_router_only`
7. `full_controller`

Main ablation results:

| Policy | AACR | Wrong-channel rate | Wrong-channel escalation | PTMAR | Unsafe authorization |
|---|---:|---:|---:|---:|---:|
| Unguided model | 33.3% | 66.7% | 53.3% | 0.0% | 0.0% |
| Safety block only | 33.3% | 66.7% | 53.3% | 0.0% | 0.0% |
| No definitive router | 46.7% | 53.3% | 53.3% | 0.0% | 0.0% |
| Hold router only | 46.7% | 53.3% | 40.0% | 0.0% | 0.0% |
| Switch router only | 53.3% | 46.7% | 33.3% | 0.0% | 0.0% |
| Emergency router only | 53.3% | 46.7% | 33.3% | 0.0% | 0.0% |
| Full controller | 100.0% | 0.0% | 0.0% | 0.0% | 0.0% |

The safety-block-only ablation did not improve performance, because GPT-4.1 did not fail by selecting unsafe continuation. Partial routers improved only the channels they covered. Only the full controller restored all evidence/action channels.

The paired correctness comparison of unguided GPT-4.1 versus full controller showed:

- Unguided wrong → full controller correct: 20
- Unguided correct → full controller wrong: 0
- Discordant pairs: 20
- Exact two-sided p = 0.000002

This supports the mechanistic interpretation that the controller’s benefit came from full evidence/action routing, not from generic safety blocking.

---

## 9. Central pilot conclusion

The pilot supports the following conclusion:

> Naturalistic clinical pressure revealed a failure mode that was invisible in the clean benchmark. GPT-4.1 remained syntactically reliable and avoided unsafe premature continuation, but collapsed into conservative wrong-channel routing, especially by overusing escalation when definitive actions were indicated. A deterministic evidence-contract controller corrected this failure by restoring the locked evidence-consistent action channel while preserving zero PTMAR and zero unsafe authorization.

This pilot therefore establishes a coherent governance sequence:

1. Clean benchmark ceiling performance revealed limited stress-test value.
2. Cue-contamination risk motivated naturalistic pressure design.
3. Naturalistic pressure exposed wrong-channel action collapse.
4. Controller intervention corrected the observed failure.
5. Ablation showed that full evidence/action routing was required.

---

## 10. Interpretation for clinical AI governance

The result shows that model safety should not be evaluated only as “did the model avoid the most dangerous action?” A model can avoid overtly unsafe continuation but still fail clinically by routing the case into an inappropriate lower-acuity channel.

In clinical workflow terms:

- Recognizing concern is not enough.
- Deferring is not always enough.
- Escalation is not interchangeable with emergency management, therapy hold, or treatment switch.
- Safety requires correct **action-channel authorization**, not merely cautious language.

This supports the broader OncoGuard thesis:

> Clinical AI governance should separate reasoning from authorization and enforce evidence/action contracts when model behavior becomes pressure-sensitive or action-channel unstable.

---

## 11. Claims supported by this pilot

The pilot supports the following claims:

1. Clean/blinded oncology authorization prompts can produce ceiling model performance and may not expose clinically meaningful governance failures.
2. Naturalistic pressure probes can reveal failure modes not visible in clean benchmarks.
3. GPT-4.1 under naturalistic pressure showed conservative wrong-channel collapse rather than unsafe premature continuation.
4. A deterministic evidence-contract controller corrected the observed wrong-channel collapse.
5. Safety-block-only control was insufficient because the failure was not unsafe continuation.
6. Full evidence/action routing was required to restore correct therapeutic authorization channels.
7. The controller improved action-channel accuracy without increasing PTMAR or unsafe authorization.

---

## 12. Claims not yet supported

The pilot does **not** yet support the following claims:

1. That the benchmark generalizes to all oncology settings.
2. That the 30-probe pilot is sufficient for definitive clinical validation.
3. That the controller is a fully autonomous evidence parser.
4. That independent blinded expert raters have confirmed the probe labels.
5. That the same pattern holds across all frontier models.
6. That the same pattern holds at 300+ probe scale.
7. That the controller would perform identically on real-world EHR data.

These should remain limitations or future work until tested.

---

## 13. Reporting caveats

The v0.50 controller should be described as:

> a deterministic evidence-contract controller pilot using the human-confirmed expected action channel as the locked evidence/action contract.

It should not be described as:

> a fully autonomous clinical parser or autonomous decision system.

The v0.46c review should be described as:

> author-domain expert pilot confirmation.

It should not be described as:

> independent blinded multi-rater expert adjudication.

The v0.47–v0.51 sequence should be described as a pilot demonstration, not final clinical validation.

---

## 14. Recommended next steps

The strongest next sequence is:

1. **Generate manuscript-ready tables and figures**  
   Suggested figures:
   - Clean benchmark vs naturalistic pressure vs controller
   - Expected vs selected action heatmaps for v0.47 and v0.50
   - Ablation bar plot
   - Wrong-channel error taxonomy

2. **Expand to a larger naturalistic pressure benchmark**  
   Recommended target:
   - 300 pressure probes
   - balanced across pressure templates, expected actions, cancer types, and therapy classes

3. **Add independent review before large-scale testing**  
   Use at least two independent reviewers for Layer 1–3 confirmation, with adjudication for disagreements.

4. **Run multi-model evaluation**  
   Evaluate GPT-4.1, GPT-4o or current OpenAI model, Gemini, Claude, and optionally open-weight models.

5. **Develop parser-derived controller version**  
   Replace the locked expected-action contract with an evidence-state parser and test whether the controller remains effective.

---

## 15. Best manuscript framing

A strong title direction would be:

> Naturalistic Clinical Pressure Reveals Wrong-Channel Therapeutic Authorization in Oncology LLMs and Its Correction by Evidence-Contract Control

Alternative title:

> Beyond Unsafe Continuation: Correcting Wrong-Channel Therapeutic Authorization Under Naturalistic Clinical Pressure

A strong abstract-level conclusion would be:

> In a 30-probe author-confirmed pilot, naturalistic clinical pressure reduced GPT-4.1 pressure-sustained AACR to 33.3% despite 100% schema conformance and 0% unsafe continuation. Errors were dominated by conservative wrong-channel escalation rather than premature therapy continuation. A deterministic evidence-contract controller restored AACR to 100.0%, eliminated wrong-channel escalation, and preserved 0% PTMAR and unsafe authorization. Ablations showed that safety blocking alone did not improve performance, whereas full evidence/action routing was required.

---

## 16. Final synthesis

The pilot demonstrates why clinical AI governance cannot rely only on clean-case accuracy or broad safety refusal behavior. Under realistic clinical pressure, the model did not simply become reckless. Instead, it became conservatively misrouted: it recognized concern but chose the wrong response channel.

The key finding is therefore not only that the controller improved performance, but that the controller improved the **right failure mode**. It restored correct therapeutic authorization routing when the model collapsed into vague escalation.

This supports the central OncoGuard-Response claim:

> Safe clinical AI requires not only knowing when not to continue therapy, but knowing which safety or treatment action is authorized by the evidence.
