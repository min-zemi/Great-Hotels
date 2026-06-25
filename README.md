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