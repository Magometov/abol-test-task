"""Конфигурация проекта"""

import os
from pathlib import Path

# ======================================================================================================================
# BASE SETTINGS
# ======================================================================================================================

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-2@(qjmpl!)n-5")

DEBUG = os.environ.get("DEBUG", True)

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", default="localhost 127.0.0.1 [::1]").split(" ")

# ======================================================================================================================
# APPS SETTINGS
# ======================================================================================================================

INSTALLED_APPS = [
    # base
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third-party
    "django_extensions",
    "rest_framework",
    "drf_spectacular",
    # applications
    "src.apps.book.apps.BookConfig",
]

# ======================================================================================================================
# MIDDLEWARE SETTINGS
# ======================================================================================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ======================================================================================================================
# ROOT URL SETTINGS
# ======================================================================================================================

ROOT_URLCONF = "src.config.urls"

# ======================================================================================================================
# TEMPLATES SETTINGS
# ======================================================================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ======================================================================================================================
# WSGI SETTINGS
# ======================================================================================================================

WSGI_APPLICATION = "src.config.wsgi.application"

# ======================================================================================================================
# DATABASE SETTINGS
# ======================================================================================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("POSTGRES_USER", "user"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "password"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}

# ======================================================================================================================
# DRF SETTINGS
# ======================================================================================================================

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# ======================================================================================================================
# SPECTACULAR SETTINGS
# ======================================================================================================================

SPECTACULAR_SETTINGS = {
    "TITLE": "API Documentation",
    "DESCRIPTION": "API Documentation",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": True,
}

# ======================================================================================================================
# MORE SETTINGS
# ======================================================================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
