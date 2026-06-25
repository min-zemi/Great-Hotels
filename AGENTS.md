# AGENTS.md

## Project Scope

Django-based hotel web application for learning Django, Git, Python tooling, and AI coding agents.

## Development Environment

* Python 3.13
* uv virtual environment

## Tools

* Black (formatting)
* Ruff (linting)
* Pytest + pytest-django (testing)
* Pytest-Cov (coverage)
* Django
* OpenCode

## Dependency Management

* Install: `uv add <package>`
* Install dev: `uv add --dev <package>`
* Sync: `uv sync`

## Commands

* Run tests: `pytest`
* Format code: `black .`
* Lint code: `ruff check .`
* Start dev server: `python manage.py runserver`
* Create migrations: `python manage.py makemigrations`
* Apply migrations: `python manage.py migrate`
* Shell: `python manage.py shell`
* Create superuser: `python manage.py createsuperuser`
* New app: `python manage.py startapp <name>`

## Django Conventions

* Apps live under a top-level `apps/` directory (e.g. `apps/hotels/`).
* Project config lives in a `config/` directory (`settings.py`, `urls.py`, `wsgi.py`).
* Use class-based views unless a simple function view is clearer.
* Business logic goes in models or service modules, **not** in views.
* Use Django's built-in auth (AbstractUser) for user management.
* Define URL namespaces per app.
* Keep settings split into `base.py`, `local.py`, `production.py` (use `django-split-settings` or manual import chain).
* Templates go in `templates/<app_name>/`.
* Static files go in `static/<app_name>/`.

## Constraints

* Keep changes small and focused.
* Follow Django and Python best practices.
* Update documentation when project structure changes.
* Write migrations for every model change.
* Never commit secrets or `local_settings.py`.

## Testing Expectations

* Add or update tests when new functionality is introduced.
* Use Django's `TestCase` or `pytest-django` fixtures.
* Test models, views, forms, URLs, and API endpoints.
* Aim for at least 80% coverage on new code.
* Use `factory_boy` for test data factories when models become complex.
