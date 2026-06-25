## Why

The project currently has a flat `model.py` at the root with all models (User, Hotel, Room, Reservation) outside the Django app structure. This violates the project convention of organizing code into apps under `apps/` and makes the schema difficult to maintain, extend, and test.

## What Changes

- Move `User` model into a new `apps/accounts/` app with Django's `AbstractUser` for built-in auth
- Move `Hotel` and `Room` models into a new `apps/hotels/` app
- Move `Reservation` model into a new `apps/reservations/` app
- Add `Room.price` (DecimalField) and `Hotel.description` (TextField) to support core booking flows
- Add unique constraint on `Reservation` (room + date) to prevent double-booking
- Add `Room.available` boolean field for soft vacancy management
- Register all models in admin and create initial migrations
- Remove the root `model.py` file

## Capabilities

### New Capabilities
- `accounts`: User registration, authentication, and profile management
- `hotels`: Hotel and Room catalog management
- `reservations`: Booking creation, cancellation, and availability checking

### Modified Capabilities
- None (no existing specs to modify)

## Impact

- Root `model.py` will be deleted; all data must migrate to new app models
- `INSTALLED_APPS` must include `apps.accounts`, `apps.hotels`, `apps.reservations`
- Settings will need `AUTH_USER_MODEL = "accounts.User"`
- Existing foreign key references in code will need updating
- Database migrations required for all three new apps
