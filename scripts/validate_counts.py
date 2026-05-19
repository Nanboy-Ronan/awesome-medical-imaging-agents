#!/usr/bin/env python3
"""
scripts/validate_counts.py

Verify that every section header of the form:
    ## Section Title (N)
    ### Subsection Title (N)
contains a count that matches the actual number of markdown bullet entries
(`- [...]`) in that section.

Subsections are counted independently from their parent section (a bullet
inside a `###` block is NOT counted in the parent `##` block).

Exit codes:
    0 — all counts match
    1 — one or more mismatches found

Usage:
    python scripts/validate_counts.py
    python scripts/validate_counts.py README.md
"""

import re
import sys
from pathlib import Path

_HEADING_WITH_COUNT = re.compile(r"^(#{2,3})\s+(.+?)\s+\((\d+)\)\s*$")
_BULLET = re.compile(r"^- \[")


def check_counts(readme_path: Path) -> list[str]:
    """
    Return a list of mismatch error strings.
    Empty list means all counts are correct.
    """
    lines = readme_path.read_text().splitlines()

    # Parse sections with (N) counts and count their bullets.
    # We track heading level so a `###` subsection "owns" its bullets
    # separately from the enclosing `##` section.

    # Stack entry: (level, heading_text, declared_count, bullet_count)
    # We maintain at most two levels: level-2 and level-3.

    results: list[tuple[int, str, int, int]] = []

    # Current counters keyed by heading level (2 or 3).
    current: dict[int, tuple[str, int]] = {}  # level → (heading, declared_count)
    counts: dict[int, int] = {}               # level → bullet count so far

    def _flush(level: int) -> None:
        if level in current:
            heading, declared = current[level]
            actual = counts.get(level, 0)
            results.append((level, heading, declared, actual))
            del current[level]
            del counts[level]

    for line in lines:
        m = _HEADING_WITH_COUNT.match(line)
        if m:
            level = len(m.group(1))
            heading = m.group(2).strip()
            declared = int(m.group(3))

            # Flush current section at this level (or deeper) before opening new one.
            for lv in sorted(current.keys(), reverse=True):
                if lv >= level:
                    _flush(lv)

            current[level] = (heading, declared)
            counts[level] = 0
            continue

        # Plain heading (no count) — flush deeper sections only.
        plain = re.match(r"^(#{2,3})\s+", line)
        if plain:
            level = len(plain.group(1))
            for lv in sorted(current.keys(), reverse=True):
                if lv >= level:
                    _flush(lv)
            continue

        # Bullet — assign to the deepest open section.
        if _BULLET.match(line) and current:
            deepest = max(current.keys())
            counts[deepest] = counts.get(deepest, 0) + 1

    # Flush remaining open sections.
    for lv in sorted(current.keys(), reverse=True):
        _flush(lv)

    # Collect mismatches.
    errors: list[str] = []
    for level, heading, declared, actual in results:
        if declared != actual:
            errors.append(
                f"{'#' * level} {heading} ({declared}): "
                f"declared {declared} but found {actual} bullets  "
                f"[diff: {actual - declared:+d}]"
            )

    return errors


def main() -> None:
    readme = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("README.md")
    if not readme.exists():
        sys.exit(f"File not found: {readme}")

    errors = check_counts(readme)

    if not errors:
        print(f"All section counts are correct in {readme}.")
        sys.exit(0)

    print(f"Section count mismatches found in {readme}:\n")
    for e in errors:
        print(f"  MISMATCH  {e}")
    print(f"\n{len(errors)} mismatch(es). Update the (N) values in the headers.")
    sys.exit(1)


if __name__ == "__main__":
    main()
