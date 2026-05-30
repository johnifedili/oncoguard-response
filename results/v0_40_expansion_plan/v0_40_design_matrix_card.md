# OncoGuard-Response v0.40 Design Matrix

## Purpose

This document defines the v0.40 expanded benchmark design before case generation.

## Design size

- 100 longitudinal oncology trajectories
- 3 visits per trajectory
- 300 visit-level therapeutic authorization decisions
- 5 cancer types
- 5 therapy classes
- 4 trajectory patterns

## Design formula

`5 cancer types × 5 therapy classes × 4 trajectory patterns = 100 trajectories`

`100 trajectories × 3 visits = 300 visit-level decisions`

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

## Pattern distribution

| trajectory_pattern                           |   count |
|:---------------------------------------------|--------:|
| clean_response_continuation                  |      25 |
| missing_evidence_then_resolution             |      25 |
| toxicity_hold_then_rechallenge_or_resolution |      25 |
| progression_or_emergency_escalation          |      25 |

## Governance rationale

The v0.30 four-model evaluation showed that frontier models avoided premature therapy continuation but had weak therapeutic authorization calibration. The v0.40 expansion is designed to support controller testing by increasing the benchmark to 300 visit-level decisions and including all five authorization actions, including emergency toxicity management.
