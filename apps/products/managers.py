from django.db import models

from categories.models import Category


class ProductManager(models.Manager):
    """Respresent a manager responsible of handling product instances."""

    def create_from_openfoodfacts(self, products):
        """Save received product and category data as model instances."""
        for product_info in products:
            # Retrieving categories and stores
            categories = product_info.pop("categories")

            # Product registration
            product = self.create(**product_info)

            # Creation of categories and association with the product
            for category_name in categories:
                category, _ = Category.objects.get_or_create(name=category_name)
                product.categories.add(category)
