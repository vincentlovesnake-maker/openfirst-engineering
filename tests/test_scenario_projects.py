import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ScenarioProjectTests(unittest.TestCase):
    def run_project(self, name):
        project = ROOT / "tests" / "fixtures" / name
        return subprocess.run(
            [sys.executable, "-m", "unittest", "-v"],
            cwd=project,
            capture_output=True,
            text=True,
            timeout=30,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )

    def test_healthy_project_ground_truth_passes(self):
        result = self.run_project("healthy_project")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK", result.stderr)

    def test_defective_project_ground_truth_fails(self):
        result = self.run_project("defective_project")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("FAIL", result.stderr)
        self.assertIn("test_other_user_cannot_read_private_document", result.stderr)


if __name__ == "__main__":
    unittest.main()
