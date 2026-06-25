## Why

The project was an empty Python skeleton with no Django code, no web framework, and no Django-specific agent instructions. To begin building a hotel web application, the project needs Django bootstrapped, the agentic configuration (AGENTS.md) updated for Django development, and proper tooling/CI configurations in place.

## What Changes

- Rewrote `AGENTS.md` with Django scope, Django commands, app/settings conventions, and testing expectations
- Updated `pyproject.toml` with `[project]` metadata, Django dependencies, and pytest-django configuration
- Scaffolded Django project with split settings (`base.py`, `local.py`, `production.py`)
- Created `apps/` top-level app directory, `templates/`, `static/`, `media/` directories
- Updated `README.md` with Django setup instructions
- Installed Django 5.2 and dev dependencies via uv

## Capabilities

### New Capabilities

- `django-setup`: Django project scaffolded with manage.py, settings, urls, wsgi/asgi
- `agentic-config`: AGENTS.md configured with Django-specific agent instructions, commands, and conventions
- `tooling-config`: pyproject.toml configured with project metadata, Django deps, Black/Ruff/pytest-django settings

### Modified Capabilities

None — this is the initial project setup.

## Impact

- Project now depends on Django 5.2+ (added to pyproject.toml dependencies)
- New `/apps/` directory for all Django apps
- New `/config/` directory for Django project configuration
- New uv.lock lockfile for reproducible installs
- AGENTS.md now serves as the authoritative agent setup document
