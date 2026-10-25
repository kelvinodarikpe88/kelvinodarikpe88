#!/usr/bin/env python3
"""
build_profile_assets.py — regenerates every SVG/PNG asset for the
github.com/kelvinodarikpe88 profile.

Design system is shared across all assets so the profile reads as one artefact:
    ink  #070C15 → #101E33   (diagonal navy field)
    blue #37A2FF → violet #8B5CF6  (accent rail / gradients)
    line #28405F             (card strokes)
    mono labels, sans body

Run:  python3 build_profile_assets.py
Out:  assets/*.svg  +  assets/*.png (2x)
"""

from __future__ import annotations

import os
import subprocess
import sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- palette
INK_TOP = "#070C15"
INK_MID = "#0B1524"
INK_BOT = "#101E33"
GRID = "#1B2B44"
LINE = "#28405F"
CARD = "#0C1726"
CARD_HI = "#0F1D30"

BLUE = "#37A2FF"
VIOLET = "#8B5CF6"
CYAN = "#22D3EE"
GREEN = "#34D399"
AMBER = "#FBBF24"
RED = "#F87171"

TXT = "#F3F7FD"
TXT_2 = "#A9C0DC"
TXT_3 = "#7C97B8"
TXT_4 = "#4E7FB8"

SANS = "'Liberation Sans','DejaVu Sans',Helvetica,Arial,sans-serif"
MONO = "'DejaVu Sans Mono',Consolas,'Liberation Mono',Menlo,monospace"


def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


# ---------------------------------------------------------------- scaffolding
def defs(extra: str = "") -> str:
    return f"""  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{INK_TOP}"/>
      <stop offset="55%" stop-color="{INK_MID}"/>
      <stop offset="100%" stop-color="{INK_BOT}"/>
    </linearGradient>
    <linearGradient id="rail" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{BLUE}"/>
      <stop offset="60%" stop-color="{VIOLET}"/>
      <stop offset="100%" stop-color="{CYAN}" stop-opacity="0.85"/>
    </linearGradient>
    <linearGradient id="blueviolet" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{BLUE}"/>
      <stop offset="100%" stop-color="{VIOLET}"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="{BLUE}" stop-opacity="0.26"/>
      <stop offset="100%" stop-color="{BLUE}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glowv" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="{VIOLET}" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="{VIOLET}" stop-opacity="0"/>
    </radialGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="{GRID}" stroke-width="1" stroke-opacity="0.5"/>
    </pattern>
    <marker id="arw" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="{TXT_3}"/>
    </marker>
    <marker id="arwb" viewBox="0 0 10 10" refX="9" refY="5"
            markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="{BLUE}"/>
    </marker>{extra}
  </defs>"""


