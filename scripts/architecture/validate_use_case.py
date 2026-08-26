#!/usr/bin/env python3
"""Validate an architecture use case and emit JSON/Markdown reports."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from urllib.parse import unquote


UNKNOWN = re.compile(r"\b(unknown|to verify|to classify|tbd|not yet|remain(?:s)? to be|requires? .* approval)\b", re.I)
PLACEHOLDER_OWNER = re.compile(r"^(unknown|tbd|to verify|unassigned|none|n/a)$", re.I)


@dataclass
class Check:
    name: str
    status: str
    detail: str


def section(text: str, heading: str) -> str:
    match = re.search(rf"^##+\s+{re.escape(heading)}\s*$", text, re.I | re.M)
    if not match:
        return ""
    tail = text[match.end():]
    stop = re.search(r"^##\s+", tail, re.M)
    return tail[: stop.start()] if stop else tail


def has_sections(text: str, names: list[str]) -> tuple[bool, list[str]]:
    missing = [name for name in names if not section(text, name)]
    return not missing, missing


def metadata(record: str, key: str) -> str:
    match = re.search(rf"^-\s+{re.escape(key)}:\s*(.+)$", record, re.I | re.M)
    return match.group(1).strip() if match else ""


def markdown_links(text: str, source: Path, root: Path) -> tuple[list[str], list[str]]:
    invalid: list[str] = []
    mermaid: list[str] = []
    for target in re.findall(r"(?<!!)\[[^]]+\]\(([^)]+)\)", text):
        target = unquote(target.strip().split("#", 1)[0])
        if not target or re.match(r"^(https?|mailto):", target, re.I):
            continue
        resolved = (source.parent / target).resolve()
        try:
            relative = resolved.relative_to(root.resolve()).as_posix()
        except ValueError:
            invalid.append(f"{target} (outside repository)")
            continue
        if not resolved.exists():
            invalid.append(target)
        elif resolved.suffix.lower() == ".mmd":
            mermaid.append(relative)
    return invalid, sorted(set(mermaid))


def ids_are_unique(text: str, prefix: str) -> bool:
    ids = re.findall(rf"`?({prefix}-\d+)`?", text, re.I)
    definitions = re.findall(rf"(?:^|\|)\s*(?:-\s*)?`?({prefix}-\d+)`?\s*(?::|—|-|\|)", text, re.I | re.M)
    normalized = [item.upper() for item in definitions]
    return bool(ids) and len(normalized) == len(set(normalized))


def reviewer_evidence(text: str) -> tuple[bool, list[str]]:
    feedback = section(text, "Stakeholder Feedback Log")
    required = ["clinical", "security", "privacy|data", "architecture"]
    missing = [item.replace("|", "/") for item in required if not re.search(item, feedback, re.I)]
    return not missing, missing


def add(checks: list[Check], name: str, passed: bool, ok: str, fail: str) -> None:
    checks.append(Check(name, "pass" if passed else "fail", ok if passed else fail))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--use-case-id", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()

    uc_id = args.use_case_id.upper().strip()
    if not re.fullmatch(r"UC-\d{3}", uc_id):
        print(f"Invalid use-case ID: {args.use_case_id}", file=sys.stderr)
        return 2

    root = Path(args.repo_root).resolve()
    matches = sorted((root / "architecture" / "use-cases").glob(f"{uc_id}-*.md"))
    if len(matches) != 1:
        print(f"Expected exactly one architecture/use-cases/{uc_id}-*.md; found {len(matches)}", file=sys.stderr)
        return 2

    source = matches[0]
    text = source.read_text(encoding="utf-8")
    record = section(text, "Record")
    checks: list[Check] = []

    title_ok = bool(re.search(rf"^#\s+{re.escape(uc_id)}:\s+\S", text, re.M))
    add(checks, "Valid use-case ID", title_ok, f"Document title uses {uc_id}.", "Title does not contain the requested ID and a description.")

    meta = {key: metadata(record, key) for key in ["Status", "Owner", "Date", "Stakeholders", "Related artifacts"]}
    missing_meta = [key for key, value in meta.items() if not value]
    add(checks, "Required metadata present", not missing_meta, "Required Record metadata is present.", f"Missing metadata: {', '.join(missing_meta)}.")

    owner_ok = bool(meta["Owner"] and not PLACEHOLDER_OWNER.match(meta["Owner"]))
    clinical_owner = bool(re.search(r"clinical[^\n|]*(owner|governance|lead|accountable)", record, re.I))
    add(checks, "Business and clinical owners identified", owner_ok and clinical_owner,
        "Responsible business and clinical owners are identified.", "A confirmed business owner and a confirmed clinical owner are required.")

    problem = section(text, "Business View")
    outcome = section(text, "Goal and Business Outcome")
    add(checks, "Problem and outcome completed", "### Problem" in problem and bool(outcome.strip()),
        "Problem and business outcome are documented.", "Problem or business outcome is missing.")

    scope = section(text, "Scope")
    add(checks, "Scope and exclusions completed", "### In scope" in scope and "### Out of scope" in scope,
        "In-scope and out-of-scope behavior is explicit.", "Both in-scope and out-of-scope sections are required.")

    autonomy = bool(re.search(r"autonom|must not.*(diagnos|prescrib|triage|decision)|human.*authority", text, re.I))
    add(checks, "AI autonomy defined", autonomy, "AI role and autonomy boundary are explicit.", "AI autonomy and prohibited decisions are not explicit.")

    oversight = bool(re.search(r"human (review|oversight)|healthcare professional.*(inspect|determin|decid)|clinical governance.*review", text, re.I))
    add(checks, "Human review point defined", oversight, "Meaningful human decision/review points are documented.", "A meaningful human review or decision point is missing.")

    info = section(text, "Information and Data")
    source_known = bool(info and re.search(r"approved knowledge source", info, re.I) and not re.search(r"Which .*sources.*\|\s*Unknown", text, re.I))
    discovery_assigned = bool(re.search(r"Which .*sources.*\|[^\n]*\|\s*(?!Unknown|TBD)[^|\n]+", text, re.I))
    add(checks, "Data sources and owners identified", source_known or discovery_assigned,
        "Required data sources are known or discovery has an assigned owner.", "Data sources are unresolved without a confirmed discovery owner/action.")

    deterministic = all(ids_are_unique(text, prefix) for prefix in ["FR", "AC"])
    add(checks, "Deterministic requirements present", deterministic,
        "Functional requirements and acceptance criteria are labeled and unique.", "Unique, labeled functional requirements and acceptance criteria are required.")

    behavioral = bool(re.search(r"no sufficiently relevant|sources conflict|out(?:side|-of-)scope|dependency.*unavailable", text, re.I))
    add(checks, "AI behavioral requirements present", behavioral,
        "AI behavior covers material alternate and failure conditions.", "AI behavior for missing, conflicting, unsafe, or unavailable evidence is incomplete.")

    metrics = bool(re.search(r"baseline", outcome, re.I) and re.search(r"target", outcome, re.I) and not UNKNOWN.search(outcome))
    add(checks, "Success metrics defined", metrics, "Outcome has approved measurable baseline(s) and target(s).",
        "Metric categories exist, but approved baselines or targets remain unresolved.")

    failures = section(text, "Alternate and Failure Flows")
    risks_ok = bool(failures and len(re.findall(r"^\|", failures, re.M)) >= 4)
    add(checks, "Risks and failure behavior documented", risks_ok,
        "High-impact failure behavior and escalation are documented.", "Material high-impact failure scenarios or escalation behavior are missing.")

    open_questions = section(text, "Assumptions and Open Questions")
    unresolved_rows = [line for line in open_questions.splitlines() if line.startswith("|") and UNKNOWN.search(line)]
    ownerless = [line for line in unresolved_rows if re.search(r"\|\s*(Unknown|TBD|To verify|Sponsor)\s*\|", line, re.I)]
    add(checks, "Open TBD items have an owner", bool(open_questions) and not ownerless,
        "Each unresolved item has a concrete accountable owner/source.", f"{len(ownerless)} unresolved item(s) lack a concrete accountable owner.")

    invalid_links, mermaid_files = markdown_links(text, source, root)
    add(checks, "Links to dependent artifacts are valid", not invalid_links,
        "All repository-relative artifact links resolve.", f"Invalid links: {', '.join(invalid_links)}.")

    pii_patterns = {
        "email address": r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
        "phone number": r"(?<![A-Z0-9-])(?:\+\d{1,3}[ .-]?)?(?:\d[ .-]?){9,12}(?!\d)",
        "patient/MRN identifier": r"\b(?:patient\s*(?:id|number)|mrn)\s*[:#]\s*[A-Z0-9-]{4,}\b",
        "named date of birth": r"\b(?:dob|date of birth)\s*[:#]\s*\d{1,4}[-/.]\d{1,2}[-/.]\d{1,4}\b",
    }
    pii_hits = [label for label, pattern in pii_patterns.items() if re.search(pattern, text, re.I)]
    add(checks, "Documentation contains no known patient identifiers", not pii_hits,
        "Static scan found no known patient-identifier patterns.", f"Potential patient identifiers detected: {', '.join(pii_hits)}.")

    status = meta["Status"].strip().lower()
    reviews_ok, missing_reviewers = reviewer_evidence(text)
    approval_ok = status == "draft" or (status == "reviewed" and bool(section(text, "Stakeholder Feedback Log"))) or (status == "approved" and reviews_ok)
    add(checks, "Approval status is consistent with required reviewers", approval_ok,
        f"Status '{meta['Status']}' is consistent with recorded review evidence.",
        f"Status '{meta['Status']}' is not supported; missing reviewer evidence: {', '.join(missing_reviewers)}.")

    # Mermaid rendering is executed by the workflow; this report declares the inputs.
    checks.insert(14, Check("Mermaid diagrams render successfully", "pending",
                            f"Workflow must render {len(mermaid_files)} linked Mermaid diagram(s)."))

    by_name = {check.name: check for check in checks}
    readiness = [
        ("A responsible business owner exists", owner_ok),
        ("The user and problem are clearly identified", bool(problem and re.search(r"### Users", problem))),
        ("The intended outcome is measurable", metrics),
        ("Scope and exclusions are explicit", by_name["Scope and exclusions completed"].status == "pass"),
        ("Required data sources are known or have assigned discovery actions", source_known or discovery_assigned),
        ("The AI role and autonomy are defined", autonomy),
        ("Human oversight is defined", oversight),
        ("High-impact failure scenarios are documented", risks_ok),
        ("An initial evaluation approach exists", bool(re.search(r"evaluation", text, re.I) and re.search(r"measure", text, re.I))),
        ("Relevant clinical, security, data, and architecture reviewers have participated", reviews_ok),
        ("Remaining unknowns do not prevent a safe POC", not unresolved_rows),
        ("The POC has a proceed, redesign, or stop decision rule", bool(re.search(r"proceed.*redesign.*stop", text, re.I | re.S))),
    ]
    ready = all(passed for _, passed in readiness)

    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    report = {
        "use_case_id": uc_id,
        "use_case_path": source.relative_to(root).as_posix(),
        "document_status": meta["Status"],
        "checks": [asdict(check) for check in checks],
        "mermaid_files": mermaid_files,
        "readiness": {"ready": ready, "criteria": [{"criterion": name, "passed": passed} for name, passed in readiness]},
        "readiness_statement": (
            f"{uc_id} is ready for architecture and POC work."
            if ready else
            f"{uc_id} is not ready for architecture and POC work. Blocking criteria: "
            + "; ".join(name for name, passed in readiness if not passed) + "."
        ),
    }
    (output / "use-case-validation-report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    lines = [f"# Validation report: {uc_id}", "", f"Source: `{report['use_case_path']}`", "", "## Checklist", "",
             "| Check | Result | Finding |", "|---|---|---|"]
    for check in checks:
        lines.append(f"| {check.name} | {check.status.upper()} | {check.detail.replace('|', '/')} |")
    lines += ["", "## Architecture and POC readiness", "", f"**{'READY' if ready else 'NOT READY'}**", "",
              report["readiness_statement"], "", "| Criterion | Result |", "|---|---|"]
    for name, passed in readiness:
        lines.append(f"| {name} | {'PASS' if passed else 'FAIL'} |")
    lines += ["", "> Patient-identifier validation is a conservative static scan and does not replace human privacy review.", ""]
    (output / "use-case-validation-summary.md").write_text("\n".join(lines), encoding="utf-8")

    print(report["readiness_statement"])
    # Pending Mermaid is resolved by the workflow; fail here only on actual checklist/readiness blockers.
    return 1 if any(check.status == "fail" for check in checks) or not ready else 0


if __name__ == "__main__":
    raise SystemExit(main())

