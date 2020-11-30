import os

import django_heroku

from .base import *

# Configuration for products dowload
PRODUCT_CLIENT_PAGE_SIZE = 500
PRODUCT_CLIENT_NUMBER_OF_PAGES = 3

# Configuration spécifique pour le déploiement Heroku
DEBUG = False

# Configuration de l'email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Configuration des fichiers statiques
STATIC_URL = '/static/'
STATICFILES_DIRS = [str(BASE_DIR / 'apps' / '_static')]
STATIC_ROOT = str(BASE_DIR / 'staticfiles')

# Le package django_heroku s'occupe de toute la config restante
django_heroku.settings(locals())