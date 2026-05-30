# OncoGuard-Response v0.42 Expanded Benchmark Card

## Purpose

v0.42 audits the expanded OncoGuard-Response benchmark generated in v0.41 from the locked v0.40 design matrix.

## Version lineage

- v0.40: expanded benchmark design matrix
- v0.41: synthetic case generation from v0.40
- v0.42: integrity audit, benchmark card, and manifest

## Benchmark size

| Item | Count |
|---|---:|
| Design trajectories | 100 |
| Design visit-level decisions | 300 |
| Generated trajectories | 100 |
| Generated visit-level decisions | 300 |
| JSON trajectory files | 100 |
| Unique trajectory IDs | 100 |

## Audit status

| Check | Result |
|---|---:|
| Audit passed | True |
| JSON schema errors | 0 |
| Design-to-generated inventory mismatches | 0 |
| Design-to-JSON mismatches | 0 |

## Expected action distribution

| expected_action               |   count |   percent |
|:------------------------------|--------:|----------:|
| continue_therapy              |     175 |      58.3 |
| escalate_evaluation           |      63 |      21   |
| hold_therapy                  |      37 |      12.3 |
| switch_therapy                |      13 |       4.3 |
| emergency_toxicity_management |      12 |       4   |

## Evidence-status distribution

| evidence_status_stage_adjusted   |   count |   percent |
|:---------------------------------|--------:|----------:|
| authorized_or_resolved           |     175 |      58.3 |
| unresolved_needs_more_evidence   |      63 |      21   |
| active_toxicity_or_safety_hold   |      37 |      12.3 |
| progression_or_failure_confirmed |      13 |       4.3 |
| emergency_toxicity_confirmed     |      12 |       4   |

## Trajectory pattern distribution

| trajectory_pattern                           |   count |
|:---------------------------------------------|--------:|
| clean_response_continuation                  |      25 |
| missing_evidence_then_resolution             |      25 |
| toxicity_hold_then_rechallenge_or_resolution |      25 |
| progression_or_emergency_escalation          |      25 |

## Cancer × therapy matrix

| cancer_type       |   HER2_directed_therapy |   PARP_platinum_based_therapy |   cytotoxic_chemotherapy |   immune_checkpoint_inhibitor |   targeted_therapy |
|:------------------|------------------------:|------------------------------:|-------------------------:|------------------------------:|-------------------:|
| NSCLC             |                       4 |                             4 |                        4 |                             4 |                  4 |
| breast_cancer     |                       4 |                             4 |                        4 |                             4 |                  4 |
| colorectal_cancer |                       4 |                             4 |                        4 |                             4 |                  4 |
| melanoma          |                       4 |                             4 |                        4 |                             4 |                  4 |
| ovarian_cancer    |                       4 |                             4 |                        4 |                             4 |                  4 |

## Intended use

This expanded benchmark is intended for evaluating oncology therapeutic authorization behavior in large language models and for testing evidence-gated controller interventions. It is not intended for clinical decision-making.

## Key governance endpoints supported

- PTMAR
- unsafe authorization rate
- AACR
- over-deferral
- over-holding
- over-emergency management
- over-switching / premature switching
- wrong-channel escalation
- schema conformance
- controller-mediated action correction
- treatment-delay risk

## Notes

The benchmark intentionally includes a high proportion of continuation-authorized visits because the v0.30 four-model pilot identified under-continuation and over-deferral as dominant governance failure modes.
