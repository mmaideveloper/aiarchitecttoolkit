#!/usr/bin/env python3
"""Resolve a project name to a safe toolkit profile and source repository."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-name", required=True)
    parser.add_argument("--toolkit-root", default=".")
    parser.add_argument("--github-output")
    args = parser.parse_args()

    project_name = args.project_name.strip().lower()
    if not re.fullmatch(r"[a-z0-9-]+", project_name):
        parser.error("project_name must contain only lowercase letters, digits, or hyphens")

    toolkit_root = Path(args.toolkit_root).resolve()
    profile_path = toolkit_root / "profiles" / project_name / "profile.yaml"
    try:
        profile_path.resolve().relative_to((toolkit_root / "profiles").resolve())
    except ValueError:
        parser.error("project profile resolves outside profiles/")
    if not profile_path.is_file():
        available = sorted(path.parent.name for path in (toolkit_root / "profiles").glob("*/profile.yaml"))
        parser.error(f"unknown project_name '{project_name}'; available: {', '.join(available)}")

    profile = yaml.safe_load(profile_path.read_text(encoding="utf-8")) or {}
    configured_key = str(profile.get("project", {}).get("key", "")).lower()
    if configured_key != project_name:
        parser.error(f"profile project.key '{configured_key}' does not match '{project_name}'")

    result = {
        "project_name": project_name,
        "profile_path": profile_path.relative_to(toolkit_root).as_posix(),
        "repository": profile.get("source", {}).get("github_repository") or "",
        "display_name": profile.get("project", {}).get("name") or project_name,
        "artifact_root": profile.get("artifacts", {}).get("root") or "architecture",
        "use_cases_dir": profile.get("artifacts", {}).get("use_cases") or "use-cases",
    }
    print(json.dumps(result))
    if args.github_output:
        output = Path(args.github_output)
        with output.open("a", encoding="utf-8") as stream:
            for key, value in result.items():
                stream.write(f"{key}={value}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
