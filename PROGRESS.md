# PROGRESS.md — чекліст виконання

Позначки: `[x]` виконано, `[ ]` не виконано, `[M]` ручна дія студента (причина в HANDOFF.md).

## 0. Підготовка

- [x] Прочитано ЛР№1–7 (`labs-input/`)
- [x] Встановлено інструменти: LibreOffice, StarUML, Vale, mermaid-cli, markdownlint-cli, Redocly CLI
- [x] CLAUDE.md, DECISIONS.md (рамка), PROGRESS.md
- [x] Репозиторій GitHub створено, перший коміт у `main`

## Реєстр Notion (draft-сторінка, приватна, workspace «Сергій's Workspace»)

| Об'єкт | ID / URL |
|---|---|
| Корінь `F2_Diploma_Кока_МС` | 42319239-ff0e-81ea-bac6-fef70614ef8c |
| БД «Календарний план» | db 42319239ff0e81f6bcbff9f3e9dd43b7, ds collection://42319239-ff0e-8109-9e2e-000b61bda435 |
| БД «Календарний план — шаблон (ЛР№1)» | db 42319239ff0e811b9e14dc15b3e64cf5, ds collection://42319239-ff0e-811c-ab64-000b2dc741d6 |
| БД «Репозиторій артефактів» | db 42319239ff0e81e38752f5c2869724b1, ds collection://42319239-ff0e-8108-a7f3-000b14c9743c |
| Thesis_Proposal | 42319239-ff0e-811f-8c0a-c0134c5d3315 |
| AI Insights (AI Disclosure) | 42319239-ff0e-81e6-b7fc-ce0527a662d8 (toggle h2 на кожну ЛР) |
| Етапи КП 1–7 (сторінки БД) | 1: 42319239-ff0e-817e-a3ed-d9f5d6eef34d; 2: 42319239-ff0e-8199-a387-fa223c50068c; 3: 42319239-ff0e-81b5-8212-ec38967e7f73; 4: 42319239-ff0e-81a4-82dc-f6adf1700f88; 5: 42319239-ff0e-817d-b5f0-efa76d80596d; 6: 42319239-ff0e-8198-8472-fe56dae40552; 7: 42319239-ff0e-813c-9bd0-ca74c4a2c0db |
| Timeline view | view://42319239-ff0e-8150-aba7-000cd3105307 |

Notion-синхронізацію великих Markdown-файлів виконує фоновий субагент (general-purpose) за інструкцією:
створити підсторінку під коренем / додати toggle h2 у AI Insights.

Репозиторій: https://github.com/Maks-Koka/F2-diploma-project

## ЛР№1 (main)

- [x] Notion: коренева сторінка `F2_Diploma_Кока_МС` (Паспорт проєкту, Репозиторій артефактів, Календарний план — порожній, Supervisor Feedback — «очікується»)
- [x] Notion: сторінка Thesis_Proposal + блок AI Insights (ЛР№1)
- [x] `docs/proposal.md`
- [x] Структура `/src`, `/docs`; коміт Conventional Commits; посилання на репозиторій у Notion
- [x] `labs/lab-01/`: README, ai-insights, defense, git-steps, звіт `.docx`
- [M] Доступ викладачу й керівнику (Can comment)
- [M] Відгук керівника і коміт `fix: адресація зауважень керівника`

## ЛР№2 (`feature/docs-skeleton`)

- [x] Науковий апарат (Notion + `docs/0_intro.md`)
- [x] Календарний план заповнено (7 етапів), Timeline view
- [x] Скелет `docs/` (README з таблицею плану, 1–4 файли)
- [x] `labs/lab-02/` повний комплект, звіт `.docx`
- [x] PR у `main`

## ЛР№3 (`feature/chapter1-analytics`)

- [x] 3 аналоги (перевірені пошуком), картка в Notion
- [x] Порівняльна матриця 5–6 технічних критеріїв + висновок 1.2
- [x] `docs/1_analysis.md`, лінтинг стилю
- [x] `labs/lab-03/` повний комплект, звіт `.docx`
- [x] PR у `main`

## ЛР№4 (`feature/chapter1-final`)

- [x] Аналіз предметної області As-Is (Notion)
- [x] To-Be, Core Features 6–8, NFR, постановка задачі
- [x] `F2_Diploma_Chapter1_Кока.docx` ≥ 5 с.
- [x] README (NFR Matrix + посилання), `1_analysis.md`
- [x] Статус етапу в календарному плані
- [x] `labs/lab-04/` повний комплект, звіт `.docx`
- [x] PR у `main` (3–4 пункти обмежень)

## ЛР№5 (`feature/chapter2-architecture`)

- [x] `docs/srs.md` (ISO/IEC/IEEE 29148)
- [x] C4 L1, L2 (Mermaid)
- [x] C4 L3 (Mermaid)
- [x] ADR-001 (Approved)
- [x] `2_design.md` з трасуванням, README
- [x] `labs/lab-05/` повний комплект + таблиця нумерації, звіт `.docx`
- [x] PR у `main`

## ЛР№6 (`feature/chapter2-architecture-data-api-logic`)

- [x] ERD (Mermaid) + специфікація таблиць + план індексів
- [x] `docs/api/openapi.yaml` (валідовано Redocly)
- [x] 3 алгоритми (текст + `graph TD`)
- [x] Інтеграційний аудит + Production Readiness Report
- [x] `labs/lab-06/` повний комплект + таблиця нумерації, звіт `.docx`
- [x] PR у `main`

## ЛР№7 (`feature/chapter2-consolidation`)

- [ ] 2.1 обґрунтування архітектури (≥ 1 с.)
- [ ] Use Case діаграма StarUML (`.mdj` + PNG) + 3 специфікації UC
- [ ] Топологія API + Data Flows
- [ ] Серверне ядро + AppSec
- [ ] `.markdownlint.json`, `.github/workflows/docs-linter.yml`, зелений CI
- [ ] `F2_Diploma_Chapters1-2_Кока.docx`
- [ ] `labs/lab-07/` повний комплект, звіт `.docx`
- [ ] PR у `main`

## Фінал

- [ ] Наскрізна перевірка ID/типів/статусів
- [ ] Перевірка посилань, вичитка, Vale
- [ ] HANDOFF.md
