# HANDOFF.md — підсумковий звіт

Стан на 26.11.2026. Виконано ЛР№1–7 для теми «Інтелектуальна платформа виявлення та оцінювання
ринкових можливостей» (DemandLens). Код застосунку не писався: лише документація, схеми, контракти,
конфігурації лінтера і CI, допоміжні скрипти збирання документів (`tools/`).

## Посилання

| Ресурс | Адреса |
|---|---|
| Репозиторій | https://github.com/Maks-Koka/F2-diploma-project |
| PR №1 ЛР№2 `feature/docs-skeleton` | https://github.com/Maks-Koka/F2-diploma-project/pull/1 |
| PR №2 ЛР№3 `feature/chapter1-analytics` | https://github.com/Maks-Koka/F2-diploma-project/pull/2 |
| PR №3 ЛР№4 `feature/chapter1-final` | https://github.com/Maks-Koka/F2-diploma-project/pull/3 |
| PR №4 ЛР№5 `feature/chapter2-architecture` | https://github.com/Maks-Koka/F2-diploma-project/pull/4 |
| PR №5 ЛР№6 `feature/chapter2-architecture-data-api-logic` | https://github.com/Maks-Koka/F2-diploma-project/pull/5 |
| PR №6 ЛР№7 `feature/chapter2-consolidation` | https://github.com/Maks-Koka/F2-diploma-project/pull/6 |
| CI Docs Quality Gate (зелений) | https://github.com/Maks-Koka/F2-diploma-project/actions/runs/45837218923 |
| Notion: корінь `F2_Diploma_Кока_МС` | https://app.notion.com/p/42319239ff0e81eabac6fef70614ef8c |

ЛР№1 виконано безпосередньо в `main` (методичка не передбачає PR). Гілки ЛР№2–7 утворюють ланцюжок
(DECISIONS.md, D-03): кожен PR відкрито в `main`, тому до злиття попередніх PR вкладка Files changed
показує і їхні зміни.

## Що перевірено інструментально

| Перевірка | Результат |
|---|---|
| Vale (`DemandLens.Subjective`, `DemandLens.Transliteration`) по `docs/` | 0 помилок |
| markdownlint (`docs/**`, `labs/**`, крім службових `report.md`, `pr-body.md`) | 0 зауважень, CI зелений |
| Redocly lint `docs/api/openapi.yaml` | 0 помилок, 0 попереджень |
| `mmdc`: 10 діаграм Mermaid у `2_design.md` | Усі компілюються |
| `tools/check_consistency.py`: ENUM, 106 полів API ↔ БД, ID | 0 розбіжностей (мутаційний тест пройдено) |
| Відносні посилання і якорі (218) | 0 битих |
| Верстка `.docx` (LibreOffice → PDF → перегляд сторінок) | Титули і таблиці виправлено; Розділ 1 — 18 с., Розділи 1–2 — 64 с. |

## Самооцінка за рубрикаторами

| ЛР | Макс. | Очікувано | Докази / ризики |
|---|---|---|---|
| ЛР№1 | 10 | 8 | Завд.1–4 виконано (Notion, proposal, AI Insights, репозиторій). Завд.5 (2 бали) потребує реального відгуку керівника; доступ для викладача і керівника надає студент |
| ЛР№2 | 5 | 5 | Науковий апарат, 7 етапів, Timeline, PR №1 |
| ЛР№3 | 5 | 5 | 3 діючі аналоги, 6 технічних критеріїв, висновок з trade-off, PR №2 |
| ЛР№4 | 6 | 6 | As-Is (B1–B10), To-Be, 8 CF, 23 NFR, Розділ 1 (18 с.), PR №3 з 4 обмеженнями |
| ЛР№5 | 8 | 8 | SRS (25 FR, 23 NFR), C4 L1–L3, ADR-001 Approved, трасування, PR №4 |
| ЛР№6 | 8 | 8 | ERD 27 таблиць, OpenAPI 17 операцій, 3 алгоритми, аудит (10 розбіжностей), PR №5 |
| ЛР№7 | 8 | 8 | 2.1, StarUML Use Case, 3 UC-специфікації, топологія API, AppSec, зелений CI, PR №6. Ризик: водяний знак UNREGISTERED на PNG |

Штрафи за дедлайн і регламент захисту не автоматизуються.

## Потребує дії студента

1. **Доступ у Notion.** Сторінка `F2_Diploma_Кока_МС` створена як приватна в workspace «Сергій's
   Workspace». Share → Invite → адреси викладача і керівника → Can comment. Без цього ЛР№1, Завд.1
   оцінюється нижче максимуму («доступ закритий» — 0 балів).
2. **Відгук керівника (ЛР№1, Завд.5, 2 бали).** Після призначення керівника надіслати йому посилання на
   `Thesis_Proposal` і репозиторій; внести реальний відгук у блок Supervisor Feedback; за наявності
   зауважень виправити `docs/proposal.md` у `main` і зробити коміт `fix: адресація зауважень керівника`
   (команди — `labs/lab-01/git-steps.md`). Відгук не імітувався (DECISIONS.md, D-10).
3. **StarUML.** PNG експортовано з незареєстрованої версії, тому на ньому водяний знак UNREGISTERED.
   За наявності ліцензії відкрити `docs/uml/use-case-diagram.mdj`, за потреби підправити розташування
   і виконати File → Export Diagram As → PNG поверх `docs/uml/use-case-diagram.png`, потім
   `python tools\build_docx.py tools\specs\chapters12.json` і `tools\specs\lab-07.json`.
4. **Timeline view.** Вигляд «Timeline (Roadmap)» бази «Календарний план» створено через API;
   перевірити відображення в Notion і за потреби вибрати масштаб «Month».
5. **Порядок злиття PR після захистів:** #1 → #2 → #3 → #4 → #5 → #6 (кожен після захисту відповідної
   ЛР). Після злиття попереднього PR diff наступного скоротиться до власних змін.
6. **Живий захист** за `labs/lab-0N/defense.md` (хронометраж 3/3/3/4/5/5/6 хв, ≈ 120 слів/хв).
7. **Перегляд AI Insights.** Чернетки й аудити виконано в сесії Claude Code, і журнали це прямо
   вказують. Перед захистом варто прочитати журнали і бути готовим пояснити кожне рішення
   «прийнято/відхилено».

## Відомі обмеження

- Розділи 5–7 вихідного промпту не надійшли; вимоги відновлено з методичок (CLAUDE.md).
- Файл «моїх даних» не надано; використано лише дані з промпту.
- Числа NFR є цільовими значеннями проєкту; їх фактичне досягнення перевіряється в Розділі 3.
- Notion автоматично перетворює деякі назви файлів (`0_intro.md`) на посилання; на зміст це не впливає.
