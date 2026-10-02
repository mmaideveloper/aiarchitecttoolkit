# CZ/SK healthcare AI compliance discovery example

Use this optional project-neutral companion to the healthcare profile with `$compliance-review`. It is a candidate discovery guide, not a verified legal inventory or a classification decision. Select CZ, SK, or both from the actual business scope. Keep internal organizational policy in a project profile or approved source folder.

## Configuration to supply at invocation

- Business purpose and intended clinical/administrative use: to establish.
- Operating jurisdictions, organizational roles and deployment date: to establish.
- Architecture artifact paths: user supplied.
- Local regulation index/register: optional user-supplied path; read-only.
- Internal compliance folder/register: ask explicitly; may be none, unknown or unavailable.
- Research: official sources plus supplied documents by default; supplied-sources-only if requested, with currency limitations.

## Candidate sources and routing questions

The identifiers below are discovery leads from a supplied archive, not findings that any instrument applies. Read the governing provisions and verify amendments and timing at review time. No dates or legal classifications are fixed by this example.

| Candidate | Investigate when / questions | Official discovery source |
|---|---|---|
| GDPR, Regulation (EU) 2016/679 | What personal-data processing, purposes, parties, health data and transfers are evidenced? | [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj) |
| AI Act, Regulation (EU) 2024/1689 | What AI functions, intended purposes and operator roles are involved? Which provisions and application dates govern? | [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) |
| MDR 2017/745 and IVDR 2017/746 | Are there medical/in-vitro diagnostic intended uses or product claims? Is a classification assessment available? | [MDR](https://eur-lex.europa.eu/eli/reg/2017/745/oj), [IVDR](https://eur-lex.europa.eu/eli/reg/2017/746/oj) |
| NIS2 2022/2555 and national cybersecurity requirements | What entity/service scope and national regime are evidenced? | [NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) |
| EHDS 2025/327 | What health-data use, EHR functionality and primary/secondary use are in scope? Verify phased provisions. | [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2025/327/oj) |
| Cyber Resilience Act 2024/2847; product liability 2024/2853 | What product/supply role, exclusions, dependencies and national implementation matter? | [CRA](https://eur-lex.europa.eu/eli/reg/2024/2847/oj), [Product liability](https://eur-lex.europa.eu/eli/dir/2024/2853/oj) |
| CZ healthcare, records, e-health, privacy, devices, cybersecurity | Discover 372/2011, 444/2024, 325/2021, 110/2019, 375/2022, 264/2025 and implementing rules 408/2025, 409/2025, 410/2025. Verify current text and relevance separately. | [e-Sbirka](https://e-sbirka.gov.cz/), [NUKIB](https://nukib.gov.cz/), [SUKL CZ](https://sukl.gov.cz/) |
| SK healthcare, providers, national health information, privacy, devices, cybersecurity | Discover 576/2004, 578/2004, 153/2013, 18/2018, 362/2011, 69/2018 and amendment 366/2024. Verify current text and relevance separately. | [Slov-Lex](https://www.slov-lex.sk/), [NBU](https://www.nbu.gov.sk/), [SUKL SK](https://www.sukl.sk/) |
| MDCG and regulator guidance | What device/AI interaction or in-house-use questions require interpretation? Guidance is distinct from legislation. | [European Commission medical devices](https://health.ec.europa.eu/medical-devices-sector_en) |
| ISO 13485, ISO 14971, IEC 62304, IEC 62366-1 | Is a specific edition required by law, contract or policy? Is licensed text available for review? | [ISO](https://www.iso.org/standards.html), [IEC](https://webstore.iec.ch/) |

Check other concerns driven by intake, including accessibility, employment, procurement, research and contractual requirements. The table is not exhaustive. An archive may contain historical telemedicine guidance, proposed/amending instruments or original and consolidated versions; do not treat them as interchangeable or current without verification.

## Synthetic invocation

> Use $compliance-review for a proposed healthcare AI architecture operating in CZ and SK. First ask about intended use, roles, data flows and launch date, prepare a candidate obligation list, and ask for our internal compliance folder. Compare applicable provisions with the supplied architecture and return prioritized recommendations with official links. All architecture examples are synthetic.

## Provenance and limitations

Candidate names were observed in the user-supplied local index. See [authoring source evidence](../docs/compliance-skill-source-evidence.json) for its exact path, modification timestamp and SHA-256. Only the index was processed; linked PDFs and policy documents were not reviewed. Official portal checks on 2026-10-02 required JavaScript or presented challenges; no current legal provisions, dates or archive amendment claims were validated during skill creation. Reverify sources when performing an actual assessment.
