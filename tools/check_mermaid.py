"""Компілює всі блоки ```mermaid у вказаних Markdown-файлах через mmdc; друкує результат по кожному."""
import re, subprocess, sys, tempfile, pathlib
ok = True
for f in sys.argv[1:]:
    text = pathlib.Path(f).read_text(encoding="utf-8")
    for i, m in enumerate(re.finditer(r"```mermaid\n(.*?)```", text, re.S), 1):
        d = pathlib.Path(tempfile.mkdtemp())
        (d / "in.mmd").write_text(m.group(1), encoding="utf-8")
        p = subprocess.run(["mmdc.cmd", "-i", str(d / "in.mmd"), "-o", str(d / "out.svg")], capture_output=True, text=True, encoding="utf-8", errors="replace")
        good = (d / "out.svg").exists()
        ok &= good
        first = m.group(1).strip().split("\n")[0]
        print(f"{f} #{i} {first}: {'OK' if good else 'FAIL'}")
        if not good:
            print((p.stderr or p.stdout)[-800:])
sys.exit(0 if ok else 1)
