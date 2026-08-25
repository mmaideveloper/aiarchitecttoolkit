# AI Solution Final Review Method

Use this ledger:

| Gate area | Requirement or risk | Required evidence | Current evidence and date | Status | Owner/action |
|---|---|---|---|---|---|
| <area> | <traceable requirement/risk> | <test, review, approval, runbook, telemetry> | <source and scope> | Pass / Conditional / Fail / Not verified / Not applicable | <owner and action> |

Minimum gate areas when applicable:

- Product acceptance and architecture conformance
- Model/provider/version identity and change controls
- Representative offline and online evaluation, thresholds, datasets, limitations, and regression evidence
- Threat model, security review, privacy/data lifecycle, safety, abuse controls, and human oversight
- Reliability targets, load/capacity, dependency failure, recovery, rollback, observability, incident response, and support ownership
- Transparency, user recourse, accessibility, records/traceability, third-party terms, and regulatory applicability
- Cost envelope and operational sustainability

Evidence is current only when it matches the reviewed release candidate and environment, remains within its validity period, and covers the relevant users, languages, data, failure modes, and integrations. Note sampling limits and uncertainty. A condition must be specific, measurable, owned, time-bound or trigger-bound, and non-blocking under an evidenced gate policy.
