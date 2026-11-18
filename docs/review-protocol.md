# Evidence and Reproducibility Review Protocol

[Main collection](../README.md) · [Comparison and evidence ledger](comparison.md) · [Research briefs](briefs/README.md)

The main collection is a broad discovery list. The comparison is a smaller, explicitly reviewed selection. Inclusion in either is not an endorsement, and the reviewed selection is not a ranking. The first edition covers 20 works chosen across mechanisms, specialties, and evaluation settings.

## What a review records

Each record in [data/comparison.yml](../data/comparison.yml) identifies a paper, the exact arXiv version or publisher publication date, the sources inspected, and a source-check date. It records the task, agent actions, training, evaluation setting, verified control evidence, interpretation limits, and code audit separately. A title change should update the existing work, not create a second paper.

Read the primary source before relying on an existing catalog summary. Use methods, tables, appendices, and code when the abstract cannot establish a claim. Keep “not established from inspected sources” distinct from “the paper did not do this.” The review-basis field discloses how much was inspected; an abstract-level review is not a full experimental audit.

The review asks:

- Does a controller select actions using observations, or does the system follow a fixed pipeline?
- Does a comparison keep the backbone, tools, data access, call budget, and compute comparable? Record verified controls; leave unexamined controls unknown.
- Are retrieved examples and training data separated from evaluation patients, institutions, and time periods? State the split actually checked, rather than assuming independence from a dataset name.
- Are tool execution, evidence quality, final-answer correctness, and clinical outcomes measured separately?
- What failure cases, negative controls, and costs affect interpretation? Preserve reported failures alongside gains.

These questions guide review; the first edition does not claim all five have been exhaustively audited for every paper.

## Evidence settings

Use descriptive settings instead of a single “clinical readiness” score:

| Setting | What it establishes | What it does not establish alone |
|---|---|---|
| Offline benchmark / retrospective dataset | Performance under a specified dataset and protocol | Prospective patient benefit |
| External retrospective dataset | Transfer to the reported external collection | Generalization to every hospital or scanner |
| Simulated workflow / synthetic corruption | Behavior in a controlled environment | Performance on real equipment or naturally occurring artifacts |
| Expert review of outputs | Clinician judgment of the reviewed outputs | A trial of clinician use or patient outcomes |
| Prospective workflow / patient-outcome study | Only the specific prospectively measured endpoint | Broader deployment claims beyond the study |

No work should receive the last label merely because it uses real patient images, real software, or expert grading. None of the first edition's records is labeled as a prospective patient-outcome study.

## Resource and execution states

| State | Required evidence |
|---|---|
| Author-linked resource | Paper or official project points to a resource; availability has not been checked |
| Source inspected | Public repository tree and/or README actually retrieved; record what was visible and what remains unverified |
| Download verified | A specific release or revision downloaded successfully; record URL, revision/hash, date and artifacts |
| Smoke test passed | A documented minimal command executed on a specified environment; retain logs and outputs |
| Result reproduced | A specified paper result recomputed under a recorded protocol, with metric, split, tolerance and discrepancies |

The current structured schema supports `source_inspected` and `not_established` resource states and `not_run` execution status. Add execution-log fields and validation before introducing a stronger claim. An implementation link not established in the inspected sources is not evidence that code is unavailable.

**All 20 initial reviews are independently not run.** Reading an installation command is not testing it. Inspecting a repository does not verify all weights, training data, data licenses, or third-party dependencies. Model services may also change after the check date. Model/API costs should be reported for the exact configuration and date of an actual run.

## Submitting corrections and reproductions

Use the [evidence review form](https://github.com/Nanboy-Ronan/awesome-medical-imaging-agents/issues/new?template=evidence-review.yml). Authors and independent reviewers are both welcome; identify your relationship to the work. Provide a primary-source section/table or a public repository revision for each factual correction.

For execution evidence, include hardware/OS, dependency versions, model revision, input source and split, exact command, random seed where applicable, expected and observed output, elapsed time and cost, and a public log or artifact. Use synthetic or appropriately licensed public examples; do not attach patient identifiers, private clinical records, credentials, or restricted datasets.

To update a record, edit `data/comparison.yml`, then run:

```sh
python scripts/generate_comparison.py
python scripts/generate_comparison.py --check
```

A reviewer should recheck the changed claim and its source before merging. Keep the correction attributable through the pull-request history. Update `checked_at` only when a source was actually checked; generation alone is not a new review.

## Brief selection

A monthly brief selects five readings with a concrete contribution, a limitation, and a relationship to other work. Clearly mark editorial interpretation. An issue can include older work when it supplies an important control or conceptual comparison; do not imply every selection was published in the issue month. State the coverage cutoff and retain past issues rather than replacing them.
