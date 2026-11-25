# DECISIONS.md — канонічні рішення та журнал конфліктів

Документ фіксує наскрізні рішення, що зв'язують ЛР№1–7. Будь-який файл у `docs/` і `labs/` має
відповідати цьому реєстру. Зміна канонічного значення виконується спочатку тут, потім у всіх файлах.

## 1. Ідентифікація проєкту

| Параметр | Значення |
|---|---|
| Студент | Кока Максим Сергійович (КМС) |
| Спеціальність | 121/F2 «Інженерія програмного забезпечення» |
| Науковий керівник | — (не призначений) |
| Тема (UA) | Інтелектуальна платформа виявлення та оцінювання ринкових можливостей |
| Назва системи (EN) | DemandLens |
| Розширена назва (EN) | DemandLens: Explainable Market Opportunity Discovery Platform |
| Репозиторій | `F2-diploma-project` (GitHub, публічний, власник `Maks-Koka`) |
| PKM | Notion, коренева сторінка `F2_Diploma_Кока_МС` |

## 2. Журнал рішень і конфліктів вимог

| ID | Рішення | Обґрунтування |
|---|---|---|
| D-01 | Назва EN — одне слово DemandLens; розширена назва вживається лише в описах | Вимога студента: назва з 1–2 слів. Веб-пошук (25.11.2026) не виявив продукту з такою назвою |
| D-02 | Календарний план містить рівно 7 етапів, синхронізованих 1:1 із 7 завданнями наукового апарату | Промпт ЛР№2 пропонує 8–10 етапів, а рубрикатор ЛР№2 вимагає «усі 7 етапів» і синхронізацію із завданнями. Пріоритет має рубрикатор |
| D-03 | Гілки ЛР№2–7 утворюють ланцюжок: кожна відгалужується від попередньої; кожен PR відкривається в `main` і не зливається до захисту | Методички вимагають PR у `main` без merge, а кожна ЛР спирається на файли попередньої. ЛР№5 пропонує гілку «від чистої main», але в такій гілці немає скелета `docs/` з ЛР№2. Після послідовного злиття PR diff кожного наступного PR скорочується до власних змін |
| D-04 | Гілка ЛР№6 — `feature/chapter2-architecture-data-api-logic` | ЛР№6 дозволяє «нову підгілку логічного проєктування (chapter2-architecture)», рубрикатор шукає `feature/chapter2-architecture`. Назва зберігає цей префікс і не конфліктує з гілкою ЛР№5 (Git не допускає одночасно `x` і `x/y`) |
| D-05 | Гілка ЛР№7 — `feature/chapter2-consolidation` | Методичка ЛР№7 не задає назву гілки |
| D-06 | Фінальна нумерація Розділу 2 — за ЛР№7, Завд.5: 2.1 обґрунтування; 2.2 C4 L1–2; 2.3 C4 L3 і серверне ядро; 2.4 AppSec; 2.5 API і топологія; 2.6 Use Cases; 2.7 моделі даних; 2.8 інтеграційний аудит; висновки | ЛР№7 — найпізніша методичка. ЛР№5 і ЛР№6 використовують іншу нумерацію; таблиці відповідності наведено в `labs/lab-05/README.md` і `labs/lab-06/README.md` |
| D-07 | Алгоритми критичних вузлів (2.6 у ЛР№6) у фінальній структурі розміщено як підрозділ 2.7.4 «Алгоритми обробки даних критичних вузлів» усередині 2.7 | Фінальна структура ЛР№7 не містить окремого підрозділу для алгоритмів. Алгоритми оперують сутностями моделі даних (CollectionRun, Complaint, NeedCluster, NicheScore), тому їх розміщено поруч із моделлю даних; інтеграційний аудит 2.8 посилається на них |
| D-08 | Розділ 1 і Розділи 1–2 зберігаються як локальні `.docx` у репозиторії та як сторінки Notion з правом коментування | ЛР№4 і ЛР№7 вимагають «хмарний документ» із доступом Can comment або «локальний .docx у репозиторії». Сторінка Notion забезпечує коментування, `.docx` — формат здачі |
| D-09 | Reddit Data API виключено з базового набору джерел; передбачено як опційний адаптер, вимкнений за замовчуванням | За даними 2026 року доступ потребує попереднього схвалення навіть для некомерційного використання, строки розгляду не гарантовані (див. розділ 5) |
| D-10 | Відгук наукового керівника не імітується. Блок Supervisor Feedback має статус «очікується»; коміт `fix: адресація зауважень керівника` створюється лише після реального відгуку | Етика академічної доброчесності; рубрикатор ЛР№1 вимагає «реальний текстовий відгук». Порядок дій — у HANDOFF.md |
| D-11 | AI Insights фіксують фактичний процес у Claude Code: чернетка → промпт із методички → звіт аудиту → виправлення. Автор чернеток і аудитів зазначається відкрито | Комплаєнс AI Disclosure без фабрикації «сирих текстів студента» |
| D-12 | Діаграма Use Case будується у StarUML (`.mdj` формується програмно, PNG експортується з StarUML) | ЛР№7 забороняє Mermaid для цієї діаграми |
| D-13 | Розділ 1 у Notion зберігає назву бази «Календарний план»; порожній шаблон ЛР№1 збережено окремою базою «Календарний план — шаблон (ЛР№1)» | ЛР№1 демонструє порожню матрицю, ЛР№2 — заповнену. Обидва стани доступні для захисту |
| D-14 | Архітектурний стиль — модульний моноліт (Django) з асинхронним конвеєром обробки (Celery + Redis), а не мікросервіси | Обмеження стеку та ресурсів одного розробника; детально — ADR-001 і 2.1 |

