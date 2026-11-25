# Мета роботи

Деталізувати шар збереження даних, специфікувати міжсервісні контракти за підходом API-First,
алгоритмізувати критичні вузли за правилами нормоконтролю та провести інтеграційний аудит
узгодженості даних, API і логіки.

# Завдання 1. Модель даних

{{include ../../docs/2_design.md shift=0 section=2.7.1}}

{{include ../../docs/2_design.md shift=0 section=2.7.2}}

{{include ../../docs/2_design.md shift=0 section=2.7.3}}

{{include ../../docs/2_design.md shift=0 section=2.7.4}}

# Завдання 2. API-контракт

{{include ../../docs/2_design.md shift=0 section=2.5.1}}

Фрагмент контракту `docs/api/openapi.yaml` (схема безпеки і спільна схема помилки):

```yaml
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
  schemas:
    Error:
      type: object
      required: [code, message, trace_id]
      additionalProperties: false
      properties:
        code:
          type: string
          pattern: '^[A-Z][A-Z0-9_]{2,63}$'
        message:
          type: string
          maxLength: 500
        details:
          type: array
          maxItems: 50
          items:
            type: object
            required: [field, issue]
        trace_id:
          type: string
          pattern: '^[0-9a-f]{32}$'
```

# Завдання 3. Алгоритми критичних вузлів

{{include ../../docs/2_design.md shift=0 section=2.7.5}}

# Завдання 4. Інтеграційний аудит

{{include ../../docs/2_design.md shift=0 section=2.8}}

# AI Insights

{{include ai-insights.md shift=1 skip_h1}}

# Завдання 5. Docs-as-Code інтеграція

Контракт розміщено в `docs/api/openapi.yaml`; у `docs/2_design.md` додано підрозділи 2.5 (контракти),
2.7 (моделі даних і алгоритми) та 2.8 (інтеграційний аудит) з відносними посиланнями на `srs.md`,
`api/openapi.yaml` і ADR. `docs/README.md` оновлено: етап 3 — Done, етап 4 — In Progress. Відкрито
Pull Request у `main`.

# Висновки

Спроєктовано модель даних із 27 таблиць у третій нормальній формі з 11 ENUM-типами і 13 індексами,
REST-контракт OpenAPI 3.0.3 із 17 операцій, схемою безпеки JWT і спільною моделлю помилок, а також
три алгоритми критичних вузлів з обробкою граничних випадків. Інтеграційний аудит виявив і усунув 10
розбіжностей; специфікації готові до реалізації.
