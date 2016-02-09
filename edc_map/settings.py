"""
Django settings for edc_map project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from unipath import Path


BASE_DIR = Path(os.path.dirname(os.path.dirname(__file__)))
PROJECT_ROOT = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(1)  # e.g.
SOURCE_ROOT = Path(os.path.dirname(os.path.realpath(__file__))).ancestor(2)  # e.g. /home/django/source
PROJECT_DIR = Path(os.path.dirname(os.path.realpath(__file__)))  # e.g.
MEDIA_ROOT = PROJECT_ROOT.child('media')
STATIC_ROOT = PROJECT_DIR.child('static')
GPS_FILE_NAME = '/Volumes/GARMIN/GPX/temp.gpx'
GPS_DEVICE = '/Volumes/GARMIN/'
GPX_TEMPLATE = os.path.join(STATIC_ROOT, 'gpx/template.gpx')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jlis1)=402q*6bwb+-hzn*65!rtl$e3cz%goiy&r#o8_&a$@r('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = ()

ALLOWED_HOSTS = []

MEDIA_URL = '/media/'
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'edc_map',
    'edc_device',
    'edc_templates',
    'edc_base',
    'edc_admin_exclude',
    'django_revision',
    'edc_dashboard',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'edc_map.urls'

WSGI_APPLICATION = 'edc_map.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
TEMPLATE_DIRS = ()

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

PROJECT_NUMBER = 'BHP000'
PROJECT_IDENTIFIER_PREFIX = '000'
PROJECT_IDENTIFIER_MODULUS = 7
IS_SECURE_DEVICE = True
FIELD_MAX_LENGTH = 'default'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
DJANGO_SETTINGS_MODULE = True
VERIFY_GPS = True
CURRENT_COMMUNITY = 'test_area'
GIT_DIR = BASE_DIR.ancestor(1)
APP_NAME = 'map'
PROJECT_TITLE = 'EDC Mapping'
INSTITUTION = 'Botswana-Harvard AIDS Institute'
PROTOCOL_REVISION = 'v1.0'
PROTOCOL_NUMBER = '000'
