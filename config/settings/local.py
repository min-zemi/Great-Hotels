from .base import *


SECRET_KEY = (
    "django-insecure-65_y&i4xdc@i-c+4t)"
    "cw86&^b+j9=*qdxv!*1a(v_77-wo)8u!"
)

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}