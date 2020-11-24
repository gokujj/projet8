from django.db import models


class FavoriteManager(models.Manager):
    """Manager responsable de gérer les instances des favoris au sein de
    l'application."""

    def create_favorite(self, product, substitute, user):
        """Enregistre un nouveau favoris dans la liste de l'utilisateur."""
        return self.get_or_create(
            product=product, substitute=substitute, user=user
        )
