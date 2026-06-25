## ADDED Requirements

### Requirement: Django project is scaffolded with split settings
The system SHALL have a Django project configured with a `config/` directory containing split settings (`base.py`, `local.py`, `production.py`).

#### Scenario: Settings module loads correctly
- **WHEN** `python manage.py check` is run
- **THEN** Django SHALL report "System check identified no issues"

#### Scenario: Local settings import from base
- **WHEN** `config.settings.local` is loaded
- **THEN** it SHALL inherit all settings from `config.settings.base` and override DEBUG to True

#### Scenario: Production settings are restricted
- **WHEN** `config.settings.production` is loaded
- **THEN** it SHALL inherit from `config.settings.base` and set DEBUG to False

### Requirement: Django management commands work
The system SHALL support standard Django management commands via `manage.py`.

#### Scenario: Runserver starts without error
- **WHEN** `python manage.py runserver` is started
- **THEN** the development server SHALL start on the default port

#### Scenario: Migrations can be created and applied
- **WHEN** `python manage.py makemigrations` and `python manage.py migrate` are run
- **THEN** Django SHALL apply migrations without errors

### Requirement: Project has standard Django directories
The project SHALL have `apps/`, `templates/`, `static/`, and `media/` directories at the repository root.

#### Scenario: Directories exist
- **WHEN** the repository is checked out
- **THEN** the `apps/`, `templates/`, `static/`, and `media/` directories SHALL exist
