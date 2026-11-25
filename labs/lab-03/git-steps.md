# ЛР№3 — Git-операції (PowerShell)

```powershell
Set-Location F2-diploma-project
git switch feature/docs-skeleton
git checkout -b feature/chapter1-analytics

# Лінтинг стилю перед комітом
vale docs/1_analysis.md

git add docs/1_analysis.md
git commit -m "docs: complete section 1.2 engineering competitive analysis and matrix"
git add labs/lab-03 tools DECISIONS.md PROGRESS.md
git commit -m "docs(lab-03): add report, AI insights and defense script"
git push -u origin feature/chapter1-analytics

gh pr create --base main --head feature/chapter1-analytics `
  --title "docs: engineering competitive analysis of analogues" `
  --body-file labs/lab-03/pr-body.md
```

Гілка створена від `feature/docs-skeleton`, тому до злиття PR №1 вкладка Files changed також показує
зміни ЛР№2 (DECISIONS.md, D-03).
