"""Exercise generator CLI checks in isolated repositories without touching real data."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class GeneratedIndexChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for directory in ("scripts", "data", "docs"):
            (self.root / directory).mkdir()
        for script in ("generate_json.py", "update_themes.py"):
            shutil.copyfile(ROOT / "scripts" / script, self.root / "scripts" / script)
        self.paper = {
            "title": "A Multi-Agent Imaging Study", "year": 2026,
            "domain": "Radiology", "paper_url": "https://example.org/paper",
            "tags": ["multi-agent"],
        }
        self.write_metadata()
        (self.root / "README.md").write_text(
            "### Radiology Agents (1)\n\n"
            "- [A Multi-Agent Imaging Study](https://example.org/paper) - Example (2026).\n"
        )

    def write_metadata(self):
        # JSON is valid YAML and avoids another test dependency.
        (self.root / "data/papers.yml").write_text(json.dumps({"papers": [self.paper]}))

    def run_generator(self, script, *args):
        return subprocess.run(
            [sys.executable, str(self.root / "scripts" / script), *args],
            cwd=self.root, capture_output=True, text=True,
        )

    def test_checks_detect_missing_stale_and_changed_source_without_writing(self):
        for script, filename in (("generate_json.py", "papers.json"),
                                 ("update_themes.py", "themes.md")):
            with self.subTest(script=script):
                output = self.root / "docs" / filename
                result = self.run_generator(script, "--check")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("missing or stale", result.stderr)
                self.assertFalse(output.exists())

                result = self.run_generator(script)
                self.assertEqual(result.returncode, 0, result.stderr)
                original = output.read_bytes()
                result = self.run_generator(script, "--check")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(output.read_bytes(), original)

                output.write_text("outdated index\n")
                result = self.run_generator(script, "--check")
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(output.read_text(), "outdated index\n")

                output.write_bytes(original)
                self.paper["tags"] = ["multi-agent", "privacy"]
                self.write_metadata()
                result = self.run_generator(script, "--check")
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(output.read_bytes(), original)

                result = self.run_generator(script)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(self.run_generator(script, "--check").returncode, 0)
                self.paper["tags"] = ["multi-agent"]
                self.write_metadata()


if __name__ == "__main__":
    unittest.main()
