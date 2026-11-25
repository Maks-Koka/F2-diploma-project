# ЛР№2 — Git-операції (PowerShell)

```powershell
Set-Location F2-diploma-project
git switch main
git pull origin main
git checkout -b feature/docs-skeleton

# Скелет пояснювальної записки
New-Item -ItemType File -Force docs\README.md, docs\0_intro.md, docs\1_analysis.md, docs\2_design.md, docs\3_implementation.md, docs\4_conclusions.md

git add docs
git commit -m "docs: initialize thesis skeleton and add scientific apparatus"
git add labs/lab-02 tools/specs/lab-02.json
git commit -m "docs(lab-02): add report, AI insights and defense script"
git push -u origin feature/docs-skeleton

# Pull Request у main (без merge до показу викладачу)
gh pr create --base main --head feature/docs-skeleton `
  --title "docs: initialize thesis skeleton and scientific apparatus" `
  --body-file labs/lab-02/pr-body.md
gh pr view --web
```
