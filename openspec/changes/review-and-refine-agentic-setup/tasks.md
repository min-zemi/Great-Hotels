## 1. Agentic Configuration

- [ ] 1.1 Rewrite AGENTS.md with Django project scope, tools, commands, conventions, and testing expectations
- [ ] 1.2 Update README.md with Django setup instructions

## 2. Tooling & Dependency Configuration

- [ ] 2.1 Add `[project]` section to pyproject.toml with name, version, Python constraint, and Django dependency
- [ ] 2.2 Add `[project.optional-dependencies] dev` section with Black, Ruff, pytest, pytest-cov, pytest-django, factory-boy
- [ ] 2.3 Add pytest ini_options with `DJANGO_SETTINGS_MODULE` and `--reuse-db`
- [ ] 2.4 Set Black `target-version = ["py313"]`
- [ ] 2.5 Install all dependencies and verify via `uv sync --extra dev`

## 3. Django Project Scaffold

- [ ] 3.1 Create `config/settings/base.py` with common settings
- [ ] 3.2 Create `config/settings/local.py` with DEBUG=True
- [ ] 3.3 Create `config/settings/production.py` with DEBUG=False
- [ ] 3.4 Remove old flat `config/settings.py`
- [ ] 3.5 Update `manage.py` to point to `config.settings.local`
- [ ] 3.6 Update `config/wsgi.py` and `config/asgi.py` to point to `config.settings.production`
- [ ] 3.7 Create `apps/__init__.py`, `templates/`, `static/`, `media/` directories
- [ ] 3.8 Clean up auto-generated docstrings in `config/urls.py`
- [ ] 3.9 Verify with `python manage.py check`, `black --check .`, `ruff check .`, and `pytest`
