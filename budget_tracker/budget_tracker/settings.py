import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',          # Required for admin site
    'django.contrib.auth',           # Required for authentication
    'django.contrib.contenttypes',
    'django.contrib.sessions',       # Required for session-based auth
    'django.contrib.messages',       # Required for admin messages
    'django.contrib.staticfiles',
    'rest_framework',               # Django REST Framework
    'rest_framework_simplejwt',     # SimpleJWT for API auth
    'users.apps.UsersConfig',       # Your users app
    'transactions.apps.TransactionsConfig',  # Your transactions app
    'reports.apps.ReportsConfig',   # Your reports app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Required for sessions
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required for auth
    'django.contrib.messages.middleware.MessageMiddleware',  # Required for messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'budget_tracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # For custom templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required for admin sidebar
                'django.contrib.auth.context_processors.auth',  # Required for admin/auth
                'django.contrib.messages.context_processors.messages',  # Required for admin
            ],
        },
    },
]

WSGI_APPLICATION = 'budget_tracker.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'budget_tracker_db'),
        'USER': os.getenv('DB_USER', 'your_postgres_username'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'your_postgres_password'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# CSRF settings
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000']

LOGIN_URL = '/login/'