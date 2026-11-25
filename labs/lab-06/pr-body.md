## Summary

Спроєктовано шар даних ERD у Mermaid, створено OpenAPI-контракт, зафіксовано логіку 3 критичних алгоритмів за правилами нормоконтролю, конфлікти інтеграції усунено (ЛР№6).

- `docs/2_design.md` 2.7: 27 таблиць (3NF), 11 ENUM, специфікація полів, 13 індексів (B-Tree, GIN, HNSW, BRIN).
- `docs/api/openapi.yaml`: OpenAPI 3.0.3, 17 операцій, JWT Bearer, спільна схема `Error`, 400/401/403/404/409/422/429/500/503.
- `docs/2_design.md` 2.7.5: ALG-01 (ідемпотентний збір), ALG-02 (кластеризація), ALG-03 (рейтинг з bootstrap) — текст і `graph TD`.
- `docs/2_design.md` 2.8: інтеграційний аудит (10 розбіжностей усунено), Production Readiness Report.
- `tools/check_consistency.py`: автоматична перевірка ENUM, полів API ↔ БД, ідентифікаторів.

Перевірки: Redocly — 0 errors / 0 warnings; Mermaid — 10/10 діаграм; consistency — 0 розбіжностей; Vale — 0 помилок.

Залежить від #4. Не зливати до показу викладачу.
