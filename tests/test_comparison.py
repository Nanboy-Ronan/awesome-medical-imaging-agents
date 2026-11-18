"""Guard against unsupported evidence claims and stale comparison output."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('comparison', ROOT / 'scripts/generate_comparison.py')
comparison = importlib.util.module_from_spec(spec)
spec.loader.exec_module(comparison)


class ComparisonReview(unittest.TestCase):
    def setUp(self):
        self.entries = yaml.safe_load((ROOT / 'data/comparison.yml').read_text())['entries']
        self.papers = yaml.safe_load((ROOT / 'data/papers.yml').read_text())['papers']

    def test_unverified_reproduction_claim_is_rejected(self):
        entries = copy.deepcopy(self.entries)
        entries[0]['reproduction_status'] = 'reproduced'
        with self.assertRaisesRegex(ValueError, 'execution log'):
            comparison.validate(entries, self.papers)

    def test_inspected_source_requires_url_and_unknown_papers_are_rejected(self):
        entries = copy.deepcopy(self.entries)
        entries[0]['code_url'] = None
        with self.assertRaisesRegex(ValueError, 'repository URL'):
            comparison.validate(entries, self.papers)
        entries = copy.deepcopy(self.entries)
        entries[0]['paper_url'] = 'https://example.org/unknown'
        with self.assertRaisesRegex(ValueError, 'Unknown or duplicate paper'):
            comparison.validate(entries, self.papers)

    def test_duplicate_identity_including_arxiv_version_is_rejected(self):
        entries = copy.deepcopy(self.entries)
        duplicate = copy.deepcopy(entries[0])
        duplicate['id'] = 'Another-Name'
        duplicate['paper_url'] = 'https://arxiv.org/pdf/2502.02673v1'
        with self.assertRaisesRegex(ValueError, 'Unknown or duplicate paper'):
            comparison.validate(entries + [duplicate], self.papers)

    def test_check_detects_source_change_and_never_overwrites_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ('scripts', 'data', 'docs'):
                (root / name).mkdir()
            shutil.copyfile(ROOT / 'scripts/generate_comparison.py', root / 'scripts/generate_comparison.py')
            (root / 'data/papers.yml').write_text(json.dumps({'papers': self.papers}))
            source = root / 'data/comparison.yml'
            source.write_text(json.dumps({'schema_version': 1, 'entries': self.entries}))
            command = [sys.executable, str(root / 'scripts/generate_comparison.py')]
            def run(*args):
                return subprocess.run(command + list(args), capture_output=True, text=True)
            output = root / 'docs/comparison.md'
            self.assertNotEqual(run('--check').returncode, 0)
            self.assertFalse(output.exists())
            result = run()
            self.assertEqual(result.returncode, 0, result.stderr)
            original = output.read_bytes()
            self.assertEqual(run('--check').returncode, 0)
            self.entries[0]['limitation'] = 'A newly checked limitation.'
            source.write_text(json.dumps({'schema_version': 1, 'entries': self.entries}))
            self.assertNotEqual(run('--check').returncode, 0)
            self.assertEqual(output.read_bytes(), original)


if __name__ == '__main__':
    unittest.main()
