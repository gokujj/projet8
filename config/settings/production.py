import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
import dj_database_url
import dj_email_url

from .base import *

# Debug should be False in production
DEBUG = False

# Host allowed to access the web application
ALLOWED_HOSTS = [
    'purbeurre.sangoku.org',
]

# Settings of the production database
DATABASES['default'] = dj_database_url.config(
    default=os.environ['DATABASE_URL']
)

# Configuration of the production
email_config = dj_email_url.config()
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = email_config['EMAIL_HOST']
EMAIL_PORT = email_config['EMAIL_PORT']
EMAIL_HOST_USER = email_config['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = email_config['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = email_config['EMAIL_USE_TLS']
EMAIL_USE_SSL = email_config['EMAIL_USE_SSL']
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


EMAIL_HOST_PASSWORD = email_config['EMAIL_HOST_PASSWORD']


# Configuration for products dowload
PRODUCT_CLIENT_PAGE_SIZE = 100
PRODUCT_CLIENT_NUMBER_OF_PAGES = 3

sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)