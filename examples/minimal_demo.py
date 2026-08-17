"""Minimal dependency-free integrity check for the toolkit source tree."""

from pathlib import Path
import re


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
}


def main() -> None:
    discovered = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
    missing = REQUIRED_SKILLS - discovered
    if missing:
        raise SystemExit(f"Missing skills: {', '.join(sorted(missing))}")

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

    print(f"Validated {len(REQUIRED_SKILLS)} architecture skills.")


if __name__ == "__main__":
    main()
