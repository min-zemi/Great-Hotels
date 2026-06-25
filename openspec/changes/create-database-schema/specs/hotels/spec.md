## ADDED Requirements

### Requirement: Hotel model
The system SHALL have a `Hotel` model with fields: `name` (CharField), `city` (CharField), `description` (TextField, optional).

#### Scenario: Hotel can be created
- **WHEN** a staff user creates a new Hotel with name, city, and description
- **THEN** the Hotel is saved and visible in the admin

#### Scenario: Hotel string representation
- **WHEN** a Hotel object is printed
- **THEN** it SHALL return the hotel name

### Requirement: Room model
The system SHALL have a `Room` model with a ForeignKey to `Hotel`, and fields: `room_type` (CharField with choices: standard, double, deluxe), `price` (DecimalField with max_digits=10, decimal_places=2), `available` (BooleanField, default=True).

#### Scenario: Room can be created
- **WHEN** a staff user creates a Room linked to an existing Hotel
- **THEN** the Room is saved with all fields and visible in the admin

#### Scenario: Room string representation
- **WHEN** a Room object is printed
- **THEN** it SHALL return `"{hotel.name} - {room_type}"`

### Requirement: Hotel and Room live in apps/hotels
The `hotels` app SHALL be under `apps/hotels/` with `models.py`, `admin.py`, and `apps.py`.

#### Scenario: App is installed
- **WHEN** `INSTALLED_APPS` is inspected
- **THEN** it MUST include `apps.hotels`

### Requirement: Admin registration
Both Hotel and Room models SHALL be registered in the Django admin via `apps/hotels/admin.py`.

#### Scenario: Hotel appears in admin
- **WHEN** a superuser navigates to the admin site
- **THEN** the Hotel model SHALL appear under the Hotels section

#### Scenario: Room appears in admin
- **WHEN** a superuser navigates to the admin site
- **THEN** the Room model SHALL appear under the Hotels section
