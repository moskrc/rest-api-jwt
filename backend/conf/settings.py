import os
import environ
from datetime import timedelta

env = environ.Env()
root_path = environ.Path(__file__) - 2
env.read_env(env_file=root_path(".env"))

# -----------------------------------------------------------------------------
# Basic Config
# -----------------------------------------------------------------------------
ENV = env("ENV", default="prod")
assert ENV in ["dev", "test", "prod", "qa"]
DEBUG = env.bool("DEBUG", default=False)
BASE_DIR = root_path()
ROOT_URLCONF = "conf.urls"
WSGI_APPLICATION = "conf.wsgi.application"

# -----------------------------------------------------------------------------
# Time & Language
# -----------------------------------------------------------------------------
LANGUAGE_CODE = env("LANGUAGE_CODE", default="en-us")
TIME_ZONE = env("TIMEZONE", default="UTC")
USE_I18N = env("USE_I18N", default=True)
USE_L10N = env("USE_L10N", default=True)
USE_TZ = env("USE_TZ", default=True)

# -----------------------------------------------------------------------------
# Emails
# -----------------------------------------------------------------------------
EMAIL_BACKEND = env(
    "EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_HOST = env("EMAIL_HOST", default="localhost")
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="user")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
EMAIL_PORT = env("EMAIL_PORT", default=587)
EMAIL_USE_TLS = env("EMAIL_USE_TLS", default=True)
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="")


# -----------------------------------------------------------------------------
# Security and Users
# -----------------------------------------------------------------------------
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# -----------------------------------------------------------------------------
# Databases
# -----------------------------------------------------------------------------
DJANGO_DATABASE_URL = env.db("DATABASE_URL")
DATABASES = {"default": DJANGO_DATABASE_URL}

# -----------------------------------------------------------------------------
# Applications configuration
# -----------------------------------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'authentication',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [root_path("templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# -----------------------------------------------------------------------------
# Static & Media Files
# -----------------------------------------------------------------------------

STATIC_URL = env("STATIC_URL", default="/static/")
STATIC_ROOT = env("STATIC_ROOT", default=root_path("static"))

MEDIA_URL = env("MEDIA_URL", default="/media/")
MEDIA_ROOT = env("MEDIA_ROOT", default=root_path("media"))
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

STATICFILES_DIRS = (
    ("img", root_path("assets/img")),
)

# -----------------------------------------------------------------------------
# User model
# -----------------------------------------------------------------------------

AUTH_USER_MODEL = "authentication.CustomUser"


# -----------------------------------------------------------------------------
# REST framework
# -----------------------------------------------------------------------------

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),  #
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': False,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('JWT',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}