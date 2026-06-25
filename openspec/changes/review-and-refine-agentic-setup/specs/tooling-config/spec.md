## ADDED Requirements

### Requirement: pyproject.toml has project metadata
The `pyproject.toml` file SHALL contain a `[project]` section with name, version, description, Python version constraint, and Django dependency.

#### Scenario: Project metadata exists
- **WHEN** pyproject.toml is read
- **THEN** it SHALL have a `[project]` section with `name = "great-hotels"`, `version`, `description`, `requires-python = ">=3.13"`, and `dependencies` including `django`

### Requirement: Dev dependencies are configured
The `pyproject.toml` file SHALL configure optional dev dependencies (black, ruff, pytest, pytest-cov, pytest-django, factory-boy) under `[project.optional-dependencies] dev`.

#### Scenario: Dev dependencies install
- **WHEN** `uv sync --extra dev` is run
- **THEN** Black, Ruff, pytest, pytest-cov, pytest-django, and factory-boy SHALL be installed in the virtual environment

### Requirement: pytest-django is configured
The `pyproject.toml` file SHALL configure pytest with `DJANGO_SETTINGS_MODULE` pointing to `config.settings.local` and `--reuse-db` flag.

#### Scenario: Pytest loads Django settings
- **WHEN** `pytest` is run
- **THEN** pytest SHALL report `django: settings: config.settings.local (from ini)` in its output

### Requirement: Black and Ruff are configured
The `pyproject.toml` file SHALL configure Black with 88-character line length and Python 3.13 target, and Ruff with 88-character line length.

#### Scenario: Black formatting passes
- **WHEN** `black --check .` is run
- **THEN** all Python files SHALL pass Black's formatting check

#### Scenario: Ruff linting passes
- **WHEN** `ruff check .` is run
- **THEN** all Python files SHALL pass Ruff's lint check with no errors
