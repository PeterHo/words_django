import os
from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)

MEDIA_ROOT = BASE_DIR.child("media")
MEDIA_URL = "/media/"

# STATIC_ROOT = BASE_DIR.child("static")
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR.child("static"),
]

LOGIN_URL = 'user:login'
LOGIN_REDIRECT_URL = 'user:home'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.child("templates"),
        ],
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
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'apps.django2html',

    'apps.words',
    'apps.prefix',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

BOOTSTRAP3 = {
    'horizontal_label_class': 'col-xs-12',
    'horizontal_field_class': 'col-xs-12',
}
