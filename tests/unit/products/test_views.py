from unittest.mock import MagicMock
from products.models import Product

import pytest

from products.views import (
    SearchView,
    ProductDetailView,
    PRODUCT_MAX_SUBSTITUTES,
)
from products.models import Product


@pytest.fixture
def search_view(rf, mocker):
    """Fixture creating an instance of SearchView."""
    # Build request
    request = rf.get(
        '/path/to/searchview', data={'search': 'nutella', 'page': 3}
    )
    request.user = MagicMock()

    # Build view
    view = SearchView()
    view.setup(request)

    # Mock dependencies
    view.mock_find_substitutes = mocker.patch(
        'products.models.Product.objects.find_substitutes'
    )
    view.mock_product = MagicMock()
    view.mock_substitutes = MagicMock()
    view.mock_find_substitutes.return_value = (
        view.mock_product,
        view.mock_substitutes,
    )

    yield view


@pytest.fixture
def product_detail_view(rf):
    request = rf.get('/path/to/product-detail-view')

    # Build view
    view = ProductDetailView()
    view.setup(request)

    yield view


class TestSearchView:
    def test_get_context_data_calls_find_substitutes(self, search_view):
        search_view.get_context_data()
        search_view.mock_find_substitutes.assert_called_with(
            product_name=search_view.request.GET.get('search'),
            user=search_view.request.user,
        )

    def test_template_name_is_correct(self):
        assert SearchView.template_name == "products/results.html"

    def test_get_context_data_paginates_substitute(self, search_view, mocker):
        mock_paginator = mocker.patch('products.views.Paginator')
        search_view.get_context_data()
        mock_paginator.assert_any_call(
            search_view.mock_substitutes, PRODUCT_MAX_SUBSTITUTES
        )
        mock_paginator.return_value.get_page.assert_any_call('3')

    def test_context_contains_correct_keys(self, search_view):
        context = search_view.get_context_data()
        assert 'product' in context
        assert 'substitutes' in context
        assert 'is_paginated' in context
        assert 'paginator' in context
        assert 'page_obj' in context

    def test_context_contains_correct_value(self, search_view, mocker):
        mock_paginator = mocker.patch('products.views.Paginator')
        context = search_view.get_context_data()
        assert context['product'] == search_view.mock_product
        assert context['substitutes'] == (
            mock_paginator.return_value.get_page.return_value
        )
        assert context['is_paginated'] == True
        assert context['paginator'] == mock_paginator.return_value
        assert context['page_obj'] == context['substitutes']


class TestProductDetailView:
    def test_render_to_response_gives_correct_template(
        self, product_detail_view
    ):
        response = product_detail_view.render_to_response(context={})
        assert ProductDetailView.template_name in response.template_name

    def test_model_is_product(self):
        assert ProductDetailView.model == Product

    def test_model_receives_product(self, product_detail_view):
        product_detail_view.object = MagicMock()
        context = product_detail_view.get_context_data()
        assert context['product'] == product_detail_view.object
