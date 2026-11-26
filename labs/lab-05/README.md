# ЛР№5. SRS (ISO/IEC/IEEE 29148), C4 Model (Levels 1–3) та ADR

Гілка: `feature/chapter2-architecture` (від `feature/chapter1-final`, DECISIONS.md D-03). PR: у `main`.

Використані артефакти: вимоги To-Be, Core Features і NFR (Розділ 1, підрозділ 1.5, ЛР№4) → SRS;
реєстр ID (DECISIONS.md). Результат використовується в ЛР№6 (ERD, OpenAPI, алгоритми трасуються на
SRS-FUN і контейнери C4) і ЛР№7 (2.1, 2.3, 2.4 спираються на C4 L3 і ADR-001).

## Відповідність вимогам і рубрикатору

| Вимога завдання | Де артефакт | Критерій рубрикатора (максимум) | Як виконано |
|---|---|---|---|
| Завд.1. SRS: System Context, FR з ID і «повинна», NFR з індексами, Verification Criteria з інструментами, Glossary 5–7 | [docs/srs.md](../../docs/srs.md); Notion «Специфікація вимог (SRS)» | 1,5 бала: 5 блоків, атомарність, ID, інструменти верифікації, лог ШІ-аудитора | 25 атомарних FR (`SRS-FUN-01…25`), 23 NFR (`SRS-NFR-<категорія>-NN`), таблиця верифікації (pytest, Postman, k6, SonarQube, Trivy, Prometheus, OWASP ZAP, testssl.sh), глосарій 7 термінів, матриця трасування |
| Завд.2. C4 L1, L2 у Mermaid, протокол на кожній стрілці, опис вузлів | [docs/2_design.md](../../docs/2_design.md) → 2.2 | 2 бали: актори, зовнішні системи, контейнери стеку, протоколи, лог з першими версіями | L1: 2 актори, 4 зовнішні API; L2: 14 контейнерів у двох представленнях; кожен зв'язок має протокол і порт; v1 у [drafts/c4-v1.md](drafts/c4-v1.md) |
| Завд.3. C4 L3 найскладнішого сервісу: Inbound/Core/Outbound, DTO, Guards, error handler, логування, метрики | `2_design.md` → 2.3 | 2 бали: шари Clean Architecture, SOLID/DI, валідація, захист, обробка помилок | Core API: 16 компонентів; Guard RoleAndOwnershipPermission, JWTAuthentication, UserRateThrottle, DTO, GlobalExceptionHandler, ObservabilityMiddleware; порти і адаптери (DIP) |
| Завд.4. ADR-001 за Нігардзом, Approved | [docs/adr/0001-choice-of-technology.md](../../docs/adr/0001-choice-of-technology.md) | 1,5 бала: технічна аргументація, ≥ 2 альтернативи, чесні негативні наслідки | 3 альтернативи (Celery + Redis, Kafka, Celery + RabbitMQ) за 7 критеріями; 6 негативних наслідків (SPOF Redis, at-least-once, ліцензія AGPLv3, CI/CD) |
| Завд.5. `srs.md`, `adr/`, трасування у `2_design.md`, README, PR | GitHub | 1 бал: PR з `feature/chapter2-architecture`, відносні посилання, Conventional Commits, README | Відносні посилання `srs.md#srs-fun-NN` і `adr/0001-…` у таблицях під кожною діаграмою; README з навігацією і статусами |

## Відповідність нумерації (методичка ЛР№5 → фінальна структура ЛР№7)

| Номер у методичці ЛР№5 | Зміст | Фінальний номер (ЛР№7, DECISIONS.md D-06) |
|---|---|---|
| 2.1. Контекстне та контейнерне моделювання (C4 L1–2) | Діаграми контексту і контейнерів | 2.2 |
| 2.2. Компонентне моделювання критичного сервісу (C4 L3) | Діаграма компонентів Core API | 2.3 |
| 2.3. Документування архітектурних рішень (ADR) | ADR-001 | 2.1.1 (реєстр ADR) + `docs/adr/` |

## Склад папки

| Файл | Призначення |
|---|---|
| [ai-insights.md](ai-insights.md) | 4 сесії аудиту: SRS, C4 L1–2, C4 L3, ADR |
| [drafts/c4-v1.md](drafts/c4-v1.md) | Перші версії діаграм до рев'ю |
| [defense.md](defense.md) | Сценарій пітчу (5 хв) і питання |
| [git-steps.md](git-steps.md) | Команди PowerShell і PR |
| `Лабораторна_5_Кока_МС.docx` | Звіт |
