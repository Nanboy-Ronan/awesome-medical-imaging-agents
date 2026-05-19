#!/usr/bin/env python3
"""
scripts/generate_readme.py

Read data/papers.yml, validate each entry, and write generated/papers.md
with one markdown table per domain section.

Usage:
    python scripts/generate_readme.py
    python scripts/generate_readme.py --data data/papers.yml --out generated/papers.md
    python scripts/generate_readme.py --validate-only
"""

import argparse
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required.  Install with:  pip install pyyaml")


# Preferred domain ordering in the output; unknown domains fall to the end.
DOMAIN_ORDER = [
    "Radiology",
    "Survey · Radiology",
    "Pathology",
    "Ultrasound",
    "Endoscopy",
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

# Human-readable section headings keyed by domain string.
SECTION_HEADINGS = {
    "Radiology": "Radiology Agents",
    "Survey · Radiology": "Radiology — Surveys",
    "Pathology": "Pathology Agents (Whole-Slide Imaging · Digital Pathology)",
    "Ultrasound": "Ultrasound Agents (Echocardiography · Robotic Ultrasound)",
    "Endoscopy": "Endoscopy and Surgical Imaging Agents",
    "3D Imaging": "3D CT / MRI / Volumetric Imaging Agents",
    "Segmentation": "Segmentation and Annotation Agents",
    "Report Generation": "Report Generation Agents",
    "Medical VLM": "Medical Vision-Language Model (VLM) Agents",
    "Multimodal": "Multimodal Agents",
    "Clinical Reasoning": "Clinical Reasoning Agents",
    "Workflow Simulation": "Workflow and Simulation Agents",
    "Benchmark": "Benchmarks and Evaluation",
    "Benchmark · Radiology": "Benchmarks — Radiology",
    "Survey": "Surveys and Position Papers",
}

URL_FIELDS = ("paper_url", "code_url", "project_url", "dataset_url", "benchmark_url")
REQUIRED_FIELDS = ("title", "year", "domain")
RECOMMENDED_FIELDS = ("summary",)


# ── Validation ────────────────────────────────────────────────────────────────

def validate(papers: list[dict]) -> tuple[list[str], list[str]]:
    """Return (errors, warnings).  Errors are fatal; warnings are advisory."""
    errors: list[str] = []
    warnings: list[str] = []

    for i, entry in enumerate(papers):
        label = f"Entry {i + 1} ({entry.get('title', '<no title>') !r})"

        for field in REQUIRED_FIELDS:
            if not entry.get(field):
                errors.append(f"{label}: missing required field '{field}'")

        for field in RECOMMENDED_FIELDS:
            if not entry.get(field):
                warnings.append(f"{label}: missing recommended field '{field}'")

        for field in URL_FIELDS:
            value = entry.get(field)
            if value and not str(value).startswith("http"):
                errors.append(
                    f"{label}: '{field}' must start with 'http', got {value!r}"
                )

        year = entry.get("year")
        if year is not None and not isinstance(year, int):
            errors.append(f"{label}: 'year' must be an integer, got {year!r}")

        for list_field in ("modality", "task", "agent_type", "tags"):
            value = entry.get(list_field)
            if value is not None and not isinstance(value, list):
                errors.append(
                    f"{label}: '{list_field}' must be a list or null, got {type(value).__name__}"
                )

    return errors, warnings


# ── Markdown helpers ──────────────────────────────────────────────────────────

def _join(items: list[str] | None, sep: str = ", ") -> str:
    """Join a list of strings, or return '—' if null/empty."""
    if not items:
        return "—"
    return sep.join(str(x) for x in items)


def _links(entry: dict) -> str:
    """Build a compact '· '-separated link string for the Links column.

    If the title is already linked to paper_url, Paper is omitted here to
    avoid duplication.
    """
    has_title_link = bool(entry.get("paper_url"))
    parts: list[str] = []

    if not has_title_link and entry.get("paper_url"):
        parts.append(f"[Paper]({entry['paper_url']})")
    if entry.get("code_url"):
        parts.append(f"[Code]({entry['code_url']})")
    if entry.get("project_url"):
        parts.append(f"[Project]({entry['project_url']})")
    if entry.get("dataset_url"):
        parts.append(f"[Dataset]({entry['dataset_url']})")
    if entry.get("benchmark_url"):
        parts.append(f"[Benchmark]({entry['benchmark_url']})")

    return " · ".join(parts) if parts else "—"


def _title_cell(entry: dict) -> str:
    title = entry["title"]
    url = entry.get("paper_url")
    if url:
        return f"[{title}]({url})"
    return title


def _table_row(entry: dict) -> str:
    cells = [
        _title_cell(entry),
        str(entry.get("year", "—")),
        _join(entry.get("modality")),
        _join(entry.get("task")),
        _join(entry.get("agent_type")),
        _links(entry),
    ]
    return "| " + " | ".join(cells) + " |"


TABLE_HEADER = (
    "| Title | Year | Modality | Task | Agent Type | Links |\n"
    "|---|---:|---|---|---|---|"
)


# ── Document generation ───────────────────────────────────────────────────────

def _sort_key(domain: str) -> tuple[int, str]:
    try:
        return (DOMAIN_ORDER.index(domain), domain)
    except ValueError:
        return (len(DOMAIN_ORDER), domain)


def generate(papers: list[dict]) -> str:
    groups: dict[str, list[dict]] = defaultdict(list)
    for entry in papers:
        groups[entry["domain"]].append(entry)

    today = date.today().isoformat()
    lines: list[str] = [
        "<!-- AUTO-GENERATED — do not edit by hand. -->",
        f"<!-- Run `python scripts/generate_readme.py` to regenerate. -->",
        f"<!-- Generated on {today} from data/papers.yml -->",
        "",
        "# Medical Imaging Agents — Structured Paper Index",
        "",
        f"Total entries: **{len(papers)}** across **{len(groups)}** domains.",
        "",
        "---",
        "",
    ]

    for domain in sorted(groups, key=_sort_key):
        entries = groups[domain]
        heading = SECTION_HEADINGS.get(domain, domain)
        lines.append(f"## {heading}")
        lines.append("")
        lines.append(TABLE_HEADER)
        for entry in entries:
            lines.append(_table_row(entry))
        lines.append("")

    return "\n".join(lines) + "\n"


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent

    parser = argparse.ArgumentParser(
        description="Generate generated/papers.md from data/papers.yml."
    )
    parser.add_argument(
        "--data",
        default=str(repo_root / "data" / "papers.yml"),
        help="Path to papers.yml (default: data/papers.yml)",
    )
    parser.add_argument(
        "--out",
        default=str(repo_root / "generated" / "papers.md"),
        help="Output path (default: generated/papers.md)",
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Run validation only; do not write output.",
    )
    args = parser.parse_args()

    data_path = Path(args.data)
    if not data_path.exists():
        sys.exit(f"Data file not found: {data_path}")

    raw = yaml.safe_load(data_path.read_text())
    if not isinstance(raw, dict) or "papers" not in raw:
        sys.exit("papers.yml must contain a top-level 'papers' key.")

    papers = raw["papers"]

    errors, warnings = validate(papers)

    for w in warnings:
        print(f"WARNING  {w}", file=sys.stderr)
    for e in errors:
        print(f"ERROR    {e}", file=sys.stderr)

    if errors:
        sys.exit(f"\n{len(errors)} validation error(s). Fix them before generating.")

    if warnings:
        print(f"\n{len(warnings)} warning(s). Output will still be generated.",
              file=sys.stderr)

    if args.validate_only:
        print(f"Validation passed ({len(papers)} entries, {len(warnings)} warning(s)).")
        return

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(generate(papers))
    print(f"Written {len(papers)} entries → {out_path}")


if __name__ == "__main__":
    main()
