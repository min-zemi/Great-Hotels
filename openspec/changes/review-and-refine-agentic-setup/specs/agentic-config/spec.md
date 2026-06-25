## ADDED Requirements

### Requirement: AGENTS.md covers Django development scope
The `AGENTS.md` file SHALL document the project as a Django-based web application and include Django-specific instructions.

#### Scenario: Django is referenced in project scope
- **WHEN** AGENTS.md is read
- **THEN** the Project Scope section SHALL mention "Django" and "hotel web application"

### Requirement: AGENTS.md includes Django management commands
The `AGENTS.md` file SHALL list Django management commands (runserver, makemigrations, migrate, shell, createsuperuser, startapp).

#### Scenario: Django commands are present
- **WHEN** the Commands section of AGENTS.md is read
- **THEN** it SHALL include entries for `runserver`, `makemigrations`, `migrate`, `shell`, `createsuperuser`, and `startapp`

### Requirement: AGENTS.md defines Django conventions
The `AGENTS.md` file SHALL specify Django project conventions including app location, settings layout, view style, and ORM usage.

#### Scenario: Conventions are documented
- **WHEN** AGENTS.md is read
- **THEN** it SHALL contain a Django Conventions section with entries for apps directory, config directory, view style (CBVs), and business logic placement

### Requirement: AGENTS.md includes dependency management instructions
The `AGENTS.md` file SHALL document how to install dependencies using `uv add` and `uv add --dev`.

#### Scenario: Dependency commands documented
- **WHEN** AGENTS.md is read
- **THEN** it SHALL include the `uv add` and `uv add --dev` commands in the Dependency Management section

### Requirement: AGENTS.md defines testing expectations
The `AGENTS.md` file SHALL specify testing requirements including Django TestCase, coverage targets, and factory_boy usage.

#### Scenario: Testing expectations documented
- **WHEN** AGENTS.md is read
- **THEN** the Testing Expectations section SHALL mention Django's TestCase, 80% coverage target, and factory_boy
