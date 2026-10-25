# CISO brief

**Who this is for.** A security leader or architect with four minutes and one question: can this person carry a control from design to audit evidence without a project manager holding it together?

**What this is not.** A certification inventory, a tool list, or a claim to have run a security programme. Everything in the public repositories is synthetic. The production outcomes are separated from the lab work on every page.

---

## 1 · The claim, in one paragraph

Controls are designed as code, tested in CI, and enforced where a change can still be stopped. The pattern repeats across four domains — application security, detection engineering, cloud and identity — and the output is always the same shape: a repository with a test suite, a merge gate, and a runbook. Architecture decisions are written down with their failure modes, because a boundary nobody stress-tested is a boundary nobody has.

---

## 2 · Coverage, stated honestly

Ten control domains against the frameworks a programme is actually audited against. `●` enforced in CI or at runtime · `◐` designed and documented · `○` named gap.

| Control domain | SOC 2 | ISO 27001 | NIST CSF | DORA / NIS2 | EU AI Act |
|---|---|---|---|---|---|
| Access control & JIT | ● | ● | ● | ● | ○ |
| Non-human identity | ● | ● | ● | ◐ | ○ |
| Vulnerability management | ● | ● | ● | ● | ○ |
| Detection & monitoring | ● | ● | ● | ● | ○ |
| Incident response | ● | ● | ● | ● | ○ |
| Log integrity & retention | ● | ◐ | ● | ● | ○ |
| Supply chain / SBOM | ◐ | ◐ | ◐ | ◐ | ○ |
| AI system governance | ○ | ◐ | ◐ | ○ | ◐ |
| Privacy engineering | ◐ | ◐ | ◐ | ◐ | ○ |
| Third-party risk | ○ | ○ | ◐ | ◐ | ○ |

**The two thin areas, named rather than shaded.** *Third-party risk* — there is no vendor estate here to assess, so the workflow is designed and unexercised. *EU AI Act conformity* — still moving, tracked rather than claimed. Supply chain and privacy engineering sit at `designed` across all four frameworks, which is the accurate description of reference work rather than deployed programme work.

A matrix with no hollow cells is a marketing asset. This one has nine.

---

## 3 · Architecture: five boundaries, one assumption to attack first

| Zone | What has to be true | Primary control |
|---|---|---|
| Untrusted → Edge | No implicit trust from network position | WAF, rate limiting, IdP/SSO with MFA |
| Edge → Workload | Authenticated identity, not a shared secret | API gateway, per-request authorisation |
| Workload → Data | Scoped, short-lived credentials only | Workload identity, no static keys |
| Everything → Control | Telemetry is complete, tamper-evident and retained | SIEM, evidence store, immutable retention |

**The assumption I would attack first is boundary three** — the data zone trusting the workload zone to hold scoped credentials. That assumption is what failed in October 2026: Railway disclosed that encrypted customer environment variables were accessed and, for a subset, **decrypted contents obtained**. Encryption at rest was not the weak point; key material living in the same trust zone as the ciphertext was. Zeabur's second incident, over 14–15 October 2026, exposed **3,218,965 environment-variable records and 321,810 accounts** read from a production database that also held platform credentials the attacker could use directly.

Neither was a cryptography failure. Both were key custody and blast radius. The control that answers it is envelope encryption with a KMS-held key-encryption key and a per-tenant data key: a stolen backup, snapshot or connection string decrypts to nothing without an independent KMS authorisation that is itself logged.

---

## 4 · Automation: the authority model

The question a CISO should ask about any automation programme is not "how much does it automate" but "what can it do at 03:00 without me". This is the answer, per action class.

| Action | Autonomous | Reversible how | Bound |
|---|---|---|---|
| Enrichment, correlation | Yes, unbounded | No state change | Read-only credentials |
| Ticket creation, dedupe, routing | Yes | Close the ticket | — |
| Block an indicator | Yes | Auto-expiry, one-command unblock | 50 per run, 24-hour TTL |
| Disable an account | Yes, high-confidence identity compromise only | Re-enable runbook, memberships captured first | One account per run |
| Isolate a host | Approval click required | One-click release | Auto-release after 72 hours |
| Rotate a credential | Yes | Re-enable if rotation fails | Disables, never deletes |

**Five non-negotiables.** Dry-run is the default and enablement is a reviewed change with a named owner. Blast-radius caps are in code, so a loop bug cannot disable a tenant. Playbooks converge on desired state, so reruns mid-incident are safe. Runners authenticate through OIDC to short-lived roles, so the automation holds no standing key. Evidence is written by the action itself — actor, target, before/after, approver, timestamp, reversal command.

