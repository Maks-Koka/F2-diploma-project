"""Конвертація .docx у PDF (LibreOffice) і PNG-сторінки (PyMuPDF) для візуальної перевірки верстки.

Використання: python tools/preview.py <file.docx> <out_dir>
"""
import subprocess
import sys
from pathlib import Path

import pymupdf

SOFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"


def main() -> None:
    docx = Path(sys.argv[1]).resolve()
    out = Path(sys.argv[2]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    subprocess.run([SOFFICE, "--headless", "--convert-to", "pdf", "--outdir", str(out), str(docx)],
                   check=True, capture_output=True)
    pdf = out / (docx.stem + ".pdf")
    doc = pymupdf.open(pdf)
    print(f"pages={doc.page_count}")
    for i, page in enumerate(doc):
        page.get_pixmap(dpi=60).save(out / f"{docx.stem}_p{i + 1:02d}.png")


if __name__ == "__main__":
    main()
