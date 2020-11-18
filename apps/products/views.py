from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.conf import settings

from .models import Product


class SearchView(TemplateView):
    template_name = "products/results.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        product, substitutes = Product.objects.find_substitutes(
            product_name=self.request.GET.get('search'), user=self.request.user
        )
        context['product'] = product
        context['substitutes'] = substitutes[
            : settings.PRODUCT_MAX_SUBSTITUTES
        ]
        return context


class ProductDetailView(DetailView):
    template_name = 'products/details.html'
    model = Product
    context_object_name = 'product'
