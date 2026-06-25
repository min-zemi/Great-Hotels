## ADDED Requirements

### Requirement: User model uses AbstractUser
The system SHALL use Django's `AbstractUser` for the User model, providing built-in authentication fields (username, password, email, first_name, last_name), password hashing, and permission groups.

#### Scenario: User can be created via admin
- **WHEN** a superuser creates a new user in the Django admin interface
- **THEN** the user is saved with a hashed password and can log in

#### Scenario: Password is stored hashed
- **WHEN** a user registers with a password
- **THEN** the password field SHALL contain a hashed value, not plain text

### Requirement: User model lives in apps/accounts
The `accounts` app SHALL be a proper Django app under `apps/accounts/` with `models.py`, `admin.py`, and `apps.py`.

#### Scenario: App is installed
- **WHEN** `INSTALLED_APPS` is inspected
- **THEN** it MUST include `apps.accounts`

#### Scenario: AUTH_USER_MODEL is set
- **WHEN** Django settings are loaded
- **THEN** `AUTH_USER_MODEL` SHALL equal `"accounts.User"`

### Requirement: Admin registration for User
The User model SHALL be registered in the Django admin via `apps/accounts/admin.py`.

#### Scenario: User appears in admin
- **WHEN** a superuser navigates to the admin site
- **THEN** the User model SHALL appear under the Accounts section
