# AI Insights (AI Disclosure) — ЛР№6

Інструмент: Claude Code (модель Claude Opus 5.5), сесія від 25.11.2026. Інструментальні перевірки:
`mmdc` (компіляція Mermaid), Redocly CLI (OpenAPI), `tools/check_consistency.py` (узгодженість),
Vale (стиль). Перша версія моделі даних — [drafts/erd-v1.md](drafts/erd-v1.md).

## Сесія 1. Аудит моделі даних (Data Layer Reviewer)

### Промпт

```text
Роль: Principal Database Architect, Lead Data Engineer та суворий технічний аудитор шарів збереження
даних в Enterprise-системах.
Обрана СУБД: PostgreSQL 17 + pgvector 0.8.
Мій код схеми в Mermaid.js: [drafts/erd-v1.md]
Завдання: 1) 3NF, надлишковість, аномалії; 2) цілісність зв'язків, FK; 3) типи даних та індекси
(B-Tree, Hash, GIN, HNSW/IVF); 4) Gap Analysis: created_at, updated_at, deleted_at, версіонування,
аудит. Наприкінці — опис кожної сутності. Стиль: сухий контрактний.
```

### Звіт аудитора і виправлення

| № | Знахідка у v1 | Категорія | Виправлення у фінальній моделі |
|---|---|---|---|
| 1 | `research_projects.keywords text_array` і `need_clusters.top_terms text_array` — неатомарні значення | 1NF | Таблиці `project_keywords`, `cluster_terms` |
| 2 | `complaints.cluster_id` прив'язує скаргу до одного запуску кластеризації; повторна кластеризація перезаписує історію (аномалія оновлення) | 3NF / історичність | Таблиця `cluster_memberships (clustering_run_id, complaint_id, cluster_id)` |
| 3 | `competitors.project_id` транзитивно визначається через `niche_id` | 3NF | `project_id` вилучено; належність — через `niches.project_id` |
| 4 | `competitors.github_stars` змішує сутність і часовий ряд | 3NF / часові дані | Таблиця `competitor_metrics` з `captured_at` і ENUM `competitor_metric` |
| 5 | `score_components.weight` дублює вагу моделі, `contribution` обчислюється з `weight × normalized` | 3NF (похідні дані) | Ваги — `scoring_model_weights`; внесок — представлення `v_score_contributions` |
| 6 | `scoring_models.weights jsonb` не гарантує повноти і діапазону ваг | Цілісність | Таблиця `scoring_model_weights` з `PK (model, criterion)` і `CHECK 0..1` |
| 7 | `float` для оцінок і `pain_score` — похибка двійкового подання | Типи | `numeric(5,2)`, `numeric(4,3)` |
| 8 | `timestamp` без часового поясу | Типи | `timestamptz` (UTC) |
| 9 | Статуси і ролі як `varchar` без обмеження значень | Типи | 11 ENUM-типів (2.7.2) |
| 10 | `documents.source varchar` — немає FK до довідника джерел | Цілісність | `source_id → data_sources` |
| 11 | `documents.author` зберігає ідентифікатор автора у відкритому вигляді | Комплаєнс (GDPR) | `author_hash char(64)` (HMAC-SHA-256) |
| 12 | Немає захисту від дублікатів документів і запусків | Цілісність | `UNIQUE (source_id, external_id)`, `UNIQUE content_hash`, `UNIQUE (project_id, idempotency_key)` |
| 13 | Курсор збору на рівні запуску не дозволяє продовжити збір окремого джерела | Логіка | Таблиця `collection_run_sources` з курсором і статусом на джерело |
| 14 | Відсутні `updated_at`, `deleted_at`, `version`, журнал аудиту, токени | Gap | Технічні поля (ознака «Т» у специфікації), `audit_events` (append-only, секціонування), `refresh_tokens` |
| 15 | Відсутній план індексів, зокрема для векторного пошуку | Продуктивність | 13 індексів: B-Tree, частковий, GIN (FTS, JSONB), HNSW (`vector_cosine_ops`), BRIN |

Підсумок: 11 → 27 таблиць, 3NF, 11 ENUM. Компіляція трьох ERD-діаграм `mmdc` — без помилок.

## Сесія 2. Аудит API-контракту (API Reviewer)

### Промпт

```text
Роль: Principal API Architect, Lead Integration Engineer та експерт із суворого аудиту інтерфейсів
(OpenAPI / gRPC Best Practices).
Обраний інструмент контракту: OpenAPI v3 (YAML).
Мій код контракту: [перша повна версія docs/api/openapi.yaml]
Завдання: 1) синтаксис і структура; 2) RESTful Best Practices (методи, статус-коди, множина
іменників); 3) обробка помилок і Edge Cases (400, 401, 429 тощо); 4) securitySchemes для JWT Bearer.
```

### Звіт аудитора і виправлення

