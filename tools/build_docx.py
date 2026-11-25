"""Збирання звітів .docx із Markdown-джерел (Docs-as-Code).

Використання:
    python tools/build_docx.py <spec.json>

spec.json:
{
  "output": "labs/lab-01/Лабораторна_1_Кока_МС.docx",
  "title": {"kind": "report", "lab": 1, "topic": "..."}  |  {"kind": "chapter", "heading": "..."},
  "sources": ["labs/lab-01/report.md", ...]
}

Підтримувана підмножина Markdown: заголовки #–####, абзаци, марковані та нумеровані списки,
таблиці, блоки коду (```mermaid рендериться в PNG через mmdc), зображення ![](path),
**жирний**, *курсив*, `код`, посилання [текст](url).
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.enum.section import WD_ORIENT  # noqa: F401
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "build" / "mermaid"
FONT = "Times New Roman"
MONO = "Consolas"

COURSE = "Технічне документування та презентація програмних рішень"
UNIVERSITY = "Чернівецький національний університет імені Юрія Федьковича"
STUDENT = "Кока Максим Сергійович"
SPECIALTY = "121/F2 «Інженерія програмного забезпечення»"


def mmdc_cmd() -> str:
    return "mmdc.cmd" if sys.platform == "win32" else "mmdc"


def render_mermaid(code: str) -> Path:
    CACHE.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256(code.encode("utf-8")).hexdigest()[:16]
    src = CACHE / f"{digest}.mmd"
    out = CACHE / f"{digest}.png"
    if not out.exists():
        src.write_text(code, encoding="utf-8")
        cfg = CACHE / "config.json"
        cfg.write_text(json.dumps({"theme": "default", "themeVariables": {"fontFamily": "Arial"}}), encoding="utf-8")
        proc = subprocess.run(
            [mmdc_cmd(), "-i", str(src), "-o", str(out), "-s", "2", "-b", "white", "-c", str(cfg)],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        # На Windows mmdc повертає ненульовий код через повідомлення taskkill; критерій — наявність PNG.
        if not out.exists():
            raise RuntimeError(f"Mermaid render failed for {src}:\n{proc.stdout}\n{proc.stderr}")
    return out


def set_base_styles(doc: Document) -> None:
    for sec in doc.sections:
        sec.top_margin = Cm(2)
        sec.bottom_margin = Cm(2)
        sec.left_margin = Cm(2.5)
        sec.right_margin = Cm(1.5)
    st = doc.styles["Normal"]
    st.font.name = FONT
    st.font.size = Pt(14)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    pf = st.paragraph_format
    pf.line_spacing = 1.5
    pf.space_after = Pt(0)
    pf.space_before = Pt(0)
    for lvl, size in ((1, 16), (2, 14), (3, 14), (4, 14)):
        hs = doc.styles[f"Heading {lvl}"]
        hs.font.name = FONT
        hs.font.size = Pt(size)
        hs.font.bold = True
        hs.font.italic = False
        hs.font.color.rgb = RGBColor(0, 0, 0)
        rpr = hs.element.get_or_add_rPr()
        rfonts = rpr.find(qn("w:rFonts"))
        if rfonts is None:
            rfonts = OxmlElement("w:rFonts")
            rpr.append(rfonts)
        for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
            rfonts.set(qn(attr), FONT)
        hs.paragraph_format.space_before = Pt(12)
        hs.paragraph_format.space_after = Pt(6)
        hs.paragraph_format.keep_with_next = True


INLINE = re.compile(r"(\*\*[^*]+\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\)|(?<![*\w])\*[^*\s][^*]*\*(?!\*))")


def add_inline(par, text: str, size: Pt | None = None, bold: bool = False) -> None:
    pos = 0
    for m in INLINE.finditer(text):
        if m.start() > pos:
            r = par.add_run(text[pos:m.start()])
            r.bold = bold or None
            if size:
                r.font.size = size
        tok = m.group(0)
        if tok.startswith("**"):
            r = par.add_run(tok[2:-2])
            r.bold = True
        elif tok.startswith("`"):
            r = par.add_run(tok[1:-1])
            r.font.name = MONO
            r.bold = bold or None
            r.font.size = Pt((size.pt if size else 14) - 2)
        elif tok.startswith("["):
            label, url = re.match(r"\[([^\]]+)\]\(([^)]+)\)", tok).groups()
            r = par.add_run(label)
            r.bold = bold or None
            if url.startswith("http"):
                r.underline = True
                r.font.color.rgb = RGBColor(0x1F, 0x4E, 0x99)
        else:
            r = par.add_run(tok[1:-1])
            r.italic = True
            r.bold = bold or None
        if size:
            r.font.size = size
        pos = m.end()
    if pos < len(text):
        r = par.add_run(text[pos:])
        r.bold = bold or None
        if size:
            r.font.size = size


def body_par(doc: Document, text: str, indent: bool = True):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if indent:
        p.paragraph_format.first_line_indent = Cm(1.25)
    add_inline(p, text)
    return p


def set_cell_border(table) -> None:
    tbl = table._tbl
    tblPr = tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:color"), "000000")
        borders.append(el)
    tblPr.append(borders)


def add_table(doc: Document, rows: list[list[str]]) -> None:
    ncols = max(len(r) for r in rows)
    table = doc.add_table(rows=len(rows), cols=ncols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell_border(table)
    size = Pt(11) if ncols >= 5 else Pt(12)
    for i, row in enumerate(rows):
        for j in range(ncols):
            cell = table.cell(i, j)
            cell.text = ""
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.first_line_indent = Cm(0)
            txt = row[j] if j < len(row) else ""
            for k, part in enumerate(txt.split("<br>")):
                if k:
                    p.add_run().add_break()
                add_inline(p, part.strip(), size=size, bold=(i == 0))
    doc.add_paragraph()


def add_image(doc: Document, path: Path, caption: str | None = None) -> None:
    from PIL import Image

    with Image.open(path) as im:
        w, h = im.size
    max_w, max_h = 16.5, 22.0
    width = max_w
    if h / w * width > max_h:
        width = max_h * w / h
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(str(path), width=Cm(width))
    if caption:
        c = doc.add_paragraph()
        c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        add_inline(c, caption, size=Pt(12))


def add_code(doc: Document, code: str) -> None:
    for line in code.rstrip("\n").split("\n"):
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.0
        r = p.add_run(line if line else " ")
        r.font.name = MONO
        r.font.size = Pt(9)
    doc.add_paragraph()


def split_row(line: str) -> list[str]:
    line = line.strip().strip("|")
    cells, buf, in_code = [], "", False
    for ch in line:
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append(buf.strip())
            buf = ""
        else:
            buf += ch
    cells.append(buf.strip())
    return [c.replace("\\|", "|") for c in cells]


def render_markdown(doc: Document, md: str, base: Path, figure_counter: list[int]) -> None:
    lines = md.split("\n")
    i = 0
    para_buf: list[str] = []

    def flush():
        if para_buf:
            body_par(doc, " ".join(s.strip() for s in para_buf))
            para_buf.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s.startswith("<!--"):
            while "-->" not in lines[i]:
                i += 1
            i += 1
            continue
        if s.startswith("```"):
            flush()
            lang = s[3:].strip()
            code = []
            i += 1
            while not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            if lang == "mermaid":
                png = render_mermaid("\n".join(code))
                add_image(doc, png)
            else:
                add_code(doc, "\n".join(code))
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            flush()
            level = len(m.group(1))
            text = re.sub(r"\s*\{#.*\}$", "", m.group(2))
            h = doc.add_heading(level=level)
            add_inline(h, text)
            i += 1
            continue
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{3,}", lines[i + 1]):
            flush()
            rows = [split_row(s)]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            add_table(doc, rows)
            continue
        m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)", s)
        if m:
            flush()
            add_image(doc, (base / m.group(2)).resolve(), m.group(1) or None)
            i += 1
            continue
        m = re.match(r"^(\s*)([-*]|\d+[.)])\s+(.*)$", line)
        if m:
            flush()
            indent = len(m.group(1)) // 2
            numbered = m.group(2)[0].isdigit()
            text = m.group(3)
            i += 1
            while i < len(lines) and lines[i].startswith("  " * (indent + 1)) and lines[i].strip() \
                    and not re.match(r"^\s*([-*]|\d+[.)])\s+", lines[i]):
                text += " " + lines[i].strip()
                i += 1
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.left_indent = Cm(1.25 + 0.75 * indent)
            p.paragraph_format.first_line_indent = Cm(-0.5)
            prefix = (m.group(2) if numbered else "–") + " "
            p.add_run(prefix)
            add_inline(p, text)
            continue
        if s.startswith(">"):
            flush()
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(1)
            add_inline(p, s.lstrip("> ").strip(), size=Pt(12))
            i += 1
            continue
        if not s:
            flush()
            i += 1
            continue
        para_buf.append(line)
        i += 1
    flush()


INCLUDE = re.compile(r"^\{\{include\s+(\S+)(?:\s+shift=(\d))?(?:\s+skip_h1)?\}\}\s*$")


def expand_includes(md: str, base: Path) -> str:
    """Підставляє вміст файлів за директивою {{include path shift=N skip_h1}}."""
    out = []
    for line in md.split("\n"):
        m = INCLUDE.match(line.strip())
        if not m:
            out.append(line)
            continue
        path = (base / m.group(1)).resolve()
        shift = int(m.group(2) or 0)
        text = expand_includes(path.read_text(encoding="utf-8"), path.parent)
        lines = text.split("\n")
        if "skip_h1" in line and lines and lines[0].startswith("# "):
            lines = lines[1:]
        in_code = False
        for ln in lines:
            if ln.strip().startswith("```"):
                in_code = not in_code
            if not in_code and re.match(r"^#{1,6}\s", ln):
                ln = "#" * shift + ln
                if ln.startswith("#####"):
                    ln = "####" + ln.lstrip("#")
            out.append(ln)
    return "\n".join(out)


def title_page(doc: Document, spec: dict) -> None:
    t = spec["title"]

    def centered(text, bold=False, size=14, space=0):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(space)
        r = p.add_run(text)
        r.bold = bold
        r.font.size = Pt(size)

    centered("Міністерство освіти і науки України")
    centered(UNIVERSITY)
    for _ in range(6):
        doc.add_paragraph()
    if t["kind"] == "report":
        centered("ЗВІТ", bold=True, size=16)
        centered(f"з лабораторної роботи № {t['lab']}")
        centered(f"з дисципліни «{COURSE}»")
        centered(f"на тему: «{t['topic']}»", space=6)
    else:
        centered(t["heading"], bold=True, size=16)
        centered("кваліфікаційної роботи бакалавра")
        centered("на тему: «Інтелектуальна платформа виявлення та оцінювання ринкових можливостей»")
        centered("(DemandLens)")
    for _ in range(5):
        doc.add_paragraph()
    for line in (
        "Виконав: студент 4 курсу",
        f"спеціальності {SPECIALTY}",
        STUDENT,
        "Науковий керівник: —",
    ):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(9)
        p.add_run(line)
    for _ in range(4):
        doc.add_paragraph()
    centered(f"Чернівці — {t.get('year', 2026)}")
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def main() -> None:
    spec = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    doc = Document()
    set_base_styles(doc)
    title_page(doc, spec)
    figure_counter = [0]
    for k, src in enumerate(spec["sources"]):
        path = (ROOT / src).resolve()
        md = expand_includes(path.read_text(encoding="utf-8"), path.parent)
        if k and spec.get("page_break_between", True):
            doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        render_markdown(doc, md, path.parent, figure_counter)
    out = ROOT / spec["output"]
    out.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out))
    print(f"OK {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
