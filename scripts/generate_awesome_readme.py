#!/usr/bin/env python3
"""Generate a strict Awesome-list README from data/papers.yml."""

from __future__ import annotations

from collections import defaultdict
from datetime import date
from pathlib import Path
import re

import yaml


DOMAIN_ORDER = [
    "Radiology",
    "Survey · Radiology",
    "Pathology",
    "Ultrasound",
    "Endoscopy",
    "Ophthalmology",
    "3D Imaging",
    "Segmentation",
    "Report Generation",
    "Medical VLM",
    "Multimodal",
    "Clinical Reasoning",
    "Workflow Simulation",
    "Benchmark",
    "Benchmark · Radiology",
    "Survey",
]

SECTION_HEADINGS = {
    "Radiology": "Radiology Agents",
    "Survey · Radiology": "Radiology Surveys",
    "Pathology": "Pathology Agents",
    "Ultrasound": "Ultrasound Agents",
    "Endoscopy": "Endoscopy and Surgical Imaging Agents",
    "Ophthalmology": "Ophthalmology Agents",
    "3D Imaging": "3D CT, MRI, and Volumetric Imaging Agents",
    "Segmentation": "Segmentation and Annotation Agents",
    "Report Generation": "Report Generation Agents",
    "Medical VLM": "Medical Vision-Language Model Agents",
    "Multimodal": "Multimodal Medical Agents",
    "Clinical Reasoning": "Clinical Reasoning Agents",
    "Workflow Simulation": "Workflow and Simulation Agents",
    "Benchmark": "Benchmarks and Evaluation",
    "Benchmark · Radiology": "Radiology Benchmarks",
    "Survey": "Surveys and Position Papers",
}

SECTION_DESCRIPTIONS = {
    "Radiology": "Agents for chest X-ray, CT, MRI, DICOM workflows, radiotherapy planning, and radiology decision support.",
    "Survey · Radiology": "Survey papers that map agent design patterns, evaluation protocols, and open challenges in radiology.",
    "Pathology": "Agents for whole-slide image analysis, digital pathology, pathology reports, and slide navigation.",
    "Ultrasound": "Agents for echocardiography interpretation, fetal ultrasound, robotic scanning, and ultrasound-guided workflows.",
    "Endoscopy": "Agents for gastrointestinal endoscopy, surgical scene understanding, and autonomous endoscopic navigation.",
    "Ophthalmology": "Agents for fundus, OCT, glaucoma, diabetic retinopathy, myopia, and neuro-ophthalmic decision support.",
    "3D Imaging": "Agents for volumetric CT, MRI, PET, dosimetry, neuroimaging, and multi-organ image analysis.",
    "Segmentation": "Agents that plan, prompt, refine, or evaluate segmentation and annotation workflows.",
    "Report Generation": "Agents focused on automated imaging report drafting, refinement, evaluation, and quality control.",
    "Medical VLM": "Vision-language agents that combine imaging encoders, language models, tools, and clinical reasoning.",
    "Multimodal": "Agents that combine imaging with clinical text, labs, EHRs, or other patient data.",
    "Clinical Reasoning": "Agents for diagnosis, differential reasoning, treatment planning, retrieval, and clinical decision support.",
    "Workflow Simulation": "Agents and environments for clinical workflow automation, simulation, and operational task execution.",
    "Benchmark": "Benchmarks, datasets, simulators, and evaluation frameworks for medical and imaging agents.",
    "Benchmark · Radiology": "Radiology-specific benchmarks for viewer navigation, tool use, and image-grounded reasoning.",
    "Survey": "Surveys and position papers on medical AI agents, evaluation, safety, and deployment.",
}


def slugify(text: str) -> str:
    text = text.lower().replace("·", "")
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text


def normalize_sentence(text: str) -> str:
    text = " ".join(str(text).split())
    if not text:
        return ""
    text = text[0].upper() + text[1:]
    if text[-1] not in ".!?":
        text += "."
    return text


