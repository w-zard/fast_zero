# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Uses `uv` for dependency management and `taskipy` as a task runner.

```bash
uv sync --group dev          # Install all dependencies
uv run task run              # Start dev server (fastapi dev)
uv run task test             # Run tests with coverage
uv run task lint             # Check code with ruff
uv run task format           # Fix and format code with ruff
```

Run a single test file or test:
```bash
uv run pytest tests/test_app.py
uv run pytest tests/test_app.py::test_create_user
```

Database migrations (Alembic):
```bash
uv run alembic upgrade head                       # Apply migrations
uv run alembic revision --autogenerate -m "msg"   # Generate migration
uv run alembic downgrade -1                       # Roll back one migration
```

## Architecture

**Stack**: FastAPI + SQLAlchemy 2.0 + Alembic + Pydantic v2 + pydantic-settings

**Package layout** (`fast_zero/`):
- `app.py` — FastAPI app instance and all route definitions
- `models.py` — SQLAlchemy ORM models using the declarative `table_registry`
- `schemas.py` — Pydantic schemas for request validation and response serialization
- `database.py` — Engine creation and `get_session()` FastAPI dependency
- `settings.py` — App config loaded from `.env` via pydantic-settings (`DATABASE_URL` required)

**Current state**: The API routes in `app.py` use an in-memory list (`database = []`) rather than the SQLAlchemy session. The database layer (models, migrations, session) is fully defined but not yet wired into the routes.

**Testing**: Tests use `TestClient` (via `httpx`) for route tests and an in-memory SQLite session fixture for ORM tests. Fixtures are in `tests/conftest.py`.

## Code Style

- Line length: 79 characters
- Quote style: single quotes
- Ruff rules enforced: imports (I), pyflakes (F), pycodestyle (E/W), pylint (PL), pytest (PT)
- Migrations directory is excluded from linting
- `task lint` runs automatically before `task test`
