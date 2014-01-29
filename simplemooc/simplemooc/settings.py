import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '123')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'simplemooc.core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'simplemooc.urls'

WSGI_APPLICATION = 'simplemooc.wsgi.application'

TEST_NAME = 'test'

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'simplemooc',
        'USER': 'simplemooc',
        'PASSWORD': 'simplemooc',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    TEST_NAME: {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_simplemooc',
        'USER': 'simplemooc',
        'PASSWORD': 'simplemooc',
        'HOST': '127.0.0.1',
        'PORT': '5432',   
    }
}

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

try:
    from settings_local import *
except ImportError:
    pass