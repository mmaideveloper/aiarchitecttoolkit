# Azure Review Method

Use a workload-specific matrix:

| Area | Requirement or target | Azure design/configuration | Evidence | Result | Finding/action |
|---|---|---|---|---|---|
| <area> | <SLO, RTO/RPO, policy, constraint> | <service and pattern> | <ADR, IaC, policy, test, telemetry, official guidance> | Meets / Partially meets / Does not meet / Not verified / Not applicable | <action> |

Review the current Azure Well-Architected pillars—reliability, security, cost optimization, operational excellence, and performance efficiency—plus governance, sustainability, and migration/exit constraints when relevant. Weight them using documented business and quality-attribute priorities rather than averaging scores blindly.

Severity:

- `Critical`: credible severe security, compliance, data-loss, or broad outage risk; stop release.
- `High`: required SLO, recovery target, policy, or accepted architecture decision is unlikely to be met.
- `Medium`: material operability, cost, scaling, resilience, or governance weakness.
- `Low`: localized optimization or maintainability issue.

Record the authoritative URL and access date for time-sensitive Azure facts. When evidence conflicts, prefer observable current configuration for deployed-state claims and authoritative approved artifacts for intended-state claims; report the drift explicitly.
