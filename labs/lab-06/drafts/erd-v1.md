# Перша версія моделі даних (до аудиту)

Чернетка сформована на етапі «рамки» (DECISIONS.md, редакція до ЛР№6) і зафіксована для протоколу
AI Insights. Фінальна версія — `docs/2_design.md`, підрозділ 2.7.

```mermaid
erDiagram
    users ||--o{ research_projects : owns
    research_projects ||--o{ collection_runs : has
    research_projects ||--o{ complaints : has
    research_projects ||--o{ competitors : has
    research_projects ||--o{ niches : has
    documents ||--o{ complaints : contains
    need_clusters ||--o{ complaints : groups
    need_clusters ||--|| niches : becomes
    niches ||--o{ niche_scores : scored
    niche_scores ||--o{ score_components : explains
    users {
        uuid id PK
        varchar email
        varchar password_hash
        varchar role
        timestamp created_at
    }
    research_projects {
        uuid id PK
        uuid owner_id FK
        varchar title
        text_array keywords
        varchar status
    }
    collection_runs {
        uuid id PK
        uuid project_id FK
        varchar status
        varchar idempotency_key
        jsonb cursor
    }
    documents {
        uuid id PK
        varchar source
        text url
        text body
        varchar author
        timestamp published_at
    }
    complaints {
        uuid id PK
        uuid document_id FK
        uuid project_id FK
        uuid cluster_id FK
        text text
        float pain_score
    }
    need_clusters {
        uuid id PK
        uuid project_id FK
        varchar label
        text_array top_terms
    }
    niches {
        uuid id PK
        uuid project_id FK
        uuid cluster_id FK
        varchar name
    }
    competitors {
        uuid id PK
        uuid project_id FK
        uuid niche_id FK
        varchar name
        int github_stars
    }
    scoring_models {
        uuid id PK
        varchar version
        jsonb weights
    }
    niche_scores {
        uuid id PK
        uuid niche_id FK
        float score
        float ci_low
        float ci_high
        varchar uncertainty
    }
    score_components {
        uuid id PK
        uuid niche_score_id FK
        varchar criterion
        float normalized
        float weight
        float contribution
    }
```
