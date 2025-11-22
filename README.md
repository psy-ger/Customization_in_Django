# Кастомізація в Django — Опис проєкту

Цей приклад демонструє, як реалізувати й інтегрувати декілька користувацьких розширень у Django‑проєкті.

У проєкті реалізовано:

- Кастомні поля моделі: `UpperCaseCharField`, `PhoneNumberField`.
- Кастомна модель `CustomModel` з JSON‑полем і методом `stats()`; пов’язана модель `RelatedItem` (inline в адмінці).
- Кастомна модель користувача `User` з полем `phone_number` (налаштовано як `AUTH_USER_MODEL`).
- Форми з кастомними полями і валідаторами (HEX, телефон), реєстраційна форма.
- Кастомний віджет (select) з власним шаблоном.
- Налаштування адмінки: `list_display`, фільтри, пошук, дії та inlines.
- Шаблонні теги і фільтри, контекстний процесор для глобальних даних.
- Middleware, яке додає заголовок `X-Custom-App` і веде простий файловий лічильник запитів (`logs/request_count.txt`).
- Представлення на основі класів (ListView/DetailView/CreateView) та базові шаблони.
- REST API (DRF): серіалізатори з вкладеними полями, viewset з фільтрацією і кастомними правами доступу.
- Приклад запуску довільного SQL через `django.db.connection` (утиліта `core.utils.run_custom_sql`).
- Логування у файл `logs/django_custom.log`.

Структура проєкту (ключові файли):

- `core/models.py` — моделі та логіка.
- `core/fields.py` — кастомні поля моделей.
- `core/forms.py` і `core/validators.py` — форми та валідатори.
- `core/widgets.py` і `core/templates/core/widgets/` — кастомний віджет і шаблон.
- `core/admin.py` — конфігурація адмінки, inlines та дії.
- `core/middleware.py` — middleware із заголовком і лічильником запитів.
- `core/templatetags/custom_tags.py` і `core/context_processors.py` — теги, фільтри і контекст.
- `core/api.py`, `core/serializers.py`, `core/permissions.py` — DRF API.
- `core/signals.py` — сигнал `post_save` для `CustomModel`.
- `customization_in_django/settings.py` — налаштування проєкту (реєстрація `core`, `AUTH_USER_MODEL`, REST, логування).

Швидкий старт (локально)

1. Створіть і активуйте віртуальне середовище, потім встановіть залежності:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Виконайте міграції та створіть суперкористувача:

```bash
python manage.py migrate
python manage.py createsuperuser
```

3. Запустіть сервер розробки:

```bash
python manage.py runserver
```

Доступні URL

- Адмін: `http://127.0.0.1:8000/admin/`
- Головна сторінка: `http://127.0.0.1:8000/`
- API (приклад): `http://127.0.0.1:8000/api/custommodels/`
