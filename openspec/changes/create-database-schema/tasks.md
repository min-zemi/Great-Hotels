## 1. App Scaffolding

- [ ] 1.1 Create `apps/accounts/` with `__init__.py`, `models.py`, `admin.py`, `apps.py`, `migrations/__init__.py`
- [ ] 1.2 Create `apps/hotels/` with `__init__.py`, `models.py`, `admin.py`, `apps.py`, `migrations/__init__.py`
- [ ] 1.3 Create `apps/reservations/` with `__init__.py`, `models.py`, `admin.py`, `apps.py`, `migrations/__init__.py`

## 2. Settings Configuration

- [ ] 2.1 Add `apps.accounts`, `apps.hotels`, `apps.reservations` to `INSTALLED_APPS`
- [ ] 2.2 Set `AUTH_USER_MODEL = "accounts.User"` in settings

## 3. Models Implementation

- [ ] 3.1 Implement `accounts/models.py` with `User` extending `AbstractUser`
- [ ] 3.2 Implement `hotels/models.py` with `Hotel` (name, city, description) and `Room` (hotel FK, room_type, price, available)
- [ ] 3.3 Implement `reservations/models.py` with `Reservation` (user FK, room FK, date) and `UniqueConstraint` on (room, date)

## 4. Admin Registration

- [ ] 4.1 Register `User` in `apps/accounts/admin.py`
- [ ] 4.2 Register `Hotel` and `Room` in `apps/hotels/admin.py`
- [ ] 4.3 Register `Reservation` in `apps/reservations/admin.py`

## 5. Migrations and Cleanup

- [ ] 5.1 Run `makemigrations` for all three apps
- [ ] 5.2 Run `migrate` to apply new schema
- [ ] 5.3 Delete root `model.py`
- [ ] 5.4 Verify admin shows all models correctly
