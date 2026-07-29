# Great Hotels

## Overview

Great Hotels is a hotel booking web application developed with Django.

Users can search for hotels by selecting a city, room type, and check-in date. Search results are updated dynamically using HTMX without reloading the page.

This project was created for the Web Engineering course.

---

## Features

- Home page
- Hotel search
- Search by city
- Search by room type
- Check-in date selection
- Dynamic search results using HTMX
- Hotel list page
- Reservation page

(Not yet implemented)
- Registration page (UI)
- Booking success page
- Responsive design

---

## Technologies

- Python
- Django
- HTMX
- HTML
- CSS
- Gunicorn
- WhiteNoise

---

## Project Structure

```
config/
apps/
hotels/
templates/
static/
manage.py
```

---

## How to Run

1. Clone the repository.

```bash
git clone <repository-url>
cd Great-Hotels
```

2. Install dependencies.

```bash
uv sync
```

3. Run the development server.

```bash
uv run python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## Production Test

Run Gunicorn:

```bash
DJANGO_SETTINGS_MODULE=config.settings.local \
uv run gunicorn config.wsgi:application
```

---

## Future Improvements

- User authentication
- Real database for hotels
- Booking storage
- Payment system