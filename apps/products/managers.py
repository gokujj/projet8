from django.db import models

from categories.models import Category


class ProductManager(models.Manager):
    """Respresent a manager responsible of handling product instances."""

    def create_from_openfoodfacts(self, products):
        """Save received product and category data as model instances."""
        for product_info in products:
            # Récupération des catégories et magasins
            categories = product_info.pop("categories")

            # Enregistrement du produit
            product = self.create(**product_info)

            # Création des catégories et association avec le produit
            for category_name in categories:
                category = Category.objects.create(name=category_name)
                product.categories.add(category)
