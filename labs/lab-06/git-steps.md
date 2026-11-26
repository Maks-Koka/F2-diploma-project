# ЛР№6 — Git-операції (PowerShell)

```powershell
Set-Location F2-diploma-project
git switch feature/chapter2-architecture
git checkout -b feature/chapter2-architecture-data-api-logic
New-Item -ItemType Directory -Force docs\api

# Перевірки перед комітом
redocly lint docs/api/openapi.yaml
python tools\check_mermaid.py docs\2_design.md
python tools\check_consistency.py
vale docs

git add docs/2_design.md docs/api docs/srs.md docs/README.md DECISIONS.md
git commit -m "docs: complete chapter 2 data models, API specs and mathematical algorithms"
git add labs/lab-06 tools PROGRESS.md
git commit -m "docs(lab-06): add report, audit logs and defense script"
git push -u origin feature/chapter2-architecture-data-api-logic

gh pr create --base main --head feature/chapter2-architecture-data-api-logic `
  --title "docs: chapter 2 data models, OpenAPI contract and critical algorithms" `
  --body-file labs/lab-06/pr-body.md
```
