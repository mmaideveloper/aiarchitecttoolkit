#!/usr/bin/env python3
"""Render an use-case Markdown document to a readable PDF."""

from __future__ import annotations

import argparse
import re
from html import escape
from pathlib import Path

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak


def register_font() -> tuple[str, str]:
    candidates = [
        ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
        ("C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/arialbd.ttf"),
    ]
    for regular, bold in candidates:
        if Path(regular).exists() and Path(bold).exists():
            pdfmetrics.registerFont(TTFont("ToolkitSans", regular))
            pdfmetrics.registerFont(TTFont("ToolkitSans-Bold", bold))
            return "ToolkitSans", "ToolkitSans-Bold"
    return "Helvetica", "Helvetica-Bold"


def inline(text: str) -> str:
    value = escape(text.strip())
    value = re.sub(r"\[([^]]+)]\(([^)]+)\)", r"<u>\1</u>", value)
    value = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", value)
    return value


def parse_table(lines: list[str], style, page_width: float):
    rows = [[inline(cell) for cell in line.strip().strip("|").split("|")] for line in lines]
    if len(rows) > 1 and all(re.fullmatch(r"\s*:?-{3,}:?\s*", re.sub("<[^>]+>", "", cell)) for cell in rows[1]):
        rows.pop(1)
    count = max(len(row) for row in rows)
    normalized = [row + [""] * (count - len(row)) for row in rows]
    data = [[Paragraph(cell, style) for cell in row] for row in normalized]
    widths = [page_width / count] * count
    table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#123B6D")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "ToolkitSans-Bold" if "ToolkitSans-Bold" in pdfmetrics.getRegisteredFontNames() else "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#AAB4C3")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F4F7FA")]),
    ]))
    return table


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    source, target = Path(args.input), Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    regular, bold = register_font()

    styles = getSampleStyleSheet()
    body = ParagraphStyle("Body", parent=styles["BodyText"], fontName=regular, fontSize=8.6, leading=11.2, spaceAfter=4)
    bullet = ParagraphStyle("Bullet", parent=body, leftIndent=12, firstLineIndent=-8, bulletIndent=2)
    table_text = ParagraphStyle("Table", parent=body, fontSize=7.2, leading=9)
    headings = {
        1: ParagraphStyle("H1", parent=styles["Heading1"], fontName=bold, fontSize=19, leading=23, textColor=colors.HexColor("#123B6D"), spaceAfter=10),
        2: ParagraphStyle("H2", parent=styles["Heading2"], fontName=bold, fontSize=13, leading=16, textColor=colors.HexColor("#123B6D"), spaceBefore=9, spaceAfter=5),
        3: ParagraphStyle("H3", parent=styles["Heading3"], fontName=bold, fontSize=10.5, leading=13, textColor=colors.HexColor("#334155"), spaceBefore=6, spaceAfter=3),
    }

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont(regular, 7)
        canvas.setFillColor(colors.HexColor("#64748B"))
        canvas.drawString(18 * mm, 10 * mm, source.stem)
        canvas.drawRightString(A4[0] - 18 * mm, 10 * mm, f"Page {doc.page}")
        canvas.restoreState()

    doc = BaseDocTemplate(str(target), pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm,
                          topMargin=18 * mm, bottomMargin=17 * mm, title=source.stem)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates(PageTemplate(id="Toolkit", frames=[frame], onPage=footer))
    story = []
    lines = source.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line:
            story.append(Spacer(1, 2.5))
            i += 1
            continue
        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading:
            story.append(Paragraph(inline(heading.group(2)), headings[len(heading.group(1))]))
            i += 1
            continue
        if line.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            story.append(parse_table(table_lines, table_text, doc.width))
            story.append(Spacer(1, 5))
            continue
        bullet_match = re.match(r"^\s*(?:[-*]|\d+\.)\s+(.*)$", line)
        if bullet_match:
            story.append(Paragraph(inline(bullet_match.group(1)), bullet, bulletText="•"))
            i += 1
            continue
        paragraph = [line]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,3})\s|^\s*(?:[-*]|\d+\.)\s+|^\|", lines[i]):
            paragraph.append(lines[i].strip())
            i += 1
        story.append(Paragraph(inline(" ".join(paragraph)), body))

    doc.build(story)
    reader = PdfReader(str(target))
    if not reader.pages or target.stat().st_size < 1000:
        raise RuntimeError("PDF verification failed: missing pages or unexpectedly small output")
    if not any((page.extract_text() or "").strip() for page in reader.pages):
        raise RuntimeError("PDF verification failed: no extractable text")
    print(f"Created {target} ({len(reader.pages)} pages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

