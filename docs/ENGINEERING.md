# Engineering portfolio — detailed reference

[Return to the profile](../README.md) · [Hiring brief](HIRING.md) · [Metrics ledger](METRICS.md)

This reference preserves the detailed domain material. Public projects demonstrate methods; employer outcome figures remain owner-reported unless the ledger states otherwise.

## The model I build against

Four planes, one feedback loop. Every repo below maps to a cell in this model — not to a tool list.

<img src="https://raw.githubusercontent.com/kelvinodarikpe88/kelvinodarikpe88/main/assets/planes.svg?v=3" alt="Operating model. Four planes with one feedback loop. 01 SHIP, shift left: threat model, code and supply chain, infrastructure-as-code and policy gates. 02 RUN, control planes: identity and access, cloud posture, workloads. 03 DEFEND, detect and respond: detection as code, AI-assisted triage behind a human gate, incident response and DFIR. 04 PROVE, evidence: continuous evidence, ATT and CK coverage, audit readiness. The feedback loop re-enters 01 SHIP." width="100%">

The loop that closes the model: **every incident becomes a test case, and every repeated gap becomes a policy.** Detection without that feedback is a cost centre; with it, it is how the architecture gets better.

| Plane | Control objective | Where it is implemented |
|---|---|---|
| **Identity** | No standing privilege; access is time-bound, reviewed and attributable | [identity-security-lab](https://github.com/kelvinodarikpe88/identity-security-lab) · [04-identity-security-architecture](https://github.com/kelvinodarikpe88/04-identity-security-architecture) · [08-iam-privilege-auditor](https://github.com/kelvinodarikpe88/08-iam-privilege-auditor) |
| **Workloads** | A compromised container cannot escalate, persist or reach the control plane | [container-security-lab](https://github.com/kelvinodarikpe88/container-security-lab) · [07-cloud-detection-lab](https://github.com/kelvinodarikpe88/07-cloud-detection-lab) |
| **APIs** | Every object is authorized server-side, per tenant, per verb | [vulnbank](https://github.com/kelvinodarikpe88/vulnbank) · [bugbounty-asset-recon-pipeline](https://github.com/kelvinodarikpe88/bugbounty-asset-recon-pipeline) |
| **Cloud infrastructure** | Drift is detected and reverted; audit logs are complete and tamper-evident | [cloud-log-integration-aws](https://github.com/kelvinodarikpe88/cloud-log-integration-aws) · [07-cloud-security-posture-management](https://github.com/kelvinodarikpe88/07-cloud-security-posture-management) · [cloud-soc-detection-lab](https://github.com/kelvinodarikpe88/cloud-soc-detection-lab) |
| **Detection** | Every rule has a test, an owner, an ATT&CK mapping and an FP budget | [detection-engineering](https://github.com/kelvinodarikpe88/detection-engineering) · [detection-as-code-cicd](https://github.com/kelvinodarikpe88/detection-as-code-cicd) · [mitre-attack-coverage-tracker](https://github.com/kelvinodarikpe88/mitre-attack-coverage-tracker) |
| **Response** | Containment is pre-approved, reversible and evidenced | [05-incident-response-orchestration](https://github.com/kelvinodarikpe88/05-incident-response-orchestration) · [cloud-forensics-ir-playbook](https://github.com/kelvinodarikpe88/cloud-forensics-ir-playbook) |
| **Governance** | Controls produce evidence continuously, not the week before the audit | [02-ai-security-compliance](https://github.com/kelvinodarikpe88/02-ai-security-compliance) · [audit-logging-compliance-checker](https://github.com/kelvinodarikpe88/audit-logging-compliance-checker) |

Full reasoning, trust boundaries and threat model: **[docs/ARCHITECTURE.md](ARCHITECTURE.md)**

---

## Application security

The part of the job I care most about: making the secure path the path of least resistance for engineers who have a deadline.

**Outcome:** open critical vulnerabilities **847 → 187** and remediation cycle **67 → 12 days**, both measured against a fixed asset scope with re-open rate and regression rate as the counter-metrics — **M-04**, **M-05** in the [ledger](METRICS.md).

| Layer | What I build | Repo |
|---|---|---|
| **Design** | STRIDE per trust boundary, abuse cases, identity attack-path graphs, security requirements as acceptance criteria | [devsecops-security-engineering-projects](https://github.com/kelvinodarikpe88/devsecops-security-engineering-projects) |
| **Build** | SAST (Semgrep/CodeQL), SCA (Trivy/OSV/Snyk), secret scanning (Gitleaks), SBOM + signing, DAST (ZAP), all failing the build on policy | [appsec-devsecops-pipeline](https://github.com/kelvinodarikpe88/appsec-devsecops-pipeline) · [09-devsecops-pipeline-security](https://github.com/kelvinodarikpe88/09-devsecops-pipeline-security) |
| **Prove** | Deliberately vulnerable target app — SQLi, unsigned JWT, IDOR, XSS — used to validate that the gates actually catch what they claim | [vulnbank](https://github.com/kelvinodarikpe88/vulnbank) |
| **Triage** | Exploitability-led prioritisation: CVSS v3.1 + EPSS + CISA KEV + reachability, deduplicated PoC evidence | [vulnerability-management-lab](https://github.com/kelvinodarikpe88/vulnerability-management-lab) · [soar-vulnerability-enrichment-bot](https://github.com/kelvinodarikpe88/soar-vulnerability-enrichment-bot) |

Operating principle: a scanner finding nobody can reproduce is noise. Every finding ships with a reproduction, an owner and a deadline derived from exploitability — not from a vendor severity label.

---

## Security architecture

Architecture is where I try to spend my credibility: choosing the boundary, then proving the boundary holds under failure.

**Outcome:** standing privileged access **−68%**, with break-glass activations and JIT approval latency tracked so the reduction cannot be bought by making access too slow to use — **M-03** in the [ledger](METRICS.md).

- **Identity-first threat modelling.** Model the attack path (`user → role → workload identity → control plane`), then remove the edge rather than adding a monitor on top of it.
- **Zero-trust segmentation.** Conditional Access and device-compliance signals as the enforcement point; legacy auth blocked by default; risk-based step-up instead of static VPN trust.
- **Policy as code.** The architecture diagram and the OPA/Rego policy are the same artefact — if it is not enforced in CI and at admission time, it is documentation, not a control.
- **Failure modes designed, not discovered.** What happens when the IdP is down, the log pipeline backs up, or a break-glass account is used at 03:00 — written before the incident.

Reference implementation: [04-identity-security-architecture](https://github.com/kelvinodarikpe88/04-identity-security-architecture) — MSAL Graph client, PIM-vs-standing-role detection, Conditional Access baseline audit, Terraform policy layer, OPA least-privilege policy, pytest + CI.

<img src="https://raw.githubusercontent.com/kelvinodarikpe88/kelvinodarikpe88/main/assets/trust-boundaries.svg?v=3" alt="Reference architecture. Five zones — untrusted, edge, workload, data, control — with the control that must hold at each boundary, the request path and the telemetry path drawn separately, and a design-assumptions panel." width="100%">

**Reading the diagram.** Every vertical boundary has to authenticate, authorise and log independently — a boundary that inherits trust from the zone beside it is not a boundary. The request path and the telemetry path are drawn separately on purpose: a control that only observes the request path is blind to anything that moves east-west. The assumption I would attack first is boundary 3, where the data zone trusts the workload zone to hold scoped credentials. That assumption is exactly what failed in October 2026: Railway disclosed that encrypted customer environment variables were accessed and, for a subset, **decrypted contents obtained** — encryption at rest did not help because the key material lived inside the same trust zone as the ciphertext. Zeabur's two 2026 incidents reached further through a different edge of the same assumption: long-lived administrative credentials held recoverably in a platform database, and 3.2 million environment-variable records read with them. Neither was a cryptography failure. Both were a key-custody and blast-radius failure.

---

## Detection engineering & security operations

**Outcome:** mean time to detect **−62%** and false positives **12% → 6%**, with alert volume and true-positive coverage held flat as the counter-metrics, and every rule change behind a CI gate — **M-01**, **M-02**, **M-08** in the [ledger](METRICS.md).

| Capability | Approach | Repo |
|---|---|---|
| **Rule lifecycle** | Sigma/YARA-L in Git → lint → unit test → compile to KQL → deploy → measure FP rate | [detection-engineering](https://github.com/kelvinodarikpe88/detection-engineering) · [detection-as-code-cicd](https://github.com/kelvinodarikpe88/detection-as-code-cicd) |
| **Coverage** | ATT&CK technique → telemetry source → rule → test case, gaps reported as data not opinion | [mitre-attack-coverage-tracker](https://github.com/kelvinodarikpe88/mitre-attack-coverage-tracker) |
| **Identity detection** | Okta SystemLog + Google Workspace + Entra: impossible travel, MFA fatigue, token replay, OAuth consent abuse | [identity-threat-detection-okta-gws](https://github.com/kelvinodarikpe88/identity-threat-detection-okta-gws) · [identity-security-lab](https://github.com/kelvinodarikpe88/identity-security-lab) |
| **Cloud detection** | CloudTrail/GuardDuty behaviour, crypto-mining, anomalous `AssumeRole` chains, S3 exposure | [cloud-soc-detection-lab](https://github.com/kelvinodarikpe88/cloud-soc-detection-lab) · [cloudtrail-anomaly-detector](https://github.com/kelvinodarikpe88/cloudtrail-anomaly-detector) |
| **Hunting** | Hypothesis-driven hunts mapped to TTPs, results feeding back into rules | [portfolio-secops-detections](https://github.com/kelvinodarikpe88/portfolio-secops-detections) · [cti-threat-hunting-simulation](https://github.com/kelvinodarikpe88/cti-threat-hunting-simulation) |
| **Operations** | L1–L3 SOPs, escalation matrices, comms templates, post-incident rule updates | [soc-l2-l3-sop-playbooks](https://github.com/kelvinodarikpe88/soc-l2-l3-sop-playbooks) · [10-security-operations-sop](https://github.com/kelvinodarikpe88/10-security-operations-sop) |

The production-equivalent stack — Sentinel/KQL, Elastic, Entra/Okta/Intune, Tenable/Qualys finding model — is documented, with the production/lab boundary stated explicitly, in [enterprise-soc-production-stack](https://github.com/kelvinodarikpe88/enterprise-soc-production-stack).

---

## Security automation

Automation is how a small team covers a cloud estate, and it is the fastest way to cause an outage with good intentions. So the design target is not "less human work". It is: **every automated action has a bounded blast radius, a reversal path and an evidence record written by the action itself** — and the expensive irreversible decisions stay behind a named human.

**Outcome:** every containment action emits its own evidence record (actor, target, before/after, approver, reversal command) and every cap — 50 indicators per run, one account per run, 72-hour host isolation — is testable code, not a runbook promise. The metric here is the reversal time, not the volume of automation.

<img src="https://raw.githubusercontent.com/kelvinodarikpe88/kelvinodarikpe88/main/assets/ai-loop.svg?v=3" alt="AI-automated security pipeline. SIGNAL ingest, DETECT rules as code, ENRICH with AI context, DECIDE with tiered authority, ACT bounded and reversible, then a human authority gate. Side panel lists agent guardrails: least-privilege tool scope per agent, retrieved content treated as untrusted input, kill switch and dry-run on every playbook, evidence as the output." width="100%">

| Stage | What runs | What it may do alone | Reversal | Evidence emitted |
|---|---|---|---|---|
| **Enrich** | Asset, identity and threat context on every alert — owner, exposure, EPSS, KEV status, last-seen | Anything read-only, unbounded | none needed, no state change | Enrichment snapshot attached to the case |
| **Decide** | Severity and disposition from correlated context, not the vendor label | Propose only | none needed | Reasoning trace and inputs kept with the case |
| **Ticket** | Case creation, deduplication, owner routing | Create and merge tickets | Close ticket | Ticket ID paired to alert ID |
| **Block indicator** | Edge, DNS and proxy blocks from confirmed IOCs | **Capped at 50 indicators per run, 24-hour TTL** | Auto-expiry plus one-command unblock | Indicator, source, scope, expiry |
| **Disable account** | IdP session revoke and account disable | Only on high-confidence identity compromise, one account per run | Re-enable runbook, with group memberships captured before the change | Before/after state, approver, timestamp |
| **Isolate host** | EDR network containment | Requires an approval click; auto-releases after 72 hours | One-click release | Host, reason, approver, release time |
| **Rotate credential** | Short-lived credential issued via OIDC, old key disabled | Never deletes, disables and waits | Re-enable if rotation fails | Key ID, issue time, consumer |

**Five non-negotiables**

1. **Dry-run is the default.** Every playbook ships with a `--dry-run` that prints the exact action list it would take. Enabling it is a separate, reviewed change with a named owner.
2. **Blast-radius caps live in code, not in a runbook.** Per-run ceilings on objects touched, accounts disabled and indicators blocked, so a loop bug cannot disable a tenant at 03:00.
3. **Idempotent and convergent.** Rerunning a playbook mid-incident has to be safe. Actions key off desired state rather than fire-once side effects.
4. **No standing credentials in the automation.** Runners authenticate through OIDC to a short-lived role. The automation never holds a permanent key to the systems it is allowed to change.
5. **Per-action evidence, produced at execution time.** Actor, target, before/after, approval, timestamp and the reversal command. The audit trail is a by-product, not a form filled in afterwards.

**Where the AI sits, and where it stops.** Enrichment, correlation, summarisation and first-draft disposition are the work that is expensive by hand and cheap to review, so the model does those. Containment a human cannot reverse in under a minute stays behind an explicit gate: named approver, stated blast radius, one action at a time. Prompts, tool scopes and retrieved content are treated as attack surface — least-privilege tool access per agent, retrieved documents as untrusted input, and a kill switch on every agent loop.

Repos: [secops-soar-ai-enrichment](https://github.com/kelvinodarikpe88/secops-soar-ai-enrichment) · [soar-vulnerability-enrichment-bot](https://github.com/kelvinodarikpe88/soar-vulnerability-enrichment-bot) · [05-incident-response-orchestration](https://github.com/kelvinodarikpe88/05-incident-response-orchestration) · [detection-as-code-cicd](https://github.com/kelvinodarikpe88/detection-as-code-cicd)

---

## Cloud security & cloud infrastructure

**Outcome:** critical findings down **847 → 187** with EPSS + KEV triage and a receipt for every retention and deletion check; the counter-metric is the re-open rate, because a posture number that falls by re-scoping assets has reduced nothing — **M-04** in the [ledger](METRICS.md).

| Domain | What I build | Repo |
|---|---|---|
| **Posture** | Multi-cloud CIS scanning with auto-remediation, drift detection, SOC 2 / PCI-DSS reporting | [07-cloud-security-posture-management](https://github.com/kelvinodarikpe88/07-cloud-security-posture-management) · [cspm-platform](https://github.com/kelvinodarikpe88/cspm-platform) |
| **Telemetry** | CloudTrail/GuardDuty, Azure Activity + Defender, GCP Audit + SCC → normalised, retained, queryable | [cloud-log-integration-aws](https://github.com/kelvinodarikpe88/cloud-log-integration-aws) · [cloud-log-integration-azure](https://github.com/kelvinodarikpe88/cloud-log-integration-azure) · [cloud-log-integration-gcp](https://github.com/kelvinodarikpe88/cloud-log-integration-gcp) |
| **Infrastructure as code** | Terraform/CloudFormation with policy gates that reject public buckets, open SGs and unencrypted volumes pre-merge | [aws-security-log-pipeline](https://github.com/kelvinodarikpe88/aws-security-log-pipeline) · [02-iac-security-gate](https://github.com/kelvinodarikpe88/02-iac-security-gate) |
| **Retention & integrity** | Continuous checks that log retention, immutability and chain-of-custody satisfy DORA / PCI-DSS / NIS2 | [audit-logging-compliance-checker](https://github.com/kelvinodarikpe88/audit-logging-compliance-checker) · [compliance-audit-dora-pci-forensics](https://github.com/kelvinodarikpe88/compliance-audit-dora-pci-forensics) |
| **Hybrid identity surface** | M365 / SharePoint / Entra conditional access, sharing policy and external-access review | [m365-sharepoint-security-lab](https://github.com/kelvinodarikpe88/m365-sharepoint-security-lab) |

---

## Identity, access & non-human identity

Identity is the highest-leverage control plane in a cloud-native estate, and the one most often reviewed annually and violated daily.

**Outcome:** standing privileged access **−68%** and joiners/movers/leavers **84% automated**, with break-glass count, JIT latency and orphaned-account count as the counter-metrics — **M-03**, **M-06** in the [ledger](METRICS.md).

- **PIM eligibility vs standing assignment** — treat any high-privilege role held as a standing assignment as critical, regardless of holder or age. Implemented in [04-identity-security-architecture](https://github.com/kelvinodarikpe88/04-identity-security-architecture).
- **Conditional Access baseline auditing** — re-derive compliance from live policy state on every run instead of trusting a one-time configuration.
- **JML automation** — joiner/mover/leaver provisioning to ~84% automated across Entra ID, Okta and Google Workspace, with access reviews that produce evidence.
- **Privilege escalation paths** — `iam:PassRole` → admin, AD privileged group membership, service-account key sprawl: [08-iam-privilege-auditor](https://github.com/kelvinodarikpe88/08-iam-privilege-auditor) · [ads-privileged-group-addition](https://github.com/kelvinodarikpe88/ads-privileged-group-addition)
- **Non-human identity** — service accounts, workload identities, API keys and MCP/agent identities: owner, scope, rotation, last-used. This is the gap I see most often in audit findings.

---

## Workload, container & Kubernetes security

- **Admission and runtime** — policy at admission (no `:latest`, no privileged, no hostPath, resource limits required) plus runtime detection for shell-in-container, unexpected egress and crypto-mining.
- **Supply chain** — image scanning, SBOM generation, signature verification, and provenance before an image is allowed to run.
- **Kubernetes audit telemetry** — API server audit logs normalised into the same detection pipeline as cloud and identity events, so a `create pods/exec` is correlated with the identity that did it.
- **Blast radius** — namespace isolation, network policy defaults, workload identity instead of node-level credentials.

Repos: [container-security-lab](https://github.com/kelvinodarikpe88/container-security-lab) · [07-cloud-detection-lab](https://github.com/kelvinodarikpe88/07-cloud-detection-lab) · [09-devsecops-pipeline-security](https://github.com/kelvinodarikpe88/09-devsecops-pipeline-security)

---

## API & attack surface security

APIs are where authorization bugs become data breaches, so this is where I test hardest.

| Focus | Method | Repo |
|---|---|---|
| **Object-level authorization** | Two-tenant harness: replay every documented request as tenant B against tenant A's object IDs; diff documented vs observed behaviour | [vulnbank](https://github.com/kelvinodarikpe88/vulnbank) · `idor_check.py` in the AppSec tooling |
| **Surface discovery** | Subdomain → port → HTTP fingerprint → endpoint inventory → parameter discovery, deduplicated and scoped | [bugbounty-asset-recon-pipeline](https://github.com/kelvinodarikpe88/bugbounty-asset-recon-pipeline) · [bugbounty-recon-vulnerability-enrichment](https://github.com/kelvinodarikpe88/bugbounty-recon-vulnerability-enrichment) |
| **AuthN/AuthZ review** | Token handling, JWT algorithm confusion, scope/role confusion, machine-to-machine credentials, OAuth consent grants | [vulnbank](https://github.com/kelvinodarikpe88/vulnbank) |
| **API-shaped machine interfaces** | MCP servers and agent tool surfaces treated as authenticated APIs with their own threat model | [mcp-threat-hunting-agent](https://github.com/kelvinodarikpe88/mcp-threat-hunting-agent) · [mcp-dfir-investigation-copilot](https://github.com/kelvinodarikpe88/mcp-dfir-investigation-copilot) |

---

## AI, LLM & agent security

- **AI governance with evidence** — ISO/IEC 42001 AIMS control matrix, model cards, risk classification, drift and fairness checks wired into CI: [02-ai-security-compliance](https://github.com/kelvinodarikpe88/02-ai-security-compliance).
- **LLM application threat model** — OWASP Top 10 for LLM Applications and MITRE ATLAS mapped onto retrieval, context assembly, tool calling and agent loops; indirect prompt injection treated as an input-validation problem with a tenant-isolation blast radius.
- **AI inside the SOC** — enrichment and triage copilots that keep a human approval gate on every containment action: [secops-soar-ai-enrichment](https://github.com/kelvinodarikpe88/secops-soar-ai-enrichment).

---

## Data protection & privacy engineering

Privacy engineering fails in the same place every time: the classification exists in a policy document, the copy exists in a warehouse, and nobody can say which columns hold personal data or how long they are allowed to live.

**Outcome:** no production metric is claimed for this domain, and that is the honest answer — none of the eight outcomes above belongs to privacy engineering. What exists is design plus an executable two-tenant test, marked `designed` in the coverage matrix. A privacy number invented for this section would undermine every number that is real.

**The four questions I design around**

| Question | Control | How it is proven |
|---|---|---|
| **Where is personal data, and what is it?** | Column-level classification propagated from the catalog into the pipeline. A new table with an untagged `email`, `name` or `ip` column fails CI | Classification coverage report, plus the untagged-column gate in the pipeline |
| **Who is allowed to see it?** | Row-level security per tenant, dynamic masking for support and analytics roles, and no shared read-only "analytics" account | Two-tenant RLS test: tenant B querying tenant A's key returns zero rows |
| **How long does it live?** | Retention as code per dataset class. Deletion is a job that produces a receipt, not a ticket | Deletion receipt: object count before and after, backup expiry date, systems enumerated |
| **Can I prove any of it?** | DSAR (GDPR Art. 15) and erasure (Art. 17) run as a scripted, logged workflow across primary store, warehouse and backups | Timestamped export bundle per request, with the list of systems that answered |

**Logs and telemetry are personal data.** Most privacy debt accumulates in the SIEM: usernames, source IPs, URLs with query strings, email bodies, prompt text — retained for 400 days because nobody chose a number. Retention is set per data class, fields needed only for correlation are hashed or tokenised, and access to raw telemetry is itself access-logged.

**The failure mode I design against.** A platform leaks its database and the ciphertext is worthless to the attacker, until the key turns out to sit in the same environment, guarded by the same boundary, readable by the same compromised process. In October 2026 Railway confirmed that encrypted customer environment variables were accessed and, for a subset of users, **decrypted contents were obtained**. Zeabur's second incident, over 14–15 October 2026, exposed **3,218,965 environment-variable records and 321,810 accounts** read from a production database that also held platform credentials the attacker could use directly. The lesson is architectural, not cryptographic: **envelope encryption with a KMS-held key-encryption key and a per-tenant data key**, so a stolen backup, snapshot or `DATABASE_URL` decrypts to nothing without an independent KMS authorisation that is itself logged. Secrets never live beside the data they protect, key custody is a separate blast radius, and rotation is a scheduled job rather than an incident.

**Frameworks wired into the work, not cited at the end of it:** GDPR Art. 5 (minimisation, storage limitation), Art. 25 (protection by design), Art. 30 (processing records generated from the catalog), Art. 32 (encryption and access control), Art. 15 and 17 (access and erasure as code); DORA Art. 9–12 (ICT risk and incident reporting); NIS2; and the transparency and data-governance duties of the EU AI Act for the AI systems in this portfolio.

**Where this sits honestly.** Classification, retention and DSAR workflows here are designed and documented; the RLS and masking checks are executable against the two-tenant harness. Across the public artifacts this domain is `designed`, not `enforced` — the coverage matrix below says so in the cell, not in a footnote.

Repos: [compliance-audit-dora-pci-forensics](https://github.com/kelvinodarikpe88/compliance-audit-dora-pci-forensics) · [02-ai-security-compliance](https://github.com/kelvinodarikpe88/02-ai-security-compliance) · [audit-logging-compliance-checker](https://github.com/kelvinodarikpe88/audit-logging-compliance-checker) · [m365-sharepoint-security-lab](https://github.com/kelvinodarikpe88/m365-sharepoint-security-lab)

---

## Incident response & DFIR

NIST 800-61 lifecycle with evidence handling that survives a regulator's questions.

[05-incident-response-orchestration](https://github.com/kelvinodarikpe88/05-incident-response-orchestration) · [cloud-forensics-ir-playbook](https://github.com/kelvinodarikpe88/cloud-forensics-ir-playbook) · [dfir-timeline-super-builder](https://github.com/kelvinodarikpe88/dfir-timeline-super-builder) · [memory-forensics-volatility3-automator](https://github.com/kelvinodarikpe88/memory-forensics-volatility3-automator) · [evtx-ransomware-hunting-engine](https://github.com/kelvinodarikpe88/evtx-ransomware-hunting-engine) · [pcap-traffic-carver-zeek](https://github.com/kelvinodarikpe88/pcap-traffic-carver-zeek) · [mac-linux-forensics-collector](https://github.com/kelvinodarikpe88/mac-linux-forensics-collector)

---

## What a CISO should read first

If you have four minutes and one question — *can this person carry a control from design to audit evidence without a project manager holding it together?* — read these two diagrams and the four answers below them.

<img src="https://raw.githubusercontent.com/kelvinodarikpe88/kelvinodarikpe88/main/assets/ciso-matrix.svg?v=3" alt="Control coverage matrix. Rows are ten control domains; columns are SOC 2, ISO 27001, NIST CSF, DORA and NIS2, and the EU AI Act. Filled markers mean enforced in CI or at runtime, half markers mean designed and documented, hollow markers mean a named gap. Third-party risk and EU AI Act conformity are the two areas deliberately thin." width="100%">

**How to read the matrix.** Rows are control domains, columns are the frameworks a security programme is actually audited against. **Filled** means enforced in CI or at runtime — it blocks something. **Half** means designed and documented but not enforced end to end. **Hollow** means a gap. A coverage matrix with no hollow cells is a marketing asset, not an assessment, so the two thin areas are named rather than shaded: **third-party risk** (there is no vendor estate here to assess, so the workflow is designed and unexercised) and **EU AI Act conformity**, which is still moving and is tracked rather than claimed. Supply chain and privacy engineering sit at `designed` across all four frameworks, which is the accurate description of reference work rather than deployed programme work.

<img src="https://raw.githubusercontent.com/kelvinodarikpe88/kelvinodarikpe88/main/assets/maturity-ladder.svg?v=3" alt="Maturity ladder in four levels. L4 enforced: blocks the merge or the request, runs in CI or at runtime. L3 tested: executable with a test suite and a CI workflow. L2 lab: runs against synthetic data and needs a tenant or cluster to go end to end. L1 design: documented reference that is not an executed system, with examples from each level." width="100%">

**The four questions I would ask me**

| Question | Short answer | Where to verify it |
|---|---|---|
| **What is enforced rather than designed?** | Merge-blocking OPA/Rego and Checkov gates, SAST/SCA/secret scanning that fail the build, Sigma rules that must pass pytest before deploy, PIM-versus-standing detection, admission policy on workloads. These stop a change from shipping. | `02-iac-security-gate` · `appsec-devsecops-pipeline` · `detection-as-code-cicd` · `04-identity-security-architecture` |
| **What is lab, and is it labelled as lab?** | Every public artifact is synthetic. Each repo states its level: enforced, tested, lab or design. The log-integration repos need a real tenant to go end to end; the container lab needs a cluster. | Ladder above, [docs/PORTFOLIO.md](PORTFOLIO.md), and the scope block at the foot of this page |
| **What breaks first at scale?** | The evidence chain, not the detection. Enrichment latency and case volume are what degrade first, which is why containment actions are capped per run and a new rule has to price its false positives before it ships. | `enterprise-soc-production-stack` · `secops-soar-ai-enrichment` |
| **What does this page not cover?** | Penetration-test-only depth, compliance paperwork as a service, and organisation building. It is an engineering portfolio: the depth is application security, detection engineering, cloud and identity, and the breadth is everything above. | This page, including the gap row in the matrix |

**What is not being claimed.** No employer code, tenant export, customer telemetry or audit evidence is published in this account. The production numbers in the next section come from production roles. The repositories come from lab and reference work. The two are kept in separate columns of the same page on purpose — the numbers are the claim, the repositories are the proof of method.

---

## Outcomes, and how each is measured

A number without an instrument is a claim. A number without a counter-metric is a claim that can be
gamed. Each of the eight below carries both, plus an evidence class that says who can check it.

<img src="https://raw.githubusercontent.com/kelvinodarikpe88/kelvinodarikpe88/main/assets/metrics.svg?v=3" alt="Eight production outcomes as cards. Mean time to detect minus 62 percent, detection false positives 12 to 6 percent, standing privileged access minus 68 percent, critical vulnerabilities 847 to 187, remediation cycle 67 to 12 days, joiner-mover-leaver 84 percent automated, SOC 2 Type II zero exceptions, detection change gate pytest gated. Each card names the instrument that produced it and the counter-metric that must hold for the claim to mean anything. All eight are class P2, owner-reported." width="100%">

| Outcome | Instrument that produced it | Counter-metric that has to hold | Class |
|---|---|---|---|
| `M-01` · Mean time to detect **−62%** | Sentinel / KQL timestamps, same alert classes before and after | Alert volume and suppression count stay flat | P2 |
| `M-02` · Detection false positives **12% → 6%** | Analyst disposition labels, sampled per rule | True-positive coverage does not fall with the noise | P2 |
| `M-03` · Standing privileged access **−68%** | PIM eligible vs permanent role assignments | Break-glass activations and JIT approval latency | P2 |
| `M-04` · Critical vulnerabilities open **847 → 187** | EPSS + KEV triage queue, fixed asset scope | Re-open rate and mean age of open criticals | P2 |
| `M-05` · Remediation cycle **67 → 12 days** | Ticket open → verified-fixed timestamps | Post-remediation regression rate | P2 |
| `M-06` · Joiners / movers / leavers **84% automated** | IdP lifecycle events, one evidence artefact each | Access-review exceptions and orphaned accounts | P2 |
| `M-07` · SOC 2 Type II **zero exceptions** | Continuous control evidence, auditor-tested | Control failure rate between audit windows | P2 |
| `M-08` · Detection change gate, **pytest on every rule change** | CI result on every rule-changing commit | Rule coverage vs ATT&CK delta | P2 |

**Class key.** **P1** re-derivable from a public artefact — anyone can re-run it today. **P2**
owner-reported from a production role: the instrument is named, the raw telemetry is not
publishable. **P3** lab-measured. **P4** target, not result. All eight above are **P2**, because
they were produced inside employers' environments under NDA. The repositories in this account are
lab and reference work, and they are the proof of *method*, not of these numbers.

Each row has a ledger entry — definition, comparison basis, what would falsify it, and how it could
be promoted to P1: **[docs/METRICS.md](METRICS.md)**. That ledger also lists what is
re-derivable today and where the public evidence is thin, including the one claim on this page whose
public artefact does not yet support it (**M-08**: `detection-as-code-cicd` still ships a placeholder
test, so the gate is real in production and unevidenced in public until that repo's tests parse and
validate rules).

**If you are assessing me, attack the counter-metric, not the headline.** Ask for alert volume
alongside MTTD, true-positive coverage alongside the false-positive rate, break-glass counts
alongside the privilege reduction, re-open rate alongside the vulnerability count. A candidate who
can produce the counter-metric without preparation is reporting a measurement; one who cannot is
reporting a memory.

---

## Toolchain

<div align="center">

**Languages & delivery**
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab_CI-FC6D26?style=flat-square&logo=gitlab&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)

**Cloud & infrastructure**
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=googlecloud&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![CloudFormation](https://img.shields.io/badge/CloudFormation-FF4F8B?style=flat-square&logo=amazonwebservices&logoColor=white)
![OPA](https://img.shields.io/badge/OPA_%2F_Rego-7D9199?style=flat-square)
![Checkov](https://img.shields.io/badge/Checkov-4B275F?style=flat-square)

**Application security**
![Semgrep](https://img.shields.io/badge/Semgrep-00C2A8?style=flat-square)
![CodeQL](https://img.shields.io/badge/CodeQL-1F4FCC?style=flat-square)
![Trivy](https://img.shields.io/badge/Trivy-1904DA?style=flat-square)
![Gitleaks](https://img.shields.io/badge/Gitleaks-8B1E3F?style=flat-square)
![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-00549E?style=flat-square)
![Burp Suite](https://img.shields.io/badge/Burp_Suite-FF6633?style=flat-square)
![Nuclei](https://img.shields.io/badge/Nuclei-0E7C86?style=flat-square)

**Detection & response**
![Sigma](https://img.shields.io/badge/Sigma-1B2A41?style=flat-square)
![KQL](https://img.shields.io/badge/KQL-0078D4?style=flat-square)
![YARA-L](https://img.shields.io/badge/YARA--L-4285F4?style=flat-square)
![Splunk](https://img.shields.io/badge/Splunk-000000?style=flat-square&logo=splunk&logoColor=white)
![Elastic](https://img.shields.io/badge/Elastic-005571?style=flat-square&logo=elastic&logoColor=white)
![Sentinel](https://img.shields.io/badge/Microsoft_Sentinel-0078D4?style=flat-square)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-C8102E?style=flat-square)

**Identity**
![Entra ID](https://img.shields.io/badge/Entra_ID-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)
![Okta](https://img.shields.io/badge/Okta-007DC1?style=flat-square&logo=okta&logoColor=white)
![Google Workspace](https://img.shields.io/badge/Google_Workspace-4285F4?style=flat-square&logo=google&logoColor=white)
![Intune](https://img.shields.io/badge/Intune-0078D4?style=flat-square)
![Keycloak](https://img.shields.io/badge/Keycloak-4D4D4D?style=flat-square&logo=keycloak&logoColor=white)

**Automation & data controls** — patterns, not logos
![SOAR](https://img.shields.io/badge/SOAR-1B3A5C?style=flat-square)
![OIDC](https://img.shields.io/badge/OIDC_workload_identity-0B5563?style=flat-square)
![Dry-run](https://img.shields.io/badge/dry--run_by_default-1E6B3A?style=flat-square)
![Blast radius](https://img.shields.io/badge/blast--radius_caps-1E6B3A?style=flat-square)
![Envelope encryption](https://img.shields.io/badge/envelope_encryption_%2B_KMS-4B275F?style=flat-square)
![Row-level security](https://img.shields.io/badge/PostgreSQL_RLS-336791?style=flat-square&logo=postgresql&logoColor=white)
![Retention](https://img.shields.io/badge/retention_as_code-7D9199?style=flat-square)
![DSAR](https://img.shields.io/badge/DSAR_Art.15%2F17-7D9199?style=flat-square)

</div>

---

## Verified credentials

| Credential | Detail | Status |
|---|---|---|
| **CompTIA Security+ ce** | SY0-701 · candidate ID `COMP001023125614` · verify `76e43bf5abcb4e299b54947fb5dcca10` | Active 2026-09-30 → 2029-09-30 |
| **ISO/IEC 27001 · 42001 · NIST CSF · SOC 2 · DORA · NIS2 · PCI-DSS** | Applied in the repos above, not just cited | Working knowledge |
| **In progress** | CISM · AWS Certified Security – Specialty · ISO/IEC 42001 Lead Implementer | — |

Verify at `cp.certmetrics.com/CompTIA/en/public/verify/credential`.

---

<details>
<summary><b>Full portfolio index — every repo, grouped by domain</b></summary>

<br/>

See **[docs/PORTFOLIO.md](PORTFOLIO.md)** for the maintained index with maturity level (tested / lab / design), stack and what each repo demonstrates.

| Domain | Repositories |
|---|---|
| AppSec & DevSecOps | `appsec-devsecops-pipeline` · `09-devsecops-pipeline-security` · `devsecops-pipeline-automation` · `vulnbank` · `vulnerability-management-lab` |
| Security architecture | `04-identity-security-architecture` · `enterprise-soc-production-stack` · `security-portfolio` |
| Detection engineering | `detection-engineering` · `detection-as-code-cicd` · `01-detection-as-code-pipeline` · `mitre-attack-coverage-tracker` · `portfolio-secops-detections` · `06-beacon-detector` |
| Cloud security & infra | `cloud-log-integration-aws` · `cloud-log-integration-azure` · `cloud-log-integration-gcp` · `07-cloud-security-posture-management` · `cspm-platform` · `cloud-soc-detection-lab` · `aws-security-log-pipeline` · `02-iac-security-gate` |
| Identity & NHI | `identity-security-lab` · `identity-threat-detection-okta-gws` · `08-iam-privilege-auditor` · `ads-privileged-group-addition` |
| Workloads & containers | `container-security-lab` · `07-cloud-detection-lab` · `endpoint-security-lab` |
| APIs & attack surface | `bugbounty-asset-recon-pipeline` · `bugbounty-recon-vulnerability-enrichment` · `network-security-logs-lab` |
| AI / LLM / MCP | `02-ai-security-compliance` · `mcp-threat-hunting-agent` · `mcp-dfir-investigation-copilot` · `secops-soar-ai-enrichment` |
| IR & DFIR | `05-incident-response-orchestration` · `cloud-forensics-ir-playbook` · `dfir-timeline-super-builder` · `evtx-ransomware-hunting-engine` · `memory-forensics-volatility3-automator` · `pcap-traffic-carver-zeek` · `mac-linux-forensics-collector` |
| Threat intelligence | `misp-threat-intel-sharing` · `cti-platform` · `cti-misp-sync-engine` · `cti-threat-hunting-simulation` |
| Governance & assurance | `audit-logging-compliance-checker` · `compliance-audit-dora-pci-forensics` · `10-security-operations-sop` · `soc-l2-l3-sop-playbooks` |
| Security automation | `secops-soar-ai-enrichment` · `soar-vulnerability-enrichment-bot` · `05-incident-response-orchestration` · `detection-as-code-cicd` |
| Data protection & privacy | `compliance-audit-dora-pci-forensics` · `audit-logging-compliance-checker` · `02-ai-security-compliance` · `m365-sharepoint-security-lab` |

</details>

---

## Working principles

1. **A control that is not enforced is a wish.** Policy lives in code, runs in CI, and blocks the merge.
2. **Every detection ships with a test and an owner.** A rule without both is technical debt with an alert attached.
3. **Least privilege is a runtime property, not a diagram.** Measure standing access continuously; assume it will drift.
4. **Evidence is a by-product, not a project.** If audit evidence has to be assembled by hand, the control is manual.
5. **Say what is lab and what is production.** The boundary is labelled on every repo here — a portfolio that overstates itself is a liability, not an asset.

> **Scope of this account.** Everything public here is lab, reference implementation or design work built on synthetic data. No employer code, tenant exports, customer telemetry or audit evidence is published. Where a repo mirrors a production pattern, the readme states which parts are production-equivalent and which are not.

---

<div align="center">

**Open to Application Security, Security Architecture, Detection Engineering and Cloud Security roles — Berlin or remote (English working environment).**

[LinkedIn](https://www.linkedin.com/in/kelvinodarikpe/) · [kelvinodarikpe88@gmail.com](mailto:kelvinodarikpe88@gmail.com) · Berlin, Germany

<sub>Profile last rebuilt October 2026 · content is versioned, typos are not</sub>

</div>