| № | Знахідка | Джерело | Виправлення |
|---|---|---|---|
| 1 | `Argument.criterion`: `allOf` + `nullable` без `type` | Redocly, error `nullable-type-sibling` | `type: string`, `nullable: true`, `enum` з `null` |
| 2 | 8 тегів без опису | Redocly, warning `tag-description` | Додано описи тегів |
| 3 | Схема `UserRole` не використовується | Redocly, warning `no-unused-components` | Додано об'єкт `user` з `role` у `TokenPair` |
| 4 | Сервер `https://localhost` | Redocly, warning `no-server-example.com` | `https://demandlens.test/api/v1` (зарезервований тестовий домен) |
| 5 | Шаблон `\p{L}` потребує Unicode-прапорця і не підтримується частиною генераторів стабів | Рев'ю | Шаблон без Unicode-класів |
| 6 | Тривалі операції мають повертати 202 і підтримувати повтор без дублікатів | Рев'ю (підтверджено) | 202 + `Location`, `Idempotency-Key` (обов'язковий), 200 для повтору, 409 для іншого тіла |
| 7 | Невласник ресурсу має отримувати 404, а не 403 (BOLA) | Рев'ю (підтверджено) | Відповідь `NotFound` з описом захисту від BOLA/IDOR |
| 8 | Тіла запитів мають забороняти невідомі поля | Рев'ю (підтверджено) | `additionalProperties: false` для всіх `*Create`, `*Patch`, `TokenRequest` |

Фінальний результат: Redocly `recommended` — 0 помилок, 0 попереджень; 17 операцій.

## Сесія 3. Нормоконтроль алгоритмів (Algorithm & Flowchart Auditor)

### Промпт

```text
Роль: Професійний нормоконтролер навчальних документів зі спеціальності «Інженерія ПЗ», Senior
Software Engineer та суворий математичний лінтер алгоритмів.
Ось мої алгоритми: ALG-01 (ідемпотентний збір), ALG-02 (кластеризація скарг), ALG-03 (рейтинг з
bootstrap).
Завдання: 1) := замість =, AND/OR/NOT, індекси Array[i]; 2) нескінченні цикли, тайм-аути, ліміти
спроб, порожні дані, помилки сторонніх сервісів; 3) інструкція для блок-схем (термінатор, процес,
рішення, ввід/вивід); фінальний опис алгоритмів.
```

### Звіт нормоконтролера і виправлення

| № | Знахідка | Виправлення |
|---|---|---|
| 1 | Іменовані параметри викликів записано через `=` (`ngram = (1; 2)`, `min_cluster_size = MinCluster` тощо, 10 випадків) — порушення правила «`=` лише для порівняння» | Форма `параметр: значення`, розділювач аргументів `;` |
| 2 | Автоматична перевірка: 9 виразів зі знаком `=` — усі в умовах (`N = 0`, `Cursor = NULL`); малих `and`/`or`/`not` — 0; `AND`/`OR`/`NOT` — 24 входження | Відповідає правилам |
| 3 | ALG-02 використовує `Probabilities[i]` без визначення | Додано `Probabilities := HDBSCAN.probabilities` |
| 4 | ALG-03 використовує `SATURATION` і `relevance` без формул | Додано формули `SATURATION[j]` і `Relevance[i]` |
| 5 | ALG-03: ділення на нуль при `Max[k] = Min[k]` | `Norm[j][k] := 0.5` для всіх ніш |
| 6 | ALG-01: очікування backoff може перевищити soft time limit задачі Celery | Перевірка `NOW() − T0 + Delay > TimeBudget` і перепланування задачі зі збереженим курсором |
| 7 | ALG-02: при K = 0 цикл зменшення `MinCluster` міг би повторюватися без межі | Ліміт `MaxAttempts := 2` |
| 8 | Блок-схеми: форми блоків | Термінатор `([…])`, процес `[…]`, рішення `{…}`, ввід/вивід `[/…/]`; 3 схеми компілюються |

## Сесія 4. Інтеграційний аудит (Data & Logic Gatekeeper)

### Промпт

```text
Роль: Principal Systems Architect, Lead Data Engineer та голова комісії з технічного аудиту програмних
систем Enterprise-рівня.
Артефакти: [ERD Mermaid], [openapi.yaml], [ALG-01…03].
Завдання: 1) API-to-Database Mismatch (типи UUID/INT, string-дата/TIMESTAMP); 2) Logic-to-API/Data
Mismatch; 3) Production Readiness: готовність до Розділу 3, Showstoppers.
```

### Інструментальна частина

`tools/check_consistency.py`: 11 ENUM ідентичні в трьох джерелах; 106 полів 14 схем OpenAPI
зіставлено з колонками 27 таблиць (23 похідні поля задокументовано); статуси алгоритмів належать ENUM;
17 операцій мають дійсні `SRS-FUN` і `API-REQ`. Мутаційний тест (підміна значення `run_status` в
OpenAPI) — скрипт виявив розбіжність, отже перевірка працездатна.

### Розбіжності, виявлені експертним аудитом, і усунення

| № | Розбіжність | Усунення |
|---|---|---|
| 1 | `attempt_count CHECK 0..5` (БД) і `maximum: 5` (API) суперечать ALG-01, де лічильник зростає при кожному виконанні і перепланувань | Лічильник без верхньої межі; ліміт 5 — для повторів однієї сторінки |
| 2 | Bootstrap-інтервал може не містити точкову оцінку — порушення `CHECK ci_low <= score <= ci_high` | Обмеження інтервалу точковою оцінкою в ALG-03 |
| 3 | 409 для того самого ключа з іншим тілом неможливо визначити без збереження ознаки тіла | `request_hash char(64)` у `collection_runs`, `scoring_runs` |
| 4 | TTL ключа 24 год (SRS, API) проти безстрокового `UNIQUE` у БД | Ключ неповторюваний у межах проєкту без обмеження часу (SRS-FUN-06, OpenAPI) |
| 5 | `description` у API ≤ 2 000 символів, у БД без обмеження | `CHECK (length(description) <= 2000)` |

Висновок аудитора (Production Readiness Report, підрозділ 2.8.3): після усунення 10 розбіжностей
критичних блокерів немає; специфікації готові до реалізації.
