# OncoGuard-Response v0.21 Multi-Policy Evaluation Scaffold

This folder defines the v0.21 multi-policy evaluation scaffold.

## Baseline reference

Frozen baseline: v0.20-pilot

- Visits: 60
- PTMAR: 23.3%
- AACR: 93.3%
- PTMAR-positive failures: 14

## Policy families

1. Permissive policy
   - Authorizes continuation unless an explicit hard-stop exists.
   - Expected behavior: lower deferral, higher risk of unsafe authorization.

2. Standard policy
   - Requires stated authorization conditions to be satisfied.
   - Expected behavior: balanced safety and continuation.

3. Conservative policy
   - Defers when evidence is missing, contradictory, or toxicity assessment is incomplete.
   - Expected behavior: lower unsafe authorization, higher deferral.

## Current status

This is a scaffold. Policy-specific scoring logic will be connected after confirming the visit-level output columns available from the v0.20 evaluation runner.
