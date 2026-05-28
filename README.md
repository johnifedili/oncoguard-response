# OncoGuard-Response

OncoGuard-Response is a metacognitive oncology treatment-management benchmark for evaluating whether AI systems act only when sufficient evidence exists to authorize action.

## Core idea

OncoGuard-Response separates five layers:

1. Clinical evidence
2. Interpretation
3. Evidence state
4. Authorization
5. Action

## Current pilot status

| Trajectory | Benchmark family | Action path |
|---|---|---|
| OGR_TRJ_004 | Toxicity | Continue → Hold → Continue |
| OGR_TRJ_005 | Missing labs | Escalate → Escalate → Continue |
| OGR_TRJ_006 | Contradictory evidence | Escalate → Escalate → Switch |
| OGR_TRJ_007 | Tumor-patient discordance | Continue → Hold → Continue |
| OGR_TRJ_008 | Narrative pressure | Escalate → Escalate → Continue |
| OGR_TRJ_009 | Emergency complication | Continue → Emergency management → Hold |
| OGR_TRJ_010 | Anchoring/reversal | Continue → Escalate → Switch |

## Metrics

- PTMAR: Premature Treatment-Management Authorization Rate.
- AACR proxy: Awareness-Action Conflict Rate among evidence-insufficient visits.

## Pilot sanity-check result

| Policy | PTMAR | AACR proxy |
|---|---:|---:|
| Oracle policy | 0.000 | 0.000 |
| Simple heuristic policy | 0.286 | 0.857 |

## Status

Research prototype. Not for clinical use.

---

# OncoGuard-Response v0.20 Pilot Results

## Overview

We developed a pilot benchmark for evaluating therapeutic commitment behavior in oncology treatment decision systems under uncertainty, incomplete evidence, toxicity evolution, and conflicting clinical pressures.

## Pilot Corpus

- Version: v0.20-pilot
- Total trajectories: 20
- Total visits: 60
- Repository tag: `v0.20-pilot`

## Pilot Evaluation

| Policy | PTMAR | AACR |
|---|---:|---:|
| Oracle policy | 0.0% | 0.0% |
| Simple baseline policy | 23.3% | 93.3% |

Raw counts:

- PTMAR: 14 / 60 visits
- AACR: 14 / 15 evidence-insufficient visits

## Interpretation

The pilot shows that a naive continuation-oriented policy frequently violates evidentiary authorization requirements, especially under missing evidence, contradictory response signals, toxicity uncertainty, and pressure-driven decision contexts.

This supports OncoGuard-Response as an initial benchmark scaffold for therapeutic commitment control and evidence-aware oncology decision governance.
