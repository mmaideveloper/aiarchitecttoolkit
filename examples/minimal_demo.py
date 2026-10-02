"""Minimal integrity check for the toolkit source tree.

Compliance workflow example:
  First: Use $compliance-review for a synthetic architecture; complete intake.
  Next: Use $compliance-review again (show saved parameters; reuse or edit).
  Direct reuse: Run $compliance-review using the previous parameters.
Settings live per scope in architecture/compliance/<scope-slug>.parameters.json;
review evidence is refreshed on every run.
"""

from pathlib import Path
import re
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SKILLS = {
    "idea-task",
    "architecture-change",
    "generate-use-case",
    "generate-bdr",
    "generate-add",
    "generate-c4",
    "generate-adr",
    "prepare-task",
    "review-architecture-conformance",
    "security-review",
    "compliance-review",
    "azure-review",
    "ai-solution-final-review",
}
REQUIRED_PROFILE_FILES = {
    "profiles/project-profile.example.yaml",
    "profiles/healthcare.example.yaml",
    "profiles/healthcare-cz-sk-compliance.example.md",
    "profiles/instructions/healthcare-use-case.md",
    "profiles/agel/profile.yaml",
    "profiles/agel/AGENTS.md",
    "profiles/agel/instructions/use-case.md",
    "profiles/jurisdigta/profile.yaml",
    "profiles/jurisdigta/AGENTS.md",
    "profiles/jurisdigta/instructions/use-case.md",
}


def main() -> None:
    discovered = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
    missing = REQUIRED_SKILLS - discovered
    if missing:
        raise SystemExit(f"Missing skills: {', '.join(sorted(missing))}")

    missing_profile_files = {
        relative for relative in REQUIRED_PROFILE_FILES if not (ROOT / relative).is_file()
    }
    if missing_profile_files:
        raise SystemExit(
            f"Missing profile files: {', '.join(sorted(missing_profile_files))}"
        )

    healthcare_profile = (ROOT / "profiles/healthcare.example.yaml").read_text(
        encoding="utf-8"
    )
    instruction_match = re.search(r"^\s*use_case:\s*([^#\r\n]+)", healthcare_profile, re.M)
    if not instruction_match:
        raise SystemExit("Healthcare profile has no use-case instruction")
    instruction_path = instruction_match.group(1).strip().strip("'\"")
    if not (ROOT / instruction_path).is_file():
        raise SystemExit(f"Broken healthcare use-case instruction: {instruction_path}")

    for project_name in ("agel", "jurisdigta"):
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts/architecture/resolve_project.py"),
                "--project-name",
                project_name,
                "--toolkit-root",
                str(ROOT),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode:
            raise SystemExit(result.stdout or result.stderr)

    for skill_name in sorted(REQUIRED_SKILLS):
        skill_file = ROOT / "skills" / skill_name / "SKILL.md"
        text = skill_file.read_text(encoding="utf-8")
        match = re.search(r"\A---\s+name:\s*([^\s]+).*?description:\s*(.+?)\s+---", text, re.S)
        if not match or match.group(1) != skill_name:
            raise SystemExit(f"Invalid frontmatter for {skill_name}")
        if "[TODO" in text or "<TODO" in text:
            raise SystemExit(f"Unresolved TODO in {skill_name}")
        for relative_link in re.findall(r"\[[^]]+\]\((?!https?://|#)([^)]+)\)", text):
            if not (skill_file.parent / relative_link).resolve().exists():
                raise SystemExit(f"Broken link in {skill_name}: {relative_link}")

    with tempfile.TemporaryDirectory() as temporary_directory:
        architecture = Path(temporary_directory) / "architecture"
        decisions = architecture / "business-decisions"
        decisions.mkdir(parents=True)
        (architecture / "index.md").write_text(
            "# Traceability\n\n- [BDR-001](business-decisions/BDR-001-adopt-toolkit.md)\n",
            encoding="utf-8",
        )
        (decisions / "BDR-001-adopt-toolkit.md").write_text(
            "# BDR-001: Adopt the toolkit\n\n- Status: Proposed\n",
            encoding="utf-8",
        )
        validator = ROOT / "scripts" / "validate_architecture.py"
        result = subprocess.run(
            [sys.executable, str(validator), str(architecture)],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode:
            raise SystemExit(result.stdout or result.stderr)

    print(f"Validated {len(REQUIRED_SKILLS)} architecture skills and artifact traceability.")


if __name__ == "__main__":
    main()
