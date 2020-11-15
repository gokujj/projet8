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
                category, _ = Category.objects.get_or_create(
                    name=category_name
                )
                product.categories.add(category)

    def find_substitutes(self, product_name):
        """Finds substitutes for product_name.
        The strategy used is to find the best products
        nutriscore with the greatest number of categories in common with
        product_name.
        """
        # Find the product corresponding to product_name in the database
        # of data
        print(f"Recu: {product_name}")
        product = (
            self.filter(name__icontains=product_name).order_by('?').first()
        )
        print(f"Trouvé: {product}")
        if not product:
            return []

        # We return a list of healthier substitutes to product
        substitutes = (
            self.exclude(pk=product.pk)
            .filter(
                categories__in=product.categories.all(),
                nutriscore__lt=product.nutriscore,
            )
            .annotate(num_common_categories=models.Count('pk'))
            .order_by('-num_common_categories', 'nutriscore')
        )
        if substitutes:
            return substitutes

        # If no healthier product is found, we look for products
        # the same nutriscore
        return (
            self.exclude(pk=product.pk)
            .filter(
                categories__in=product.categories.all(),
                nutriscore=product.nutriscore,
            )
            .annotate(num_common_categories=models.Count('pk'))
            .order_by('-num_common_categories')
        )
