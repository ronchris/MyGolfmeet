"""
Django settings for MyGolfmeet project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd&w2h)ixcq1$5v!1q9*e%=%n%*+pq-q4uh4vk1!a@b%j=z3_&m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

AUTH_PROFILE_MODULE = 'golfapp.UserInfo'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'south',
    'golfapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request'
)

ROOT_URLCONF = 'MyGolfmeet.urls'

WSGI_APPLICATION = 'MyGolfmeet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = "/MyGolfmeet/golfapp/static/"

# Security

PASSWORD_HASHERS = {
      "django.contrib.auth.hashers.BCryptPasswordHasher",
      "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
      "django.contrib.auth.hashers.PBKDF2PasswordHasher",
      "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
      "django.contrib.auth.hashers.SHA1PasswordHasher",
      "django.contrib.auth.hashers.MD5PasswordHasher",
      "django.contrib.auth.hashers.CryptPasswordHasher"

}

# Upload images directory

MEDIA_URL = '/media/'

MEDIA_ROOT = "/MyGolfmeet/golfapp/media/"

SITE_ID = "1"
