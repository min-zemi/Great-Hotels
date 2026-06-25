## ADDED Requirements

### Requirement: Reservation model
The system SHALL have a `Reservation` model with ForeignKeys to `User` and `Room`, and a `date` DateField. A unique constraint SHALL be applied to the combination of `(room, date)` to prevent double-booking.

#### Scenario: Reservation can be created
- **WHEN** a user creates a Reservation for a Room on a specific date
- **THEN** the Reservation is saved and visible in the admin

#### Scenario: Double-booking is prevented
- **WHEN** a user attempts to create a second Reservation for the same Room on the same date
- **THEN** the system SHALL raise an IntegrityError or validation error

#### Scenario: Reservation string representation
- **WHEN** a Reservation object is printed
- **THEN** it SHALL return `"{user.username} - {date}"`

### Requirement: Reservation lives in apps/reservations
The `reservations` app SHALL be under `apps/reservations/` with `models.py`, `admin.py`, and `apps.py`.

#### Scenario: App is installed
- **WHEN** `INSTALLED_APPS` is inspected
- **THEN** it MUST include `apps.reservations`

### Requirement: Admin registration
The Reservation model SHALL be registered in the Django admin via `apps/reservations/admin.py`.

#### Scenario: Reservation appears in admin
- **WHEN** a superuser navigates to the admin site
- **THEN** the Reservation model SHALL appear under the Reservations section
