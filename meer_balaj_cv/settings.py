"""
Django settings for meer_balaj_cv project.

Generated by 'django-admin startproject' using Django 3.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""


# ayyanaws12345$$A





# ayyan

# 797928911849321

# PF-fnSP8AeTk2hdLsBynd7OJ3Rw


# CLOUDINARY_URL=cloudinary://797928911849321:PF-fnSP8AeTk2hdLsBynd7OJ3Rw@ayyan

from pathlib import Path
import os
import cloudinary_storage
from django.test.utils import ignore_warnings
ignore_warnings(message="No directory at", module="whitenoise.base").enable()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'meerbalajcv/static/js', 'serviceworker.js')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s%p&b^d34!ww2_)er&cfa0gxts^y#e^%7yu)@ev63jbzr!*+gm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['192.168.10.17','127.0.0.1','localhost']
# ALLOWED_HOSTS = ['meerbalaj.herokuapp.com']
ALLOWED_HOSTS = ['meerbalaj.com','www.meerbalaj.com','https://meerbalaj.com']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'meerbalajcv',
    'registration',
    'crispy_forms',
    'cloudinary_storage',
    'pwa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meer_balaj_cv.urls'

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

WSGI_APPLICATION = 'meer_balaj_cv.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Karachi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'







STATIC_URL = '/static/'

MEDIA_URL = '/media/'

  

# if DEBUG:
    # STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# else:
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
PROJECT_ROOT = os.path.join(os.path.abspath(__file__))

  
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"



REGISTRATION_OPEN = True                
ACCOUNT_ACTIVATION_DAYS = 7     
REGISTRATION_AUTO_LOGIN = True  
LOGIN_REDIRECT_URL = '/admin'  
LOGIN_URL = '/accounts/login/' 
SITE_ID = 1




# for email send in login and logut


ACCOUNT_EMAIL_VERIFICATION = "none"


# mail conf



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'



import dj_database_url 
prod_db = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)



CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'ayyan',
    'API_KEY': '797928911849321',
    'API_SECRET': 'PF-fnSP8AeTk2hdLsBynd7OJ3Rw'
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'



















PWA_APP_NAME = "MeerBalajCV"
PWA_APP_DESCRIPTION = "MeerBalajCV PWA"
PWA_APP_THEME_COLOR = "#060b1b"
PWA_APP_BACKGROUND_COLOR = "#151A33"
PWA_APP_DISPLAY = "standalone"
PWA_APP_SCOPE = "/"
PWA_APP_ORIENTATION = "any"
PWA_APP_START_URL = "/"
PWA_APP_STATUS_BAR_COLOR = "default"
PWA_APP_ICONS = [
{
    "src": "static/home/images/favicon-1.png",
    "sizes": "144x144"
}]
PWA_APP_ICONS_APPLE = [
{
    "src": "static/home/images/favicon-1.png",
    "sizes": "144x144"
}]
PWA_APP_SPLASH_SCREEN = [
{
    "src": "static/home/images/favicon-1.png",
    "media": "(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)"
}]
PWA_APP_DIR = "ltr"
PWA_APP_LANG = "en-US"