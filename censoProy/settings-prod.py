"""
Django settings for censoProy project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta # Para darle tiempo de vida a los tokens

import django_heroku # Para configuracion automática de alguna configuración para Heroku (e.g. Statics)

import json # Para leer archivo json de credenciales de DB

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c#&_rlisqx$ko#2ckoga_98dy4yigzu*ib=*2ume5w4@11q)9h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "https://censoindigena.herokuapp.com"]

# CORS_ALLOWED_ORIGINS = [
    # "http://localhost:8080", 
    # "http://localhost:8081",
    # "http://localhost:8082",
    # "https://censofront.herokuapp.com"
    # ]
CORS_ALLOW_ALL_ORIGINS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'censoIndigenasApp',
    'corsheaders',
]

SIMPLE_JWT = { # Alguna configuracion para los tokens a usar para autorizacion
    'ACCESS_TOKEN_LIFETIME'     : timedelta(minutes = 10),
    'REFRESH_TOKEN_LIFETIME'    : timedelta(days = 1),
    'ROTATE_REFRESH_TOKENS'     : False,  # Si se debe devolver un nuevo Refresh Token al hacer uso de un Refresh Token
    'BLACKLIST_AFTER_ROTATION'  : False,  # Si un Refresh Token utilizado debe mandarse a la lista negra (necesita de app de lista negra instalada)
    'UPDATE_LAST_LOGIN'         : True,   # Actualizar campo de Last time logged in de la tabla User
    'ALGORITHM'                 : 'HS256',
    'USER_ID_FIELD'             : 'id', # Campo de la tabla User a usar como identificador
    'USER_ID_CLAIM'             : 'user_id', # Forma de referirse a este identificador unico en la metadata del token
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
]

REST_FRAMEWORK = { # En settings.py del proyecto
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAdminUser'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication', # Usaremos Tokens de JWT
    )
}

AUTH_USER_MODEL = 'censoIndigenasApp.Usuario'

ROOT_URLCONF = 'censoProy.urls'

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

WSGI_APPLICATION = 'censoProy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

with open('utils/db_credentials.json', 'r') as archivo:
     db_credentials = json.load(archivo)

DATABASES = {
    
  'default': {
        'ENGINE'   : 'django.db.backends.postgresql_psycopg2',
        'NAME'     : db_credentials["db_name"],
        'USER'     : db_credentials["db_user"],
        'PASSWORD' : db_credentials["db_pass"],
        'HOST'     : db_credentials["db_ip"],
        'PORT'     : db_credentials["db_port"]
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

django_heroku.settings(locals())