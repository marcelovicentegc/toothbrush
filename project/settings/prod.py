from project.settings.base import *

DEBUG = False



import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
        dsn="https://f5e0b6ea568c4016aafb5ff8e2519007@sentry.io/1318153",
        integrations=[DjangoIntegration()]
)


with open('/var/www/flossing.app/sensitive/secret_key.txt') as f:
        SECRET_KEY = f.read().strip()
            
with open('/var/www/flossing.app/sensitive/db_toothbrush_name.txt') as f:
        DB_TOOTHBRUSH_NAME = f.read().strip()

with open('/var/www/flossing.app/sensitive/db_toothbrush_user.txt') as f:
        DB_TOOTHBRUSH_USER = f.read().strip()

with open('/var/www/flossing.app/sensitive/db_toothbrush_password.txt') as f:
        DB_TOOTHBRUSH_PASSWORD = f.read().strip()
                                        
ALLOWED_HOSTS = ['flossing.app', 'www.flossing.app','localhost', '104.248.120.30']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_TOOTHBRUSH_NAME,
        'USER': DB_TOOTHBRUSH_USER,
        'PASSWORD': DB_TOOTHBRUSH_PASSWORD,
        'HOST': 'localhost',
        'PORT': '',
        }
}

STATIC_ROOT = '/var/www/flossing.app/static/'
MEDIA_ROOT = '/var/www/flossing.app/media/'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True                                
SECURE_HSTS_SECONDS = 63072000
X_FRAME_OPTIONS = 'DENY' 
