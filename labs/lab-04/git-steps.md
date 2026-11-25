# ЛР№4 — Git-операції (PowerShell)

```powershell
Set-Location F2-diploma-project
git switch feature/chapter1-analytics
git checkout -b feature/chapter1-final

vale docs/1_analysis.md docs/README.md
python tools\build_docx.py tools\specs\chapter1.json

git add docs/1_analysis.md docs/README.md
git commit -m "docs: finalize chapter 1 with as-is/to-be models and requirements"
git add labs/lab-04 tools PROGRESS.md
git commit -m "docs(lab-04): add chapter 1 document, report and AI insights"
git push -u origin feature/chapter1-final

gh pr create --base main --head feature/chapter1-final `
  --title "docs: finalize chapter 1 analysis and requirements" `
  --body-file labs/lab-04/pr-body.md
```
