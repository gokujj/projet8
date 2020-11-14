import pytest
from products.models import Product


def test_product_manager_create_products_from_openfoodfacts_data(
    valid_products, db
):
    Product.objects.create_from_openfoodfacts(valid_products)
    assert Product.objects.get(id=12345678).name == "Pizza margherita"