**Where the model stops.** Enrichment, correlation, summarisation and first-draft disposition are automated because they are expensive by hand and cheap to review. Containment that a human cannot reverse in under a minute stays behind an explicit gate: named approver, stated blast radius, one action at a time. Prompts, tool scopes and retrieved content are treated as attack surface, not as trusted configuration.

---

## 5 · Data protection, in four questions

1. **Where is personal data and what is it?** Column-level classification propagated from the catalog into the pipeline; an untagged `email`, `name` or `ip` column fails CI.
2. **Who may see it?** Row-level security per tenant plus dynamic masking, proven by a two-tenant test where tenant B querying tenant A's key returns zero rows.
3. **How long does it live?** Retention as code per dataset class; deletion is a job that emits a receipt with object counts and backup expiry.
4. **Can it be proven?** DSAR (GDPR Art. 15) and erasure (Art. 17) run as logged workflows across primary store, warehouse and backups.

Telemetry is treated as personal data: per-class retention, hashed correlation fields, and access to raw logs is itself access-logged.

---

## 6 · First 90 days, if this were a real estate

| Weeks | Focus | Done looks like |
|---|---|---|
| 1–2 | Establish the real boundary | Architecture reviewed against observed traffic, not the diagram; the top three trust assumptions written down |
| 3–6 | Close the key-custody gap | Envelope encryption with KMS-held KEK and per-tenant DEKs; no secret readable from the same boundary as the data it protects |
| 5–8 | Make detection a build artefact | Rules in Git, pytest on every change, ATT&CK coverage recomputed on push, FP budget agreed with SOC |
| 7–10 | Bound the automation | Dry-run everywhere, per-run caps in code, OIDC runners, per-action evidence |
| 9–12 | Prove it | First continuous-evidence pack assembled from CI and runtime rather than by hand |

---

## 7 · How to audit the numbers

Eight outcomes are claimed. None of them is verifiable from this repository, and that is a
deliberate design choice rather than an oversight: they were produced inside employers' tenants
under NDA. What *is* verifiable is whether each number has a measurement behind it — so the brief
tests the method instead of the value.

| Metric | The question that separates a measurement from a memory | What a weak answer sounds like |
|---|---|---|
| MTTD −62% | "Which alert classes, and what was alert volume over the same two quarters?" | "It was measured across the SOC." |
| FP rate 12% → 6% | "Sampled or complete? What happened to true-positive coverage?" | "The analysts stopped complaining." |
| Standing access −68% | "Permanent role assignments, or all privileged access? How many break-glass activations since?" | "We turned on PIM." |
| Critical vulns 847 → 187 | "Same asset scope? What is the re-open rate and the mean age of the 187?" | "We closed the backlog." |
| Remediation 67 → 12 days | "Median or mean? Verified fix or ticket closure? What is the regression rate?" | "The team got faster." |
| JML 84% | "Evidence artefact per event, or ticket created? How many orphaned accounts remain?" | "It is mostly automated now." |
| SOC 2 zero exceptions | "Over which audit window, and what failed between windows?" | "We passed." |
| pytest gate | "Show the CI job on a rule-changing commit." | "We have a process for that." |

Three things follow from this table, and they are the useful part of the brief for a hiring panel:

1. **A candidate who names the counter-metric unprompted has been measuring.** A candidate who
   produces the headline and then improvises the counter-metric has been remembering.
2. **A metric without a stated comparison basis cannot be audited**, which is why each ledger row
   fixes the basis (same alert classes, same asset scope, same severity mix) before quoting a value.
3. **A portfolio that shows its weakest evidence is more trustworthy than one that does not.**
   [METRICS.md](METRICS.md) lists the claim whose public artefact does not yet support it (M-08) and
   the repositories that are thinner than their description (single-file skeletons).

Full ledger, including definitions, falsification conditions and promotion paths:
**[METRICS.md](METRICS.md)**.

---

## 8 · Limits of this document

No employer code, tenant export, customer telemetry or audit evidence appears here or in the repositories. The production metrics cited on the profile come from production roles; the repositories are lab and reference implementations on synthetic data. Where a repository mirrors a production pattern, its README states which parts are production-equivalent and which are not.

Verification paths: [../README.md](../README.md) · [ARCHITECTURE.md](ARCHITECTURE.md) · [PORTFOLIO.md](PORTFOLIO.md) · [METRICS.md](METRICS.md)
