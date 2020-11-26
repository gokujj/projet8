from django.views.generic import View
from django.http import JsonResponse

from products.models import Product


class ProductsCompletionView(View):
    """Vue gérant l'autocomplétion des produits dans le formulaire de
    recherche."""

    def get(self, request, *args, **kwargs):
        """Gère de les requêtes GET pour l'auto-completion des produits."""
        term = request.GET.get('term')
        products = Product.objects.filter(name__icontains=term).order_by(
            '-nutriscore', 'name'
        )
        # Create a list product names without duplicates
        product_names = list(
            dict.fromkeys(product.name.capitalize() for product in products)
        )
        # Returns response as json and use safe=False because product_name
        # is not a dictionary
        return JsonResponse(product_names, safe=False)
