import pytest

VALID_PRODUCTS = [
    {
        "id": 12345678,
        "name": "Pizza margherita",
        "categories": ["CategoryA", "categoryB", "categoryC"],
        "nutriscore": "a",
        "url": "http://fr.openfoodfacts.org/v1/products/12351345238",
        "description": "pizza toute simple",
        "image_url": "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg",
        "image_nutrition_url": (
            "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
        )
    },
    {
        "id": 87654321,
        "name": "Pizza margherita",
        "categories": "CategoryA,categoryB,categoryC",
        "nutriscore": "a",
        "url": "http://fr.openfoodfacts.org/v1/products/12351345238",
        "description": "pizza toute simple",
        "image_url": "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg",
        "image_nutrition_url": (
            "http://fr.openfoodfacts.org/v1/products/12351345238/img.jpg"
        )
        # ...
    }
]


@pytest.fixture
def valid_products():
    return VALID_PRODUCTS
