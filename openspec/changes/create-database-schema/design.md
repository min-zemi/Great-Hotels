## Context

The codebase currently defines all models (User, Hotel, Room, Reservation) in a root-level `model.py`, outside any Django app. There are no `apps/<name>/` apps created yet, and the `apps/` directory only contains `__init__.py`. The project convention (per AGENTS.md) requires apps to live under `apps/` and business logic in models or service modules.

## Goals / Non-Goals

**Goals:**
- Migrate all models from `model.py` into proper Django apps under `apps/`
- Use Django's `AbstractUser` for the User model to leverage built-in auth
- Add `Room.price` (DecimalField), `Hotel.description` (TextField), `Room.available` (BooleanField)
- Add unique constraint on `Reservation` for `(room, date)` to prevent double-booking
- Register all models in Django admin
- Write and apply migrations for all new apps
- Update `settings.py` with `AUTH_USER_MODEL` and new `INSTALLED_APPS`

**Non-Goals:**
- No views, templates, or URL routing (pure schema layer)
- No API endpoints
- No user-facing functionality beyond admin

## Decisions

1. **Django `AbstractUser` over custom `User` model** — Using `AbstractUser` gives us built-in authentication (login, password hashing, permissions) for free. The current `User` model stores plain passwords, which is insecure.
2. **Three separate apps (accounts, hotels, reservations)** — Separating concerns aligns with Django best practices and makes each domain independently testable and maintainable.
3. **`UniqueConstraint` on Reservation (room + date)** — Prevents double-booking at the database level rather than relying on application logic alone.
4. **DecimalField for `Room.price`** — Precise decimal arithmetic for currency values; avoids floating-point rounding issues.
5. **BooleanField `Room.available`** — Simple soft availability toggle for hotel staff, independent of reservation logic.

## Risks / Trade-offs

- **Migration from root model.py** — Existing data in SQLite will need migration. New `makemigrations` will create initial migrations; existing data in root `model.py`'s table won't carry over automatically. The old `model.py` must be removed after migrations.
- **AUTH_USER_MODEL change** — Must be set before any migrations are created. Django requires `AUTH_USER_MODEL` to be set on the first migration. Since no prior migrations exist in this project, this is safe.
- **ForeignKey references** — Any existing code referencing the old model paths will need updating.
