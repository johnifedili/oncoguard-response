## Figure and Table Plan

### Main Figures

1. Unguided AACR by model.
2. Unguided wrong-channel rate by model.
3. Controller before/after AACR across models.
4. Model-specific error phenotypes.
5. Controller intervention phenotypes.
6. Expected-vs-selected heatmaps by model.

### Main Tables

1. Three-model unguided comparison.
2. Three-model controller before/after comparison.
3. Error phenotype comparison.
4. Controller intervention comparison.
5. Paired correctness tests.

### Supplementary Tables

1. Expected-vs-selected matrices by model.
2. Full endpoint definitions.
3. Model registry and API provenance.
4. File hash manifest.
5. Controller intervention audit logs.
6. Prompt lineage and cue-repair history.

---

## Data Availability

The benchmark artifacts, scored outputs, controller outputs, tables, figures, and provenance files are maintained in the `oncoguard-response` repository. The primary hard prompt set is `results/v0_66d_targeted_actioncue_repair/v0_66d_model_testing_allowed_hard_prompts.csv`. The three-model synthesis is locked at v0.77, and the methods/provenance supplement is locked at v0.80.

## Code Availability

Evaluation, scoring, controller, synthesis, manuscript scaffold, and provenance-generation scripts are maintained in the repository. Script hashes and primary file SHA256 values are provided in the v0.80 methods/provenance supplement.

## Ethics Statement

This study used synthetic benchmark prompts and did not involve patient data, human subjects, or clinical deployment. The results should not be interpreted as evidence of safety for real-world patient care.

## Author Contributions

Chijioke John Ifedili conceptualized the study, designed the benchmark, developed the evaluation and controller framework, conducted the analyses, interpreted the results, and drafted the manuscript scaffold.

## Funding

No external funding is reported for this draft unless otherwise specified.

## Competing Interests

The author declares no competing interests unless otherwise specified.

## Acknowledgments

The author acknowledges the use of language-model assistance for drafting, coding support, and iterative manuscript development. All scientific framing, benchmark design decisions, and final interpretations remain the responsibility of the author.
