from django.urls import resolve

from products.views import SearchView, ProductDetailView


def test_url_resolves_to_searchview():
    view = resolve('/products/substitutes/')
    assert view.func.view_class == SearchView


def test_url_resolves_to_productdetailview():
    view = resolve('/products/1/')
    assert view.func.view_class == ProductDetailView