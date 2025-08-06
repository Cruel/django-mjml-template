import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "test"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = ("django_mjml_template",)

MIDDLEWARE_CLASSES = ()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": ("django.template.context_processors.request",),
        },
    },
]
