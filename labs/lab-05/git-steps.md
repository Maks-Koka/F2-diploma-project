# ЛР№5 — Git-операції (PowerShell)

```powershell
Set-Location F2-diploma-project
git switch feature/chapter1-final
git checkout -b feature/chapter2-architecture
New-Item -ItemType Directory -Force docs\adr

# Перевірка компіляції діаграм і стилю
python tools\check_mermaid.py docs\2_design.md
vale docs/srs.md docs/2_design.md docs/adr/0001-choice-of-technology.md

git add docs/srs.md docs/2_design.md docs/adr docs/README.md DECISIONS.md
git commit -m "docs: implement ISO 29148 SRS, model C4 levels 1-3 via Mermaid and log ADR-001"
git add labs/lab-05 tools PROGRESS.md
git commit -m "docs(lab-05): add report, AI audit logs and defense script"
git push -u origin feature/chapter2-architecture

gh pr create --base main --head feature/chapter2-architecture `
  --title "docs: SRS (ISO 29148), C4 levels 1-3 and ADR-001" `
  --body-file labs/lab-05/pr-body.md
```
