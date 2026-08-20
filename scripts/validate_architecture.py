"""Validate identifiers, lifecycle states, references, and links in architecture artifacts."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path


ARTIFACTS = {
    "BDR": ("business-decisions", {"Proposed", "Accepted", "Rejected", "Superseded"}),
    "UC": ("use-cases", {"Draft", "Reviewed", "Approved", "Retired"}),
    "ADD": ("design", {"Draft", "In Review", "Approved", "Superseded"}),
    "ADR": ("decisions", {"Proposed", "Accepted", "Rejected", "Deprecated", "Superseded"}),
    "ACR": ("reviews", {"Draft", "Complete"}),
}
ID_PATTERN = re.compile(r"\b(BDR|UC|ADD|ADR|ACR)-(\d{3,})\b")
STATUS_PATTERN = re.compile(r"(?im)^-\s*Status:\s*(.+?)\s*$")
LINK_PATTERN = re.compile(r"\[[^]]*]\(([^)]+)\)")


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    documents = sorted(root.rglob("*.md"))
    definitions: dict[str, list[Path]] = defaultdict(list)
    contents: dict[Path, str] = {}

    for path in documents:
        text = path.read_text(encoding="utf-8")
        contents[path] = text
        match = ID_PATTERN.search(path.name)
        if not match:
            relative_parts = path.relative_to(root).parts
            if path.name.lower() != "index.md" and "diagrams" not in relative_parts:
                errors.append(f"Unrecognized artifact filename: {path.relative_to(root)}")
            continue

        artifact_id = match.group(0)
        kind = match.group(1)
        definitions[artifact_id].append(path)
        expected_folder, allowed_statuses = ARTIFACTS[kind]
        if expected_folder not in path.relative_to(root).parts:
            errors.append(f"{artifact_id} is outside {expected_folder}/: {path.relative_to(root)}")

        status_match = STATUS_PATTERN.search(text)
        if not status_match:
            errors.append(f"Missing status in {path.relative_to(root)}")
        elif status_match.group(1) not in allowed_statuses:
            errors.append(
                f"Invalid {kind} status '{status_match.group(1)}' in {path.relative_to(root)}"
            )

    for artifact_id, paths in definitions.items():
        if len(paths) > 1:
            joined = ", ".join(str(path.relative_to(root)) for path in paths)
            errors.append(f"Duplicate {artifact_id}: {joined}")

    known_ids = set(definitions)
    for path, text in contents.items():
        for target in LINK_PATTERN.findall(text):
            clean_target = target.strip().split("#", 1)[0]
            if not clean_target or re.match(r"^(?:https?://|mailto:)", clean_target):
                continue
            linked_path = (path.parent / clean_target).resolve()
            linked_match = ID_PATTERN.search(linked_path.name)
            if linked_path.exists() and linked_match:
                known_ids.add(linked_match.group(0))

    for path, text in contents.items():
        for match in ID_PATTERN.finditer(text):
            referenced_id = match.group(0)
            if referenced_id not in known_ids:
                errors.append(f"Unknown reference {referenced_id} in {path.relative_to(root)}")
        for target in LINK_PATTERN.findall(text):
            clean_target = target.strip().split("#", 1)[0]
            if not clean_target or re.match(r"^(?:https?://|mailto:)", clean_target):
                continue
            if not (path.parent / clean_target).resolve().exists():
                errors.append(f"Broken link '{target}' in {path.relative_to(root)}")

    if not (root / "index.md").exists():
        errors.append("Missing architecture/index.md traceability index")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        type=Path,
        default=Path("architecture"),
        help="Architecture artifact root (default: architecture)",
    )
    return parser.parse_args()


def main() -> int:
    root = parse_args().root.resolve()
    if not root.is_dir():
        print(f"Architecture root does not exist: {root}")
        return 2
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Validated {len(list(root.rglob('*.md')))} architecture documents under {root}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
