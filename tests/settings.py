SECRET_KEY = "dump-secret-key"

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
)

BRIEFME_VALIDATOR_CONTACT_URL = "/contact/"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}
