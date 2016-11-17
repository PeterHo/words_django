from .base import *

DEBUG = True

SECRET_KEY = 'c!^iyuxfdo8d14kza)r3!ymoja7=^%fp(rlq)#ej)ml8fju%=9'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': os.path.join(os.environ['HOME'], 'Nutstore', 'English', 'db.sqlite3'),
    }
}

