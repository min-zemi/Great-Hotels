import os

import dj_database_url

from .base import *


DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]


ALLOWED_HOSTS = []

render_external_hostname = os.environ.get(
    "RENDER_EXTERNAL_HOSTNAME"
)

if render_external_hostname:
    ALLOWED_HOSTS.append(render_external_hostname)


CSRF_TRUSTED_ORIGINS = []

if render_external_hostname:
    CSRF_TRUSTED_ORIGINS.append(
        f"https://{render_external_hostname}"
    )


DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        conn_health_checks=True,
    )
}


SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)