## 3. Архітектура (контейнери C4 L2)

| Контейнер | Технологія | Призначення |
|---|---|---|
| Web App | Next.js 15 + TypeScript + Tailwind CSS | SSR/SPA-інтерфейс аналітика |
| API Gateway | Nginx 1.27 | TLS-термінація, reverse proxy, ліміт розміру тіла, базовий rate limiting, CORS |
| Core API | Django 5.2 + DRF 3.16 (Gunicorn) | Модульний моноліт: identity, projects, analytics, scoring, reporting |
| Ingestion Worker | Celery 5.5 (Python 3.12) | Ідемпотентний збір даних із зовнішніх API |
| Analytics Worker | Celery 5.5 + pandas + scikit-learn | Виявлення скарг, кластеризація, обчислення рейтингу |
| Scheduler | Celery Beat | Планові повторні збори |
| Primary DB | PostgreSQL 17 + pgvector | Основне сховище (запис) |
| Replica DB | PostgreSQL 17 (streaming replication) | Читання звітів, резервування |
| Broker/Cache | Redis 7.4 | Брокер Celery, кеш, лічильники rate limiting |
| Observability | OpenTelemetry Collector, Prometheus, Grafana, Jaeger | Трасування, метрики, дашборди |

Версії інструментів уточнюються в ЛР№5 веб-пошуком; у документах вказуються лише перевірені значення.

## 4. Реєстр ідентифікаторів

### 4.1. Core Features (CF) → функціональні вимоги (SRS-FUN)

| CF | Модуль | Функція | SRS-FUN |
|---|---|---|---|
| CF-01 | ingestion | Ідемпотентний збір публікацій із відкритих API з урахуванням лімітів | 04, 05 |
| CF-02 | ingestion | Нормалізація, дедуплікація та псевдонімізація документів | 06 |
| CF-03 | analytics | Виявлення скарг і оцінювання інтенсивності проблеми | 07 |
| CF-04 | analytics | Тематична кластеризація потреб | 08 |
| CF-05 | analytics | Порівняння конкурентів ніші | 09 |
| CF-06 | scoring | Прозоре ранжування ніш із рівнем невизначеності | 10, 11 |
| CF-07 | reporting | Пояснення рейтингу та експорт звітів | 12, 13, 14 |
| CF-08 | identity | Автентифікація, RBAC і журнал аудиту | 01, 02, 15, 16 |

Proposal (ЛР№1) містить 7 функцій: CF-01…CF-07; CF-08 додано в ЛР№4 за результатами аудиту.

### 4.2. Функціональні вимоги

