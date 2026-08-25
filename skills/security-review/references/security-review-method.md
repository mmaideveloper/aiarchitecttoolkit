# Security Review Method

Use this evidence matrix:

| Asset or boundary | Threat scenario | Expected control | Evidence | Effectiveness | Finding/action |
|---|---|---|---|---|---|
| <asset/boundary> | <credible attacker action> | <requirement/control> | <artifact, file:line, configuration, test, or runtime evidence> | Effective / Partial / Ineffective / Not verified / Not applicable | <risk and action> |

Rate findings using likelihood and impact in the project-defined risk model. If none exists, use:

- `Critical`: credible path to catastrophic safety, confidentiality, integrity, availability, tenant-isolation, or irreversible-data impact; stop release.
- `High`: exploitable or likely material impact with inadequate prevention or detection; resolve before release unless an authorized exception exists.
- `Medium`: meaningful defense-in-depth, monitoring, recovery, or hardening gap.
- `Low`: limited exposure or security-maintainability weakness.

For every finding include: identifier, severity, affected scope, scenario, evidence, impact, likelihood rationale, remediation, verification method, owner if known, and related architecture requirement or decision. Record uncertainty instead of inflating confidence.
