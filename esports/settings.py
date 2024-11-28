"""
Django settings for esports project using Django 5.1.2.
"""

import os
import environ
from pathlib import Path
from logging.handlers import RotatingFileHandler

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# # Reading .env file
# environ.Env.read_env()
# # Django Secret Key
# SECRET_KEY = env('DJANGO_SECRET_KEY')
# # Debug Mode (True/False)
# DEBUG = env('DJANGO_DEBUG')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-danlrj=e#psi)fj!1x1hsn0lm4+y!yfs9^59=07^oac03p6zdi'

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
    # apps
    'dashboard',
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

ROOT_URLCONF = 'esports.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'esports.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
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


# Logging configuration
LOGGING = {
    'version': 1,  # Set to 1 to specify the version
    'disable_existing_loggers': False,  # Keep Django's default logging configuration
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        # Modify the file handler to include rotation
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),
            'formatter': 'verbose',
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 3,  # Keep the last 3 log files
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            # Use both file and console handlers
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        # Custom logger for your app
        'myapp': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# This is where collected static files will be stored for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Directory for user-uploaded and dynamically created files
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# OpenAI API Key
OPENAI_API_KEY = "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"  # Replace with your actual API key

# Media settings (if not already defined)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Create necessary directories
EXTRACTED_FRAMES_DIR = os.path.join(MEDIA_ROOT, 'extracted_frames')
TEMP_DIR = os.path.join(MEDIA_ROOT, 'temp')

# Create directories if they don't exist
os.makedirs(EXTRACTED_FRAMES_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)
