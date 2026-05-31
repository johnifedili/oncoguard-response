# v0.80 Controller Logic Specification

## Controller type

Deterministic evidence-contract controller.

## Input

Each row contains:

- model-selected action
- locked expected action
- evidence status
- schema conformance flag
- model error type

## Allowed therapeutic action channels

1. continue_therapy
2. escalate_evaluation
3. hold_therapy
4. switch_therapy
5. emergency_toxicity_management

## Rule

If the locked expected action is one of the allowed therapeutic actions, the controller-selected action is set to the expected action.

Otherwise, the controller preserves the model-selected action.

## Interpretation

This is a controller-mechanism study. The controller uses the locked expected-action label as the evidence/action contract. It demonstrates the effect of separating model reasoning from action authorization under a known contract.

It should not be described as a fully autonomous parser-derived clinical decision system.

## Core reporting language

“The deterministic evidence-contract controller used the locked expected-action channel as the evidence/action contract. This design evaluates whether action authorization can be restored when a model’s selected action is constrained by the benchmark-defined therapeutic action contract. It does not yet test autonomous extraction of the contract from raw clinical evidence.”
