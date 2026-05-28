# Manuscript Results Subsection — Multi-Policy Therapeutic-Response Simulation

## Multi-policy therapeutic-response simulation

To evaluate whether OncoGuard-Response could function as a policy-simulation framework rather than a static scoring tool, we extended the frozen v0.20 pilot into visit-level multi-policy analyses. The original pilot contained 20 oncology response trajectories, each represented as a three-visit sequence, yielding 60 visit-level therapeutic authorization decisions.

Because each trajectory could begin with unresolved evidence and later reach an authorized continuation point, trajectory-level failure labels were not assumed to apply uniformly across all visits. An initial audit identified 26 visits in which `continue_therapy` was the expected action while the trajectory-level evidence label still indicated unresolved evidence. To avoid falsely classifying valid later continuation decisions as premature therapy misuse, we introduced a visit-stage-adjusted evidence-status variable, `evidence_status_stage_adjusted`.

The adjusted visit-level authorization states were: authorized or resolved (28 visits), unresolved or needing more evidence (16 visits), active toxicity or safety hold (8 visits), confirmed progression or treatment failure (6 visits), and confirmed emergency toxicity (2 visits).

## v0.21 adjusted policy simulation

In the v0.21 adjusted analysis, three authorization policies were simulated across the same 60 visit-level evaluations: permissive, standard, and conservative. The permissive policy authorized continuation unless an explicit hard-stop action was present. The standard policy followed the expected authorization action at each visit. The conservative policy deferred when evidence remained unresolved while respecting safety holds, treatment switches, and emergency toxicity-management actions.

The permissive policy produced a premature therapy misuse action rate (PTMAR) of 26.7% and an unsafe authorization rate of 26.7%, with no deferrals. These PTMAR-positive events were dominated by unresolved evidence states, indicating that permissive continuation can authorize therapy before sufficient evaluation is complete. In contrast, the standard and conservative policies both achieved 0.0% PTMAR, 0.0% unsafe authorization, 100.0% authorization alignment contract rate (AACR), and a 26.7% deferral rate.

These findings show that visit-stage adjustment resolved the apparent conflict between expected continuation and trajectory-level unresolved evidence labels, and that contract-following policies eliminated observed premature therapeutic authorization in the adjusted visit-level evaluation.

## v0.22 safety-margin policy extension

The v0.22 analysis introduced a stricter conservative-margin policy to test whether additional safety-margin reassessment could be quantified. Unlike the standard policy, which followed the expected authorization path exactly, the conservative-margin policy required one additional reassessment when `continue_therapy` immediately followed a prior non-continuation visit. This simulated a cautious governance posture after recent escalation, toxicity hold, treatment switch, or unresolved evidence.

Under v0.22, the permissive policy again produced PTMAR and unsafe authorization in 26.7% of visit-level evaluations. The standard policy preserved 0.0% PTMAR, 0.0% unsafe authorization, 100.0% AACR, and a 26.7% deferral rate. The conservative-margin policy also preserved 0.0% PTMAR and 0.0% unsafe authorization, but triggered 7 additional reassessments. This increased the deferral rate from 26.7% to 38.3%, reduced AACR from 100.0% to 88.3%, and introduced 11.7% over-deferral.

| Policy | PTMAR (%) | AACR (%) | Defer rate (%) | Unsafe authorization (%) | Over-deferral (%) |
|---|---:|---:|---:|---:|---:|
| Permissive | 26.7 | 73.3 | 0.0 | 26.7 | 0.0 |
| Standard | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 |
| Conservative-margin | 0.0 | 88.3 | 38.3 | 0.0 | 11.7 |

## Interpretation

Together, the v0.21 and v0.22 analyses demonstrate that OncoGuard-Response can quantify therapeutic-response governance tradeoffs. A permissive policy minimized deferral but produced unsafe continuation. A standard contract-following policy eliminated observed premature therapy misuse while preserving full alignment with the expected authorization path. A conservative-margin policy maintained zero observed therapy misuse but introduced additional reassessment and over-deferral.

This supports the central benchmark framing: oncology response evaluation is not only a question of whether treatment should continue, but whether continuation is authorized by the current evidence state and governance posture.
