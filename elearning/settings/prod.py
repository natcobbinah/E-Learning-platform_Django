from environs import Env
from .base import *
DEBUG = False
env = Env()

DEBUG = True
env.read_env()
ADMINS = [
    (env.str("ADMIN_NAME"), env.str("ADMIN_EMAIL")),
]
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {}
}
