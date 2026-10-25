# Portfolio index

**Kelvin Odarikpe** · maintained index of public security engineering work · last revised October 2026

## How to read the maturity label

| Label | Meaning |
|---|---|
| **LAB** | Runnable lab: code, CI workflow and/or declarative artefacts present. Some need a cloud account, tenant or cluster to execute end-to-end; the readme states which parts run offline. |
| **DOC** | Documented reference: design, SOPs, detection content or a spec with supporting artefacts. Not presented as an executed system. |
| **STUB** | Skeleton awaiting build. Listed for transparency and scheduled for consolidation — see [REPO-CURATION.md](REPO-CURATION.md). |

Nothing here is employer code, tenant export, customer telemetry or audit evidence. All data is synthetic.

---

## 1 · Application security & DevSecOps

| Repo | Maturity | Stack | Demonstrates |
|---|---|---|---|
| [appsec-devsecops-pipeline](https://github.com/kelvinodarikpe88/appsec-devsecops-pipeline) | DOC | GitHub Actions, Semgrep, Gitleaks, Trivy, OSV, Snyk, ZAP, Checkov, tfsec | Full shift-left pipeline: SAST → SCA → secrets → IaC → DAST with gate definitions |
| [09-devsecops-pipeline-security](https://github.com/kelvinodarikpe88/09-devsecops-pipeline-security) | DOC | Semgrep, CodeQL, ZAP, Trivy, SBOM, Cosign | Pipeline security design including artefact signing and SBOM generation |
| [devsecops-pipeline-automation](https://github.com/kelvinodarikpe88/devsecops-pipeline-automation) | DOC | Python, CI | Automated pipeline stages for security tooling |
| [devsecops-pipeline](https://github.com/kelvinodarikpe88/devsecops-pipeline) | DOC | HCL, Terraform | Infrastructure for a DevSecOps toolchain |
| [01-devsecops-pipeline](https://github.com/kelvinodarikpe88/01-devsecops-pipeline) | STUB | Python | Early scaffold, superseded by `appsec-devsecops-pipeline` |
| [devsecops-security-engineering-projects](https://github.com/kelvinodarikpe88/devsecops-security-engineering-projects) | DOC | Multi | Ten-project programme map: SIEM/SOAR, detection as code, CTI, cloud, EDR, identity, AI, CI/CD, metrics |
| [vulnbank](https://github.com/kelvinodarikpe88/vulnbank) | LAB | Python | Deliberately vulnerable target: SQLi, unsigned JWT, IDOR, XSS — used to validate that gates detect what they claim |
| [vulnerability-management-lab](https://github.com/kelvinodarikpe88/vulnerability-management-lab) | LAB | Python, KQL, CI | Exploitability-led triage (CVSS + EPSS + KEV), KEV detection rule, scan scheduling, NIS2 notify template |
| [soar-vulnerability-enrichment-bot](https://github.com/kelvinodarikpe88/soar-vulnerability-enrichment-bot) | STUB | Python | SOAR enrichment for scanner findings, dedup and risk scoring |
| [appsec-framework](https://github.com/kelvinodarikpe88/appsec-framework) | DOC | — | AppSec programme structure and control set |
| [WebGoat](https://github.com/kelvinodarikpe88/WebGoat) | fork | Java | Reference target (upstream OWASP project) |

## 2 · Security architecture

| Repo | Maturity | Stack | Demonstrates |
|---|---|---|---|
| [04-identity-security-architecture](https://github.com/kelvinodarikpe88/04-identity-security-architecture) | LAB | Python, MSAL/Graph, Terraform, OPA, pytest, CI | Reference implementation: PIM-vs-standing detection, Conditional Access baseline audit, policy as code, unit tests in CI |
| [enterprise-soc-production-stack](https://github.com/kelvinodarikpe88/enterprise-soc-production-stack) | LAB | Sentinel/KQL, Elastic, Entra, Okta, Intune, Tenable | Production-equivalent stack with the production/lab boundary stated explicitly |
| [security-portfolio](https://github.com/kelvinodarikpe88/security-portfolio) | DOC | — | Umbrella index of the security engineering portfolio |
| [alerting-detection-strategy-framework](https://github.com/kelvinodarikpe88/alerting-detection-strategy-framework) | fork | — | ADS framework used as a design reference for alert quality |
| [ads-privileged-group-addition](https://github.com/kelvinodarikpe88/ads-privileged-group-addition) | LAB | Shell, AD | Case study: secure privileged group membership change with approval, logging and verification |

## 3 · Detection engineering & security operations

| Repo | Maturity | Stack | Demonstrates |
|---|---|---|---|
| [detection-engineering](https://github.com/kelvinodarikpe88/detection-engineering) | LAB | Sigma, YARA-L, HCL, KQL | Detection-as-code rule library with SOAR playbooks and Google SecOps content |
| [detection-as-code-cicd](https://github.com/kelvinodarikpe88/detection-as-code-cicd) | LAB | YARA-L, Sigma, pytest, GitHub Actions | CI/CD for detection content with automated testing |
| [01-detection-as-code-pipeline](https://github.com/kelvinodarikpe88/01-detection-as-code-pipeline) | DOC | Sigma, Python, CI | Pipeline design: lint → test → compile → deploy with SOC 2 / ISO 42001 evidence |
| [04-detection-as-code](https://github.com/kelvinodarikpe88/04-detection-as-code) | LAB | Sigma, pytest, CI | Minimal rule-as-code reference with tests |
| [mitre-attack-coverage-tracker](https://github.com/kelvinodarikpe88/mitre-attack-coverage-tracker) | LAB | Python | Coverage matrix across AWS, Okta, Entra ID and endpoint telemetry |
| [portfolio-secops-detections](https://github.com/kelvinodarikpe88/portfolio-secops-detections) | LAB | Chronicle YARA-L, Splunk SPL | Multi-platform detection content: Chronicle, Splunk, Defender XDR hunting concepts |
| [03-attack-coverage-tracker](https://github.com/kelvinodarikpe88/03-attack-coverage-tracker) | STUB | Go | Go implementation of the coverage tracker |
| [06-beacon-detector](https://github.com/kelvinodarikpe88/06-beacon-detector) | STUB | Go | Detects regular-interval C2 beaconing in flow logs |
| [soc-automation-platform](https://github.com/kelvinodarikpe88/soc-automation-platform) | LAB | Python | L3 automation: triage, enrichment, evidence collection |
| [03-soc-automation-platform](https://github.com/kelvinodarikpe88/03-soc-automation-platform) | STUB | Python | Earlier scaffold for the same platform |
| [soc-l2-l3-sop-playbooks](https://github.com/kelvinodarikpe88/soc-l2-l3-sop-playbooks) | DOC | — | L2/L3 SOPs, escalation matrices, containment playbooks |
| [10-security-operations-sop](https://github.com/kelvinodarikpe88/10-security-operations-sop) | DOC | — | Daily operating SOPs, comms templates, meeting agendas |
| [soc-analyst-docs](https://github.com/kelvinodarikpe88/soc-analyst-docs) | DOC | — | Incident reports and case-log examples |
| [soc-automation-toolkit](https://github.com/kelvinodarikpe88/soc-automation-toolkit) | STUB | — | Toolkit scaffold |
| [edr-alert-triage-automator](https://github.com/kelvinodarikpe88/edr-alert-triage-automator) | STUB | Python | Process-tree enrichment and high-severity routing |
| [identity-threat-detection-okta-gws](https://github.com/kelvinodarikpe88/identity-threat-detection-okta-gws) | LAB | Python | Rules for Okta SystemLog and Google Workspace identity vectors |
| [cloudtrail-anomaly-detector](https://github.com/kelvinodarikpe88/cloudtrail-anomaly-detector) | STUB | Python | Behavioural analysis of CloudTrail API call sequences |
| [secops-soar-ai-enrichment](https://github.com/kelvinodarikpe88/secops-soar-ai-enrichment) | DOC | Python, LLM | SOAR enrichment with an LLM context layer and approval gate |

## 4 · Cloud security & cloud infrastructure

| Repo | Maturity | Stack | Demonstrates |
|---|---|---|---|
| [cloud-log-integration-aws](https://github.com/kelvinodarikpe88/cloud-log-integration-aws) | LAB | CloudFormation, KQL, CI | CloudTrail/GuardDuty ingestion, GuardDuty crypto-mining rule, TTP matrix, NIS2 notify, coverage evidence |
| [cloud-log-integration-azure](https://github.com/kelvinodarikpe88/cloud-log-integration-azure) | LAB | Python, KQL, CI | Azure Activity / Defender / Entra sign-in pipeline and detections |
| [cloud-log-integration-gcp](https://github.com/kelvinodarikpe88/cloud-log-integration-gcp) | LAB | Python, KQL, CI | GCP Audit Logs / SCC findings pipeline and detections |
| [cloud-soc-detection-lab](https://github.com/kelvinodarikpe88/cloud-soc-detection-lab) | LAB | Python, Terraform | Multi-cloud detection lab: AWS, Azure and GCP events into one detection set |
| [07-cloud-security-posture-management](https://github.com/kelvinodarikpe88/07-cloud-security-posture-management) | DOC | Python | Multi-cloud CIS scanning with auto-remediation matrix and SOC 2 / PCI reporting |
| [cspm-platform](https://github.com/kelvinodarikpe88/cspm-platform) | STUB | Python | CSPM platform scaffold |
| [aws-security-log-pipeline](https://github.com/kelvinodarikpe88/aws-security-log-pipeline) | STUB | Terraform | CloudTrail + CloudWatch ingestion with S3 retention |
| [02-iac-security-gate](https://github.com/kelvinodarikpe88/02-iac-security-gate) | STUB | HCL, Checkov, OPA | Policy gate that rejects non-compliant infrastructure pre-merge |
| [audit-logging-compliance-checker](https://github.com/kelvinodarikpe88/audit-logging-compliance-checker) | STUB | Python | Continuous verification of DORA / PCI-DSS retention requirements |
| [m365-sharepoint-security-lab](https://github.com/kelvinodarikpe88/m365-sharepoint-security-lab) | LAB | Python, KQL, CI | M365 / SharePoint sharing, external access and Conditional Access monitoring |
| [09-security-posture-report](https://github.com/kelvinodarikpe88/09-security-posture-report) | STUB | Shell | Posture reporting scaffold |
| [cloud-soc-integration-lab](https://github.com/kelvinodarikpe88/cloud-soc-integration-lab) | DOC | Shell | Multi-cloud SOC integration: Sentinel, Chronicle, SOAR, Defender, AWS, Azure |

## 5 · Identity, access & non-human identity

| Repo | Maturity | Stack | Demonstrates |
|---|---|---|---|
| [identity-security-lab](https://github.com/kelvinodarikpe88/identity-security-lab) | LAB | Python, Okta API, YARA-L, KQL, CI | Okta collector, impossible-travel and risk-correlation detections, account-compromise playbook, TTP matrix, SOC 2 CC mapping |
| [08-iam-privilege-auditor](https://github.com/kelvinodarikpe88/08-iam-privilege-auditor) | STUB | Python | Finds `iam:PassRole` escalation paths to admin |
| [02-ai-security-compliance](https://github.com/kelvinodarikpe88/02-ai-security-compliance) | DOC | Python | ISO/IEC 42001 AIMS control matrix, risk register, model cards, drift and fairness checks |

## 6 · Workload, container & endpoint security

| Repo | Maturity | Stack | Demonstrates |
|---|---|---|---|
| [container-security-lab](https://github.com/kelvinodarikpe88/container-security-lab) | LAB | Kubernetes, YAML, CI | Admission policy, workload values for production, coverage evidence, NIS2 template |
| [07-cloud-detection-lab](https://github.com/kelvinodarikpe88/07-cloud-detection-lab) | STUB | HCL | Cloud detection lab scaffold |
| [endpoint-security-lab](https://github.com/kelvinodarikpe88/endpoint-security-lab) | LAB | Python, KQL, CI | Endpoint telemetry, triage routing and coverage evidence |
| [network-security-logs-lab](https://github.com/kelvinodarikpe88/network-security-logs-lab) | LAB | Python, KQL, CI | Network telemetry detection set with TTP mapping |

## 7 · API & attack surface

| Repo | Maturity | Stack | Demonstrates |
|---|---|---|---|
| [bugbounty-asset-recon-pipeline](https://github.com/kelvinodarikpe88/bugbounty-asset-recon-pipeline) | STUB | Python | Subdomain → port → HTTP → endpoint inventory pipeline |
| [bugbounty-recon-vulnerability-enrichment](https://github.com/kelvinodarikpe88/bugbounty-recon-vulnerability-enrichment) | STUB | Python | Recon plus Nuclei scanning and vulnerability enrichment |
| [mcp-threat-hunting-agent](https://github.com/kelvinodarikpe88/mcp-threat-hunting-agent) | STUB | Python, MCP | MCP server exposing SIEM query and ATT&CK mapping as tools — an agent-facing API surface with its own threat model |
| [mcp-dfir-investigation-copilot](https://github.com/kelvinodarikpe88/mcp-dfir-investigation-copilot) | STUB | Python, MCP | MCP server exposing forensic memory and log engines to an investigator agent |

## 8 · AI, LLM & agent security

| Repo | Maturity | Stack | Demonstrates |
|---|---|---|---|
| [02-ai-security-compliance](https://github.com/kelvinodarikpe88/02-ai-security-compliance) | DOC | Python, ISO 42001 | AI management system controls with CI-generated evidence |
| [secops-soar-ai-enrichment](https://github.com/kelvinodarikpe88/secops-soar-ai-enrichment) | DOC | Python, LLM | LLM-assisted triage with human approval on containment |
| [mcp-threat-hunting-agent](https://github.com/kelvinodarikpe88/mcp-threat-hunting-agent) | STUB | MCP | Agent tool surface design + scoping |

## 9 · Incident response & DFIR

| Repo | Maturity | Stack | Demonstrates |
|---|---|---|---|
| [05-incident-response-orchestration](https://github.com/kelvinodarikpe88/05-incident-response-orchestration) | DOC | Python | NIST 800-61 lifecycle, evidence collection, chain of custody, approval gates |
| [cloud-forensics-ir-playbook](https://github.com/kelvinodarikpe88/cloud-forensics-ir-playbook) | STUB | Python | AWS/GCP IR: EC2 isolation, EBS snapshot capture |
| [dfir-timeline-super-builder](https://github.com/kelvinodarikpe88/dfir-timeline-super-builder) | STUB | Python | Multi-OS telemetry into a unified incident timeline |
| [memory-forensics-volatility3-automator](https://github.com/kelvinodarikpe88/memory-forensics-volatility3-automator) | STUB | Python, Volatility 3 | RAM analysis for rootkits and injected code |
| [evtx-ransomware-hunting-engine](https://github.com/kelvinodarikpe88/evtx-ransomware-hunting-engine) | STUB | Python | EVTX scanning for persistence and lateral movement |
| [pcap-traffic-carver-zeek](https://github.com/kelvinodarikpe88/pcap-traffic-carver-zeek) | STUB | Python, Zeek | PCAP analysis for C2 beaconing and DNS tunnelling |
| [mac-linux-forensics-collector](https://github.com/kelvinodarikpe88/mac-linux-forensics-collector) | STUB | Python | Live-response artefacts: LaunchDaemons, cron, sockets |
| [malware-static-triage-pipeline](https://github.com/kelvinodarikpe88/malware-static-triage-pipeline) | STUB | Python, YARA | PE analysis, fuzzy hashing, YARA generation |
| [malware-static-dynamic-triage](https://github.com/kelvinodarikpe88/malware-static-dynamic-triage) | STUB | Python | Static + dynamic analysis pipeline |
| [sandbox-cuckoo-report-parser](https://github.com/kelvinodarikpe88/sandbox-cuckoo-report-parser) | STUB | Python | CAPEv2/Cuckoo report → SecOps telemetry |
| [csirt-automation](https://github.com/kelvinodarikpe88/csirt-automation) | DOC | Python | CSIRT automation design |

## 10 · Threat intelligence

| Repo | Maturity | Stack | Demonstrates |
|---|---|---|---|
| [misp-threat-intel-sharing](https://github.com/kelvinodarikpe88/misp-threat-intel-sharing) | LAB | Python, MISP, STIX | Threat intel sharing workflows and IOC lifecycle |
| [cti-platform](https://github.com/kelvinodarikpe88/cti-platform) | DOC | Python | CTI platform design: collection, scoring, dissemination |
| [cti-misp-sync-engine](https://github.com/kelvinodarikpe88/cti-misp-sync-engine) | STUB | Python | MISP STIX/TAXII → SIEM lookup tables |
| [cti-threat-hunting-simulation](https://github.com/kelvinodarikpe88/cti-threat-hunting-simulation) | STUB | Python | APT TTPs → YARA-L hunt hypotheses |
| [08-threat-intelligence-automation](https://github.com/kelvinodarikpe88/08-threat-intelligence-automation) | STUB | — | CTI automation scaffold |

## 11 · Governance, risk & assurance

| Repo | Maturity | Stack | Demonstrates |
|---|---|---|---|
| [compliance-audit-dora-pci-forensics](https://github.com/kelvinodarikpe88/compliance-audit-dora-pci-forensics) | STUB | Python | Log integrity and chain-of-custody for DORA / PCI-DSS |
| [vuln-management](https://github.com/kelvinodarikpe88/vuln-management) | LAB | Python | Vulnerability management workflow and reporting |
| [06-central-log-analysis](https://github.com/kelvinodarikpe88/06-central-log-analysis) | DOC | ELK, Kafka | Central logging: ECS normalisation, parsers, CC4.1 mapping |
| [secops-master-suite](https://github.com/kelvinodarikpe88/secops-master-suite) | STUB | Python | Suite scaffold |

---

## Maintenance

Repos labelled **STUB** are being consolidated: three or four real implementations replace a larger number of skeletons, and superseded repos are archived rather than deleted so links keep resolving. The plan, with per-repo decisions, is in [REPO-CURATION.md](REPO-CURATION.md).

Profile overview: [README](../README.md) · Architecture model: [ARCHITECTURE.md](ARCHITECTURE.md)
