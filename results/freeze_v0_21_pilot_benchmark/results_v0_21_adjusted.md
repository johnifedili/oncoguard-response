# OncoGuard-Response v0.21 Adjusted Multi-Policy Evaluation

## Overview

The v0.21 analysis extended the frozen v0.20 pilot by converting 20 trajectory-level records into 60 visit-level authorization decisions and simulating three therapeutic-response authorization policies: permissive, standard, and conservative.

A preliminary audit showed that trajectory-level evidence labels could incorrectly mark later resolved continuation visits as unresolved. To address this, the v0.21 analysis introduced a visit-stage-adjusted evidence status variable, `evidence_status_stage_adjusted`, derived from the expected authorization action at each visit.

## Visit-level authorization states

The adjusted visit-level authorization states were:

| Visit-level authorization state | Count |
|---|---:|
| Authorized or resolved | 28 |
| Unresolved / needs more evidence | 16 |
| Active toxicity or safety hold | 8 |
| Progression or failure confirmed | 6 |
| Emergency toxicity confirmed | 2 |

This produced 60 visit-level evaluations from the 20 three-visit trajectories.

## Multi-policy simulation results

| Policy | PTMAR (%) | AACR (%) | Defer rate (%) | Unsafe authorization (%) | Correct authorization (%) |
|---|---:|---:|---:|---:|---:|
| Permissive | 26.7 | 73.3 | 0.0 | 26.7 | 73.3 |
| Standard | 0.0 | 100.0 | 26.7 | 0.0 | 100.0 |
| Conservative | 0.0 | 100.0 | 26.7 | 0.0 | 100.0 |

## Interpretation

The permissive policy eliminated deferral but produced therapy-misuse behavior in 26.7% of visit-level evaluations. These PTMAR-positive events were dominated by unresolved evidence states, indicating that permissive continuation can authorize therapy before sufficient evaluation is complete.

By contrast, the standard policy achieved 0.0% PTMAR and 100.0% AACR after visit-stage adjustment, indicating that the expected authorization pathway was internally consistent. The conservative policy produced the same results under the current v0.21 rules because conservative deferral was triggered only when the expected authorization path already required escalation.

## Methodological correction

The initial v0.21 policy simulation used trajectory-level evidence-state labels copied across all three visits within each trajectory. This produced apparent conflicts in which later continuation visits were labeled as unresolved even when the expected action indicated authorization or resolution.

The adjusted analysis corrected this by separating:

1. the trajectory-level failure being tested, and  
2. the visit-level authorization status at each decision point.

This distinction is important because an oncology response trajectory may begin with missing or incomplete evidence and later reach a valid continuation point after further assessment.

## Main takeaway

OncoGuard-Response can simulate how different therapeutic authorization policies behave over the same oncology response trajectories. In the adjusted v0.21 analysis, permissive continuation increased therapy-misuse risk, while contract-following policies eliminated PTMAR by respecting unresolved evidence states and safety-hold decisions.
