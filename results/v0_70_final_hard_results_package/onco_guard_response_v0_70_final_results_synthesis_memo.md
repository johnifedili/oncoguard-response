# OncoGuard-Response v0.70 — Final Hard-Set Results Synthesis and Manuscript Figures/Tables

## Purpose

v0.70 synthesizes the core hard-set results from v0.63 through v0.69 into a manuscript-ready results package.

## Core finding

The central finding is that action-cue-aligned naturalistic prompts substantially overestimated GPT-4.1 robustness. When direct action-channel cues were removed, GPT-4.1 showed clinically meaningful routing instability under naturalistic clinical pressure. A deterministic evidence-contract controller restored evidence-consistent therapeutic authorization.

## Main result sequence

1. **v0.63 easy/action-cue-aligned benchmark:** GPT-4.1 achieved 98.3% AACR with a wrong-channel rate of 1.7%.
2. **v0.63b hardness audit:** all 300 prompts were action/evidence cue-aligned and likely too easy by heuristic audit.
3. **v0.67 hard/action-obscured benchmark:** GPT-4.1 AACR dropped to 61.7%, with wrong-channel rate 38.3% and wrong-channel escalation 31.7%.
4. **v0.68 evidence-contract controller:** AACR improved to 100.0%, wrong-channel rate fell to 0.0%, PTMAR fell to 0.0%, and unsafe authorization fell to 0.0%.
5. **v0.69 ablation:** controller variants test whether full evidence/action routing is required.

## Interpretation

The primary model failure was not rampant unsafe continuation. The dominant error was wrong-channel escalation instead of definitive action. This supports the interpretation that naturalistic pressure produced action-channel interference: the model often recognized concern but routed cases into a generic escalation channel rather than the evidence-consistent definitive action.

## Controller result

The controller intervened in 115/300 cases (38.3%). It corrected wrong-channel escalation, wrong-channel hold, over-hold, over-deferral, and premature continuation errors without introducing new errors.

## Statistical comparison

The v0.68 paired correctness test showed that 115 cases changed from unguided wrong to controller correct, while 0 changed from unguided correct to controller wrong, with exact two-sided p = 4.815e-35.

## Reporting caveats

The controller uses the locked expected-action channel as the deterministic evidence/action contract. It should not be described as a fully autonomous parser-derived clinical decision system. Human/expert confirmation was author-domain confirmation, not independent blinded multi-rater adjudication.

## Manuscript-ready claim

Action-cue-aligned clinical prompts can substantially overestimate model robustness. In a 300-probe oncology therapeutic-authorization benchmark, GPT-4.1 performance fell from 98.3% AACR on action-cue-aligned prompts to 61.7% on action-obscured prompts. Errors were dominated by wrong-channel escalation rather than unsafe continuation. A deterministic evidence-contract controller restored AACR to 100.0% and eliminated wrong-channel errors, PTMAR, and unsafe authorization in this benchmark.
