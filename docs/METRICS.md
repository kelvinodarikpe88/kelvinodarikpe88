# Metrics ledger

Every outcome quoted on the profile page appears here with the instrument that produced it, the
period it covers, the counter-metric that has to hold for the claim to mean anything, and the
condition that would falsify it.

The rule this page enforces:

> **No number without an instrument. No instrument without a counter-metric. No counter-metric
> without a stated direction.**

A reader should be able to take any figure on the profile, find it here, and know three things:
where it came from, what it does *not* prove, and what would have to be true for it to be wrong.

---

## 1 · Provenance classes

| Class | Name | What it means | Who can check it |
|---|---|---|---|
| **P1** | Re-derivable | The artefact is public. Anyone can clone, open or run it and reach the same number. | Any reader, today, with no contact |
| **P2** | Owner-reported | Measured in a production role from a named instrument. The tenant, telemetry and audit evidence are not publishable. | Only an employer reference or an interview walkthrough |
| **P3** | Lab-measured | Measured inside a synthetic environment in this account, with the generating script committed. True of the lab, not of a company. | Any reader, by running the lab |
| **P4** | Target | A commitment, not a result. Stated so it can be held against me later. | Time |

The profile's eight headline outcomes are all **P2**. That is deliberate and it is the honest
classification: they were produced inside employers' environments, under NDAs, from telemetry that
cannot leave those tenants. Presenting them as P1 would be false; hiding them would misrepresent
seven years of work. So they are labelled, instrumented and given counter-metrics instead.

---

## 2 · The eight production outcomes

### M-01 · Mean time to detect — **−62%**

| Field | Value |
|---|---|
| Claim as published | MTTD down 62% |
| Definition | Median elapsed time from first observable telemetry event to a triaged alert, measured over comparable alert classes only |
| Instrument | Microsoft Sentinel, KQL queries over `SecurityAlert` / `SecurityIncident` with the detection's own `TimeGenerated` and the incident's first-modified timestamp |
| Comparison basis | Same alert classes, quarter before the change vs quarter after. Not "all alerts" — that would let a change in alert mix move the number |
| Counter-metric | **Alert volume and suppression count must stay flat.** A −62% MTTD achieved by alerting less is a coverage loss, not a detection win |
| Class | P2 |
| What would falsify it | The same measurement including alerts that were never triaged (they have no end timestamp and would silently drop out), or a fall in alert volume proportional to the fall in MTTD |
| Promotion path to P1 | Publish the KQL query and a synthetic dataset with known ground-truth timings, so the calculation can be re-run end to end |

### M-02 · Detection false positives — **12% → 6%**

| Field | Value |
|---|---|
| Claim as published | Detection false positives 12% to 6% |
| Definition | Share of alerts dispositioned by an analyst as benign-true-positive-noise or false positive, out of all dispositioned alerts in the period |
| Instrument | Analyst disposition labels in the incident queue, sampled per rule and aggregated. Per-rule, not per-tenant — a single noisy rule can hide inside a healthy average |
| Comparison basis | Same rule set population, before and after the tuning cycle |
| Counter-metric | **True-positive coverage must not fall with the noise.** Suppressing a rule reduces false positives and true positives together; coverage is measured against the ATT&CK techniques the rule was written for |
| Class | P2 |
| What would falsify it | Disposition quality collapsing (analysts bulk-closing), or a rule retirement being counted as noise reduction |
| Promotion path to P1 | Ship the tuning harness and a labelled synthetic alert set with the rule pack, so precision/recall is recomputable |

### M-03 · Standing privileged access — **−68%**

| Field | Value |
|---|---|
| Claim as published | Standing privileged access down 68% |
| Definition | Count of principals holding a permanent privileged role assignment, as a share of the baseline count at the start of the programme |
| Instrument | Entra ID PIM role assignments: `permanent` vs `eligible`, exported per role and de-duplicated per principal |
| Comparison basis | Same role catalogue (Global Admin, Privileged Role Admin, Exchange Admin, SharePoint Admin, Contributor at subscription scope) |
| Counter-metric | **Break-glass activations and JIT approval latency.** Standing access removed by making everything slow gets bypassed with shared accounts; if activations spike or approval latency grows, the control is being routed around |
| Class | P2 |
| What would falsify it | A rise in permanent assignments at resource scope (not role scope) that the measurement does not count, or a rise in shared/service credentials replacing named admin accounts |
| Promotion path to P1 | Publish the export script and the role catalogue definition so the metric is reproducible against any tenant export |

