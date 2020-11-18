from django.db import models
from django.conf import settings


class Favorite(models.Model):
    """Favorite saved by user to substitute a product."""

    substitute = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name="favorites_as_substitute",
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name="favorites_as_product",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorites",
    )

    class Meta:
        verbose_name_plural = 'favorites'
        unique_together = ('substitute', 'product', 'user')

    def __str__(self):
        return f"({user.name}, {product.name}, {substitute.name})"
