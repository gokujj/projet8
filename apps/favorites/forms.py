from django import forms
from django.core.exceptions import ValidationError

from products.models import Product
from .models import Favorite


class FavoriteCreationForm(forms.Form):
    """Formulaire validant que les données de produits reçues pour un
    favori existent."""

    product = forms.IntegerField(label="product", required=True)
    substitute = forms.IntegerField(label="substitute", required=True)

    def clean_product(self):
        """Valide que le produit exite en base de données."""
        product_id = self.cleaned_data['product']
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise ValidationError("Product does not exist in database")
        return product

    def clean_substitute(self):
        """Valide que le produit exite en base de données."""
        substitute_id = self.cleaned_data['substitute']
        try:
            substitute = Product.objects.get(pk=substitute_id)
        except Product.DoesNotExist:
            raise ValidationError("Product does not exist in database")
        return substitute

    def save(self, user, *args, **kwargs):
        """Sauvegarde les produits dans les favoris de l'utilisateur passé
        en argument."""
        return Favorite.objects.create_favorite(
            product=self.cleaned_data['product'],
            substitute=self.cleaned_data['substitute'],
            user=user,
        )
