#!/usr/bin/env python3
"""Record the GitHub workflow Mermaid-rendering outcome in validation reports."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report-dir", required=True)
    parser.add_argument("--status", required=True, choices=["success", "failure", "cancelled", "skipped"])
    args = parser.parse_args()

    report_dir = Path(args.report_dir)
    json_path = report_dir / "use-case-validation-report.json"
    markdown_path = report_dir / "use-case-validation-summary.md"
    report = json.loads(json_path.read_text(encoding="utf-8"))
    passed = args.status == "success"
    diagram_count = len(report.get("mermaid_files", []))
    detail = (
        f"All {diagram_count} linked Mermaid diagram(s) rendered successfully."
        if passed else
        f"Linked Mermaid rendering workflow outcome: {args.status}."
    )
    for check in report["checks"]:
        if check["name"] == "Mermaid diagrams render successfully":
            check["status"] = "pass" if passed else "fail"
            check["detail"] = detail
            break
    json_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    markdown = markdown_path.read_text(encoding="utf-8")
    replacement = f"| Mermaid diagrams render successfully | {'PASS' if passed else 'FAIL'} | {detail} |"
    lines = [replacement if line.startswith("| Mermaid diagrams render successfully |") else line for line in markdown.splitlines()]
    markdown_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

