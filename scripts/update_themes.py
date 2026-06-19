#!/usr/bin/env python3
"""
scripts/update_themes.py

Build a Themes Index from two sources:

  1. data/papers.yml  — explicit canonical tags (precise, highest priority)
  2. README.md        — keyword inference on every paper entry (broad coverage)

The combined index replaces the "## Themes Index" section in README.md,
from that heading down to (but not including) the next "## " heading.

Usage:
    python scripts/update_themes.py
    python scripts/update_themes.py --dry-run       # print to stdout
    python scripts/update_themes.py --validate-only # stats only, no output
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required.  Install with:  pip install pyyaml")

REPO_ROOT = Path(__file__).resolve().parent.parent

# ── Canonical theme vocabulary ─────────────────────────────────────────────────
# THEMES keys are display headings.
# "trigger_tags": exact strings that, when found in a YAML entry's `tags` list,
#   route the paper into this theme.  Matching is case-insensitive.
# "keywords":  regex patterns searched against lowercased (title + description)
#   for papers parsed from the README.  A single match is sufficient.
THEMES: dict[str, dict] = {
    "Fairness and Bias": {
        "trigger_tags": ["fairness", "bias"],
        "keywords": [
            r"\bfairness\b", r"\bunfairness\b",
            r"\bbias\b", r"\bbiased\b",
            r"\bdisparity\b", r"\bdisparities\b",
            r"racial bias", r"subgroup fairness", r"demographic gap",
        ],
    },
    "Hallucination and Reliability": {
        "trigger_tags": ["hallucination"],
        "keywords": [
            r"\bhallucination", r"\bhallucinate",
            r"\babstention\b", r"\babstain\b",
            r"premature closure", r"conflict.aware abstention",
        ],
    },
    "Safety and Robustness": {
        "trigger_tags": ["safety"],
        "keywords": [
            # "adversarial" alone is excluded — it matches "adversarial debate"
            # (a reasoning technique), which is a false positive.
            r"adversarial attack", r"adversarial agent",
            r"\battack\b", r"\bpoisoning\b",
            r"\bbiosecurity\b", r"cyber.attack", r"\bcollusion\b",
            r"prompt.injection", r"soft.prompt attack",
        ],
    },
    "Privacy and Federated Learning": {
        "trigger_tags": ["privacy"],
        "keywords": [
            r"privacy.preserving", r"federated learning",
            r"differential privacy", r"\bprivacy\b.*agent",
        ],
    },
    "RAG and Retrieval": {
        "trigger_tags": ["RAG"],
        "keywords": [
            r"\bRAG\b", r"retrieval.augmented", r"retrieval augmented",
            r"\bgraphrag\b",
        ],
    },
    "Multi-Agent Collaboration": {
        "trigger_tags": ["multi-agent"],
        "keywords": [
            r"multi[-\s]agent", r"\bmultiagent\b",
        ],
        # Sections where multi-agent is the *default*, not a cross-cutting theme.
        # Uses the canonical mapped section labels (post _SECTION_MAP lookup).
        "exclude_sections": {
            "Clinical Reasoning Agents",
            "Workflow Agents",
            "Agent Skills",
        },
    },
    "Reinforcement Learning": {
        "trigger_tags": ["reinforcement-learning"],
        "keywords": [
            r"reinforcement learning", r"\bRL\b[-\s]trained",
            r"policy network", r"agentic reinforcement",
        ],
    },
    "Human-in-the-Loop": {
        "trigger_tags": ["human-in-the-loop"],
        "keywords": [
            r"human.in.the.loop",
            r"interactive annotation",
            r"clinician.in.the.loop",
            r"clinician review loop",
        ],
    },
}

# ── README parsing ─────────────────────────────────────────────────────────────
THEMES_HEADING = "## Themes Index"

# Map YAML `domain` values → canonical section label for the index.
_YAML_DOMAIN_TO_SECTION: dict[str, str] = {
    "Radiology": "Radiology Agents",
    "Survey · Radiology": "Radiology — Surveys",
    "Pathology": "Pathology Agents",
    "Ultrasound": "Ultrasound Agents",
    "Endoscopy": "Endoscopy Agents",
    "Ophthalmology": "Ophthalmology Agents",
    "3D Imaging": "3D Imaging Agents",
    "Segmentation": "Segmentation Agents",
    "Report Generation": "Report Generation Agents",
    "Medical VLM": "Medical VLM Agents",
    "Multimodal": "Multimodal Agents",
    "Clinical Reasoning": "Clinical Reasoning Agents",
    "Workflow Simulation": "Workflow Agents",
    "Benchmark": "Benchmarks",
    "Benchmark · Radiology": "Benchmarks — Radiology",
    "Survey": "Surveys",
}

# Map (partial) README section header text → canonical label used in the index.
# The count suffix like "(28)" is stripped before matching.
_SECTION_MAP: dict[str, str] = {
    "Radiology Agents": "Radiology Agents",
    "Pathology Agents": "Pathology Agents",
    "Ultrasound Agents": "Ultrasound Agents",
    "Endoscopy and Surgical Imaging Agents": "Endoscopy Agents",
    "Ophthalmology Agents": "Ophthalmology Agents",
    "3D CT / MRI / Volumetric Imaging Agents": "3D Imaging Agents",
    "Segmentation and Annotation Agents": "Segmentation Agents",
    "Report Generation Agents": "Report Generation Agents",
    "Medical Vision-Language Model (VLM) Agents": "Medical VLM Agents",
    "Clinical Reasoning Agents": "Clinical Reasoning Agents",
    "Workflow and Simulation Agents": "Workflow Agents",
    "Agent Skills and Tool Learning": "Agent Skills",
    "Benchmark Papers": "Benchmarks",
    "Safety, Robustness, and Fairness": "Safety",
}

# Subsections whose papers are skipped entirely.
_SKIP_SUBSECTIONS: set[str] = {"Backbone Foundation Models (not agents)"}

# Stop parsing at these sections — they contain non-paper content.
_STOP_SECTIONS: set[str] = {
    "Themes Index",
    "Datasets",
    "Toolboxes",
    "Surveys and Position Papers",
    "Related Awesome Lists",
    "Generating the Paper Index",
    "Contributing",
    "License",
}

_HEADER_RE = re.compile(r"^(#{1,3})\s+(.+?)(?:\s+\(\d+\))?\s*$")
_ENTRY_RE = re.compile(r"^- \[(.+?)\]\((.+?)\)\s*—\s*(.+)$")
_YEAR_RE = re.compile(r"\b(20\d{2})\b")


def _strip_links(text: str) -> str:
    """Remove trailing '[Code](...) · [Demo](...)' link clusters from description."""
    return re.sub(r"\s*\[[A-Z][^\]]*\]\(https?://[^)]+\).*$", "", text).strip()


def _extract_year(description: str) -> int | None:
    m = _YEAR_RE.search(description)
    return int(m.group(1)) if m else None


def _resolve_section(raw_name: str) -> str | None:
    """Return canonical section label or None if this section is not tracked."""
    for key, label in _SECTION_MAP.items():
        if key in raw_name:
            return label
    return None


def parse_readme_papers(readme_text: str) -> list[dict]:
    """
    Walk README.md and return one dict per paper entry found in tracked sections.
    Keys: title, url, section, description, year.
    """
    papers: list[dict] = []
    current_section: str | None = None
    skip_mode = False          # True when inside a _SKIP_SUBSECTIONS block

    for line in readme_text.splitlines():
        # Section headers
        hm = _HEADER_RE.match(line)
        if hm:
            level = len(hm.group(1))
            raw_name = hm.group(2).strip()

            # Hard stop
            if raw_name in _STOP_SECTIONS:
                break

            if raw_name in _SKIP_SUBSECTIONS:
                skip_mode = True
                continue

            resolved = _resolve_section(raw_name)
            if level <= 2:
                skip_mode = False
                current_section = resolved   # may be None for untracked sections
            else:
                # Level-3 subsection: update section but don't reset skip_mode
                # (it was set to True by _SKIP_SUBSECTIONS match above)
                if not skip_mode:
                    current_section = resolved
            continue

        # Reset skip_mode at horizontal rules between top-level sections
        if line.strip() == "---":
            skip_mode = False
            continue

        if skip_mode or current_section is None:
            continue

        # Skip benchmark table rows
        if line.startswith("|"):
            continue

        # Paper entry
        em = _ENTRY_RE.match(line)
        if em:
            title = em.group(1)
            url = em.group(2)
            description = _strip_links(em.group(3))
            papers.append(
                {
                    "title": title,
                    "url": url,
                    "section": current_section,
                    "description": description,
                    "year": _extract_year(description),
                }
            )

    return papers


# ── Theme matching ─────────────────────────────────────────────────────────────

def _compiled_keywords(theme_cfg: dict) -> list[re.Pattern]:
    return [re.compile(p, re.IGNORECASE) for p in theme_cfg.get("keywords", [])]


_COMPILED: dict[str, list[re.Pattern]] = {
    name: _compiled_keywords(cfg) for name, cfg in THEMES.items()
}


def _infer_themes_from_text(title: str, description: str, section: str) -> set[str]:
    text = title + " " + description
    result: set[str] = set()
    for theme_name, cfg in THEMES.items():
        excluded = cfg.get("exclude_sections", set())
        if section in excluded:
            continue
        for pat in _COMPILED[theme_name]:
            if pat.search(text):
                result.add(theme_name)
                break
    return result


def _themes_from_yaml_tags(tags: list[str] | None) -> set[str]:
    if not tags:
        return set()
    result: set[str] = set()
    for theme_name, cfg in THEMES.items():
        triggers = {t.lower() for t in cfg["trigger_tags"]}
        if any(t.lower() in triggers for t in tags):
            result.add(theme_name)
    return result


# ── Build index ────────────────────────────────────────────────────────────────

def build_index(
    readme_papers: list[dict],
    yaml_papers: list[dict],
) -> dict[str, list[dict]]:
    """
    Return {theme_name: [paper_dict, ...]} sorted newest-first.

    YAML explicit tags take precedence over keyword inference.
    A paper can appear in multiple themes.
    Deduplication is by URL.
    """
    # Build a URL→yaml_entry lookup for precedence checks.
    yaml_by_url: dict[str, dict] = {}
    for yp in yaml_papers:
        if yp.get("paper_url"):
            yaml_by_url[yp["paper_url"]] = yp

    index: dict[str, list[dict]] = defaultdict(list)
    seen_per_theme: dict[str, set[str]] = defaultdict(set)

    # ── Pass 1: YAML-explicit entries ──────────────────────────────────────────
    for yp in yaml_papers:
        themes = _themes_from_yaml_tags(yp.get("tags"))
        if not themes:
            continue
        url = yp.get("paper_url") or ""
        domain = yp.get("domain", "")
        section = _YAML_DOMAIN_TO_SECTION.get(domain, domain)
        venue = yp.get("venue") or ""
        year = yp.get("year")
        entry = {
            "title": yp["title"],
            "url": url,
            "section": section,
            "year": year,
            "venue": venue,
        }
        for theme in themes:
            if url not in seen_per_theme[theme]:
                index[theme].append(entry)
                seen_per_theme[theme].add(url)

    # ── Pass 2: README-inferred entries (skip if YAML already covered them) ───
    for rp in readme_papers:
        url = rp["url"]
        if url in yaml_by_url:
            # YAML handles this paper; only add to themes not already covered.
            yaml_themes = _themes_from_yaml_tags(yaml_by_url[url].get("tags"))
            inferred = _infer_themes_from_text(rp["title"], rp["description"], rp["section"])
            additional = inferred - yaml_themes
            for theme in additional:
                if url not in seen_per_theme[theme]:
                    entry = {
                        "title": rp["title"],
                        "url": url,
                        "section": rp["section"],
                        "year": rp["year"],
                        "venue": None,
                    }
                    index[theme].append(entry)
                    seen_per_theme[theme].add(url)
        else:
            inferred = _infer_themes_from_text(rp["title"], rp["description"], rp["section"])
            for theme in inferred:
                if url not in seen_per_theme[theme]:
                    entry = {
                        "title": rp["title"],
                        "url": url,
                        "section": rp["section"],
                        "year": rp["year"],
                        "venue": None,
                    }
                    index[theme].append(entry)
                    seen_per_theme[theme].add(url)

    # Sort each theme newest-first.
    for theme in index:
        index[theme].sort(key=lambda e: -(e["year"] or 0))

    return index


# ── Rendering ──────────────────────────────────────────────────────────────────

def _paper_line(entry: dict) -> str:
    title = entry["title"]
    url = entry["url"]
    section = entry["section"]
    year = entry.get("year") or ""
    venue = entry.get("venue") or ""

    title_part = f"[{title}]({url})" if url else title
    venue_year = f"{venue} ({year})" if venue else str(year)

    return f"- {title_part} — {venue_year} · *{section}*"


def generate_themes_section(index: dict[str, list[dict]], total_tagged: int) -> str:
    lines: list[str] = [
        THEMES_HEADING,
        "",
        ("*Cross-cutting topics that span multiple domain sections above. "
         "Each paper is listed once in its primary section; this index lets you "
         "find it by theme.*"),
        "",
    ]

    any_found = False
    for theme_name in THEMES:          # preserve THEMES dict order
        entries = index.get(theme_name, [])
        if not entries:
            continue
        any_found = True
        lines.append(f"### {theme_name} ({len(entries)})")
        lines.append("")
        for entry in entries:
            lines.append(_paper_line(entry))
        lines.append("")

    if not any_found:
        lines.append("*No papers matched canonical theme keywords yet.*")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


# ── README injection ───────────────────────────────────────────────────────────

_NEXT_H2_RE = re.compile(r"^## ")


def inject_into_readme(readme_text: str, themes_section: str) -> str:
    lines = readme_text.splitlines(keepends=True)

    start_line = next(
        (i for i, line in enumerate(lines) if line.rstrip("\n") == THEMES_HEADING),
        None,
    )
    if start_line is None:
        raise ValueError(
            f"README is missing the {THEMES_HEADING!r} heading.\n"
            "Add it to README.md before running this script."
        )

    end_line = next(
        (i for i in range(start_line + 1, len(lines)) if _NEXT_H2_RE.match(lines[i])),
        len(lines),
    )

    return "".join(lines[:start_line]) + themes_section + "\n" + "".join(lines[end_line:])


# ── CLI ────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate and inject a Themes Index into README.md."
    )
    parser.add_argument("--data", default=str(REPO_ROOT / "data" / "papers.yml"))
    parser.add_argument("--readme", default=str(REPO_ROOT / "README.md"))
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the themes section to stdout; do not modify README.md.")
    parser.add_argument("--validate-only", action="store_true",
                        help="Print stats only; do not write any output.")
    args = parser.parse_args()

    readme_path = Path(args.readme)
    if not readme_path.exists():
        sys.exit(f"README not found: {readme_path}")

    data_path = Path(args.data)
    if not data_path.exists():
        sys.exit(f"Data file not found: {data_path}")

    readme_text = readme_path.read_text()

    raw = yaml.safe_load(data_path.read_text())
    if not isinstance(raw, dict) or "papers" not in raw:
        sys.exit("papers.yml must contain a top-level 'papers' key.")
    yaml_papers: list[dict] = raw["papers"]

    readme_papers = parse_readme_papers(readme_text)
    index = build_index(readme_papers, yaml_papers)
    total_tagged = sum(len(v) for v in index.values())

    if args.validate_only:
        print(f"README papers parsed: {len(readme_papers)}")
        print(f"YAML papers:          {len(yaml_papers)}")
        for theme, entries in index.items():
            print(f"  {theme}: {len(entries)}")
        print(f"Total theme entries:  {total_tagged}")
        return

    themes_section = generate_themes_section(index, total_tagged)

    if args.dry_run:
        print(themes_section)
        return

    updated = inject_into_readme(readme_text, themes_section)
    readme_path.write_text(updated)
    print(
        f"Themes index injected into {readme_path}\n"
        f"  README papers parsed: {len(readme_papers)}\n"
        f"  Themes populated: "
        + ", ".join(f"{t} ({len(v)})" for t, v in index.items() if v)
    )


if __name__ == "__main__":
    main()
