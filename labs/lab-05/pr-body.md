## Summary

SRS за ISO 29148 додано, спроєктовано 3 рівні C4 Model у Mermaid, зафіксовано архітектурний компроміс в ADR-001 (ЛР№5).

- `docs/srs.md`: System Context, 25 атомарних FR (`SRS-FUN-01…25`), 23 NFR, Verification Criteria (pytest, k6, SonarQube, Trivy, Postman, Prometheus), Glossary, матриця трасування.
- `docs/2_design.md`: C4 L1, L2 (два представлення), L3 Core API з шарами Inbound/Core/Outbound; трасування на `srs.md` і ADR.
- `docs/adr/0001-choice-of-technology.md`: Celery + Redis проти Kafka і RabbitMQ, статус Approved.
- `docs/README.md`: навігація на SRS і ADR, етап 2 — Done, етап 3 — In Progress.

Перевірки: `tools/check_mermaid.py` — 4/4 діаграми компілюються; Vale — 0 помилок.

Залежить від #3. Не зливати до рев'ю викладачем.
