# ЛР№7 — Git-операції (PowerShell)

```powershell
Set-Location F2-diploma-project
git switch feature/chapter2-architecture-data-api-logic
git checkout -b feature/chapter2-consolidation

# Use Case діаграма: генерація .mdj і експорт PNG через StarUML CLI
python tools\gen_usecase_mdj.py

# Локальна перевірка перед пушем (ті самі правила, що в CI)
markdownlint --config .markdownlint.json "docs/**/*.md" "labs/**/*.md" --ignore "labs/**/report.md" --ignore "labs/**/pr-body.md"
vale docs
redocly lint docs/api/openapi.yaml

git add docs DECISIONS.md tools/gen_usecase_mdj.py
git commit -m "docs: consolidate chapter 2 with use cases, API topology and AppSec"
git add .markdownlint.json .github/workflows/docs-linter.yml
git commit -m "ci: add docs quality gate with markdownlint, vale and redocly"
git add labs/lab-07 tools PROGRESS.md HANDOFF.md
git commit -m "docs(lab-07): add chapters 1-2 document, report and defense script"
git push -u origin feature/chapter2-consolidation

gh pr create --base main --head feature/chapter2-consolidation `
  --title "docs: consolidate chapter 2 and add docs quality gate" `
  --body-file labs/lab-07/pr-body.md
gh pr checks --watch
```