| ID | Коротка назва |
|---|---|
| SRS-FUN-01 | Видача пари JWT (access/refresh) за коректними обліковими даними |
| SRS-FUN-02 | Перевірка ролі RBAC і належності об'єкта для кожного запиту |
| SRS-FUN-03 | Створення дослідницького проєкту з ключовими словами та джерелами |
| SRS-FUN-04 | Запуск запуску збору з ключем ідемпотентності |
| SRS-FUN-05 | Збір документів із джерела з rate limiting, backoff і Circuit Breaker |
| SRS-FUN-06 | Нормалізація, дедуплікація та псевдонімізація документів |
| SRS-FUN-07 | Виявлення скарг та обчислення pain_score |
| SRS-FUN-08 | Кластеризація скарг у теми потреб |
| SRS-FUN-09 | Реєстрація конкурентів і збір їхніх публічних метрик |
| SRS-FUN-10 | Обчислення рейтингу ніші за версіонованою моделлю |
| SRS-FUN-11 | Обчислення довірчого інтервалу та рівня невизначеності |
| SRS-FUN-12 | Формування пояснення: внески критеріїв, джерела, аргументи «за», ризики |
| SRS-FUN-13 | Видача ранжованого списку ніш з пагінацією |
| SRS-FUN-14 | Експорт звіту у форматах JSON і CSV |
| SRS-FUN-15 | Запис журналу аудиту для мутуючих дій |
| SRS-FUN-16 | Керування джерелами даних (лише ADMIN) |

### 4.3. Нефункціональні вимоги (канонічні числа)

| ID | Вимога |
|---|---|
| SRS-NFR-PERF-01 | `GET /api/v1/projects/{projectId}/niches`: p95 ≤ 200 мс, p99 ≤ 500 мс при 200 RPS протягом 10 хв; частка помилок < 0,5 % |
| SRS-NFR-PERF-02 | `GET …/niches/{nicheId}/explanation`: p95 ≤ 300 мс при 100 RPS |
| SRS-NFR-PERF-03 | `POST …/collection-runs` і `POST …/scoring-runs`: p95 ≤ 150 мс (постановка в чергу, відповідь 202) |
| SRS-NFR-PERF-04 | Обробка (нормалізація + виявлення скарг) ≥ 2 000 документів/хв на один Analytics Worker (2 vCPU, 4 GiB RAM) |
| SRS-NFR-PERF-05 | Кластеризація 50 000 скарг ≤ 10 хв на одному Analytics Worker |
| SRS-NFR-SCAL-01 | Збільшення кількості Analytics Worker з 1 до 4 підвищує пропускну здатність обробки не менше ніж у 3,2 раза |
| SRS-NFR-SEC-01 | Access JWT RS256, TTL 15 хв; refresh TTL 7 діб з ротацією та відкликанням; публічний ключ публікується через JWKS |
| SRS-NFR-SEC-02 | Паролі хешуються Argon2id (memory_cost = 65 536 KiB, time_cost = 3, parallelism = 4) |
| SRS-NFR-SEC-03 | 100 % ендпоінтів, крім `/auth/tokens*`, `/healthz`, `/.well-known/jwks.json`, захищено JWT і RBAC; 0 ендпоінтів без перевірки належності об'єкта (BOLA) |
| SRS-NFR-SEC-04 | Rate limiting: 100 запитів/хв на користувача; 5 спроб входу/хв на IP; відповідь 429 із заголовком `Retry-After` |
| SRS-NFR-SEC-05 | TLS 1.2+ (TLS 1.3 пріоритетно), HSTS max-age = 31 536 000 с |
| SRS-NFR-SEC-06 | 0 вразливостей рівня HIGH/CRITICAL у звіті Trivy; SonarQube Quality Gate: 0 Vulnerabilities, Security Rating A |
| SRS-NFR-COMP-01 | Ідентифікатори авторів псевдонімізуються HMAC-SHA-256 із секретною сіллю; сирі тексти зберігаються ≤ 180 діб; видалення проєкту виконує soft delete і фізичне очищення через 30 діб |
| SRS-NFR-COMP-02 | Частота запитів до кожного джерела ≤ 80 % від задокументованого ліміту; кожен запит містить ідентифікувальний User-Agent |
| SRS-NFR-REL-01 | Доступність Core API ≥ 99,5 % за календарний місяць |
| SRS-NFR-REL-02 | RPO ≤ 15 хв (WAL-архівування + streaming replica), RTO ≤ 30 хв |
| SRS-NFR-REL-03 | Повторний запуск збору з тим самим Idempotency-Key створює 0 дублікатів; не більше 5 повторів з експоненційним backoff (база 2 с, верхня межа 300 с, jitter ± 20 %) |
| SRS-NFR-REL-04 | Circuit Breaker на джерело: відкривається після 5 послідовних помилок, half-open через 60 с |
| SRS-NFR-OBS-01 | 100 % HTTP-запитів і задач Celery мають trace_id (W3C Trace Context); метрики знімаються кожні 15 с; логи у форматі JSON |
| SRS-NFR-MAINT-01 | Покриття тестами pytest ≥ 80 % рядків backend; SonarQube Maintainability Rating A; дублювання коду ≤ 3 % |
| SRS-NFR-REPRO-01 | Однаковий знімок даних, версія моделі оцінювання і seed дають ідентичний рейтинг (розбіжність 0) |
| SRS-NFR-EXPL-01 | Кожна рекомендація містить 5 внесків критеріїв, ≥ 3 посилання на джерела, ≥ 1 аргумент «за», ≥ 1 ризик і довірчий інтервал |

