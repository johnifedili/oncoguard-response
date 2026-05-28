# OncoGuard-Response v0.22 Safety-Margin Policy Results

## Overview

The v0.22 analysis extended the v0.21 adjusted multi-policy simulation by adding a conservative safety-margin policy. Unlike the standard policy, which follows the expected authorization path exactly, the conservative-margin policy requires one additional reassessment when therapy continuation immediately follows a prior non-continuation visit.

This models a stricter clinical governance posture: even when continuation appears authorized, a system may require an additional safety check after recent escalation, toxicity hold, treatment switch, or unresolved evidence.

## Policy definitions

Three policies were compared across 60 visit-level evaluations:

1. **Permissive policy**  
   Authorizes continuation unless an explicit hard-stop action is present.

2. **Standard policy**  
   Follows the expected authorization action at each visit.

3. **Conservative-margin policy**  
   Follows the expected authorization action but adds an extra reassessment requirement when `continue_therapy` follows a prior non-continuation action.

## Results

| Policy | PTMAR (%) | AACR (%) | Defer rate (%) | Unsafe authorization (%) | Over-deferral (%) | Correct authorization (%) |
|---|---:|---:|---:|---:|---:|---:|
| Permissive | 26.7 | 73.3 | 0.0 | 26.7 | 0.0 | 73.3 |
| Standard | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 | 100.0 |
| Conservative-margin | 0.0 | 88.3 | 38.3 | 0.0 | 11.7 | 88.3 |

The conservative-margin policy triggered 7 additional reassessment events after prior non-continuation visits.

## Interpretation

The permissive policy eliminated deferral but produced premature therapy misuse and unsafe authorization in 26.7% of visit-level evaluations. The standard policy eliminated observed PTMAR and unsafe authorization while preserving full concordance with the expected authorization path.

The conservative-margin policy also preserved 0.0% PTMAR and 0.0% unsafe authorization, but at the cost of additional reassessment. Compared with the standard policy, it increased deferral from 26.7% to 38.3%, reduced AACR from 100.0% to 88.3%, and introduced 11.7% over-deferral.

## Main takeaway

v0.22 demonstrates that OncoGuard-Response can quantify not only unsafe continuation, but also the tradeoff between safety-margin conservatism and potential over-deferral. This positions the benchmark as a therapeutic-response governance simulator rather than a simple accuracy scorecard.
