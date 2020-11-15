from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Utilisateur personnalisé représentant les visiteurs inscrits de notre
    application."""