### 4.4. Use Cases

| ID | Назва | Актор | Специфікація |
|---|---|---|---|
| UC-01 | Автентифікуватися в системі | Аналітик | — |
| UC-02 | Створити дослідницький проєкт | Аналітик | — |
| UC-03 | Запустити збір даних | Аналітик | Так (AF-03A, AF-03B, EF-03A, EF-03B) |
| UC-04 | Запустити ранжування ніш | Аналітик | Так (AF-04A, EF-04A) |
| UC-05 | Переглянути пояснення рейтингу ніші | Аналітик | Так (AF-05A, AF-05B, EF-05A) |
| UC-06 | Порівняти конкурентів ніші | Аналітик | — |
| UC-07 | Експортувати звіт | Аналітик | — |
| UC-08 | Керувати джерелами даних | Адміністратор | — |
| UC-09 | Переглянути журнал аудиту | Адміністратор | — |
| UC-10 | Перевірити токен доступу | — (include) | — |
| UC-11 | Повторити збір після збою джерела | — (extend до UC-03) | — |

Адміністратор успадковує (generalization) усі прецеденти Аналітика.
Вторинні актори: HN Search API (Algolia), Stack Exchange API, GitHub REST API, Wikimedia Analytics API.

### 4.5. API-маршрути (OpenAPI 3.0, база `/api/v1`)

| ID | Метод | Шлях | Ролі | Успіх |
|---|---|---|---|---|
| API-REQ-01 | POST | `/auth/tokens` | анонімний | 201 |
| API-REQ-02 | POST | `/auth/tokens/refresh` | анонімний (refresh) | 201 |
| API-REQ-03 | POST | `/projects` | ANALYST, ADMIN | 201 |
| API-REQ-04 | GET | `/projects` | ANALYST, ADMIN | 200 |
| API-REQ-05 | GET | `/projects/{projectId}` | власник, ADMIN | 200 |
| API-REQ-06 | POST | `/projects/{projectId}/collection-runs` | власник | 202 |
| API-REQ-07 | GET | `/projects/{projectId}/collection-runs/{runId}` | власник, ADMIN | 200 |
| API-REQ-08 | GET | `/projects/{projectId}/complaints` | власник, ADMIN | 200 |
| API-REQ-09 | POST | `/projects/{projectId}/scoring-runs` | власник | 202 |
| API-REQ-10 | GET | `/projects/{projectId}/niches` | власник, ADMIN | 200 |
| API-REQ-11 | GET | `/projects/{projectId}/niches/{nicheId}/explanation` | власник, ADMIN | 200 |
| API-REQ-12 | POST | `/projects/{projectId}/competitors` | власник | 201 |
| API-REQ-13 | GET | `/projects/{projectId}/niches/{nicheId}/competitors` | власник, ADMIN | 200 |
| API-REQ-14 | POST | `/projects/{projectId}/reports` | власник | 201 |
| API-REQ-15 | GET | `/data-sources` | ANALYST, ADMIN | 200 |
| API-REQ-16 | PATCH | `/data-sources/{sourceCode}` | ADMIN | 200 |
| API-REQ-17 | GET | `/audit-events` | ADMIN | 200 |

Службові маршрути поза контрактом бізнес-API: `GET /healthz`, `GET /metrics` (лише внутрішня мережа),
`GET /.well-known/jwks.json`.

### 4.6. ENUM-типи (однакові в ERD, OpenAPI, алгоритмах, UC)

| Тип | Значення |
|---|---|
| `user_role` | `ANALYST`, `ADMIN` |
| `project_status` | `DRAFT`, `ACTIVE`, `ARCHIVED` |
| `run_status` | `PENDING`, `RUNNING`, `COMPLETED`, `PARTIALLY_COMPLETED`, `FAILED`, `CANCELLED` |
| `source_code` | `HACKER_NEWS`, `STACK_EXCHANGE`, `GITHUB_ISSUES`, `WIKIMEDIA_PAGEVIEWS`, `REDDIT` |
| `detection_method` | `LEXICON`, `CLASSIFIER` |
| `niche_status` | `CANDIDATE`, `SCORED`, `ARCHIVED` |
| `uncertainty_level` | `LOW`, `MEDIUM`, `HIGH` |
| `criterion_code` | `DEMAND_VOLUME`, `PAIN_INTENSITY`, `GROWTH_TREND`, `COMPETITION_GAP`, `SOURCE_DIVERSITY` |
| `argument_kind` | `PRO`, `RISK` |
| `report_format` | `JSON`, `CSV` |
| `competitor_metric` | `GITHUB_STARS`, `GITHUB_OPEN_ISSUES`, `GITHUB_RELEASES_12M`, `HN_MENTIONS_90D` |

