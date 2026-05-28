# OncoGuard-Response v0.22 Safety-Margin Policy Manifest

## Project

OncoGuard-Response

## Version

v0.22 safety-margin policy simulation

## Baseline reference

This analysis builds on the v0.21 adjusted multi-policy evaluation, which corrected trajectory-level evidence-label carryover by introducing `evidence_status_stage_adjusted`.

Input source:

- `../v0_21_multi_policy/visit_level_policy_inputs_v0_21_adjusted.csv`

## Purpose

v0.22 evaluates whether a conservative safety-margin policy can preserve zero premature therapy misuse while quantifying the cost of additional reassessment and potential over-deferral.

## Policy definitions

### Permissive policy

Authorizes continuation unless an explicit hard-stop action is present.

### Standard policy

Follows the expected authorization action at each visit.

### Conservative-margin policy

Follows the expected authorization action but adds one extra reassessment when `continue_therapy` immediately follows a prior non-continuation visit.

This models a stricter safety posture after recent escalation, toxicity hold, treatment switch, or unresolved evidence.

## Generated data files

- `policy_visit_scores_v0_22_safety_margin.csv`
- `multi_policy_summary_v0_22_safety_margin.csv`
- `conservative_margin_trigger_audit_v0_22.csv`
- `results_v0_22_safety_margin.md`

## Generated figures

- `figures/figure_1_v0_22_ptmar_by_policy.png`
- `figures/figure_2_v0_22_aacr_by_policy.png`
- `figures/figure_3_v0_22_defer_rate_by_policy.png`
- `figures/figure_4_v0_22_unsafe_authorization_by_policy.png`
- `figures/figure_5_v0_22_over_deferral_by_policy.png`
- `figures/figure_6_v0_22_safety_margin_triggers.png`
- `figures/figure_7_v0_22_multi_policy_comparison.png`
- `figures/figure_index_v0_22.csv`
- `figures/figure_captions_v0_22.md`

## Final v0.22 results

| Policy | PTMAR (%) | AACR (%) | Defer rate (%) | Unsafe authorization (%) | Over-deferral (%) | Correct authorization (%) | Safety-margin triggers |
|---|---:|---:|---:|---:|---:|---:|---:|
| Permissive | 26.7 | 73.3 | 0.0 | 26.7 | 0.0 | 73.3 | 0 |
| Standard | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 | 100.0 | 0 |
| Conservative-margin | 0.0 | 88.3 | 38.3 | 0.0 | 11.7 | 88.3 | 7 |

## Main interpretation

The permissive policy eliminated deferral but produced premature therapy misuse and unsafe authorization in 26.7% of visit-level evaluations.

The standard policy followed the expected authorization pathway with 0.0% PTMAR, 100.0% AACR, and 0.0% unsafe authorization.

The conservative-margin policy preserved 0.0% PTMAR and 0.0% unsafe authorization, but triggered 7 additional reassessments, increasing deferral from 26.7% to 38.3% and introducing 11.7% over-deferral.

## Manuscript takeaway

v0.22 shows that OncoGuard-Response can quantify the governance tradeoff between unsafe continuation and conservative over-deferral. This positions the benchmark as a policy-simulation framework for oncology therapeutic-response authorization, not merely a static accuracy or alignment scorecard.