def canvas(w: int, h: int, body: str, extra_defs: str = "") -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}"
     viewBox="0 0 {w} {h}" role="img">
{defs(extra_defs)}
  <rect width="{w}" height="{h}" fill="url(#bg)"/>
  <rect width="{w}" height="{h}" fill="url(#grid)"/>
{body}
</svg>
"""


def eyebrow(x, y, label, color=None, size=12, tracking=3.6):
    color = TXT_4 if color is None else color
    return (f'  <text x="{x}" y="{y}" font-family="{SANS}" font-size="{size}" '
            f'font-weight="600" letter-spacing="{tracking}" fill="{color}">'
            f'{esc(label)}</text>\n')


def title(x, y, label, size=30, color=None, weight=700):
    color = TXT if color is None else color
    return (f'  <text x="{x}" y="{y}" font-family="{SANS}" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}">{esc(label)}</text>\n')


def body(x, y, label, size=13, color=None, weight=400, mono=False, tracking=0,
         anchor=None):
    color = TXT_2 if color is None else color
    fam = MONO if mono else SANS
    tr = f' letter-spacing="{tracking}"' if tracking else ""
    an = f' text-anchor="{anchor}"' if anchor else ""
    return (f'  <text x="{x}" y="{y}" font-family="{fam}" font-size="{size}"{an} '
            f'font-weight="{weight}"{tr} fill="{color}">{esc(label)}</text>\n')


def card(x, y, w, h, fill=None, stroke=None, r=10, opacity=1.0, sw=1):
    fill = CARD if fill is None else fill
    stroke = LINE if stroke is None else stroke
    return (f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
            f'fill="{fill}" fill-opacity="{opacity}" stroke="{stroke}" '
            f'stroke-width="{sw}"/>\n')


def rule(x1, y1, x2, y2, color=None, w=1, dash=None, opacity=1.0, marker=None):
    color = LINE if color is None else color
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return (f'  <path d="M{x1},{y1} L{x2},{y2}" stroke="{color}" '
            f'stroke-width="{w}" fill="none" opacity="{opacity}"{d}{m}/>\n')


def pill(x, y, label, color=BLUE, fs=10.5, padx=10, h=22):
    est = len(label) * fs * 0.60 + padx * 2
    return (card(x, y, est, h, fill="#0E1B2C", stroke=LINE, r=5)
            + body(x + padx, y + h / 2 + 3.7, label, size=fs, color=color,
                   weight=600, mono=True, tracking=0.8)), est


# ================================================================ 1 · HERO
def build_hero() -> str:
    W, H = 1280, 420
    b = []
    b.append(f'  <ellipse cx="1060" cy="40" rx="440" ry="300" fill="url(#glow)"/>\n')
    b.append(f'  <ellipse cx="180" cy="430" rx="380" ry="200" fill="url(#glowv)"/>\n')
    b.append(f'  <rect x="0" y="0" width="7" height="{H}" fill="url(#rail)"/>\n')

    b.append(eyebrow(56, 66, "SECURITY ENGINEERING · PUBLIC PORTFOLIO"))
    b.append(title(54, 128, "Kelvin Odarikpe", size=54))
    b.append(body(56, 166,
                  "Application Security · Security Architecture · Detection Engineering",
                  size=20, color=TXT_2, weight=500))
    b.append(body(56, 194,
                  "Cloud Security & Infrastructure · Identity · Workloads · APIs",
                  size=16, color=TXT_3))
    b.append(body(56, 219,
                  "Security Automation · Data Protection & Privacy · AI & ML",
                  size=16, color=TXT_3))

    # stat strip
    stats = [("−62%", "MTTD", GREEN), ("−68%", "standing privilege", GREEN),
             ("847→187", "criticals open", GREEN), ("67→12d", "remediation", GREEN),
             ("0", "SOC 2 exceptions", CYAN)]
    x = 56
    y = 250
    for val, lab, col in stats:
        w = 214
        b.append(card(x, y, w, 66, fill=CARD_HI, stroke=LINE, r=8))
        b.append(f'  <rect x="{x}" y="{y}" width="3" height="66" rx="1.5" fill="{col}"/>\n')
        b.append(body(x + 18, y + 31, val, size=22, color=col, weight=700))
        b.append(body(x + 18, y + 50, lab, size=11, color=TXT_3, mono=True, tracking=0.6))
        x += w + 12

    b.append(body(56, 352,
                  "Every control below ships with a test, a CI gate and a runbook — "
                  "not a slide deck.", size=13.5, color=TXT_2))
    b.append(body(56, 378,
                  "Lab · reference · design work on synthetic data. No employer code, "
                  "tenant export or customer telemetry.", size=11.5, color=TXT_4))

    b.append(body(1224, 66, "BERLIN · DE", size=11.5, color=TXT_4, mono=True, tracking=1.2))
    b.append(body(1224, 92, "OCT 2026", size=11.5, color=TXT_4, mono=True, tracking=1.2))
    # right-align both
    b = [ln.replace('<text x="1224"', '<text x="1224" text-anchor="end"')
         if 'x="1224"' in continent else ln for ln in b for continent in [ln]]
    b = [ln.replace('text-anchor="end" font-family', 'text-anchor="end" font-family')
         for ln in b]
    return canvas(W, H, "".join(b))


# ================================================================ 2 · PLANES
def build_planes() -> str:
    W, H = 1280, 534
    b = []
    b.append(f'  <ellipse cx="1080" cy="30" rx="420" ry="240" fill="url(#glow)"/>\n')
    b.append(f'  <rect x="0" y="0" width="7" height="{H}" fill="url(#rail)"/>\n')
    b.append(eyebrow(56, 56, "OPERATING MODEL"))
    b.append(title(54, 96, "Four planes, one feedback loop", size=30))
    b.append(body(56, 122,
                  "Every repository maps to a cell in this model — not to a tool list.",
                  size=13, color=TXT_3))

    planes = [
        ("01", "SHIP", "shift left", BLUE,
         ["Threat model", "STRIDE · identity attack paths", "SAST · SCA · secrets · SBOM",
          "IaC & policy gates", "Checkov · OPA/Rego · admission",
          "block on critical · admit only signed"]),
        ("02", "RUN", "control planes", CYAN,
         ["Identity & access", "PIM/JIT · CA baseline · NHI", "Cloud posture",
          "CSPM · guardrails · drift", "Workloads", "containers · EDR · runtime"]),
        ("03", "DEFEND", "detect & respond", VIOLET,
         ["Detection as code", "Sigma/YARA-L · pytest · CI", "AI-assisted triage",
          "enrichment · human gate", "IR & DFIR", "NIST 800-61 · chain of custody"]),
        ("04", "PROVE", "evidence", GREEN,
         ["Continuous evidence", "CI-generated · timestamped", "Coverage",
          "ATT&CK · control matrix", "Audit readiness",
          "SOC 2 · ISO 27001 · DORA · NIS2"]),
    ]

    cw, gap, top = 278, 24, 150
    for i, (num, name, sub, col, items) in enumerate(planes):
        x = 48 + i * (cw + gap)
        b.append(card(x, top, cw, 236, fill=CARD, stroke=LINE, r=12))
        b.append(f'  <rect x="{x + 14}" y="{top}" width="{cw - 28}" height="3.5" '
                 f'rx="1.75" fill="{col}"/>\n')
        b.append(body(x + 20, top + 40, num, size=26, color=col, weight=700, mono=True))
        b.append(body(x + 62, top + 34, name, size=17, color=TXT, weight=700, tracking=1.4))
        b.append(body(x + 62, top + 52, sub, size=10.5, color=TXT_4, mono=True, tracking=0.6))
        b.append(rule(x + 20, top + 68, x + cw - 20, top + 68, LINE, 1))

        # each pair keeps its mono detail tight to the label above it
        yy = top + 96
        for j, it in enumerate(items):
            if j % 2 == 0:
                b.append(f'  <circle cx="{x+26}" cy="{yy-4}" r="2.6" fill="{col}"/>\n')
                b.append(body(x + 38, yy, it, size=12, color=TXT_2, weight=600))
                yy += 17
            else:
                b.append(body(x + 38, yy, it, size=10.6, color=TXT_3, mono=True))
                yy += 31

    # feedback band — explicit geometry only, no marker or glyph dependencies
    band_y, band_h = 414, 76
    b.append(card(48, band_y, 1184, band_h, fill="#0A1420", stroke=LINE, r=10))
    b.append(f'  <rect x="49" y="{band_y + 12}" width="3.5" height="{band_h - 24}" '
             f'rx="1.75" fill="{VIOLET}"/>\n')
    b.append(eyebrow(72, band_y + 26, "FEEDBACK LOOP · RE-ENTERS 01 SHIP", VIOLET,
                     size=10.5, tracking=2.2))
    b.append(body(72, band_y + 50,
                  "Evidence produced in PROVE re-tunes DEFEND, which re-prioritises RUN, "
                  "which re-scopes SHIP. Coverage is recomputed on every push.",
                  size=12, color=TXT_2))
    return canvas(W, H, "".join(b))


# ================================================================ 3 · AI LOOP
def build_ai_loop() -> str:
    W, H = 1280, 560
    b = []
    b.append(f'  <ellipse cx="640" cy="0" rx="520" ry="240" fill="url(#glowv)"/>\n')
    b.append(f'  <rect x="0" y="0" width="7" height="{H}" fill="url(#rail)"/>\n')
    b.append(eyebrow(56, 56, "AI-AUTOMATED SECURITY"))
    b.append(title(54, 96, "Where the model acts — and where it must not", size=30))
    b.append(body(56, 122,
                  "Automation is scoped by blast radius. Read from left to right: "
                  "authority decreases as consequence increases.",
                  size=13, color=TXT_3))

    stages = [
        ("SIGNAL", CYAN, "ingest", ["SIEM · EDR · cloud audit", "IdP · SaaS · network"]),
        ("DETECT", BLUE, "rules as code", ["Sigma · YARA-L · KQL", "pytest on every change"]),
        ("ENRICH", VIOLET, "AI", ["asset · identity · threat ctx", "EPSS · KEV correlation"]),
        ("DECIDE", AMBER, "tiered", ["auto: read / contain", "gate: destructive action"]),
        ("ACT", GREEN, "bounded", ["scoped credential", "audited · reversible"]),
    ]

    n = len(stages)
    cw, gap, top = 218, 20, 158
    for i, (name, col, sub, lines) in enumerate(stages):
        x = 48 + i * (cw + gap)
        b.append(card(x, top, cw, 128, fill=CARD, stroke=col, r=10, opacity=0.92))
        b.append(f'  <rect x="{x}" y="{top}" width="{cw}" height="3" rx="1.5" fill="{col}"/>\n')
        b.append(body(x + 18, top + 34, name, size=15, color=col, weight=700, tracking=1.6))
        b.append(body(x + 18, top + 52, sub, size=10.5, color=TXT_4, mono=True, tracking=0.6))
        yy = top + 76
        for ln in lines:
            b.append(body(x + 18, yy, ln, size=10.8, color=TXT_2))
            yy += 17
        if i < n - 1:
            b.append(rule(x + cw + 3, top + 64, x + cw + gap - 5, top + 64,
                          TXT_3, 1.4, marker="arw"))

    # the human gate
    gy = 320
    b.append(card(48, gy, 800, 96, fill="#160F1E", stroke=AMBER, r=10, opacity=0.9))
    b.append(body(68, gy + 32, "HUMAN AUTHORITY GATE", size=13, color=AMBER,
                  weight=700, tracking=1.8, mono=True))
    b.append(body(68, gy + 56,
                  "Destructive or irreversible actions — key rotation, tenant-wide revoke, "
                  "host isolation in prod —", size=11.6, color=TXT_2))
    b.append(body(68, gy + 74,
                  "stop here for an explicit approval, a stated blast radius and a named owner.",
                  size=11.6, color=TXT_2))

    # guardrails column
    gx = 872
    b.append(card(gx, gy, 360, 96, fill=CARD, stroke=LINE, r=10))
    b.append(body(gx + 18, gy + 30, "AGENT GUARDRAILS", size=11, color=VIOLET,
                  weight=700, tracking=1.6, mono=True))
    gl = ["Least-privilege tool scope per agent",
          "Retrieved content = untrusted input",
          "Kill switch + dry-run on every playbook"]
    yy = gy + 50
    for g in gl:
        b.append(f'  <circle cx="{gx+22}" cy="{yy-4}" r="2.4" fill="{VIOLET}"/>\n')
        b.append(body(gx + 34, yy, g, size=10.6, color=TXT_3))
        yy += 17

    # evidence bar
    ey = 448
    b.append(card(48, ey, 1184, 76, fill="#0A1420", stroke=GREEN, r=10, opacity=0.85))
    b.append(body(68, ey + 30, "EVIDENCE IS THE OUTPUT, NOT A SIDE EFFECT", size=11,
                  color=GREEN, weight=700, tracking=1.6, mono=True))
    b.append(body(68, ey + 54,
                  "Every automated action emits a timestamped, attributable record that "
                  "feeds SOC 2, ISO 27001 and DORA reporting without a manual collection "
                  "exercise.", size=11.6, color=TXT_2))

    b.append(body(56, 546,
                  "MCP servers are treated as an agent-facing API surface with their own "
                  "threat model — tool scoping, prompt injection and confused-deputy risk "
                  "are assessed, not assumed.",
                  size=11, color=TXT_4))
    return canvas(W, H, "".join(b))


# ================================================================ 4 · CISO MATRIX
def matrix_dot(kind, cx, cy, color):
    """Deterministic markers — no font glyphs, so cairosvg renders them identically."""
    if kind == 2:      # enforced
        return (f'  <circle cx="{cx}" cy="{cy}" r="9.5" fill="none" stroke="{color}" '
                f'stroke-width="1" opacity="0.32"/>\n'
                f'  <circle cx="{cx}" cy="{cy}" r="5.4" fill="{color}"/>\n')
    if kind == 1:      # designed, not enforced
        return (f'  <circle cx="{cx}" cy="{cy}" r="6.4" fill="none" stroke="{color}" '
                f'stroke-width="1.4"/>\n'
                f'  <path d="M{cx},{cy - 6.4} A6.4,6.4 0 0,1 {cx},{cy + 6.4} Z" '
                f'fill="{color}" opacity="0.9"/>\n')
    return (f'  <circle cx="{cx}" cy="{cy}" r="6.2" fill="none" stroke="{color}" '
            f'stroke-width="1.4"/>\n'
            f'  <circle cx="{cx}" cy="{cy}" r="1.7" fill="{color}" opacity="0.45"/>\n')


def build_ciso_matrix() -> str:
    W, H = 1280, 700
    b = []
    b.append(f'  <ellipse cx="1100" cy="20" rx="400" ry="230" fill="url(#glow)"/>\n')
    b.append(f'  <rect x="0" y="0" width="7" height="{H}" fill="url(#rail)"/>\n')
    b.append(eyebrow(56, 56, "CONTROL COVERAGE · HONEST VIEW"))
    b.append(title(54, 96, "What is enforced, what is designed, what is missing", size=30))
    b.append(body(56, 122,
                  "Rows are control domains. Columns are the frameworks a CISO is "
                  "actually audited against.",
                  size=13, color=TXT_3))

    cols = ["SOC 2", "ISO 27001", "NIST CSF", "DORA / NIS2", "EU AI Act"]
    rows = [
        ("Access control & JIT", [2, 2, 2, 2, 0]),
        ("Non-human identity", [2, 2, 2, 1, 0]),
        ("Vulnerability management", [2, 2, 2, 2, 0]),
        ("Detection & monitoring", [2, 2, 2, 2, 0]),
        ("Incident response", [2, 2, 2, 2, 0]),
        ("Log integrity & retention", [2, 1, 2, 2, 0]),
        ("Supply chain / SBOM", [1, 1, 1, 1, 0]),
        ("AI system governance", [0, 1, 1, 0, 1]),
        ("Privacy engineering", [1, 1, 1, 1, 0]),
        ("Third-party risk", [0, 0, 1, 1, 0]),
    ]
    LV = {2: (GREEN, "Enforced in CI / runtime"),
          1: (AMBER, "Designed & documented"),
          0: (RED, "Gap — named, not hidden")}

    mx, my = 56, 182
    label_w = 316
    cell_w = 170
    row_h = 34
    table_w = label_w + cell_w * len(cols)
    hx = mx + label_w

    # column headers, centred on each cell
    for i, c in enumerate(cols):
        b.append(body(hx + i * cell_w + cell_w / 2, my - 16, c, size=10.6,
                      color=TXT_4, weight=600, mono=True, tracking=0.9,
                      anchor="middle"))
    b.append(rule(mx, my - 6, mx + table_w, my - 6, LINE, 1, opacity=0.9))

    for r, (name, vals) in enumerate(rows):
        y = my + r * row_h
        if r % 2 == 0:
            b.append(f'  <rect x="{mx}" y="{y}" width="{table_w}" '
                     f'height="{row_h}" fill="{CARD}" fill-opacity="0.55" rx="4"/>\n')
        b.append(body(mx + 12, y + 22, name, size=12, color=TXT_2, weight=500))
        for c, v in enumerate(vals):
            col = LV[v][0]
            b.append(matrix_dot(v, hx + c * cell_w + cell_w / 2, y + row_h / 2, col))

    # legend
    ly = my + len(rows) * row_h + 34
    lx = 56
    for v in (2, 1, 0):
        col, lab = LV[v]
        b.append(matrix_dot(v, lx + 7, ly - 4, col))
        b.append(body(lx + 24, ly, lab, size=11.5, color=TXT_3))
        lx += 250

    b.append(card(56, ly + 26, 1168, 88, fill="#160F1E", stroke=AMBER, r=10, opacity=0.6))
    b.append(body(76, ly + 54, "WHY SHOW THE GAPS", size=11, color=AMBER,
                  weight=700, tracking=1.6, mono=True))
    b.append(body(76, ly + 78,
                  "A coverage matrix with no red cells is a marketing asset, not a control "
                  "assessment. Third-party risk and EU AI Act", size=11.6, color=TXT_2))
    b.append(body(76, ly + 92,
                  "conformity are the two areas where this portfolio is deliberately thin — "
                  "and where the next 90 days of work go.",
                  size=11.6, color=TXT_2))
    return canvas(W, H, "".join(b))


# ================================================================ 5 · TRUST BOUNDARIES
def build_trust() -> str:
    W, H = 1280, 600
    b = []
    b.append(f'  <ellipse cx="640" cy="0" rx="560" ry="220" fill="url(#glow)"/>\n')
    b.append(f'  <rect x="0" y="0" width="7" height="{H}" fill="url(#rail)"/>\n')
    b.append(eyebrow(56, 56, "REFERENCE ARCHITECTURE"))
    b.append(title(54, 96, "Trust boundaries and where controls sit", size=30))
    b.append(body(56, 122,
                  "Each vertical dashed line is a boundary that must authenticate, "
                  "authorise and log independently.",
                  size=13, color=TXT_3))

    zones = [
        ("UNTRUSTED", RED, 48, 150,
         ["Internet", "Partner APIs", "SaaS tenants"], "no implicit trust"),
        ("EDGE", AMBER, 258, 196,
         ["WAF · rate limit", "IdP / SSO · MFA", "API gateway"], "authenticate"),
        ("WORKLOAD", BLUE, 512, 210,
         ["Containers · pods", "Serverless", "EDR · runtime"], "authorise per request"),
        ("DATA", VIOLET, 780, 210,
         ["Postgres · object store", "KMS · secrets", "Backups · snapshots"], "encrypt + minimise"),
        ("CONTROL", GREEN, 1048, 184,
         ["SIEM · detection", "Evidence store", "IR automation"], "observe + prove"),
    ]

    top = 158
    for name, col, x, w, items, note in zones:
        b.append(card(x, top, w, 182, fill=CARD, stroke=col, r=10, opacity=0.55))
        b.append(f'  <rect x="{x}" y="{top}" width="{w}" height="3" rx="1.5" fill="{col}"/>\n')
        b.append(body(x + 18, top + 34, name, size=13, color=col, weight=700, tracking=1.6))
        b.append(body(x + 18, top + 52, note, size=10, color=TXT_4, mono=True, tracking=0.5))
        yy = top + 80
        for it in items:
            b.append(f'  <rect x="{x+18}" y="{yy-13}" width="{w-36}" height="26" rx="5" '
                     f'fill="#0F1D30" stroke="{LINE}" stroke-width="0.8"/>\n')
            b.append(body(x + 30, yy + 4, it, size=10.6, color=TXT_2))
            yy += 32

    # boundaries
    for x in (248, 500, 766, 1034):
        b.append(rule(x, top - 14, x, top + 202, TXT_3, 1.2, dash="5 5", opacity=0.6))
        b.append(f'  <rect x="{x-7}" y="{top+206}" width="14" height="14" rx="3" '
                 f'fill="{INK_TOP}" stroke="{TXT_3}" stroke-width="1.2"/>\n')
        b.append(f'  <path d="M{x-3},{top+210} l3,3 l5,-6" stroke="{GREEN}" '
                 f'stroke-width="1.6" fill="none"/>\n')

    # flow arrows
    ay = top + 252
    b.append(rule(120, ay, 1120, ay, BLUE, 1.4, marker="arwb", opacity=0.55))
    b.append(body(120, ay + 20, "request path", size=10.5, color=TXT_4, mono=True, tracking=0.8))
    b.append(rule(1120, ay + 36, 120, ay + 36, VIOLET, 1.4, marker="arw", opacity=0.45))
    b.append(body(1120, ay + 56, "telemetry path", size=10.5, color=TXT_4,
                  mono=True, tracking=0.8, anchor="end"))

    # assumptions
    b.append(card(56, 486, 1176, 84, fill="#0A1420", stroke=LINE, r=10))
    b.append(body(76, 514, "DESIGN ASSUMPTIONS WORTH CHALLENGING", size=11,
                  color=BLUE, weight=700, tracking=1.6, mono=True))
    b.append(body(76, 538,
                  "The DATA zone trusts the WORKLOAD zone to hold scoped credentials — the "
                  "assumption that failed in October 2026, when encrypted",
                  size=11.4, color=TXT_2))
    b.append(body(76, 556,
                  "environment variables were read and decrypted contents obtained. "
                  "Boundary 3 is where I would spend the first week.",
                  size=11.4, color=TXT_2))
    return canvas(W, H, "".join(b))


# ================================================================ 6 · EVIDENCE LADDER
def build_ladder() -> str:
    W, H = 1280, 424
    b = []
    b.append(f'  <ellipse cx="1050" cy="20" rx="380" ry="200" fill="url(#glowv)"/>\n')
    b.append(f'  <rect x="0" y="0" width="7" height="{H}" fill="url(#rail)"/>\n')
    b.append(eyebrow(56, 56, "MATURITY, STATED PLAINLY"))
    b.append(title(54, 96, "Four levels — and which repos sit at each", size=28))
    b.append(body(56, 122,
                  "Labelled on every repository. A portfolio that overstates itself is a "
                  "liability, not an asset.", size=13, color=TXT_3))

    levels = [
        ("L4", "ENFORCED", GREEN, "Blocks the merge or the request. Runs in CI or at runtime.",
         "OPA/Rego gates · Sigma in CI · PIM/JIT"),
        ("L3", "TESTED", BLUE, "Executable, with a test suite and a CI workflow.",
         "detection-as-code · IAM auditor · threat-intel sync"),
        ("L2", "LAB", CYAN, "Runs against synthetic data; needs a tenant or cluster to go end-to-end.",
         "log-integration (AWS/Azure/GCP) · container lab"),
        ("L1", "DESIGN", VIOLET, "Documented reference: design, SOP or spec. Not an executed system.",
         "IR playbooks · SOC L2/L3 SOPs · architecture references"),
    ]

    y = 150
    for i, (tag, name, col, desc, ex) in enumerate(levels):
        b.append(card(48, y, 1184, 54, fill=CARD, stroke=LINE, r=9))
        b.append(f'  <rect x="49" y="{y + 10}" width="3.5" height="34" rx="1.75" '
                 f'fill="{col}"/>\n')
        b.append(body(72, y + 24, tag, size=15, color=col, weight=700, mono=True))
        b.append(body(112, y + 24, name, size=12.5, color=TXT, weight=700, tracking=1.4))
        b.append(body(112, y + 42, desc, size=10.6, color=TXT_3))
        b.append(body(720, y + 32, ex, size=10.4, color=TXT_4, mono=True))
        y += 64
    return canvas(W, H, "".join(b))


# ================================================================ render
def render(svg_name: str, png_name: str, scale: float = 2.0) -> str:
    src = os.path.join(OUT, svg_name)
    dst = os.path.join(OUT, png_name)
    try:
        import cairosvg  # type: ignore
        cairosvg.svg2png(url=src, write_to=dst, scale=scale)
        return f"  {png_name:<26} ok"
    except Exception as e:  # pragma: no cover
        return f"  {png_name:<26} SKIPPED ({e})"


# GitHub renders profiles in both themes: the banner is generated twice from the
# same layout, only the palette changes.
LIGHT = {
    "INK_TOP": "#FFFFFF", "INK_MID": "#F5F9FE", "INK_BOT": "#E9F1FA",
    "GRID": "#DCE6F2", "LINE": "#C6D5E8", "CARD": "#FFFFFF", "CARD_HI": "#F6FAFF",
    "TXT": "#0A1526", "TXT_2": "#22405F", "TXT_3": "#47678B", "TXT_4": "#5B7CA1",
    "BLUE": "#1C6FD6", "VIOLET": "#6D3FCF", "CYAN": "#0E7C93",
    "GREEN": "#0B8F63", "AMBER": "#A9700A", "RED": "#C0392B",
}


def build_hero_light() -> str:
    saved = {k: globals()[k] for k in LIGHT}
    globals().update(LIGHT)
    try:
        return build_hero()
    finally:
        globals().update(saved)


# ================================================================ 8 · METRICS
PROV = {
    "P1": (GREEN, "P1 RE-DERIVABLE"),
    "P2": (BLUE, "P2 OWNER-REPORTED"),
    "P3": (VIOLET, "P3 LAB-MEASURED"),
    "P4": (TXT_3, "P4 TARGET"),
}


def build_metrics() -> str:
    W = 1280
    CW, CH, GAP = 576, 132, 16
    X1, X2 = 56, 648
    Y0, STEP = 166, 148
    ROWS = 4
    H = Y0 + ROWS * STEP + 76

    b = []
    b.append(f'  <ellipse cx="640" cy="0" rx="620" ry="230" fill="url(#glow)"/>\n')
    b.append(f'  <rect x="0" y="0" width="7" height="{H}" fill="url(#rail)"/>\n')
    b.append(eyebrow(56, 56, "OUTCOMES · EVIDENCE CLASS"))
    b.append(title(54, 96, "Every number, and what keeps it honest", size=30))
    b.append(body(56, 122,
                  "Eight production outcomes. Each carries the instrument that produced "
                  "it and the counter-metric that has to stay flat for the claim to hold.",
                  size=13, color=TXT_3))

    cards = [
        (BLUE, "MEAN TIME TO DETECT", "\u221262%",
         "Sentinel / KQL detection timestamps, quarter on quarter",
         "Alert volume and suppression count must stay flat"),
        (CYAN, "DETECTION FALSE POSITIVES", "12% \u2192 6%",
         "Analyst disposition labels on a sampled alert population",
         "True-positive coverage must not fall with the noise"),
        (VIOLET, "STANDING PRIVILEGED ACCESS", "\u221268%",
         "PIM / JIT eligibility vs permanent role assignments",
         "Break-glass activations and JIT approval latency"),
        (AMBER, "CRITICAL VULNERABILITIES OPEN", "847 \u2192 187",
         "EPSS + KEV triage queue snapshot, same asset scope",
         "Re-open rate and mean age of open criticals"),
        (BLUE, "REMEDIATION CYCLE TIME", "67 \u2192 12 days",
         "Ticket open to verified-fixed timestamps, per severity",
         "Post-remediation regression rate"),
        (GREEN, "JOINER / MOVER / LEAVER", "84% automated",
         "IdP lifecycle events, each with an evidence artefact",
         "Access-review exceptions and orphaned accounts"),
        (VIOLET, "SOC 2 TYPE II", "zero exceptions",
         "Continuous control evidence, tested in the audit window",
         "Control failure rate between audit windows"),
        (CYAN, "DETECTION CHANGE GATE", "pytest gated",
         "CI result on every rule-changing commit",
         "Rule coverage vs ATT&CK delta"),
    ]

    for i, (accent, name, value, instr, counter) in enumerate(cards):
        col, row = i % 2, i // 2
        x = X1 if col == 0 else X2
        y = Y0 + row * STEP
        b.append(card(x, y, CW, CH, fill=CARD_HI, stroke=LINE, r=12))
        b.append(f'  <rect x="{x}" y="{y + 10}" width="3" height="{CH - 20}" '
                 f'rx="1.5" fill="{accent}" opacity="0.95"/>\n')
        b.append(body(x + 22, y + 27, name, size=10.4, color=TXT_4, weight=600,
                      mono=True, tracking=1.5))

        _, lab = "P2", PROV["P2"][1]
        pw = len(lab) * 9.5 * 0.6 + 20
        b.append(pill(x + CW - pw - 14, y + 13, lab, color=PROV["P2"][0],
                      fs=9.5, padx=10, h=20)[0])

        b.append(body(x + 22, y + 62, value, size=25, color=TXT, weight=700))
        b.append(rule(x + 22, y + 76, x + CW - 22, y + 76, LINE, 1, opacity=0.35))

        b.append(body(x + 22, y + 96, "MEASURED BY", size=8.8, color=TXT_4,
                      weight=600, mono=True, tracking=0.9))
        b.append(body(x + 22, y + 112, instr, size=11.2, color=TXT_2))
        b.append(body(x + CW - 22, y + 96, "COUNTER-METRIC", size=8.8,
                      color=TXT_4, weight=600, mono=True, tracking=0.9,
                      anchor="end"))
        b.append(body(x + CW - 22, y + 112, counter, size=11.2, color=TXT_3,
                      anchor="end"))

    ly = Y0 + ROWS * STEP + 22
    b.append(rule(56, ly - 24, 1224, ly - 24, LINE, 1, opacity=0.5))
    lx = 56
    for key in ("P1", "P2", "P3", "P4"):
        colr, lab = PROV[key]
        b.append(f'  <rect x="{lx}" y="{ly - 9}" width="9" height="9" rx="2" '
                 f'fill="{colr}"/>\n')
        note = "  \u2190 all eight cards" if key == "P2" else ""
        b.append(body(lx + 16, ly, lab + note, size=10, color=TXT_3, weight=600,
                      mono=True, tracking=0.4))
        lx += 250 if key != "P2" else 300
    b.append(body(56, ly + 30,
                  "P2 means owner-reported from production roles: the instrument is named, "
                  "the raw telemetry is not publishable. Each card has a ledger row with "
                  "period, baseline and a falsification condition \u2014 docs/METRICS.md.",
                  size=11, color=TXT_3))
    return canvas(W, H, "".join(b))


BUILDERS = {
    "hero.svg": build_hero,
    "hero-light.svg": build_hero_light,
    "planes.svg": build_planes,
    "ai-loop.svg": build_ai_loop,
    "ciso-matrix.svg": build_ciso_matrix,
    "trust-boundaries.svg": build_trust,
    "maturity-ladder.svg": build_ladder,
    "metrics.svg": build_metrics,
}


def main() -> int:
    print("writing svg")
    for name, fn in BUILDERS.items():
        p = os.path.join(OUT, name)
        with open(p, "w", encoding="utf-8") as f:
            f.write(fn())
        print(f"  {name:<26} {os.path.getsize(p):>7,} bytes")

    print("rendering png (2x)")
    for name in BUILDERS:
        print(render(name, name.replace(".svg", ".png")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
