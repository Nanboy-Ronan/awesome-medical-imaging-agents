#!/usr/bin/env python3
"""Convert data/papers.yml → docs/papers.json, or check it with --check."""
import argparse
import json
import pathlib
import sys
import yaml


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="Fail if the generated JSON is missing or stale; do not write.")
    args = parser.parse_args()
    root = pathlib.Path(__file__).parent.parent
    with open(root / "data" / "papers.yml") as f:
        data = yaml.safe_load(f)
    papers = data["papers"]
    out = root / "docs" / "papers.json"
    generated = json.dumps(papers, ensure_ascii=False, indent=2)
    if args.check:
        if not out.exists() or out.read_text() != generated:
            sys.exit("docs/papers.json is missing or stale. Run: python scripts/generate_json.py")
        print(f"JSON index is current ({len(papers)} papers).")
        return
    out.parent.mkdir(exist_ok=True)
    out.write_text(generated)
    print(f"Wrote {len(papers)} papers to {out}")


if __name__ == "__main__":
    main()
