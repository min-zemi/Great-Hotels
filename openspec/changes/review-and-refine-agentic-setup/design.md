## Context

The project was an empty Python skeleton with only `.gitignore`, `README.md`, `pyproject.toml`, and `AGENTS.md`. No Django code existed. The goal was to transform this into a Django project with proper agentic configuration, so that future development follows consistent conventions and all tooling is pre-configured.

## Goals / Non-Goals

**Goals:**
- Bootstrap a Django 5.2 project with split settings (base/local/production)
- Update `AGENTS.md` to include Django commands, conventions, and testing expectations
- Configure `pyproject.toml` with project metadata, dependencies, and Django-aware pytest settings
- Create the standard Django directory structure (`apps/`, `templates/`, `static/`, `media/`)
- Set up uv with proper dev/optional dependency groups

**Non-Goals:**
- Creating any Django apps or models
- Writing application business logic
- Setting up production deployment infrastructure
- Configuring CI/CD pipelines

## Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Settings layout | Split `base.py` / `local.py` / `production.py` | Follows Django best practices (Two Scoops of Django pattern); keeps secrets out of version control via `local.py` gitignore |
| App directory | Top-level `apps/` directory | Keeps apps organized and separate from project config; avoids cluttering the root |
| Settings module config | `config.settings.local` for dev, `config.settings.production` for WSGI | Clear separation; `manage.py` uses local, production WSGI uses production |
| Dependency management | `uv` with `[project.optional-dependencies] dev` | uv is the project's chosen package manager; opt-in dev installs via `--extra dev` |
| Testing framework | pytest with pytest-django (pytest.ini_options in pyproject.toml) | Already had pytest; pytest-django provides Django integration; `--reuse-db` speeds up test runs |

## Risks / Trade-offs

- **Wildcard imports in settings** → `from .base import *` triggers Ruff F403. Mitigated with `# noqa: F403` inline suppression.
- **New Django version** → Django 5.2 may have breaking changes from older versions. Currently no issue since project is greenfield.
- **uv.lock in repo** → Lockfile checked in for reproducible builds, but may cause merge conflicts. Accepted trade-off.
