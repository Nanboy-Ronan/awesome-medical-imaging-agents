# Contributing to Awesome Lists

Thank you for your interest in contributing! 🎉  

We welcome additions that improve and grow our curated collections of high-quality resources.

## What We're Looking For

- Useful tools, libraries, frameworks, articles, or resources.
- Well-maintained projects with clear documentation.
- Content that’s relevant to the theme of the specific Awesome List.
- Respectful discussion, thoughtful suggestions, and constructive feedback.

## Contribution Guidelines

1. **Fork the repository** you want to contribute to.
2. **Create a new branch** for your changes.
3. **Make your edits**:
   - Use the [classification guide](docs/taxonomy.md) to choose one primary section and add supported task, modality, mechanism, and evaluation metadata.
   - Update the README entry and `data/papers.yml` together; supporting foundation models and datasets have separate pages under `docs/`.
   - Follow the existing style and format.
   - Keep descriptions short and informative.
   - Ensure links are correct and not broken.
   - Avoid duplicates and low-quality resources.
4. **Submit a Pull Request** with a clear explanation of what you’re adding or changing.

## Pull Request Checklist

Before you submit, please ensure:

- [ ] The link is active and points to a legitimate resource.
- [ ] The resource is valuable, trustworthy, and relevant.
- [ ] Descriptions are clear and objective.
- [ ] The list remains alphabetically sorted (if applicable).
- [ ] You have not added multiple links to promote a single source.
- [ ] The primary placement follows the classification guide; overlapping themes use tags or cross-references.
- [ ] Section counts and count-based links are updated, and metadata/count validation passes.
- [ ] `python scripts/update_themes.py` has regenerated the theme index when relevant.

After editing papers, refresh and check the generated indexes from the repository root:

```sh
python scripts/generate_json.py
python scripts/update_themes.py
python scripts/generate_comparison.py
python scripts/generate_readme.py --validate-only
python scripts/validate_counts.py
python scripts/validate_counts.py docs/themes.md
python scripts/generate_json.py --check
python scripts/update_themes.py --check
python scripts/generate_comparison.py --check
```

The generators require PyYAML (`python -m pip install pyyaml`). The `--check` commands
do not modify files and fail when an index is missing or stale. CI runs them for paper,
documentation, and script changes. For generator changes, also run
`python -m unittest discover -s tests`.

## Evidence Reviews and Research Briefs

The broad paper list and the reviewed comparison have different scopes. New list entries do not automatically become reviewed comparison entries. Follow the [review protocol](docs/review-protocol.md) when editing `data/comparison.yml`, and use the [evidence review issue form](https://github.com/Nanboy-Ronan/awesome-medical-imaging-agents/issues/new?template=evidence-review.yml) for corrections or execution evidence.

Record the primary-source version, review scope, and actual source-check date. Keep author-reported results separate from independent tests. A public repository is not evidence of a successful installation or a reproduced result. Stronger execution claims require public logs and an extension of the comparison schema before acceptance.

For a [research brief](docs/briefs/README.md), select five readings, state the coverage cutoff, cite primary sources, preserve limitations and negative results, and mark editorial interpretation. Keep earlier issues in the archive. Authors may submit clarifications through issues or PRs; maintainers do not need to contact authors to publish a source-backed review.

## What We Don’t Accept

- Broken links or duplicates.
- Spam, self-promotion, or low-quality content.
- Entire frameworks or tools with no documentation.

## Communication

For discussions, suggestions, or feedback:

- Open an issue.
- Keep your tone respectful and constructive.

Let’s make something Awesome together. 🙌
