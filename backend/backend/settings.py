"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xmzh+(cx$ifwt15nbxx5escn9+tm7#lm_ljv=i!j#st)jyvy4r'

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
    'django.core.mail',
    'django.contrib.sites',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
   'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'user',
    'corsheaders',
    'rest_framework',
    'connectadmin',
    'oauth2_provider',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'backend.security_headers_middleware.SecurityHeadersMiddleware',
]

ROOT_URLCONF = 'backend.urls'
SITE_ID = 1


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

AUTH_USER_MODEL = 'user.CustomUser'

WSGI_APPLICATION = 'backend.wsgi.application'
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10  # You can set any default page size you want
}



# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
     "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "connectsphere",
        "USER": "postgres",
        "PASSWORD":"admin@123",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id':'331173960696-5r60tcf7mme4bku25mga0r8otirmte8e.apps.googleusercontent.com',
            'secret': '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',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

CORS_ALLOW_CREDENTIALS = True
CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']
ROOT_URLCONF = 'backend.urls'
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CORS_ALLOWED_ORIGINS = [
  
    'http://localhost:3000',
    'http://127.0.0.1:3000'
]

CORS_ORIGIN_WHITELIST = [
    'http://google.com',
    'http://localhost:8000',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:3000'
]






EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'stopnshop890@gmail.com'
EMAIL_HOST_PASSWORD = 'qoruttdlboezrrcc'

AUTHENTICATION_BACKENDS = [
    'rest_framework_simplejwt.authentication.JWTAuthentication',
    'allauth.account.auth_backends.AuthenticationBackend',
    'drf_social_oauth2.backends.DjangoOAuth2',
    'social_core.backends.google.GoogleOAuth2',
]
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '331173960696-5r60tcf7mme4bku25mga0r8otirmte8e.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]