def entry_url(entry: dict) -> str | None:
    for field in ("paper_url", "project_url", "code_url", "dataset_url", "benchmark_url"):
        if entry.get(field):
            return entry[field]
    return None


def sort_key(entry: dict) -> tuple[int, str]:
    return (-int(entry.get("year") or 0), entry["title"].casefold())


def render_entry(entry: dict) -> str:
    title = entry["title"]
    url = entry_url(entry)
    venue = entry.get("venue") or "Publication"
    year = entry.get("year")
    summary = normalize_sentence(entry.get("summary") or "")
    description = f"Published in {venue} ({year})."
    if summary:
        description += f" {summary}"
    if url:
        return f"- [{title}]({url}) - {description}"
    return f"- {title} - {description}"


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    data = yaml.safe_load((root / "data" / "papers.yml").read_text())
    groups: dict[str, list[dict]] = defaultdict(list)
    seen_urls: set[str] = set()

    for entry in data["papers"]:
        url = entry_url(entry)
        if url and url in seen_urls:
            continue
        if url:
            seen_urls.add(url)
        groups[entry["domain"]].append(entry)

    ordered_domains = [domain for domain in DOMAIN_ORDER if groups.get(domain)]
    total_entries = sum(len(groups[domain]) for domain in ordered_domains)

    lines = [
        "# Awesome Medical Imaging Agents [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        "> Agentic AI systems for medical image analysis, including radiology agents, pathology agents, ultrasound agents, surgical imaging agents, segmentation agents, and medical vision-language model agents.",
        "",
        "This repository curates research papers, benchmarks, datasets, and open-source systems for medical imaging agents. It focuses on tool use, retrieval-augmented generation, multi-agent collaboration, planning, segmentation, report generation, clinical reasoning, safety, and evaluation across CT, MRI, chest X-ray, ultrasound, pathology, endoscopy, ophthalmology, PET, and other imaging modalities.",
        "",
        "## Contents",
        "",
        "- [Taxonomy](#taxonomy)",
        "- [Scope](#scope)",
    ]

    for domain in ordered_domains:
        heading = SECTION_HEADINGS[domain]
        lines.append(f"- [{heading}](#{slugify(heading)})")

    lines.extend(
        [
            "",
            "## Taxonomy",
            "",
            '<a href="https://github.com/Nanboy-Ronan/awesome-medical-imaging-agents#readme"><img src="assets/medical-imaging-agents-taxonomy.svg" alt="Visual taxonomy of medical imaging agents" width="720"></a>',
            "",
            "## Scope",
            "",
            "- Medical imaging agents for radiology, pathology, ultrasound, CT, MRI, chest X-ray, dermatology, endoscopy, PET, ophthalmology, and cardiac imaging.",
            "- Agent workflows for tool use, retrieval-augmented generation, multi-agent collaboration, self-reflection, planning, report generation, quality control, and human-in-the-loop review.",
            "- Research resources including peer-reviewed papers, arXiv preprints, benchmarks, datasets, reproducible code, and related open-source systems.",
            "- Safety and evaluation work on hallucination detection, fairness, robustness, uncertainty, abstention, privacy, and clinically grounded evaluation.",
            "",
        ]
    )

    for domain in ordered_domains:
        heading = SECTION_HEADINGS[domain]
        entries = sorted(groups[domain], key=sort_key)
        lines.extend(
            [
                f"## {heading}",
                "",
                SECTION_DESCRIPTIONS[domain],
                "",
            ]
        )
        lines.extend(render_entry(entry) for entry in entries)
        lines.append("")

    lines.extend(
        [
            "## Footnotes",
            "",
            f"- Structured metadata for this list is maintained in [data/papers.yml](data/papers.yml).",
            f"- A machine-readable table view is available in [docs/papers.json](docs/papers.json).",
            f"- Last updated: {date.today().isoformat()}.",
            "",
            "## Contributing",
            "",
            "Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.",
            "",
        ]
    )

    (root / "README.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
