"""Збирає PNG-сторінки попереднього перегляду в одне зображення-сітку для швидкої перевірки верстки.

Використання: python tools/contact_sheet.py <preview_dir> <stem> <out.png> [cols]
"""
import sys
from pathlib import Path

from PIL import Image


def main() -> None:
    src = Path(sys.argv[1])
    pages = sorted(src.glob(f"{sys.argv[2]}_p*.png"))
    cols = int(sys.argv[4]) if len(sys.argv) > 4 else 4
    ims = [Image.open(p) for p in pages]
    w, h = ims[0].size
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w, rows * h), "white")
    for i, im in enumerate(ims):
        sheet.paste(im, ((i % cols) * w, (i // cols) * h))
    sheet.save(sys.argv[3])
    print(len(ims), sheet.size)


if __name__ == "__main__":
    main()