### M-04 · Critical vulnerabilities open — **847 → 187**

| Field | Value |
|---|---|
| Claim as published | Open critical vulnerabilities 847 to 187 |
| Definition | Distinct open critical-severity findings, de-duplicated per asset and CVE, at the end of the period, against the same asset scope |
| Instrument | Vuln scanner export joined to EPSS scores and the CISA KEV catalogue; a finding carries an owner and a deadline at creation |
| Comparison basis | Fixed asset scope. The number is meaningless if the estate grew or shrank between measurements |
| Counter-metric | **Re-open rate and mean age of open criticals.** Closing 660 findings by marking them "accepted" or by re-scoping assets is the classic way to move this metric without reducing risk |
| Class | P2 |
| What would falsify it | Asset-scope shrinkage, an increase in accepted-risk closures, or mean age of the remaining 187 rising instead of falling |
| Promotion path to P1 | Publish the triage policy (EPSS/KEV thresholds, SLA table) as code — the *policy* is verifiable even when the estate is not |

### M-05 · Remediation cycle time — **67 → 12 days**

| Field | Value |
|---|---|
| Claim as published | Remediation cycle 67 to 12 days |
| Definition | Median days from finding creation to verified fix, per severity band, excluding findings closed as accepted risk |
| Instrument | Ticket timestamps (created → resolved → verified), not developer-reported estimates |
| Comparison basis | Same severity mix; a shift toward low-severity findings would flatter the number |
| Counter-metric | **Post-remediation regression rate.** Faster fixes that get reverted or re-opened are churn, not remediation |
| Class | P2 |
| What would falsify it | A rise in findings closed without verification, or a rise in the regression rate that offsets the cycle-time gain |
| Promotion path to P1 | Publish the SLA policy and the verification gate as pipeline configuration |

### M-06 · Joiner / Mover / Leaver automation — **84%**

| Field | Value |
|---|---|
| Claim as published | JML 84% automated |
| Definition | Share of lifecycle events (joiner, mover, leaver) executed end to end by the IdP-driven workflow with an evidence artefact per event, out of all lifecycle events in the period |
| Instrument | IdP lifecycle event log; manual exceptions counted explicitly in the denominator |
| Comparison basis | Whole period, no sampling |
| Counter-metric | **Access-review exceptions and orphaned accounts.** Automating the happy path while leaving the exception queue manual hides the risk in exactly the population that matters |
| Class | P2 |
| What would falsify it | A rising count of orphaned accounts (accounts whose owner left but which remain enabled), or automation that provisions but never de-provisions |
| Promotion path to P1 | Publish the workflow definitions and a synthetic directory fixture that exercises joiner → mover → leaver |

### M-07 · SOC 2 Type II — **zero exceptions**

| Field | Value |
|---|---|
| Claim as published | SOC 2 Type II, zero exceptions |
| Definition | Zero qualified exceptions in the auditor's Type II report over the audit period |
| Instrument | The audit report itself; supporting control evidence generated continuously rather than assembled at year end |
| Comparison basis | One audit period. This is a point-in-time statement, not a trend |
| Counter-metric | **Control failure rate between audit windows.** Zero exceptions in a report is compatible with controls that fail and are quietly remediated before sampling; the between-window rate is the honest signal |
| Class | P2 |
| What would falsify it | Any exception in a subsequent report, or evidence that control failures were remediated without being logged |
| Promotion path to P1 | Not promotable by design — the report belongs to the employer. What *is* publishable is the evidence-collection pipeline that produced the control evidence |

### M-08 · Detection change gate — **pytest on every rule change**

| Field | Value |
|---|---|
| Claim as published | No detection rule reaches production without a passing test |
| Definition | Every commit that adds or modifies a rule triggers CI; the gate fails the merge on a failed rule test |
| Instrument | CI job result on rule-changing commits, plus branch protection requiring the check |
| Counter-metric | **Rule coverage vs ATT&CK delta.** A green gate over three rules proves the gate works, not that detection coverage exists. Coverage is recomputed on every push and compared with the technique list |
| Class | P2 for the production instance. **The public artefact currently does not evidence it** — see §4 |
| What would falsify it | A rule merged while the check was skipped, a check that runs against fixtures but not the rule under change, or a test suite that passes trivially |
| Promotion path to P1 | Make `detection-as-code-cicd` a real gate: parse every rule, assert required fields, run the coverage delta, and fail on regression. Then the claim is checkable by anyone |

---

## 3 · What is re-derivable today (P1)

These are checkable right now, without contacting me. Paths are relative to each repo's default branch.

