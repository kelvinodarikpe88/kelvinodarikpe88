# Repository curation plan

**79 public repositories → 6 pinned, ~55 active, 10 archived.**

This is the part of a profile rebuild that most people skip. A hiring manager opens the profile tab, sees 79 repos, and within ten seconds decides whether the account signals "engineer who ships" or "account that collects repositories". Descriptions, topics, pinned selection and archival are what move that judgement.

---

## 1 · What is actually wrong today

| Observation | Effect on a reviewer | Fix in this plan |
|---|---|---|
| **79 public repos, 30+ of them 0–2 KB skeletons** | Reads as bulk-generated. Depth is invisible behind noise. | 10 archived, the rest given honest descriptions; flagship repos carry the depth |
| **Nine lab repos share an identical skeleton** — same `deploy/config/production.env` (4 generic lines), same `scripts/deploy.sh`, same `docs/templates/notify-nis2.md`, same `evidence/coverage.json` | The fastest way to read "template" rather than "work". This is the single biggest credibility risk on the account. | Differentiate them or merge into 3 real repos (see §5). Do this before an active job search |
| **Numeric prefixes (`01-`, `04-`, `09-`)** | Looks like course modules or an ordered tutorial series, not products | Optional rename table in §4 (GitHub redirects old links automatically) |
| **Duplicates**: `03-attack-coverage-tracker` vs `mitre-attack-coverage-tracker`; `03-soc-automation-platform` vs `soc-automation-platform`; `secops-master-suite` vs `security-portfolio` | Suggests the work was restarted rather than finished | Archive the superseded copy |
| **Most repos had no description or topics** | Zero discoverability from search; nothing signals domain ownership | `repo_metadata.json` sets one precise line and 5–8 topics per repo |
| **Forks mixed with original work** (`WebGoat`, `alerting-detection-strategy-framework`) | Dilutes the "I built this" signal on the repos tab | Archive both; the README references the ADS framework as a design source instead |

---

## 2 · Decisions

| Decision | Repositories | Rationale |
|---|---|---|
| **Pinned (6)** | `appsec-devsecops-pipeline` · `04-identity-security-architecture` · `detection-engineering` · `cloud-log-integration-aws` · `container-security-lab` · `vulnbank` | One pin per domain a hiring panel cares about: AppSec, architecture+identity, detection, cloud, workloads, API/offensive validation |
| **Flagship, keep prominent** | `identity-security-lab` · `mitre-attack-coverage-tracker` · `enterprise-soc-production-stack` · `vulnerability-management-lab` · `portfolio-secops-detections` · `cloud-soc-detection-lab` · `cloud-log-integration-azure` · `cloud-log-integration-gcp` · `m365-sharepoint-security-lab` · `network-security-logs-lab` · `endpoint-security-lab` · `ads-privileged-group-addition` · `misp-threat-intel-sharing` · `secops-soar-ai-enrichment` · `detection-as-code-cicd` | Real artefacts (CI, detections, collectors, case study) |
| **Keep, described honestly** | all remaining active repos | Useful as breadth once labelled; the portfolio index states maturity |
| **Archive** | `test-connection` · `WebGoat` (fork) · `alerting-detection-strategy-framework` (fork) · `01-devsecops-pipeline` · `03-attack-coverage-tracker` · `03-soc-automation-platform` · `soc-automation-toolkit` · `secops-master-suite` · `09-security-posture-report` · `08-threat-intelligence-automation` · `06-beacon-detector` | Duplicates, forks, empty scaffolds, scratch repo |
| **Delete** | none | Archival keeps existing links resolving and preserves history — deleting buys nothing |

Archiving is applied by the script and is fully reversible (`archived: false`).

---

## 3 · What the profile must say in five seconds

Current bio: *"Detection Engineering + Security Automation + Cloud Security"* — accurate but dated, and it omits the two domains with the best public evidence (AppSec, identity).

Replacement, in the profile settings (160-character limit):

```
Security Engineer — AppSec · Security Architecture · Detection Engineering · Cloud & Identity | Berlin
```

Website field: point at the portfolio index once published —
`https://github.com/kelvinodarikpe88/kelvinodarikpe88/blob/main/docs/PORTFOLIO.md`
or a personal domain if you register one; an empty field is a missed signal but a dead link is worse.

Social links to add in **Settings → Public profile**: LinkedIn (`https://www.linkedin.com/in/kelvinodarikpe/`), and a blog if you start publishing research.

---

## 4 · Optional renames

GitHub redirects old repository URLs after a rename, so links in the README keep resolving. Rename only if you agree the numeric prefix reads as coursework.

