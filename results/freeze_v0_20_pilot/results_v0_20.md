# OncoGuard-Response v0.20 Pilot Results

## Frozen pilot cohort

The frozen v0.20 pilot included 20 oncology response trajectories comprising 60 visit-level evaluations. The trajectory inventory, primary metric summary, failure taxonomy, and figure outputs were saved under the frozen pilot results directory.

Frozen files:

- `trajectory_inventory_v0_20.csv`
- `pilot_ptmar_aacr_summary_v0.csv`
- `failure_taxonomy_v0_20.csv`
- `figures/figure_1_metric_summary_v0_20.png`
- `figures/figure_2_failure_taxonomy_v0_20.png`

## Primary therapy-misuse endpoint

Across the 60 visit-level evaluations, the premature therapy misuse action rate (PTMAR) was 23.3%. This corresponds to 14 PTMAR-positive visits out of 60 total visits.

This finding indicates that nearly one in four evaluated candidate responses contained a therapy-response action that was inconsistent with the evidence state or authorization constraints of the case.

## Authorization-contract alignment

The authorization alignment contract rate (AACR) was 93.3%. This indicates that most candidate responses remained aligned with the expected authorization contract.

Importantly, high AACR with persistent PTMAR suggests that candidate responses can appear broadly contract-aligned while still making safety-relevant therapeutic commitment errors.

## Failure-taxonomy analysis

Failure-taxonomy analysis of the 14 PTMAR-positive visits identified three recurrent evidence-state failure modes:

| Evidence-state failure mode | Failure count |
|---|---:|
| Contradictory evidence | 5 |
| Missing critical evidence | 5 |
| Incomplete toxicity assessment | 4 |

These findings suggest that therapy-misuse events were not random output failures. Instead, failures clustered around unresolved evidence-state constraints, including contradictory evidence, missing critical evidence, and incomplete toxicity assessment.

## Interpretation

The v0.20 pilot demonstrates that OncoGuard-Response can separate general authorization-contract alignment from specific therapeutic-response misuse events. This distinction is important because a response may appear clinically plausible or mostly aligned with an authorization contract while still moving toward an unsafe or premature treatment-response decision.

The benchmark therefore measures a clinically meaningful governance failure: whether candidate responses respect evidence sufficiency before therapeutic-response commitment.

## Figure captions

**Figure 1. OncoGuard-Response v0.20 pilot metric summary.**  
The frozen v0.20 pilot included 20 trajectories and 60 visit-level evaluations. The premature therapy misuse action rate was 23.3%, while the authorization alignment contract rate was 93.3%.

**Figure 2. Evidence-state failure taxonomy among PTMAR-positive visits.**  
Failure-taxonomy analysis identified 14 PTMAR-positive visits. These clustered into contradictory evidence, missing critical evidence, and incomplete toxicity assessment, suggesting that therapy-misuse events reflected unresolved evidence-state constraints rather than nonspecific output failure.

## Locked v0.20 takeaway

In the frozen v0.20 pilot, OncoGuard-Response identified a non-trivial therapeutic-response misuse signal despite high overall authorization-contract alignment. PTMAR was 23.3%, AACR was 93.3%, and all PTMAR-positive events mapped to evidence-state failure modes.
