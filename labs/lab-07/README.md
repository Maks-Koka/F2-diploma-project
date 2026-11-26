# ЛР№7. Консолідація архітектурного контуру, Use Cases і Docs Quality Gate у CI/CD

Гілка: `feature/chapter2-consolidation` (від `feature/chapter2-architecture-data-api-logic`, DECISIONS.md
D-03, D-05). PR: у `main`.

Використані артефакти: C4 L2–L3 і ADR-001 (ЛР№5) → 2.1, 2.3.1, 2.4; `openapi.yaml`, ERD, ALG-01…03
(ЛР№6) → 2.5.2–2.5.3, 2.6; Розділ 1 (ЛР№4) → зведений документ Розділів 1–2.

## Відповідність вимогам і рубрикатору

| Вимога завдання | Де артефакт | Критерій рубрикатора (максимум) | Як виконано |
|---|---|---|---|
| Завд.1. 2.1 обґрунтування (≥ 1 с.): макростиль, патерни, Circuit Breaker, Eventual Consistency, SPOF, FinOps | [docs/2_design.md](../../docs/2_design.md) → 2.1.2–2.1.4 | 1,25 бала: без «води», звіт ШІ-техліда і трек виправлень | ≈ 2 сторінки; 9 патернів з проблемою, яку розв'язують; числові аргументи; лог 7 зауважень |
| Завд.2. Use Case у StarUML (межі, актори, include/extend, узагальнення), 2–3 специфікації | `docs/uml/use-case-diagram.mdj`, `.png`; `2_design.md` → 2.6 | 3 бали: StarUML, Happy Path з реакцією сервера, Pre/Postconditions, AF, EF з відкатами | 12 UC, 2 первинні і 4 вторинні актори, 9 «include», 1 «extend», 1 узагальнення; UC-03, UC-04, UC-05: 7 AF, 5 EF |
| Завд.3. Топологія API-маршрутів і Data Flows | `2_design.md` → 2.5.2–2.5.3 | 1,25 бала: відповідність контракту, Max Body Size, пагінація, CORS, лог | 17 маршрутів = 17 операцій `openapi.yaml`; 3 Data Flows з 1 MiB, CORS, `page_size` ≤ 100, IDOR-перевірками |
| Завд.4. Серверне ядро і AppSec | `2_design.md` → 2.3.1, 2.4.1 | 1,25 бала: OWASP Top 10, Argon2id, DTO, Guards, Audit Logging | 12 загроз OWASP / API Security з механізмом, компонентом і вимогою |
| Завд.5. Моноліт Розділів 1–2, `.markdownlint.json`, `.github/workflows/docs-linter.yml`, зелений CI | [F2_Diploma_Chapters1-2_Кока.docx](F2_Diploma_Chapters1-2_Кока.docx); CI | 1,25 бала: моноліт, зелений пайплайн | Документ Розділів 1–2; 3 jobs (markdownlint, Vale, Redocly) |

Підрозділ 2.2 «Компонентне моделювання…» методички ЛР№7 відповідає фінальному 2.3, а 2.3 «AppSec»
— фінальному 2.4 (нумерація Завд.5 ЛР№7, DECISIONS.md D-06).

## Склад папки

| Файл | Призначення |
|---|---|
| [ai-insights.md](ai-insights.md) | 5 сесій: 2.1, Use Cases, API, AppSec, CI |
| [defense.md](defense.md) | Сценарій пітчу (6 хв) і питання |
| [git-steps.md](git-steps.md) | Команди PowerShell і PR |
| `F2_Diploma_Chapters1-2_Кока.docx` | Зведений документ Розділів 1–2 |
| `Лабораторна_7_Кока_МС.docx` | Звіт |
