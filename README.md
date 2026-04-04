# Awesome Agents in Medicine [![Awesome Lists](https://srv-cdn.himpfen.io/badges/awesome-lists/awesomelists-flat.svg)](https://github.com/awesomelistsio/awesome)

[![Maintenance](https://img.shields.io/badge/Maintained%3F-YES-green.svg)](https://github.com/Nanboy-Ronan/awesome-agents-in-medicine/graphs/commit-activity)
![PR Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
![ ](https://img.shields.io/github/last-commit/Nanboy-Ronan/awesome-agents-in-medicine)
[![GitHub stars](https://img.shields.io/github/stars/Nanboy-Ronan/awesome-agents-in-medicine?color=blue&style=plastic)](https://github.com/Nanboy-Ronan/awesome-agents-in-medicine/stargazers)
[![GitHub watchers](https://img.shields.io/github/watchers/Nanboy-Ronan/awesome-agents-in-medicine?color=yellow&style=plastic)](https://github.com/Nanboy-Ronan/awesome-agents-in-medicine)
[![GitHub forks](https://img.shields.io/github/forks/Nanboy-Ronan/awesome-agents-in-medicine?color=red&style=plastic)](https://github.com/Nanboy-Ronan/awesome-agents-in-medicine/network/members)
[![GitHub Contributors](https://img.shields.io/github/contributors/Nanboy-Ronan/awesome-agents-in-medicine?color=green&style=plastic)](https://github.com/Nanboy-Ronan/awesome-agents-in-medicine/graphs/contributors)

> A curated academic list of AI agents in medicine.
>
> Last updated: 2026-04-04

## Table of Contents

- [Awesome Agents in Medicine Paper List :page_with_curl:](#paper-list)
  - [Surveys & Perspectives](#surveys--perspectives)
  - [Clinical QA & Knowledge Agents](#clinical-qa--knowledge-agents)
  - [Workflow & Simulation Agents](#workflow--simulation-agents)
  - [Imaging & Vision Agents](#imaging--vision-agents)
  - [Multimodal Tool-Using Agents](#multimodal-tool-using-agents)
  - [Agent Skills & Tool Learning](#agent-skills--tool-learning)
  - [Foundation Models (LLM/MLLM, not agents)](#foundation-models-llmmlm-not-agents)
  - [Safety, Security & Evaluation](#safety-security--evaluation)
  - [Others](#others)
- [Benchmarks :fire:](#benchmarks)
- [Datasets :card_file_box:](#datasets)
- [Toolboxes :toolbox:](#toolboxes)
- [Related Awesome Lists :astonished:](#related-awesome-lists)
- [Contributing :wink:](#contributing)
- [License](#license)

## Paper List

### Surveys & Perspectives

- [Rethinking Health Agents: From Siloed AI to Collaborative Decision Mediators](https://arxiv.org/abs/2603.24986) — arXiv (2026). Perspective on shifting health agents from isolated assistants toward collaborative mediators embedded in real clinical decision processes.
- [Agentic AI in Healthcare & Medicine: A Seven-Dimensional Taxonomy for Empirical Evaluation of LLM-based Agents](https://arxiv.org/abs/2602.04813) — IEEE Access (2026). Taxonomy and rubric for evaluating healthcare LLM agents across seven capability dimensions.
- [The Doctor Will (Still) See You Now: On the Structural Limits of Agentic AI in Healthcare](https://arxiv.org/abs/2602.18460) — arXiv (2026). Qualitative study arguing that safety, regulation, and accountability constraints sharply limit real clinical autonomy for healthcare agents.
- [Beyond Medical Chatbots: Meddollina and the Rise of Continuous Clinical Intelligence](https://arxiv.org/abs/2601.22645) — arXiv (2026). Argues for governance-first clinical intelligence with bounded inference and principled deferral.
- [Six Interventions for the Responsible and Ethical Implementation of Medical AI Agents](https://arxiv.org/abs/2603.13743) — arXiv (2026). Outlines governance and ethics interventions for deploying medical AI agents responsibly.
- [A Survey of LLM-based Agents in Medicine: How far are we from Baymax?](https://arxiv.org/pdf/2502.11211) — arXiv (2025). Comprehensive review of how LLM-based agents are reshaping diagnostics, imaging, and virtual care workflows.
- [LLM-Based Agents for Tool Learning: A Survey](https://link.springer.com/article/10.1007/s41019-025-00296-9) — Data Science and Engineering (2025). Broad survey of tool-learning agents, including a biomedical section that highlights clinical tool use.
- [Towards Next-Generation Medical Agent: How o1 is Reshaping Decision-Making in Medical Scenarios](https://arxiv.org/abs/2411.14461) — arXiv (2024). Perspective on integrating frontier reasoning models into clinician workflows.
- [Adaptive Reasoning and Acting in Medical Language Agents](https://arxiv.org/abs/2410.10020) — arXiv (2024). Discusses design patterns for agents that plan, critique, and self-improve in clinical tasks.
- [Agentic Systems in Radiology: Design, Applications, Evaluation, and Challenges](https://arxiv.org/pdf/2510.09404v2) — arXiv (2025). Survey of agent patterns tailored to radiology pipelines and how to evaluate them in practice.
- [Beyond Chatbots: Moving Toward Multistep Modular AI Agents in Medical Education](https://mededu.jmir.org/2025/1/e76661/) — JMIR Medical Education (2025). Viewpoint advocating modular, multistep agent pipelines for clinical teaching workflows.

### Clinical QA & Knowledge Agents

- [Within the MDT Room: Situated in Multidisciplinary Team-Grounded Agent Debate for Clinical Diagnosis](https://arxiv.org/abs/2603.28393) — arXiv (2026). Frames rare-disease diagnosis as a multidisciplinary team debate grounded in situated clinical evidence.
- [Improving Clinical Diagnosis with Counterfactual Multi-Agent Reasoning](https://arxiv.org/abs/2603.27820) — arXiv (2026). Uses counterfactual critique across agents to test competing diagnostic hypotheses before commitment.
- [From Physician Expertise to Clinical Agents: Preserving, Standardizing, and Scaling Physicians' Medical Expertise with Lightweight LLM](https://arxiv.org/abs/2603.23520) — arXiv (2026). Encodes expert physician diagnostic and therapeutic styles into a lightweight model to standardize and scale case-dependent clinical reasoning.
- [PubMed Reasoner: Dynamic Reasoning-based Retrieval for Evidence-Grounded Biomedical Question Answering](https://arxiv.org/abs/2603.27335) — arXiv (2026). Couples iterative retrieval with reasoning to produce evidence-grounded biomedical answers from current literature.
- [MediHive: A Decentralized Agent Collective for Medical Reasoning](https://arxiv.org/abs/2603.27150) — arXiv (2026). Decentralized specialist agents collaborate on complex medical reasoning while exposing uncertainty and disagreement.
- [ClinicalAgents: Multi-Agent Orchestration for Clinical Decision Making with Dual-Memory](https://arxiv.org/abs/2603.26182) — arXiv (2026). Adds short- and long-term memory modules to improve multi-step clinical decision making.
- [SkinGPT-X: A Self-Evolving Collaborative Multi-Agent System for Transparent and Trustworthy Dermatological Diagnosis](https://arxiv.org/abs/2603.26122) — arXiv (2026). Collaborative dermatology agents iteratively refine diagnoses and explanations for transparent skin-condition assessment.
- [GSEM: Graph-based Self-Evolving Memory for Experience Augmented Clinical Reasoning](https://arxiv.org/abs/2603.22096) — arXiv (2026). Organizes prior clinical experiences as a graph memory to support retrieval and adaptation during reasoning.
- [Agentic Cognitive Profiling: Realigning Automated Alzheimer's Disease Detection with Clinical Construct Validity](https://arxiv.org/abs/2603.17392) — arXiv (2026). Reframes Alzheimer's screening as an agentic cognitive profiling workflow designed to better match clinical constructs.
- [MedCoRAG: Interpretable Hepatology Diagnosis via Hybrid Evidence Retrieval and Multispecialty Consensus](https://arxiv.org/abs/2603.05129) — arXiv (2026). Evidence-grounded hepatology diagnosis agent that fuses hybrid retrieval with multispecialty consensus.
- [MedCollab: Causal-Driven Multi-Agent Collaboration for Full-Cycle Clinical Diagnosis via IBIS-Structured Argumentation](https://arxiv.org/abs/2603.01131) — arXiv (2026). Multi-agent diagnostic workflow that structures debate as causal arguments across the full clinical cycle.
- [HypAgent: A Hypothesis-Driven LLM Agent for Clinical Phenotyping and Prediction from EHR Data](https://arxiv.org/abs/2602.16378) — arXiv (2026). Hypothesis-first agent pipeline for EHR phenotyping and downstream risk prediction.
- [Closing Reasoning Gaps in Clinical Agents with Differential Reasoning Learning](https://arxiv.org/abs/2602.09945) — arXiv (2026). Learns from discrepancies between agent reasoning and reference rationales, then retrieves targeted instructions to patch likely logic gaps at inference time.
- [CoMMa: Contribution-Aware Medical Multi-Agents From A Game-Theoretic Perspective](https://arxiv.org/abs/2602.09159) — arXiv (2026). Decentralized specialist agents estimate marginal evidence contribution to produce more stable and interpretable oncology decisions.
- [MedClarify: An information-seeking AI agent for medical diagnosis with case-specific follow-up questions](https://arxiv.org/abs/2602.17308) — arXiv (2026). Diagnostic agent that asks targeted follow-up questions to reduce ambiguity before final recommendations.
- [EHRNavigator: A Multi-Agent System for Patient-Level Clinical Question Answering over Heterogeneous Electronic Health Records](https://arxiv.org/abs/2601.10020) — arXiv (2026). Multi-agent QA system that navigates heterogeneous EHR sources to answer patient-level clinical questions.
- [AgenticSum: An Agentic Inference-Time Framework for Faithful Clinical Text Summarization](https://arxiv.org/abs/2602.20040) — arXiv (2026). Multi-step clinical summarization pipeline designed to improve faithfulness and preserve source-grounded facts.
- [Agent-Based Large Language Model System for Extracting Structured Data from Breast Cancer Synoptic Reports: A Dual-Validation Study](https://www.medrxiv.org/content/10.1101/2025.11.25.25340989v1) — MedRxiv (2025). Agentic LLM pipeline for structured extraction from breast cancer synoptic reports with dual validation.
- [ClinNoteAgents: An LLM Multi-Agent System for Predicting and Interpreting Heart Failure 30-Day Readmission from Clinical Notes](https://arxiv.org/abs/2512.07081) — arXiv (2025). Multi-agent clinical note understanding for HF readmission risk and interpretation.
- [Multi-agent Self-triage System with Medical Flowcharts](https://arxiv.org/abs/2511.12439) — arXiv (2025). Retrieval, decision, and chat agents guide patient self-triage via validated flowcharts.
- [ChatMyopia: An AI Agent for Pre-consultation Education in Primary Eye Care Settings](https://arxiv.org/abs/2507.19498) — arXiv (2025). Pre-consultation education agent that integrates image tools and RAG for myopia counseling.
- [SOLVE-Med: Specialized Orchestration for Leading Vertical Experts across Medical Specialties](https://arxiv.org/abs/2511.03542) — arXiv (2025). Router-and-orchestrator agents coordinate domain-specialist models for medical QA.
- [Agentic memory-augmented retrieval and evidence grounding for medical question-answering tasks](https://www.medrxiv.org/content/10.1101/2025.08.06.25333160v1) — MedRxiv (2025). Couples tool-augmented recall with long-horizon QA to reduce hallucinations.
- [RadioRAG: Online Retrieval-augmented Generation for Radiology Question Answering](https://arxiv.org/abs/2407.15621) — arXiv (2024). Streaming RAG agent that keeps pulling prior studies and reports while answering radiology questions.
- [Bridging Clinical Narratives and ACR Appropriateness Guidelines: A Multi-Agent RAG System for Medical Imaging Decisions](https://arxiv.org/abs/2510.04969) — arXiv (2025). Maps free-text clinical context to imaging guideline recommendations with multi-agent retrieval and reasoning.
- [MedAgents: Large Language Models as Collaborators for Zero-shot Medical Reasoning](https://aclanthology.org/2024.findings-acl.33.pdf) — Findings of ACL (2024). Introduces collaborating LLM roles for differential diagnosis.
- [DoctorAgent-RL: A Multi-Agent Collaborative Reinforcement Learning System for Multi-Turn Clinical Dialogue](https://arxiv.org/abs/2505.19630) — arXiv (2025). RL-trained doctor and patient agents for multi-turn clinical consultations.
- [DeepRare: A Rare Disease Diagnosis Agentic System Powered by LLMs](https://arxiv.org/abs/2506.20430) — arXiv (2025). Multi-agent rare-disease diagnosis with tool use and evidence-linked reasoning.
- [HARMON-E: Hierarchical Agentic Reasoning for Multimodal Oncology Notes to Extract Structured Data](http://arxiv.org/abs/2512.19864v2) — arXiv (2025). Cascaded agents turn free-text oncology encounters into structured registries with validator feedback.
- [Mapis: A Knowledge-Graph Grounded Multi-Agent Framework for Evidence-Based PCOS Diagnosis](http://arxiv.org/abs/2512.15398v1) — arXiv (2025). Agents route KG lookups, case comparison, and critique to support difficult endocrine diagnoses.
- [MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making](https://proceedings.neurips.cc/paper_files/paper/2024/file/90d1fc07f46e31387978b88e7e057a31-Paper-Conference.pdf) — NeurIPS (2024). Uses self-reflection and role specialization to step through treatment decisions.
- [Agentic Medical Knowledge Graphs Enhance Medical Question Answering: Bridging the Gap Between LLMs and Evolving Medical Knowledge](http://arxiv.org/abs/2502.13010) — arXiv (2025). Grounds agents in dynamic knowledge graphs for up-to-date recommendations.
- [KERAP: A Knowledge-Enhanced Reasoning Approach for Accurate Zero-shot Diagnosis Prediction Using Multi-agent LLMs](https://arxiv.org/abs/2507.02773) — arXiv (2025). Hierarchical agents blend retrieval-augmented prompts with structured reasoning for rare cases.
- [MedAide: Information Fusion and Anatomy of Medical Intents via LLM-based Agent Collaboration](http://arxiv.org/abs/2410.12532) — arXiv (2024). Decomposes physician intents into coordinated agent subtasks.
- [Multi Agent based Medical Assistant for Edge Devices](http://arxiv.org/abs/2503.05397) — arXiv (2025). Lightweight cooperating agents for remote/edge clinical deployments.
- [TxAgent: An AI Agent for Therapeutic Reasoning Across a Universe of Tools](https://arxiv.org/pdf/2503.10970v1) — arXiv (2025). Tool-using agent that navigates drug facts, contraindications, and dosing rules step by step.
- [CDR-Agent: Intelligent Selection and Execution of Clinical Decision Rules Using Large Language Model Agents](https://arxiv.org/pdf/2505.23055v1) — arXiv (2025). Agent coordinates retrieval and rule execution to surface guideline-backed recommendations.
- [OEMA: Ontology-Enhanced Multi-Agent Collaboration Framework for Zero-Shot Clinical Named Entity Recognition](https://arxiv.org/pdf/2511.15211v2) — arXiv (2025). Uses planner-critic agents grounded in medical ontologies for accurate NER on EHR notes.

### Workflow & Simulation Agents

- [Symphony for Medical Coding: A Next-Generation Agentic System for Scalable and Explainable Medical Coding](https://arxiv.org/abs/2603.29709) — arXiv (2026). Multi-agent coding workflow for scalable ICD-style coding with explicit rationale and validation steps.
- [CarePilot: A Multi-Agent Framework for Long-Horizon Computer Task Automation in Healthcare](https://arxiv.org/abs/2603.24157) — arXiv (2026). Targets long-horizon healthcare desktop workflows such as navigation, documentation, and task completion across software systems.
- [Can LLM Agents Generate Real-World Evidence? Evaluating Observational Studies in Medical Databases](https://arxiv.org/abs/2603.22767) — arXiv (2026). Evaluates whether agents can execute end-to-end observational study workflows over medical databases.
- [OpenHospital: A Thing-in-itself Arena for Evolving and Benchmarking LLM-based Collective Intelligence](https://arxiv.org/abs/2603.14771) — arXiv (2026). Introduces a hospital-style arena for evolving and benchmarking collaborative medical agent systems.
- [When OpenClaw Meets Hospital: Toward an Agentic Operating System for Dynamic Clinical Workflows](https://arxiv.org/abs/2603.11721) — arXiv (2026). Proposes an agentic operating system for hospital workflows that coordinates documentation, tool use, and adaptive task execution.
- [Empowering Locally Deployable Medical Agent via State Enhanced Logical Skills for FHIR-based Clinical Tasks](https://arxiv.org/abs/2603.06902) — arXiv (2026). Training-free logical-skill memory improves privacy-preserving local agents on FHIR-based clinical information system tasks.
- [A Multi-Agent Framework for Interpreting Multivariate Physiological Time Series](https://arxiv.org/abs/2603.04142) — arXiv (2026). Coordinates specialized agents to interpret multivariate physiological signals for clinical decision support.
- [ClinicalReTrial: A Self-Evolving AI Agent for Clinical Trial Protocol Optimization](https://arxiv.org/abs/2601.00290) — arXiv (2026). Self-improving agent that iterates on trial protocol drafts to reduce design flaws and improve feasibility.
- [Causal-Enhanced AI Agents for Medical Research Screening](https://arxiv.org/abs/2601.02814) — arXiv (2026). Agentic screening pipeline for systematic reviews that adds causal signals to reduce hallucinations.
- [DemMA: Dementia Multi-Turn Dialogue Agent with Expert-Guided Reasoning and Action Simulation](https://arxiv.org/abs/2601.06373) — arXiv (2026). Multi-turn dialogue agent that simulates dementia patient behavior for training and evaluation.
- [From Passive to Proactive: A Multi-Agent System with Dynamic Task Orchestration for Intelligent Medical Pre-Consultation](https://arxiv.org/abs/2511.01445) — arXiv (2025). Hierarchical agent orchestration for proactive triage and history collection.
- [MedTutor-R1: Socratic Personalized Medical Teaching with Multi-Agent Simulation](https://arxiv.org/abs/2512.05671) — arXiv (2025). Multi-agent pedagogical simulator and Socratic tutor for one-to-many clinical teaching.
- [Agent Hospital: A Simulacrum of Hospital with Evolvable Medical Agents](https://arxiv.org/pdf/2405.02957) — arXiv (2024). End-to-end hospital simulator with patient, clinician, and admin agents.
- [Learning to Be a Doctor: Searching for Effective Medical Agent Architectures](https://arxiv.org/abs/2504.11301) — arXiv (2025). Benchmarks agent-based curricula across simulated clinical tasks.
- [Mediator-Guided Multi-Agent Collaboration among Open-Source Models for Medical Decision-Making](http://arxiv.org/abs/2508.05996) — arXiv (2025). Introduces a mediator agent that coaches specialized LLMs through patient encounters.
- [Surgical Agent Orchestration Platform for Voice-directed Patient Data Interaction](https://arxiv.org/pdf/2511.07392v2) — arXiv (2025). Voice-first assistant that routes surgical team requests across documentation and data tools.
- [MedDCR: Learning to Design Agentic Workflows for Medical Coding](https://arxiv.org/pdf/2511.13361v1) — arXiv (2025). Trains agents to chain codebook retrieval, reasoning, and validation for ICD/DRG assignment.
- [Hybrid-Code: A Privacy-Preserving, Redundant Multi-Agent Framework for Reliable Local Clinical Coding](https://arxiv.org/abs/2512.23743) — arXiv (2025). Redundant, on-prem agents deliver resilient clinical coding while preserving patient privacy.
- [An Agentic AI Framework for Training General Practitioner Student Skills](https://arxiv.org/abs/2512.18440) — arXiv (2025). Simulated patient and tutor agents improve GP student training in virtual consultations.
- [Multi-Agent Medical Decision Consensus Matrix System: An Intelligent Collaborative Framework for Oncology MDT Consultations](http://arxiv.org/abs/2512.14321v1) — arXiv (2025). Coordinates planner, specialist, and auditor agents to reach treatment consensus in tumor boards.
- [Automated stereotactic radiosurgery planning using a human-in-the-loop reasoning large language model agent](http://arxiv.org/abs/2512.20586v1) — arXiv (2025). Planning agent drafts SRS shot plans with clinician review loops for quality and safety.

### Imaging & Vision Agents

- [AD-CARE: A Guideline-grounded, Modality-agnostic LLM Agent for Real-world Alzheimer's Disease Diagnosis with Multi-cohort Assessment, Fairness Analysis, and Reader Study](https://arxiv.org/abs/2603.25322) — arXiv (2026). Alzheimer's diagnosis agent validated across cohorts with fairness analysis and clinician reader study.
- [MedOpenClaw: Auditable Medical Imaging Agents Reasoning over Uncurated Full Studies](https://arxiv.org/abs/2603.24649) — arXiv (2026). Imaging agent framework designed to reason over full uncurated studies with auditable intermediate decisions.
- [Evolving Medical Imaging Agents via Experience-driven Self-skill Discovery](https://arxiv.org/abs/2603.05860) — arXiv (2026). Self-evolving imaging agent that discovers effective composite tool chains from successful trajectories and reuses them as new skills.
- [From Scanning Guidelines to Action: A Robotic Ultrasound Agent with LLM-Based Reasoning](https://arxiv.org/abs/2603.14393) — arXiv (2026). Turns ultrasound scanning guidelines into a reasoning-driven robotic agent for autonomous acquisition.
- [EviAgent: Evidence-Driven Agent for Radiology Report Generation](https://arxiv.org/abs/2603.13956) — arXiv (2026). Evidence-grounded radiology reporting agent that emphasizes interpretable report generation.
- [QCAgent: an agentic framework for quality-controllable pathology report generation from whole slide image](https://arxiv.org/abs/2603.01647) — arXiv (2026). Pathology reporting agent framework with explicit quality-control loops over whole-slide analysis.
- [MMNavAgent: Multi-Magnification WSI Navigation Agent for Clinically Consistent Whole-Slide Analysis](https://arxiv.org/abs/2603.02079) — arXiv (2026). Multi-magnification navigation agent that improves clinically consistent exploration of pathology slides.
- [OPGAgent: An Agent for Auditable Dental Panoramic X-ray Interpretation](https://arxiv.org/abs/2603.00462) — arXiv (2026). Dental X-ray agent with auditable reasoning traces for clinical review.
- [An Explainable Agentic AI Framework for Uncertainty-Aware and Abstention-Enabled Acute Ischemic Stroke Imaging Decisions](https://arxiv.org/abs/2601.01008) — arXiv (2026). Imaging agent that explains decisions and abstains under uncertainty for acute stroke workflows.
- [Experience-Guided Self-Adaptive Cascaded Agents for Breast Cancer Screening and Diagnosis with Reduced Biopsy Referrals](https://arxiv.org/abs/2602.23899) — arXiv (2026). Cascaded imaging agents adapt from prior cases to improve screening decisions while reducing unnecessary biopsies.
- [Route, Retrieve, Reflect, Repair: Self-Improving Agentic Framework for Visual Detection and Linguistic Reasoning in Medical Imaging](https://arxiv.org/abs/2601.08192) — arXiv (2026). Iterative vision-language agent that refines detections and rationales with retrieval and repair loops.
- [MedSAM-Agent: Empowering Interactive Medical Image Segmentation with Multi-turn Agentic Reinforcement Learning](https://arxiv.org/abs/2602.03320) — arXiv (2026). Interactive segmentation agent trained with multi-turn RL for tool orchestration.
- [CXReasonAgent: Evidence-Grounded Diagnostic Reasoning Agent for Chest X-rays](https://arxiv.org/abs/2602.23276) — arXiv (2026). Evidence-grounded chest X-ray agent that structures diagnostic reasoning around retrieved findings.
- [Which Tool Response Should I Trust? Tool-Expertise-Aware Chest X-ray Agent with Multimodal Agentic Learning](https://arxiv.org/abs/2602.21517) — arXiv (2026). Learns when to trust different tool outputs in chest X-ray workflows using expertise-aware agent collaboration.
- [MedRAX: Medical Reasoning Agent for Chest X-ray (ICML 2025)](https://arxiv.org/pdf/2502.02673v1) — arXiv (2025). Director-worker agents coordinate report generation from chest radiographs.
- [Radiologist Copilot: An Agentic Assistant with Orchestrated Tools for Radiology Reporting with Quality Control](https://arxiv.org/abs/2512.02814) — arXiv (2025). Tool-orchestrated agent drafts volumetric reports with explicit quality-control passes.
- [LungNoduleAgent: A Collaborative Multi-Agent System for Precision Diagnosis of Lung Nodules](https://arxiv.org/abs/2511.21042) — arXiv (2025). Collaborative agents analyze CT nodules and reason about malignancy.
- [A Multi-Agent System for Complex Reasoning in Radiology Visual Question Answering](https://arxiv.org/abs/2508.02841) — arXiv (2025). Coordinates specialized agents for question decomposition, visual evidence retrieval, and answer synthesis.
- [Agentic large language models improve retrieval-based radiology question answering](https://arxiv.org/abs/2508.00743) — arXiv (2025). Multi-step retrieval-and-reasoning agent (RaR) for radiology QA.
- [A Multimodal Multi-Agent Framework for Radiology Report Generation](https://arxiv.org/abs/2505.09787) — arXiv (2025). Multi-agent pipeline for chest imaging report drafting and refinement.
- [CBM-RAG: Demonstrating Enhanced Interpretability in Radiology Report Generation with Multi-Agent RAG and Concept Bottleneck Models](https://arxiv.org/abs/2504.20898) — arXiv (2025). Improves report transparency via agentic RAG plus bottleneck concepts.
- [AT-CXR: Uncertainty-Aware Agentic Triage for Chest X-rays](https://arxiv.org/abs/2508.19322) — arXiv (2025). Triage agent that defers or escalates based on calibrated uncertainty.
- [PASS: Probabilistic Agentic Supernet Sampling for Interpretable and Adaptive Chest X-Ray Reasoning](https://arxiv.org/abs/2508.10501) — arXiv (2025). Builds interpretable reasoning paths with probabilistic agent selection.
- [RadFabric: Agentic AI System with Reasoning Capability for Radiology](https://arxiv.org/abs/2506.14142) — arXiv (2025). Radiology agent blends visual grounding and text-based reasoning for CXR interpretation.
- [MAARTA: Multi-Agentic Adaptive Radiology Teaching Assistant](https://arxiv.org/abs/2506.17320) — arXiv (2025). Tutoring agents guide trainees with attention feedback and targeted remediation.
- [IMACT-CXR: An Interactive Multi-Agent Conversational Tutoring System for Chest X-Ray Interpretation](https://arxiv.org/abs/2511.15825) — arXiv (2025). Multi-agent tutor combines gaze analysis, annotation, and retrieval for CXR education.
- [CT-Agent: A Multimodal-LLM Agent for 3D CT Radiology Question Answering](https://arxiv.org/abs/2505.16229) — arXiv (2025). Slice-aware CT agent answers volumetric questions with tool calls.
- [Scan-do Attitude: Towards Autonomous CT Protocol Management using a Large Language Model Agent](https://arxiv.org/abs/2509.20270) — arXiv (2025). LLM agent configures acquisition and reconstruction protocols for CT workflows.
- [Zero-Shot Large Language Model Agents for Fully Automated Radiotherapy Treatment Planning](https://arxiv.org/abs/2510.11754) — arXiv (2025). Planning agent automates radiotherapy workflows with iterative plan refinement.
- [GMAT: Grounded Multi-Agent Clinical Description Generation for Text Encoder in Vision-Language MIL for Whole Slide Image Classification](https://arxiv.org/abs/2508.01293) — arXiv (2025). Multi-agent generation of clinical descriptions to steer WSI classification.
- [CPathAgent: An Agent-based Foundation Model for Interpretable High-Resolution Pathology Image Analysis Mimicking Pathologists' Diagnostic Logic](https://arxiv.org/abs/2505.20510) — arXiv (2025). Agentic pathology foundation model mimics diagnostic workflow for interpretability.
- [Evidence-based diagnostic reasoning with multi-agent copilot for human pathology](https://arxiv.org/abs/2506.20964) — arXiv (2025). Multi-agent copilot integrates pathology slides with evidence-based reasoning.
- [Patho-AgenticRAG: Towards Multimodal Agentic Retrieval-Augmented Generation for Pathology VLMs via Reinforcement Learning](https://arxiv.org/abs/2508.02258) — arXiv (2025). RL-trained agentic RAG reduces pathology VLM hallucinations.
- [Pathology-CoT: Learning Visual Chain-of-Thought Agent from Expert Whole Slide Image Diagnosis Behavior](https://arxiv.org/abs/2510.04587) — arXiv (2025). Learns sequential field-of-view decisions for WSI diagnosis.
- [PathFound: An Agentic Multimodal Model Activating Evidence-seeking Pathological Diagnosis](https://arxiv.org/abs/2512.23545) — arXiv (2025). Evidence-seeking pathology agent iterates between regions and findings.
- [VoxelPrompt: A Vision Agent for End-to-End Medical Image Analysis](http://arxiv.org/abs/2410.08397) — arXiv (2024). Multi-stage vision agent prompting for volumetric imaging tasks.
- [Med-VRAgent: A Framework for Medical Visual Reasoning-Enhanced Agents](http://arxiv.org/abs/2510.18424) — arXiv (2025). Couples visual question answering with tool-use planning.
- [WSI-Agents: A Collaborative Multi-Agent System for Multi-Modal Whole Slide Image Analysis (MICCAI)](https://arxiv.org/pdf/2507.14680) — arXiv (2025). Delegates slide parsing, reporting, and triaging across agents.
- [PathFinder: A Multi-Modal Multi-Agent System for Medical Diagnostic Decision-Making Applied to Histopathology](https://arxiv.org/pdf/2502.08916) — arXiv (2025). Uses planner, analyzer, and verifier agents for pathology QA.
- [CXRAgent: Director-Orchestrated Multi-Stage Reasoning for Chest X-Ray Interpretation](https://arxiv.org/abs/2510.21324) — arXiv (2025). Director agent routes tasks among radiology specialists.
- [RadAgents: Multimodal Agentic Reasoning for Chest X-ray Interpretation with Radiologist-like Workflows](https://arxiv.org/abs/2509.20490) — arXiv (2025). Emulates radiology conferences with discussion-style agents.
- [EndoAgent: A Memory-Guided Reflective Agent for Intelligent Endoscopic Vision-to-Decision Reasoning](https://arxiv.org/abs/2508.07292) — arXiv (2025). Adds episodic memory and action planning for endoscopy.
- [M^3 Builder: A Multi-agent System for Automated Machine Learning in Medical Imaging](https://link.springer.com/chapter/10.1007/978-3-032-06004-4_12) — Springer (2026). Automates imaging pipelines with planner, builder, and evaluator agents.
- [Medical AI Consensus: A Multi-Agent Framework for Radiology Report Generation and Evaluation](http://arxiv.org/abs/2509.17353) — arXiv (2025). Ensembles expert agents to reach consensus on imaging impressions.
- [Hybrid Retrieval-Generation Reinforced Agent for Medical Image Report Generation](http://arxiv.org/abs/1805.08298) — arXiv (2018). Early agent that jointly retrieves priors and drafts radiology reports.
- [PathAgent: Toward Interpretable Analysis of Whole-slide Pathology Images via Large Language Model-based Agentic Reasoning](https://arxiv.org/pdf/2511.17052v1) — arXiv (2025). Combines slide parsers with language agents to narrate lesion findings.
- [SurvAgent: Hierarchical CoT-Enhanced Case Banking and Dichotomy-Based Multi-Agent System for Multimodal Survival Prediction](https://arxiv.org/pdf/2511.16635v1) — arXiv (2025). Multimodal agents pool pathology, imaging, and clinical signals for survival analysis.
- [Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis](http://arxiv.org/abs/2512.14157v1) — arXiv (2025). Adds vision-tool reward shaping so agents decide when to call segmentation, detection, or retrieval modules.
- [Echo-CoPilot: A Multi-View, Multi-Task Agent for Echocardiography Interpretation and Reporting](http://arxiv.org/abs/2512.09944v2) — arXiv (2025). Multi-stage agent handles view selection, measurements, and report drafting for echo studies.
### Multimodal Tool-Using Agents

- [TheraAgent: Multi-Agent Framework with Self-Evolving Memory and Evidence-Calibrated Reasoning for PET Theranostics](https://arxiv.org/abs/2603.13676) — arXiv (2026). Multi-agent PET theranostics framework with case memory and trial-grounded reasoning.
- [CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework](https://arxiv.org/abs/2603.01607) — arXiv (2026). Evidence-grounded multimodal agent framework emphasizing traceability and accountable clinical reasoning.
- [Meissa: Multi-modal Medical Agentic Intelligence](https://arxiv.org/abs/2603.09018) — arXiv (2026). Lightweight offline 4B multimodal medical agent trained on structured trajectories for strategy selection and multi-step tool or multi-agent interaction.
- [MedAgent-Pro: Towards Evidence-based Multi-modal Medical Diagnosis via Reasoning Agentic Workflow](https://openreview.net/forum?id=ZOuU0udyA4) — OpenReview / ICLR 2026 Poster (2026). Integrates imaging, labs, and guidelines with explicit tool calling.
- [AURA: A Multi-Modal Medical Agent for Understanding, Reasoning & Annotation](https://arxiv.org/abs/2507.16940) — arXiv (2025). Unified multimodal agent that annotates and reasons over MRI, CT, and EHR text.
- [MMedAgent: Learning to Use Medical Tools with Multi-modal Agent](https://arxiv.org/pdf/2407.02483) — arXiv (2024). Shows how agents call segmentation, retrieval, and calculator tools on demand.
- [Inquire, Interact, and Integrate: A Proactive Agent Collaborative Framework for Zero-Shot Multimodal Medical Reasoning](http://arxiv.org/abs/2405.11640) — arXiv (2024). Planner-agent loop that interleaves questioning, evidence integration, and summarization.
- [MMedAgent-RL: Optimizing Multi-Agent Collaboration for Multimodal Medical Reasoning](https://arxiv.org/abs/2506.00555) — ICLR (2026). RL-based collaboration among GP and specialist agents for multimodal diagnosis.

### Agent Skills & Tool Learning

- [Large language model agents can use tools to perform clinical calculations](https://www.nature.com/articles/s41746-025-01475-8) — npj Digital Medicine (2025). Tool-use agents improve clinical calculator accuracy via OpenMedCalc and code-interpreter style tools.
- [AgentMD: Empowering language agents for risk prediction with large-scale clinical tool learning](https://www.nature.com/articles/s41467-025-64430-x) — Nature Communications (2025). Agent curates and selects risk calculators at scale to improve risk prediction.
- [RiskAgent: Synergizing Language Models with Validated Tools for Evidence-Based Risk Prediction](https://arxiv.org/abs/2503.03802) — arXiv (2025). Tool-using agent that collaborates with evidence-based clinical decision tools for generalist risk prediction.
- [Picking the Right Specialist: Attentive Neural Process-based Selection of Task-Specialized Models as Tools for Agentic Healthcare Systems](https://arxiv.org/abs/2602.14901) — arXiv (2026). Learns specialist-tool routing policies so healthcare agents can select the most suitable expert model per task.
- [From Agents to Governance: Essential AI Skills for Clinicians in the Large Language Model Era](https://www.jmir.org/2026/1/e86550) — JMIR (2026). Defines a tiered competency framework for clinicians supervising agentic workflows.

### Foundation Models (LLM/MLLM, not agents)

- [BioGPT: Generative Pre-trained Transformer for Biomedical Text Generation and Mining](https://arxiv.org/abs/2210.10341) — arXiv (2023) — Model (LLM). Biomedical text generation backbone often used inside downstream agent pipelines.
- [BioMedGPT: Open Multimodal Generative Pre-trained Transformer for BioMedicine](https://arxiv.org/abs/2308.09442) — arXiv (2023) — Model (MLLM). Vision-language foundation model for biomedical image/text understanding; typically wrapped by agent controllers.
- [ChatCAD+: Towards a Universal and Reliable Interactive CAD using LLMs](https://arxiv.org/abs/2305.15964) — arXiv (2023) — Model (MLLM). Interactive CAD/VQA backbone for medical imaging workflows, not an agent by itself.
- [ChatDoctor: A Medical Chat Model Fine-Tuned on a Large Language Model Meta-AI (LLaMA) Using Medical Domain Knowledge](https://arxiv.org/abs/2303.14070) — arXiv (2023) — Model (LLM). Clinical dialogue-tuned base model commonly embedded inside agent toolchains.
- [DoctorGLM: Fine-tuning your Chinese Doctor is not a Herculean Task](https://arxiv.org/abs/2304.01097) — arXiv (2023) — Model (LLM). Chinese clinical assistant model leveraged as the core reasoning engine in many agent systems.
- [MEDITRON-70B: Scaling Medical Pretraining for Large Language Models](https://arxiv.org/abs/2311.16079) — arXiv (2023) — Model (LLM). Strong medical foundation model often paired with external tools in agent workflows.
- [Med-Flamingo: a Multimodal Medical Few-shot Learner](https://arxiv.org/abs/2307.15189) — arXiv (2023) — Model (MLLM). Few-shot LVLM pretraining that agents wrap for image+text diagnostic reasoning.
- [PMC-LLaMA: Towards Building Open-source Language Models for Medicine](https://arxiv.org/abs/2304.14454) — arXiv (2023) — Model (LLM). PMC-pretrained medical LLM used as a lightweight base for agent orchestration.
- [HuatuoGPT: Towards Taming Language Model to Be a Doctor](https://arxiv.org/abs/2305.15075) — arXiv (2023) — Model (LLM). Chinese clinical dialogue and diagnosis base model used in downstream agent systems.
- [LLaVA-Med: Training a Large Language-and-Vision Assistant for Biomedicine in One Day](https://arxiv.org/abs/2306.00890) — arXiv (2023) — Model (MLLM). Rapidly trained LVLM used as a base for multimodal agents.
- [SurgicalGPT: End-to-End Language-Vision GPT for Visual Question Answering in Surgery](https://arxiv.org/abs/2304.09974) — arXiv (2023) — Model (MLLM). Surgical VQA model that can be wrapped by agent controllers.

### Safety, Security & Evaluation

- [Ablation Study of a Fairness Auditing Agentic System for Bias Mitigation in Early-Onset Colorectal Cancer Detection](https://arxiv.org/abs/2603.17179) — arXiv (2026). Evaluates an agentic auditing system that surfaces and mitigates bias in colorectal cancer detection models.
- [DUCX: Decomposing Unfairness in Tool-Using Chest X-ray Agents](https://arxiv.org/abs/2603.00777) — arXiv (2026). Audits how unfairness arises across tool selection and reasoning stages in CXR agents.
- [Emerging Cyber Attack Risks of Medical AI Agents](http://arxiv.org/abs/2504.03759) — arXiv (2025). Threat model of prompt-injection and tool-abuse pathways in clinical agents.
- [AgentsEval: Clinically Faithful Evaluation of Medical Imaging Reports via Multi-Agent Reasoning](https://arxiv.org/abs/2601.16685) — arXiv (2026). Multi-agent evaluation framework with a perturbation-based benchmark for report faithfulness.
- [Many-to-One Adversarial Consensus: Exposing Multi-Agent Collusion Risks in AI-Based Healthcare](https://arxiv.org/abs/2512.03097) — arXiv (2025). Demonstrates collusion attacks on multi-agent medical advisors and a verifier-agent defense.
- [Best Practices for Large Language Models in Radiology](https://arxiv.org/abs/2412.01233) — arXiv (2024). Practical guidance and evaluation protocols for deploying radiology-facing agents safely.
- [Agent-Based Output Drift Detection for Breast Cancer Response Prediction in a Multisite Clinical Decision Support System](https://arxiv.org/abs/2512.18450) — arXiv (2025). Uses agents to detect performance drift across sites in clinical imaging decision support.
- [Clinically Grounded Agent-based Report Evaluation: An Interpretable Metric for Radiology Report Generation](https://arxiv.org/abs/2508.02808) — arXiv (2025). Agent-based metric for clinically grounded evaluation of radiology report quality.
- [Medical Imaging AI Competitions Lack Fairness](https://arxiv.org/abs/2512.17581) — arXiv (2025). Highlights fairness gaps that can propagate into imaging agent pipelines.
- [Intersectional Fairness in Vision-Language Models for Medical Image Disease Classification](https://arxiv.org/abs/2512.15249) — arXiv (2025). Audits subgroup fairness for medical VLMs commonly used by imaging agents.
- [Metric Privacy in Federated Learning for Medical Imaging: Improving Convergence and Preventing Client Inference Attacks](https://arxiv.org/abs/2502.01352) — arXiv (2025). Privacy-preserving training approach for imaging models used in agent systems.
- [Impatient Users Confuse AI Agents: High-fidelity Simulations of Human Traits for Testing Agents](https://arxiv.org/abs/2510.04491) — arXiv (2025). Demonstrates how human impatience skews medical agent behavior.
- [A Multi-agent Large Language Model Framework to Automatically Assess Performance of a Clinical AI Triage Tool](https://arxiv.org/pdf/2510.26498v1) — arXiv (2025). Uses collaborating reviewer agents to audit triage tool accuracy and consistency.
- [Reasoning-Style Poisoning of LLM Agents via Stealthy Style Transfer: Process-Level Attacks and Runtime Monitoring in RSV Space](http://arxiv.org/abs/2512.14448v1) — arXiv (2025). Shows how adversaries can implant attack styles into clinical agents and monitors for distribution drift.
- [Biosecurity-Aware AI: Agentic Risk Auditing of Soft Prompt Attacks on ESM-Based Variant Predictors](http://arxiv.org/abs/2512.17146v1) — arXiv (2025). Biosecurity lens on agent pipelines that chain protein language models with planning controllers.

### Others

- [MedBeads: An Agent-Native, Immutable Data Substrate for Trustworthy Medical AI](https://arxiv.org/abs/2602.01086) — arXiv (2026). Proposes an immutable, graph-structured clinical data substrate to give medical agents deterministic and tamper-evident patient context.
- [Image-Guided Navigation of a Robotic Ultrasound Probe for Autonomous Spinal Sonography Using a Shadow-aware Dual-Agent Framework](http://arxiv.org/abs/2111.02167) — arXiv (2021). Cooperative perception-control agents for ultrasound-guided robotics.
- [Multi-agent Searching System for Medical Information](http://arxiv.org/abs/2203.12465) — arXiv (2022). Early agentic pipeline that dispatches searchers and summarizers for literature triage.

## Benchmarks :fire:

- [Doctorina MedBench: End-to-End Evaluation of Agent-Based Medical AI](https://arxiv.org/abs/2603.25821) — arXiv (2026). Simulated physician-patient benchmark for end-to-end evaluation of medical agents beyond static QA.
- [MedMASLab: A Unified Orchestration Framework for Benchmarking Multimodal Medical Multi-Agent Systems](https://arxiv.org/abs/2603.09909) — arXiv (2026). Standardized multimodal benchmark and orchestration framework spanning heterogeneous architectures, organ systems, and disease categories.
- [GAIA-Medicine: Benchmarking Large Language Models in Medical Reasoning and Diagnosis](https://arxiv.org/abs/2602.18585) — arXiv (2026). Evaluates medical reasoning and diagnosis quality across diverse clinical scenarios.
- [LiveMedBench: A Contamination-Free Medical Benchmark for LLMs with Automated Rubric Evaluation](https://arxiv.org/abs/2602.10367) — arXiv (2026). Live-style benchmark designed to reduce contamination while scoring medical outputs with automated rubrics.
- [ClinTrialBench: A Multi-Dimensional Framework to Evaluate LLMs and AI Agents in Clinical Trial Eligibility and Matching](https://arxiv.org/abs/2602.15578) — arXiv (2026). Benchmark for trial eligibility and patient-matching decisions with clinical constraints.
- [MedSage: A Comprehensive Benchmark for Assessing Medical Assistance Capabilities of Large Language Models](https://arxiv.org/abs/2602.13242) — arXiv (2026). Measures medical assistant performance across QA, reasoning, and decision-support tasks.
- [ART: Action-based Reasoning Task Benchmarking for Medical AI Agents](https://arxiv.org/abs/2601.08988) — arXiv (2026). Evaluates safe, multi-step agent reasoning over structured EHR tasks.
- [HealthBench](https://openai.com/index/healthbench/) — OpenAI (2025). Rubric-based benchmark of 5,000 multi-turn health conversations with physician-authored criteria.
- [MedAgentsBench: Benchmarking Thinking Models and Agent Frameworks for Complex Medical Reasoning](https://arxiv.org/pdf/2503.07459) — arXiv (2025). Evaluates chain-of-thought, tool-use, and collaboration on multi-turn patient cases.
- [MedAgentBoard: Benchmarking Multi-Agent Collaboration with Conventional Methods for Diverse Medical Tasks](https://arxiv.org/abs/2505.12371) — NeurIPS Datasets & Benchmarks (2025). Compares multi-agent, single-LLM, and conventional methods across text, imaging, and EHR tasks.
- [AgentClinic: a multimodal agent benchmark to evaluate AI in simulated clinical environments](https://arxiv.org/pdf/2405.07960) — arXiv (2024). Couples simulated patient avatars with radiology, pathology, and lab tools.
- [AI Hospital: Benchmarking Large Language Models in a Multi-agent Medical Interaction Simulator](https://aclanthology.org/2025.coling-main.680.pdf) — COLING (2025). Focuses on doctor-patient dialogues and operations management.
- [MedAgentBench: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents](https://arxiv.org/abs/2501.14654) — arXiv (2025). Defines longitudinal inpatient cases for reinforcement-style training.
- [MedBench v4: A Robust and Scalable Benchmark for Evaluating Chinese Medical Language Models, Multimodal Models, and Intelligent Agents](https://arxiv.org/pdf/2511.14439v2) — arXiv (2025). Large-scale multilingual benchmark spanning clinical QA, imaging, and tool-use tasks.
- [SCARE: A Benchmark for SQL Correction and Question Answerability Classification for Reliable EHR Question Answering](https://arxiv.org/pdf/2511.17559v1) — arXiv (2025). Evaluates how agents handle database-grounded clinical questions and detect unanswerable prompts.
- [LLM-Assisted Emergency Triage Benchmark: Bridging Hospital-Rich and MCI-Like Field Simulation](https://arxiv.org/abs/2509.26351) — arXiv (2025). Tests agent robustness on high-stress, time-sensitive triage scenarios with evolving patient context.
- [ReX-MLE: The Autonomous Agent Benchmark for Medical Imaging Challenges](http://arxiv.org/abs/2512.17838v1) — arXiv (2025). Measures end-to-end tool planning, execution, and reporting across varied medical imaging tasks.
- [MedInsightBench: Evaluating Medical Analytics Agents Through Multi-Step Insight Discovery in Multimodal Medical Data](http://arxiv.org/abs/2512.13297v1) — arXiv (2025). Scores how agents surface findings, evidence, and next actions over text+image+tabular cases.
- [CP-Env: Evaluating Large Language Models on Clinical Pathways in a Controllable Hospital Environment](http://arxiv.org/abs/2512.10206v2) — arXiv (2025). Hospital simulator that stresses pathway adherence, order entry, and safety guardrails for agent controllers.
- [MLB: A Scenario-Driven Benchmark for Evaluating Large Language Models in Clinical Applications](https://arxiv.org/abs/2601.06193) — arXiv (2026). Scenario-driven benchmark spanning knowledge, safety, medical records, and smart services.

## Datasets :card_file_box:

- [Stanford-BMI/MedAgentBench](https://arxiv.org/pdf/2501.14654) — Full patient trajectories, orders, and notes aligned with the MedAgentBench protocol.
- [AgentClinic](https://agentclinic.github.io/) — Multimodal simulator dumps (EHR text, imaging references, lab tables) for benchmarking AgentClinic systems.
- [vapa/MedicalAgentQA](https://huggingface.co/datasets/vapa/MedicalAgentQA) — Compact QA set targeting reasoning, evidence citation, and tool selection for medical agents.
- [HealthBench](https://openai.com/index/healthbench/) — 5,000 multi-turn physician-authored health conversations with rubric criteria for evaluation.
- [super-dainiu/medagents-benchmark](https://huggingface.co/datasets/super-dainiu/medagents-benchmark) — Hugging Face dataset for MedAgentsBench hard medical QA subsets.

## Toolboxes :toolbox:

- [gersteinlab/MedAgents](https://github.com/gersteinlab/MedAgents) — Official implementation for the MedAgents role-playing architecture and evaluation suite.
- [Wangyixinxin/MMedAgent](https://github.com/Wangyixinxin/MMedAgent) — Codebase showing multimodal tool-use (retrieval, segmentation, calculators) via controller, solver, and reviewer agents.
- [bowang-lab/MedRAX](https://github.com/bowang-lab/MedRAX) — ICML 2025 MedRAX pipeline with agent orchestration for chest X-ray reasoning.
- [Tyyds-ai/EndoAgent](https://github.com/Tyyds-ai/EndoAgent) — Long-context planner and reflective memory for endoscopy diagnosis.
- [jinlab-imvr/MedAgent-Pro](https://github.com/jinlab-imvr/MedAgent-Pro) — Evidence-grounded workflow implementation with multimodal tools and verification agent.
- [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) — Large open-source medical skill library for OpenClaw/NanoClaw, covering clinical, genomics, drug discovery, bioinformatics, and medical device workflows.
- [CUHK-AIM-Group/MedSAM-Agent](https://github.com/CUHK-AIM-Group/MedSAM-Agent) — Interactive segmentation agent with multi-turn RL and tool orchestration.
- [SamuelSchmidgall/AgentClinic](https://github.com/SamuelSchmidgall/AgentClinic) — Simulator, scoring harness, and baselines for the AgentClinic benchmark.
- [stanfordmlgroup/MedAgentBench](https://github.com/stanfordmlgroup/MedAgentBench) — Official implementation of the MedAgentBench virtual EHR benchmark.
- [openai/simple-evals](https://github.com/openai/simple-evals) — Reference eval code for HealthBench and related benchmarks.

## Related Awesome Lists

- [HealthcareAgent](https://github.com/AI-Hub-Admin/HealthcareAgent) — List of awesome AI agents for healthcare and common agentic AI API interface.
- [Awesome-AI-Agents-for-Healthcare](https://github.com/AgenticHealthAI/Awesome-AI-Agents-for-Healthcare) — Latest advances on agentic AI and AI agents for healthcare.
  
## Contributing

Contributions are welcome!

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/)
