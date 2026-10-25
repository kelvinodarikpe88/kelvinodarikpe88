# Kelvin Odarikpe | Security Engineer

**Application Security · Product Security · Cloud & Platform Security · Detection Engineering · AI Security**

Berlin, Germany · Open to Berlin and remote opportunities · English working environment

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/kelvinodarikpe88/kelvinodarikpe88/main/assets/hero.svg?v=3">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/kelvinodarikpe88/kelvinodarikpe88/main/assets/hero-light.svg?v=3">
  <img alt="Kelvin Odarikpe — Security Engineer, Berlin. Application Security, Security Architecture, Detection Engineering, Cloud Security and Infrastructure, Identity, Workloads, APIs, Security Automation, Data Protection and Privacy, AI and ML. Production outcomes shown: MTTD down 62 percent, standing privilege down 68 percent, critical vulnerabilities 847 to 187, remediation 67 to 12 days, SOC 2 Type II zero exceptions." src="https://raw.githubusercontent.com/kelvinodarikpe88/kelvinodarikpe88/main/assets/hero-light.png?v=3" width="100%">
</picture>

[**Contact Kelvin**](mailto:kelvinodarikpe88@gmail.com) · [**LinkedIn**](https://www.linkedin.com/in/kelvinodarikpe/) · [**Hiring brief**](docs/HIRING.md) · [**CISO brief**](docs/CISO-BRIEF.md) · [**Project index**](docs/PORTFOLIO.md)

I connect security engineering with the decisions people need to make. I build and review application controls, automate cloud and identity guardrails, investigate threats, and explain risk in terms engineers and leadership can act on.

My approach: **understand the system → identify the failure path → implement the control → test it → keep the evidence.**

## Start with the question you need answered

| Reader | What to assess | Start here |
|---|---|---|
| **Hiring manager / recruiter** | Role fit, practical scope, communication and working style | [Two-minute hiring brief](docs/HIRING.md) |
| **CISO / security leader** | Risk ownership, trade-offs, evidence and operating model | [CISO brief](docs/CISO-BRIEF.md) · [Metrics ledger](docs/METRICS.md) |
| **Engineering / platform lead** | Architecture, implementation boundaries, tests and delivery | [Architecture model](docs/ARCHITECTURE.md) · [Engineering reference](docs/ENGINEERING.md) |
| **Legal / privacy / GRC partner** | How requirements become controls and reviewable evidence | [Privacy and governance approach](#privacy-governance-and-legal-collaboration) |

## Where I contribute

| Role family | Engineering focus | What I communicate |
|---|---|---|
| **Application / Product Security Engineer** | Threat modelling, secure code review, API authorization, SAST/DAST/SCA, vulnerability remediation | Reproduction, affected boundary, proposed fix, owner and retest |
| **Cloud / Platform Security Engineer** | AWS/Azure, Terraform, Kubernetes, IAM, secrets and CI/CD integrity | Secure defaults, operational impact, exceptions and recovery paths |
| **Detection / Security Operations Engineer** | Sentinel/KQL, Elastic, Sigma, ATT&CK, investigation and incident response | Detection logic, telemetry gaps, false positives and containment choices |
| **Security Architecture** | Identity, workload, API and data trust boundaries; policy-as-code | Design assumptions, attack paths, residual risk and decisions |
| **AI / LLM Security Engineer** | RAG and agent boundaries, prompt injection, tool authority, evaluation and human approval | Failure cases, data exposure, evaluation limits and escalation |

## Selected public engineering work

These are **lab, design and reference implementations**. They demonstrate methods and are distinct from employer production outcomes. Repository maturity and known gaps are documented in the [project index](docs/PORTFOLIO.md) and [metrics ledger](docs/METRICS.md).

| Project | Review focus | Useful question to ask |
|---|---|---|
| [**AppSec / DevSecOps pipeline**](https://github.com/kelvinodarikpe88/appsec-devsecops-pipeline) | Security checks and delivery workflow | Which findings should block delivery, and how is that decision enforced? |
| [**Identity security architecture**](https://github.com/kelvinodarikpe88/04-identity-security-architecture) | Privilege, Conditional Access and policy-as-code | Where does standing access remain, and who can approve an exception? |
| [**ATT&CK coverage tracker**](https://github.com/kelvinodarikpe88/mitre-attack-coverage-tracker) | Detection coverage and evidence artifacts | What does the coverage measure actually count, and what does it miss? |
| [**Security automation / AI enrichment**](https://github.com/kelvinodarikpe88/secops-soar-ai-enrichment) | Enrichment, response boundaries and tests | Which actions can run automatically, and which need human approval? |

[Browse the complete portfolio →](docs/PORTFOLIO.md)

## Platform engineering: Veriseya

**[Veriseya — public product preview](https://veriseya.com)** brings AI, security and regulatory review into a connected workspace. It is my own platform project, with Python/FastAPI, React, PostgreSQL row-level security, identity boundaries and evidence-oriented workflows in its architecture.

The public frontend and limited Supabase pilot are live. The full API/worker deployment is being prepared; uploads, hosted model execution and scheduled collectors are not enabled in that pilot. A preview is not evidence of a fully operational production backend or regulatory certification.

[Explore the preview →](https://veriseya.com) · [Review my platform and security approach →](docs/ENGINEERING.md)

## Communication is part of the control

- **With engineers:** explain the failure path, reproduce it, propose a practical fix, and agree how to test it.
- **With leadership:** connect exposure to business impact, show the trade-off, name the decision owner, and make the next action clear.
- **During incidents:** maintain a timeline, separate confirmed facts from hypotheses, and make containment and recovery decisions traceable.
- **With reviewers:** provide scope, evidence, limitations and residual risk so another person can challenge the conclusion.

## Privacy, governance and legal collaboration

I work at the boundary between technical controls and governance: data flows, access controls, retention, audit evidence, vendor/AI-provider risks and incident response inputs.

**My contribution is engineering and evidence.** Legal counsel, privacy specialists and accountable business owners determine legal interpretation, applicability and acceptance. I translate agreed requirements into implementation tasks, tests and review records.

Relevant working areas include **GDPR, ISO/IEC 27001, SOC 2, EU AI Act, ISO/IEC 42001, NIST AI RMF and DORA**. Referencing a framework is not a claim of legal qualification, certification or complete control coverage.

[Read the CISO brief →](docs/CISO-BRIEF.md) · [Explore privacy and AI security work →](docs/ENGINEERING.md)

## Outcomes with an evidence trail

<img src="https://raw.githubusercontent.com/kelvinodarikpe88/kelvinodarikpe88/main/assets/metrics.svg?v=3" alt="Eight owner-reported professional outcomes. Each has a measurement instrument, counter-metric and P2 evidence label. Details and known gaps are in the metrics ledger." width="100%">

**All eight headline outcomes are P2: owner-reported professional results.** Public repositories demonstrate methods; they do not independently prove employer metrics. Comparison periods still need owner input, and the ledger records public evidence gaps, including M-08's placeholder detection test.

[Inspect definitions, counter-metrics and known gaps →](docs/METRICS.md)

## Technical toolkit

**Build & review:** Python · Bash · FastAPI · pytest · GitHub Actions · GitLab CI · Semgrep · CodeQL · Trivy · Gitleaks · OWASP ZAP

**Cloud & identity:** AWS · Azure · Terraform · Docker · Kubernetes · Entra ID · Okta · OIDC · IAM · policy-as-code

**Detect & respond:** Microsoft Sentinel · KQL · Elastic · Sigma · MITRE ATT&CK · incident response · DFIR

**AI & assurance:** RAG · agent/tool boundaries · evaluation fixtures · human approval · evidence workflows · control mapping

Tool familiarity, lab work and production experience are not interchangeable; see the [engineering reference](docs/ENGINEERING.md) for scope.

## Contact and opportunities

I am interested in **Application Security, Product Security, Cloud/Platform Security, Detection Engineering and Security Architecture** opportunities in Berlin or remote teams. I also welcome roles combining security engineering with AI risk and governance.

**Hiring teams:** include the role, location/remote arrangement and engineering scope in your message.

[**Email: kelvinodarikpe88@gmail.com**](mailto:kelvinodarikpe88@gmail.com) · [**LinkedIn**](https://www.linkedin.com/in/kelvinodarikpe/) · [**Hiring brief**](docs/HIRING.md)

<sub>Updated 25 October 2026 · Public work uses synthetic or reference data. Employer code, customer telemetry and private audit evidence are not published.</sub>
