# Мета роботи

Перетворити архітектурні специфікації на зв'язне текстове обґрунтування, змоделювати поведінку
системи діаграмою прецедентів і транзакційними специфікаціями, задокументувати топологію API та
контур безпеки, автоматизувати контроль якості документації в CI/CD і консолідувати Розділи 1–2.

# Завдання 1. Обґрунтування архітектурного стилю і патернів

{{include ../../docs/2_design.md shift=0 section=2.1}}

# Завдання 2. Use Case діаграма і специфікації

{{include ../../docs/2_design.md shift=0 section=2.6}}

# Завдання 3. Топологія API і потоки даних

{{include ../../docs/2_design.md shift=0 section=2.5.2}}

{{include ../../docs/2_design.md shift=0 section=2.5.3}}

# Завдання 4. Серверне ядро і Application Security

{{include ../../docs/2_design.md shift=0 section=2.3.1}}

{{include ../../docs/2_design.md shift=0 section=2.4}}

# Завдання 5. Консолідація і Docs Quality Gate

Зібрано документ `F2_Diploma_Chapters1-2_Кока.docx` з `docs/1_analysis.md` і `docs/2_design.md` у
структурі 2.1–2.8 і висновків до розділу. Створено `.markdownlint.json` і
`.github/workflows/docs-linter.yml` з трьома перевірками (markdownlint, Vale, Redocly), що
запускаються для кожного Pull Request у `main`.

# AI Insights

{{include ai-insights.md shift=1 skip_h1}}

# Висновки

Сформовано обґрунтування архітектури з кількісними аргументами, діаграму прецедентів у StarUML і три
транзакційні специфікації з альтернативними і винятковими потоками, топологію 17 маршрутів API з
потоками даних і контур AppSec за OWASP. Розділи 1–2 консолідовано в одному документі, якість
документації контролюється автоматичним конвеєром у GitHub Actions.