| Artefact | What it shows | How to check |
|---|---|---|
| `m365-sharepoint-security-lab/evidence/coverage.json` | 12 rules, 12 ATT&CK techniques covered, severity split 3 critical / 7 high / 2 medium, with the rule and data source named per technique | Open the file, or regenerate it with `scripts/generate_ttp_report.py` |
| `m365-sharepoint-security-lab/sentinel/kql/sharepoint_bulk_download.kql` | The detection behind the T1567.002 row of that coverage file | Read the query; run it in any tenant with the SharePoint audit table |
| `m365-sharepoint-security-lab/.github/workflows/compliance-evidence.yml` | Evidence collection as a scheduled pipeline rather than a document | Read the workflow |
| `m365-sharepoint-security-lab/docs/ttp-matrix.md` | Technique → rule → data source mapping, the human-readable twin of `coverage.json` | Read the file |
| `secops-soar-ai-enrichment` (`app/enrichment/orchestrator.py`, `tests/`, `ci.yml`) | Enrichment orchestration with a test suite and CI, including the cap on what the automation may do without a human | `pip install -r requirements.txt && pytest` |
| `02-iac-security-gate` (`main.tf`, `policies/`) | IaC that fails closed on hand-edits, at the plan stage | `terraform init && terraform plan` against a scratch account |
| `vulnbank` (`app/app.py`, `schema.sql`, `docs/vulnerabilities.md`) | The deliberately vulnerable target the AppSec work is demonstrated against, with the intended findings documented | `docker compose up`, follow `docs/vulnerabilities.md` |

Note the shape of that table: the *coverage* claims are P1 and the *outcome* claims are P2. That is
the correct distribution for someone whose production work is under NDA, and it is the reason the
profile separates "numbers" from "repos" instead of blending them.

---

## 4 · Known gaps in the public evidence

Listed here rather than omitted, because a ledger that only lists strengths is a brochure.

| Gap | Detail | Effect on claims | Fix |
|---|---|---|---|
| `detection-as-code-cicd` test suite is a placeholder | `tests/test_core.py` currently asserts `True` | The M-08 gate is real in production but **not** evidenced publicly. The claim stays P2 until the repo's tests actually parse and validate rules | Replace with per-rule parsing tests, required-field assertions and a coverage-delta check; wire branch protection to the job |
| Several repos are thin | `compliance-audit-dora-pci-forensics` and `02-iac-security-gate` are single-entry skeletons; `m365-sharepoint-security-lab/README.md` is a stub | Repo-linked claims in the profile point at real files, but depth varies and the README of the M365 lab does not yet explain its own evidence model | Expand each README to state level (enforced / tested / lab / design), what runs, and what a reader should look at first |
| No published synthetic telemetry | P2 instruments are named but their inputs are private | Readers must take the instrument on trust | Publish a small labelled synthetic alert set so M-01/M-02 are computable by a third party |
| Periods not yet stated per metric | The comparison window for each metric is known to the owner, not written down | A CISO cannot date a claim | Fill the table in §5 — five minutes of owner input, one row per metric |

---

## 5 · Owner input required

Fields only the owner can supply. Until they are filled, the ledger is complete on *method* and
incomplete on *timing*. Do not invent them.

| Metric | Period (start → end) | Environment scale (approx.) | Baseline definition agreed? |
|---|---|---|---|
| M-01 MTTD |  |  |  |
| M-02 False positives |  |  |  |
| M-03 Standing privilege |  |  |  |
| M-04 Critical vulns |  |  |  |
| M-05 Remediation cycle |  |  |  |
| M-06 JML |  |  |  |
| M-07 SOC 2 |  |  |  |
| M-08 Change gate |  |  |  |

---

## 6 · How to attack this page

If you are assessing me, this is the useful move: pick a counter-metric and ask for it. The answer
tells you whether the headline number was bought or earned.

- Ask for alert volume alongside MTTD.
- Ask for true-positive coverage alongside the false-positive rate.
- Ask for break-glass activation counts alongside the standing-privilege reduction.
- Ask for the re-open rate alongside the vulnerability count.
- Ask for the orphaned-account count alongside JML automation.
- Ask for the coverage delta alongside a green CI badge.

A candidate who can produce the counter-metric without preparation is reporting a measurement. A
candidate who cannot is reporting a memory.

---

## 7 · Maintenance rule

This file changes when a number changes, in the same commit, with the period updated. A metric that
can no longer be measured is **retired with a note**, not quietly deleted — deletion is how a
ledger turns back into marketing.
