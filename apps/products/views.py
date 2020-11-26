from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.conf import settings
from django.core.paginator import Paginator

from .models import Product

PRODUCT_MAX_SUBSTITUTES = getattr(settings, 'PRODUCT_MAX_SUBSTITUTES', 6)


class SearchView(TemplateView):
    template_name = "products/results.html"

    def get_context_data(self, *args, **kwargs):
        """Prepares the context to be sent to the page template."""
        context = super().get_context_data(*args, **kwargs)
        product, substitutes = Product.objects.find_substitutes(
            product_name=self.request.GET.get('search'), user=self.request.user
        )

        # Pagination of the results
        paginator = Paginator(substitutes, PRODUCT_MAX_SUBSTITUTES)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Preparation of the context
        context['product'] = product
        context['substitutes'] = page_obj
        context['is_paginated'] = True
        context['paginator'] = paginator
        context['page_obj'] = page_obj

        return context


class ProductDetailView(DetailView):
    template_name = 'products/details.html'
    model = Product
    context_object_name = 'product'
