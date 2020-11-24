import os
import django_heroku

from .base import *

# Configuration spécifique pour le déploiement Heroku
DEBUG = False

# Configuration de l'email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = 465
EMAIL_HOST_USER = 'gokujj@pythonclassmates.org'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

# Configuration des fichiers statiques
STATIC_URL = '/static/'
STATICFILES_DIRS = [str(BASE_DIR / 'apps' / '_static')]
STATIC_ROOT = str(BASE_DIR / 'staticfiles')

# Le package django_heroku s'occupe de toute la config restante
django_heroku.settings(locals())
