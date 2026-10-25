"""Deterministic SVG frames for an illustrative security workflow."""
import math

STAGES = [('SIGNAL', 'Alert / evidence'), ('DETECT', 'Rules / telemetry'), ('AI CONTEXT', 'Enrich / explain'), ('HUMAN REVIEW', 'Approve / reject'), ('BOUNDED ACTION', 'Scope / rollback'), ('EVIDENCE', 'Record / verify')]

def frame(t: int) -> str:
    active = (t // 6) % 6
    shapes = []
    for i, (title, detail) in enumerate(STAGES):
        x = 34 + i * 194
        color = '#37A2FF' if i == active else '#28405F'
        fill = '#132C48' if i == active else '#0E1B2C'
        shapes.append(f'<rect x="{x}" y="103" width="168" height="104" rx="14" fill="{fill}" stroke="{color}" stroke-width="2"/>')
        shapes.append(f'<text x="{x+16}" y="128" font-size="11" fill="#7C97B8">0{i+1}</text>')
        shapes.append(f'<text x="{x+16}" y="155" font-size="12" font-weight="700" fill="#F3F7FD">{title}</text>')
        shapes.append(f'<text x="{x+16}" y="180" font-size="11" fill="#A9C0DC">{detail}</text>')
        if i < 5:
            shapes.append(f'<path d="M{x+171} 155h18m-5-4 5 4-5 4" fill="none" stroke="#5683AD" stroke-width="2"/>')
        if i == active:
            shapes.append(f'<circle cx="{x+145}" cy="126" r="{4 + math.sin((t%6)*math.pi/6):.2f}" fill="#38D9D1"/>')
    return '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="280" viewBox="0 0 1200 280"><rect width="1200" height="280" rx="18" fill="#070F1D"/><g font-family="Arial,Helvetica,sans-serif"><text x="34" y="39" fill="#37A2FF" font-size="12" letter-spacing="3">SECURITY ENGINEERING + AI</text><text x="34" y="73" fill="#F3F7FD" font-size="24" font-weight="700">From signal to a decision you can explain.</text>'+''.join(shapes)+'<text x="34" y="247" fill="#8CA8C7" font-size="12">Illustrative workflow · synthetic inputs · AI enriches context · a human authorizes consequential actions</text></g></svg>'

