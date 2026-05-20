#!/usr/bin/env python3
"""Convert data/papers.yml → docs/papers.json for the GitHub Pages site."""
import json
import pathlib
import yaml


def main():
    root = pathlib.Path(__file__).parent.parent
    with open(root / "data" / "papers.yml") as f:
        data = yaml.safe_load(f)
    papers = data["papers"]
    out = root / "docs" / "papers.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(papers, ensure_ascii=False, indent=2))
    print(f"Wrote {len(papers)} papers to {out}")


if __name__ == "__main__":
    main()
