# Manuscript Results — OncoGuard-Response v0.21 Multi-Policy Evaluation

## Multi-policy simulation

To evaluate how different therapeutic-response authorization postures affect oncology decision behavior, we extended the frozen v0.20 pilot into a v0.21 multi-policy simulation. The frozen pilot contained 20 oncology response trajectories, each represented as a three-visit sequence, yielding 60 visit-level authorization decisions.

Three policy postures were simulated over the same visit-level trajectories: permissive, standard, and conservative. The permissive policy authorized continuation unless an explicit hard-stop action was present. The standard policy followed the expected authorization action for each visit. The conservative policy deferred or escalated when evidence remained unresolved, while respecting safety holds, therapy switches, and emergency toxicity-management actions.

## Stage-adjusted evidence-status correction

An initial audit showed that trajectory-level evidence labels could falsely mark later resolved continuation visits as unresolved. Specifically, 26 visits had an expected action of `continue_therapy` while retaining a trajectory-level unresolved evidence label. To avoid falsely classifying valid later continuation decisions as premature therapy misuse, we introduced a visit-stage-adjusted evidence-status variable, `evidence_status_stage_adjusted`.

This adjustment separated the trajectory-level failure being tested from the visit-level authorization state. The adjusted visit-level statuses were: authorized or resolved (28 visits), unresolved or needing more evidence (16 visits), active toxicity or safety hold (8 visits), confirmed progression or treatment failure (6 visits), and confirmed emergency toxicity (2 visits).

## Adjusted multi-policy results

In the adjusted v0.21 analysis, the permissive policy produced a premature therapy misuse action rate (PTMAR) of 26.7% and an unsafe authorization rate of 26.7%. These failures were dominated by unresolved evidence states, indicating that permissive continuation can authorize therapy before sufficient evaluation is complete.

By contrast, the standard policy produced 0.0% PTMAR, 100.0% authorization alignment contract rate (AACR), 26.7% deferral, and 0.0% unsafe authorization. The conservative policy produced the same results under the current v0.21 rules: 0.0% PTMAR, 100.0% AACR, 26.7% deferral, and 0.0% unsafe authorization.

## Interpretation

These findings show that OncoGuard-Response can make therapeutic authorization tradeoffs measurable. A permissive policy eliminated deferral but introduced unsafe continuation, whereas contract-following policies eliminated observed premature therapy misuse by respecting unresolved evidence states and safety-hold decisions.

The v0.21 analysis therefore demonstrates that oncology response evaluation can be framed not only as a question of whether therapy should continue, but also as a governance problem: whether continuation is authorized by the current evidence state.
