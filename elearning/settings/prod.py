import os
from environs import Env
from .base import *
DEBUG = False
env = Env()

DEBUG = True
env.read_env()
ADMINS = [
    (env.str("ADMIN_NAME"), env.str("ADMIN_EMAIL")),
]
ALLOWED_HOSTS = ['elearningproject.com','www.elearningproject.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

# Security
CSRF_COOKIE_SECURE = True 
SESSION_COOKIE_SECURE = True 
SECURE_SSL_REDIRECT = True