| Current | Suggested |
|---|---|
| `04-identity-security-architecture` | `identity-security-architecture` |
| `07-cloud-security-posture-management` | `cloud-security-posture-management` |
| `09-devsecops-pipeline-security` | `devsecops-pipeline-security` |
| `01-detection-as-code-pipeline` | `detection-as-code-pipeline` |
| `02-ai-security-compliance` | `ai-security-compliance-iso42001` |
| `02-iac-security-gate` | `iac-security-gate` |
| `05-incident-response-orchestration` | `incident-response-orchestration` |
| `08-iam-privilege-auditor` | `iam-privilege-auditor` |
| `10-security-operations-sop` | `security-operations-sop` |
| `06-central-log-analysis` | `central-log-analysis` |

If you rename, update the links in `README.md` and `docs/PORTFOLIO.md` afterwards (search for the old name).

---

## 5 · The nine-repo template problem

`identity-security-lab`, `cloud-log-integration-{aws,azure,gcp}`, `container-security-lab`, `network-security-logs-lab`, `endpoint-security-lab`, `m365-sharepoint-security-lab` and `vulnerability-management-lab` all contain the same skeleton files. A reviewer who opens two of them sees one repository, twice.

Two honest ways out:

**A — Differentiate (preferred).** Give each repo one artefact nobody else has:
- `identity-security-lab` → already has the strongest content (Okta collector, five runbooks, SOC 2 CC mapping). Add a detection test suite and it becomes the flagship.
- `cloud-log-integration-aws` → real CloudFormation + GuardDuty detection + coverage evidence. Add a Terraform variant and a sample CloudTrail fixture the rule actually fires on.
- Each provider repo → one provider-specific failure mode documented and detected (e.g. Azure: disabled diagnostic settings; GCP: audit log sink deleted; AWS: CloudTrail stopped).
- `container-security-lab` → admission policies with `conftest`/Kyverno plus a violation test matrix.
- `endpoint-security-lab` → one real EDR telemetry sample (Sysmon config + expected detections).
- `network-security-logs-lab` → Zeek/DNS fixtures for tunnelling and beaconing.
- `m365-sharepoint-security-lab` → anonymous-link and external-sharing detection with a Graph query.
- `vulnerability-management-lab` → KEV-driven SLA model with a worked example.

**B — Merge.** Collapse the provider repos into one `cloud-security-labs` repo with `aws/ azure/ gcp/` directories, and the endpoint/network ones into `detection-labs`. Fewer, deeper repositories.

Either is defensible. Nine identical skeletons is not.

---

## 6 · Execution order

1. **Publish the profile repo** — `scripts/push_profile.sh profile` (README + assets + docs). This is the visible change.
2. **Refresh metadata** — `export GITHUB_TOKEN=...` then `python3 scripts/apply_profile_metadata.py` to review, `--apply` to write descriptions and topics.
3. **Archive the noise** — `python3 scripts/apply_profile_metadata.py --apply --archive`.
4. **Update the bio** — `python3 scripts/apply_profile_metadata.py --apply --profile`, then add the social links in the UI (the API cannot set those).
5. **Pin the six repos** — profile page → *Customize your pins* (UI only).
6. **Publish the AppSec flagship** — `scripts/push_profile.sh appsec` replaces the skeleton with the full programme (17 docs, CI workflows, OPA policies, verification harness).
7. **Verify** — `python3 scripts/apply_profile_metadata.py --verify` re-reads every repo and reports mismatches.
8. **Fix the template problem** — §5, before applying to roles where a reviewer will open more than one repo.

---

## 7 · Highest-value builds next

Ranked by how much reviewer confidence each unlocks per hour of work:

| # | Repo | Work | Why it matters |
|---|---|---|---|
| 1 | `identity-security-lab` | Add pytest coverage for the detections + a synthetic Okta log fixture | Turns the strongest repo into an unarguable one |
| 2 | `07-cloud-security-posture-management` | Ship the scanner (currently design-only) with 10 CIS controls and tests | "CSPM" is a claim until there is a scanner |
| 3 | `02-iac-security-gate` | Checkov + Conftest policies with a pass/fail fixture matrix | Directly matches platform-security job requirements |
| 4 | `bugbounty-asset-recon-pipeline` | Working recon pipeline with scope guardrails and rate limiting | Proves API/attack-surface competence with code |
| 5 | `08-iam-privilege-auditor` | `iam:PassRole` escalation graph over a sample IAM policy set | Identity is your differentiator; make it concrete |

One deep repo beats five more skeletons. If time is short, do #1 and #2 only.
