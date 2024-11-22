"""
Django settings for snapchat project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(f=*eh)c*l1ygi^%&!*w-n(+#t!x$w-la-3$(q@%vjn$@_)ie!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'messaging',
    'stories',
    'friendships',
    'tailwind',
    'theme',
    'django_browser_reload'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'snapchat.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Dossier global de templates
        'APP_DIRS': True,  # Pour inclure les templates locaux des applications
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'snapchat.context_processors.navigation_menu'
            ],
        },
    },
]


WSGI_APPLICATION = 'snapchat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TAILWIND_APP_NAME = 'theme'

AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = [
    'users.authentication.EmailBackend',  # Use the custom email authentication backend
    #'django.contrib.auth.backends.ModelBackend',  # Keep the default backend as fallback
]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

NAVIGATION_MENU = {
    'register': [
        {'name': 'Login', 'url': 'login'},
    ],
    'login': [
        {'name': 'Register', 'url': 'register'},
    ],
    'stories': [
        {'name': 'amis', 'url': 'friends'},
        {'name': 'ajouter une story', 'url': 'add_story'},
        {'name': 'déconnexion', 'url': 'logout'},
        {'name': 'profile', 'url': 'profile'},
        {'name': 'mes stories', 'url': 'my_stories'},
    ],
    'friends': [
        {'name': 'ajouter une story', 'url': 'add_story'},
        {'name': 'stories', 'url': 'stories'},
        {'name': 'déconnexion', 'url': 'logout'},
        {'name': 'profile', 'url': 'profile'},
        {'name': 'mes stories', 'url': 'my_stories'},
    ],
    'add_story': [
        {'name': 'stories', 'url': 'stories'},
        {'name': 'déconnexion', 'url': 'logout'},
        {'name': 'profile', 'url': 'profile'},
        {'name': 'amis', 'url': 'friends'},
        {'name': 'mes stories', 'url': 'my_stories'},
    ],
    'story': [
        {'name': 'stories', 'url': 'stories'},
        {'name': 'déconnexion', 'url': 'logout'},
        {'name': 'profile', 'url': 'profile'},
        {'name': 'amis', 'url': 'friends'},
        {'name': 'mes stories', 'url': 'my_stories'},
    ],
    'profile': [
        {'name': 'stories', 'url': 'stories'},
        {'name': 'déconnexion', 'url': 'logout'},
        {'name': 'amis', 'url': 'friends'},
        {'name': 'mes stories', 'url': 'my_stories'},
    ],
    'my_stories': [
        {'name': 'stories', 'url': 'stories'},
        {'name': 'déconnexion', 'url': 'logout'},
        {'name': 'profile', 'url': 'profile'},
        {'name': 'amis', 'url': 'friends'},
    ]
}
