# Classification Guide

[Back to the main list](../README.md#taxonomy) · [Browse themes](themes.md)

This is an editorial taxonomy for this collection. It separates application, task, mechanism, and evaluation so that a paper can be found from several perspectives without duplicating its full description.

## 1. Application and input — where is it used?

Use the clinical setting to describe the application and `modality` to describe the input. These are separate properties: ultrasound is used in several specialties, while radiology covers several modalities.

| Application | Typical inputs | Main-list location |
|---|---|---|
| Radiology and image-guided treatment | CXR, CT, MRI, mammography, PET, angiography | [Radiology](../README.md#radiology-agents-57) |
| Computational pathology | Whole-slide images, tissue tiles, microscopy | [Pathology](../README.md#pathology-agents-whole-slide-imaging--digital-pathology-41) |
| Ultrasound and echocardiography | Still images, cine loops, probe observations | [Ultrasound](../README.md#ultrasound-agents-echocardiography--robotic-ultrasound-29) |
| Endoscopy and surgery | Endoscopic video, surgical scenes, robot observations | [Endoscopy and surgery](../README.md#endoscopy-and-surgical-imaging-agents-28) |
| Ophthalmology | Fundus images, OCT, ophthalmic video | [Ophthalmology](../README.md#ophthalmology-agents-16) |
| Other or multiple specialties | For example, dermatology or combined imaging and clinical records | Use the closest existing section and record the actual modalities; do not force a specialty assignment |

**3D/volumetric** describes an input representation, and **medical VLM** describes a model interface. Their existing sections provide useful entry points, but neither is a separate clinical specialty. A VLM belongs in the agent collection only when the work demonstrates agent behavior.

## 2. Clinical task — what does it do?

Record the clinical objective separately from the mechanism used to accomplish it. Multiple tasks can apply to an end-to-end system.

| Task family | Inclusion rule | Where to start |
|---|---|---|
| Acquisition, navigation, and preparation | Select acquisition protocols or views; control probes or instruments; prepare imaging data | Radiology, ultrasound, surgery, and 3D imaging sections |
| Diagnosis and visual reasoning | Answer image-grounded questions, combine findings, form differential diagnoses, or triage cases | Specialty sections and clinical reasoning |
| Segmentation, localization, and annotation | Produce or refine masks, landmarks, regions, or annotation prompts | Segmentation and annotation; specialty sections |
| Reporting and communication | Draft, structure, compare, or check imaging reports | Report generation and radiology |
| Treatment planning and intervention | Plan or refine radiotherapy, procedures, or image-guided actions | Radiology and surgery |
| Workflow, simulation, and discovery | Coordinate care/research steps, simulate clinical interactions, or support education | Workflow and simulation; agent skills |

“Tool use,” “RAG,” and “multi-agent collaboration” explain how a task is performed. Record them as mechanisms even when older metadata also includes them in `task`.

## 3. Agent mechanism — how does it operate?

These are overlapping labels. Assign a mechanism only when the paper or released implementation supports it; the word “agent” in the title is insufficient.

| Mechanism | Evidence to look for | Existing metadata / index |
|---|---|---|
| Tool use and planning | A controller selects operations, calls tools, or adapts the next action to observations | `agent_type: tool-using`; agent skills and tool learning |
| Retrieval-augmented reasoning | Retrieval of cases, documents, or knowledge informs the workflow | `agent_type: RAG` or `tags: RAG`; [retrieval index](themes.md#agent-mechanisms) |
| Multi-agent collaboration | Distinct roles exchange information or coordinate decisions | `agent_type: multi-agent` or `tags: multi-agent`; themes index |
| Reinforcement learning | A reward-based learning objective trains an action policy or agent behavior | `agent_type: RL-trained` or `tags: reinforcement-learning`; themes index |
| Human-in-the-loop | Clinician feedback, corrections, review, or escalation forms part of the workflow | `tags: human-in-the-loop`; themes index |
| Memory and self-improvement | Stored experience, reusable skills, or an explicit update loop changes subsequent behavior | `tags: self-evolving` / `self-improving` when supported; themes index |

Ordinary context retention alone does not establish self-improvement. Several models combined in a fixed ensemble do not automatically establish multi-agent collaboration. Reinforcement learning can train a non-LLM agent, and an agent can operate without reinforcement learning.

## 4. Evaluation and resources — how is it assessed or reused?

Separate the **resource type** from the **property evaluated**. A benchmark can evaluate tool use, hallucinations, fairness, or several of these together.

| Dimension | Categories | What to record |
|---|---|---|
| Resource type | Agent system; benchmark/environment; dataset; toolbox; foundation model; survey/position paper | The work's primary contribution and direct paper/code/data links |
| Evaluation target | Final output; intermediate actions and evidence; complete workflow | What is scored, the comparator, and whether evaluation is retrospective, simulated, or prospective when reported |
| Trustworthiness | Hallucination/reliability; uncertainty/abstention; safety/robustness; fairness; privacy | Explicitly studied properties, rather than assumed clinical readiness |

Use [Benchmarks and Evaluation](../README.md#benchmarks-and-evaluation) for evaluation resources, [themes](themes.md#trustworthiness) for overlapping properties, and the separate [datasets](datasets.md) and [foundation models](foundation-models.md) pages for supporting resources. Publication venue and benchmark performance do not by themselves demonstrate clinical deployment readiness.

## Choosing a primary home

1. **Identify the contribution type.** Put benchmark-led papers in Benchmark Papers, surveys in Surveys and Position Papers, and safety-audit-led papers in Safety, Robustness, and Fairness. A system that merely introduces an evaluation dataset can stay with its application.
2. **For an agent system, identify the central contribution.** Use a specialty section when the clinical setting defines the work. Use a task or representation section when the contribution centers on segmentation, reporting, volumetric interaction, or general multimodal imaging. Use the framework sections for broader reasoning, workflow, or reusable agent skills.
3. **If two sections fit, choose the main research question.** A CT reporting system can live in radiology when CT interpretation is central, or in reporting when report construction and verification are central. Record the other aspects in metadata and cross-references.
4. **Keep one full paper description.** Start Here, benchmark overview tables, toolboxes, and theme links are navigation views. They may reference the same work. Their counts must not be added to estimate unique papers.
5. **Preserve uncertainty.** Use `null` for unknown metadata. Do not infer an agent architecture from a specialty, a title keyword, or a backbone model.

This organization preserves existing paper placements. It does not claim that every legacy entry has been individually reassessed against these rules.

## Worked examples from the collection

The following examples illustrate classification using the collection's existing descriptions. They are not rankings or new assessments of the papers.

| Work | Application / input | Task | Mechanism | Primary home |
|---|---|---|---|---|
| MedRAX | Radiology / CXR | Image interpretation and reasoning | Tool use; director-worker coordination | Radiology |
| RadAgent | Radiology / CT | Interpretation and reporting | Stepwise tool use | Radiology |
| EndoAgent | Endoscopy | Vision-to-decision reasoning | Memory; reflection | Endoscopy and surgery |
| MedSAM-Agent | Medical imaging / interactive segmentation | Mask refinement | Multi-turn agentic reinforcement learning | Segmentation and annotation |
| MMedAgent | Multiple imaging modalities | Select and execute medical tools | Tool use | Medical VLM |
| ABRA | Radiology / DICOM viewer | Evaluate viewer-based agent workflows | Benchmark rather than a mechanism label | Benchmark Papers |
| MedSAM3 | Medical images and video | Prompted segmentation | Supporting foundation model | Foundation models page |

## Maintaining the classification

The README is maintained by hand. `data/papers.yml` stores structured metadata, while `scripts/update_themes.py` combines explicit YAML tags with keyword matches from tracked README sections to generate `docs/themes.md`. The themes index is a discovery aid; keyword matches need editorial review and are not authoritative architecture annotations.

The existing `domain` field is a **primary collection section**, not a pure clinical-specialty field: it includes values such as `Segmentation`, `Medical VLM`, and `Benchmark`. Keep those values compatible with current generators. Use `modality` for inputs, `task` for objectives, `agent_type` for architectures, and `tags` for cross-cutting properties.

When adding a paper, update its primary README section and structured metadata together, adjust that section's count and count-based links, then run:

```sh
python scripts/generate_readme.py --validate-only
python scripts/validate_counts.py
python scripts/update_themes.py
```

The schema and themes commands require PyYAML. `generate_readme.py` validates metadata or produces a separate structured index; it does not rebuild the hand-maintained README.
