## Summary

Розділ 1 повністю сформовано, вимоги зафіксовано (ЛР№4).

- `docs/1_analysis.md`: 1.1 актуальність, 1.2 огляд підходів, 1.4 As-Is (P1–P3, B1–B10), 1.5 To-Be, 8 Core Features, 22 NFR, постановка задачі, висновки до розділу.
- `docs/README.md`: NFR Matrix, розташування документа Розділу 1, статус етапів.
- `labs/lab-04/F2_Diploma_Chapter1_Кока.docx` — монолітний Розділ 1 (17 с.).

## Ключові архітектурні обмеження

- Target load: 200 RPS, p95 ≤ 200 ms / p99 ≤ 500 ms (read API), async operations 202 Accepted p95 ≤ 150 ms.
- Auth: OAuth 2.0-compatible JWT RS256 (access 15 min, refresh 7 days) + RBAC with object ownership checks; Argon2id.
- DB: PostgreSQL 17 with streaming replication and WAL archiving (RPO ≤ 15 min, RTO ≤ 30 min), pgvector.
- Ingestion: official APIs only, ≤ 80 % of quota, ≤ 5 retries with exponential backoff, Circuit Breaker per source.

Залежить від #2. Не зливати до рев'ю викладачем.
