# OncoGuard-Response v0.40/v0.50 Controller and Ablation Protocol

## Main hypothesis

An evidence-gated therapeutic authorization controller can improve oncology LLM authorization calibration by reducing over-deferral, over-holding, wrong-channel escalation, schema failure routing, and premature switching, while preserving zero premature therapy misuse and zero unsafe authorization.

## Benchmark expansion target

- 100 longitudinal oncology trajectories
- 3 visits per trajectory
- 300 visit-level authorization decisions

## Controller architecture

The v0.50 controller will include:

1. Schema validator
2. Evidence-status gate
3. Action router

## Primary endpoint

AACR improvement from unguided model output to controller-mediated output.

## Co-primary safety endpoint

PTMAR and unsafe authorization should remain 0.0% or not increase.

## Secondary endpoints

Secondary endpoints include over-deferral reduction, over-hold reduction, over-emergency reduction, over-switch reduction, wrong-channel escalation reduction, schema failure routing, defer rate normalization, and treatment-delay risk reduction.

## Ablation arms

| Arm | Schema validator | Evidence-status gate | Action router | Purpose |
|---|---:|---:|---:|---|
| Unguided LLM | No | No | No | Baseline model behavior |
| Prompt-only | No | No | No | Tests whether instruction alone improves governance |
| Schema-only | Yes | No | No | Tests whether format control improves deployment reliability |
| Gate-only | Yes | Yes | No | Tests evidence sufficiency gating |
| Router-only | Yes | No | Yes | Tests wrong-channel correction |
| Full controller | Yes | Yes | Yes | Tests full governance system |

## Core manuscript claim if successful

The controller did not make the model more knowledgeable; it made therapeutic authorization more governable.
