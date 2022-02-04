"""
Django settings for test_app project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'at*k-_n3&-r@p+^5q@8#po-q9py4ffj&s(fbfn2=d(-@^$mv&n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

TENANT_APPS = ['test_app.tenant']
SHARED_APPS = ['test_app.shared', 'test_app.tenant']

DB_ENGINE = 'tenant_schemas.postgresql_backend'
DATABASE_ROUTERS = ['tenant_schemas.routers.TenantSyncRouter']

DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'

try:
    import tenant_schemas
    INSTALLED_APPS = ['tenant_schemas']

except ImportError:
    pass

try:
    import django_tenants
    INSTALLED_APPS = ['django_tenants']
    DB_ENGINE = 'django_tenants.postgresql_backend'
    DATABASE_ROUTERS = ['django_tenants.routers.TenantSyncRouter']
    DEFAULT_FILE_STORAGE = 'django_tenants.storage.TenantFileSystemStorage'

except ImportError:
    pass

INSTALLED_APPS += [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'tenant_schemas_celery',
    'test_app.shared',
    'test_app.tenant',
]

TENANT_MODEL = 'shared.Client'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'test_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'HOST': os.environ.get("DATABASE_HOST", "127.0.0.1"),
        'NAME': 'tenant_celery',
        'PASSWORD': 'qwe123',
        'USER': 'tenant_celery',
        'TEST': {
            'NAME': 'tenant_celery',
        }
    },
    'otherdb1': {
        'ENGINE': DB_ENGINE,
        'HOST': os.environ.get("DATABASE_HOST", "127.0.0.1"),
        'NAME': 'tenant_celery',
        'PASSWORD': 'qwe123',
        'USER': 'tenant_celery',
        'TEST': {
            'NAME': 'tenant_celery',
        }
    },
    'otherdb2': {
        'ENGINE': DB_ENGINE,
        'HOST': os.environ.get("DATABASE_HOST", "127.0.0.1"),
        'NAME': 'tenant_celery',
        'PASSWORD': 'qwe123',
        'USER': 'tenant_celery',
        'TEST': {
            'NAME': 'tenant_celery',
        }
    },
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

CELERY_BROKER_URL = os.environ.get("BROKER_URL", 'amqp://tenants:tenants@localhost:5672/')
CELERYBEAT_SCHEDULE = {
    'test-periodic-task': {
        'task': 'test_app.tenant.tasks.periodic_print_schema',
        'schedule': 5.0,
    },
}
CELERY_TASK_TENANT_CACHE_SECONDS = os.environ.get("TASK_TENANT_CACHE_SECONDS", 10)
