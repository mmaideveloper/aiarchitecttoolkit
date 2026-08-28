from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
RESOLVER = ROOT / "scripts" / "architecture" / "resolve_project.py"


class ProjectProfileTests(unittest.TestCase):
    def resolve(self, project_name: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(RESOLVER),
                "--project-name",
                project_name,
                "--toolkit-root",
                str(ROOT),
            ],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_known_projects_resolve_with_instruction_files(self) -> None:
        for project_name in ("agel", "jurisdigta"):
            with self.subTest(project_name=project_name):
                result = self.resolve(project_name)
                self.assertEqual(result.returncode, 0, result.stderr)
                resolved = json.loads(result.stdout)
                self.assertEqual(resolved["project_name"], project_name)

                profile_path = ROOT / resolved["profile_path"]
                profile = yaml.safe_load(profile_path.read_text(encoding="utf-8"))
                self.assertEqual(profile["project"]["key"], project_name)
                self.assertTrue((ROOT / profile["project_instructions"]["agents"]).is_file())
                for instruction in profile["document_instructions"]["use_case"]:
                    self.assertTrue((ROOT / instruction).is_file())
                self.assertIn("required_owner_roles", profile["validation"]["use_case"])

    def test_unknown_project_is_rejected(self) -> None:
        result = self.resolve("unknown-project")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown project_name", result.stderr)

    def test_jurisdigta_repository_is_evidence_backed(self) -> None:
        result = self.resolve("jurisdigta")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            json.loads(result.stdout)["repository"],
            "mmaideveloper/aijurisdictionagents",
        )

    def test_agel_requires_repository_configuration_or_override(self) -> None:
        result = self.resolve("agel")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["repository"], "")


if __name__ == "__main__":
    unittest.main()
