# ЛР№1 — Git-операції (PowerShell)

Гілка: `main`. Pull Request для ЛР№1 не передбачено методичкою (перший коміт і пуш у `main`).

```powershell
# Ініціалізація локального репозиторію
New-Item -ItemType Directory -Force F2-diploma-project; Set-Location F2-diploma-project
git init -b main
New-Item -ItemType Directory -Force src, docs
New-Item -ItemType File -Force src\.gitkeep

# Створення публічного віддаленого репозиторію та прив'язка origin
gh repo create F2-diploma-project --public --source . --remote origin

# Перший коміт за Conventional Commits
git add .gitignore src/.gitkeep docs/proposal.md
git commit -m "feat: initialize docs-as-code structure with thesis proposal"
git push -u origin main

# Службові файли проєкту та матеріали ЛР№1
git add CLAUDE.md DECISIONS.md PROGRESS.md HANDOFF.md tools labs/lab-01
git commit -m "docs(lab-01): add PKM setup report, AI insights and defense script"
git push origin main

# Перевірка
git log --oneline
curl.exe -s -o NUL -w "%{http_code}" https://github.com/Maks-Koka/F2-diploma-project
```

Після отримання реального відгуку керівника (DECISIONS.md, D-10):

```powershell
git switch main
# внести зміни у docs/proposal.md відповідно до відгуку
git add docs/proposal.md
git commit -m "fix: адресація зауважень керівника"
git push origin main
```
