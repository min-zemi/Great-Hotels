# Great Hotels

## Project Overview
Django-based hotel web application for learning Django, Git, Python tooling, and AI coding agents.

## Environment
- Python 3.13
- uv virtual environment

## Tools
- Django
- Black (formatting)
- Ruff (linting)
- Pytest + pytest-django (testing)
- Pytest-Cov (coverage)

## Setup

```bash
uv venv
source .venv/bin/activate
uv sync
python manage.py migrate
python manage.py runserver
```

## Available URLs

| URL | View | Arguments | Return Value | Description |
|------|------|-----------|--------------|-------------|
| `/` | `home` | None | HttpResponse | Displays the hotel booking home page. |
| `/hotels/` | `hotel_list` | None | HttpResponse | Displays a list of matching hotels. |
| `/register/` | `register` | None | HttpResponse | Displays the user registration page. |
| `/reserve/` | `reserve` | None | HttpResponse | Processes a reservation request (currently a placeholder). |
| `/success/` | `success` | None | HttpResponse | Displays the reservation success page. |

## Notes
The current implementation provides basic Django view functions connected to URLs.
Database access and reservation logic will be implemented in later exercises.