### 4.7. Сутності ERD (PostgreSQL 17)

`users`, `refresh_tokens`, `data_sources`, `research_projects`, `project_keywords`, `project_sources`,
`collection_runs`, `documents`, `project_documents`, `complaints`, `clustering_runs`, `need_clusters`,
`competitors`, `competitor_metrics`, `scoring_models`, `scoring_runs`, `niches`, `niche_scores`,
`score_components`, `score_evidence`, `niche_arguments`, `reports`, `audit_events`.

Первинні ключі — `UUID` (UUIDv7, генерується застосунком), крім `audit_events.id` (`BIGINT GENERATED ALWAYS AS IDENTITY`).
Час — `TIMESTAMPTZ` (UTC). Оцінки — `NUMERIC`. Сирі відповіді API — `JSONB`. Ембединги — `vector(384)`.

### 4.8. Алгоритми критичних вузлів

| ID | Назва | Сутності |
|---|---|---|
| ALG-01 | Ідемпотентний інкрементальний збір із backoff, лімітом повторів і Circuit Breaker | `collection_runs`, `documents`, `project_documents` |
| ALG-02 | Кластеризація скарг з обробкою порожніх і малих вибірок | `complaints`, `clustering_runs`, `need_clusters` |
| ALG-03 | Обчислення рейтингу ніші з bootstrap-оцінкою невизначеності | `niches`, `scoring_runs`, `niche_scores`, `score_components`, `score_evidence`, `niche_arguments` |

### 4.9. Модель оцінювання (scoring model v1.0.0)

| Критерій | Вага | Нормалізація |
|---|---|---|
| `DEMAND_VOLUME` — кількість унікальних скарг кластера за 180 діб | 0,30 | log1p + min-max у межах проєкту |
| `PAIN_INTENSITY` — медіана `pain_score` скарг | 0,25 | вже в [0; 1] |
| `GROWTH_TREND` — нахил лінійної регресії місячних згадок (6 міс.) | 0,20 | min-max, від'ємний нахил → 0 |
| `COMPETITION_GAP` — 1 − нормалізована насиченість конкурентами | 0,15 | min-max |
| `SOURCE_DIVERSITY` — ентропія Шеннона розподілу за джерелами / log(кількість джерел) | 0,10 | вже в [0; 1] |

Score = 100 × Σ(weight × normalized). Bootstrap: B = 500 перевибірок скарг, seed = 42,
95 % CI = [P2,5; P97,5]. Рівень невизначеності: ширина CI ≤ 10 → `LOW`; ≤ 25 → `MEDIUM`; > 25 або
кількість скарг < 30 → `HIGH`.

## 5. Джерела даних (перевірено веб-пошуком 25.11.2026)

| Код | API | Ліміт | Умови | Статус |
|---|---|---|---|---|
| `HACKER_NEWS` | HN Search API (Algolia), без ключа | 10 000 запитів/год на IP | Вміст належить авторам, публічний доступ через API | Увімкнено |
| `STACK_EXCHANGE` | Stack Exchange API v2.3, безкоштовний ключ StackApps | 10 000 запитів/добу з ключем (300 без ключа), ≤ 30 запитів/с | Вміст під CC BY-SA, обов'язкова атрибуція | Увімкнено |
| `GITHUB_ISSUES` | GitHub REST API, персональний токен | 5 000 запитів/год; окремий ліміт пошуку; вторинні ліміти | GitHub Terms of Service, API Terms | Увімкнено |
| `WIKIMEDIA_PAGEVIEWS` | Wikimedia Analytics API (pageviews) | Фіксованого ліміту немає; послідовні запити; обов'язковий User-Agent | Дані pageviews відкриті | Увімкнено |
| `REDDIT` | Reddit Data API | 100 запитів/хв на OAuth-клієнт (за даними третіх сторін) | Потрібне попереднє схвалення навіть для некомерційного використання | Вимкнено (D-09) |
