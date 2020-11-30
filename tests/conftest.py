import pytest
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress

from products.models import Product
from categories.models import Category
from favorites.models import Favorite

User = get_user_model()


@pytest.fixture
def user(transactional_db):
    """Fixture creating a user with a verified email."""
    user = User.objects.create_user(
        "testuser", "testuser@oc.com", "asdnFSdh7sd8Fa8f"
    )
    EmailAddress.objects.create(
        user=user, email="testuser@oc.com", verified=True, primary=True
    )
    yield user


@pytest.fixture
def category(transactional_db):
    category, _ = Category.objects.get_or_create(name="category")
    yield category


@pytest.fixture
def other_category(transactional_db):
    other_category, _ = Category.objects.get_or_create(name="other category")
    yield other_category


@pytest.fixture
def product_a_other_category(transactional_db, category, other_category):
    product = Product.objects.create(
        id=1,
        name="Test product 1",
        url="http://test-products.org/1",
        nutriscore="a",
        description="lorem ipsum",
        image_url="http://test-products.org/image.png",
        image_nutrition_url="http://test-products.org/image.png",
    )
    product.categories.add(category)
    product.categories.add(other_category)
    yield product


@pytest.fixture
def product_b_other_category(transactional_db, category, other_category):
    product = Product.objects.create(
        id=2,
        name="Test product 2",
        url="http://test-products.org/2",
        nutriscore="b",
        description="lorem ipsum",
        image_url="http://test-products.org/image.png",
        image_nutrition_url="http://test-products.org/image.png",
    )
    product.categories.add(category)
    product.categories.add(other_category)
    yield product


@pytest.fixture
def product_c_other_category(transactional_db, category, other_category):
    product = Product.objects.create(
        id=3,
        name="Test product 3",
        url="http://test-products.org/3",
        nutriscore="c",
        description="lorem ipsum",
        image_url="http://test-products.org/image.png",
        image_nutrition_url="http://test-products.org/image.png",
    )
    product.categories.add(category)
    product.categories.add(other_category)
    yield product


@pytest.fixture
def product_d_other_category(transactional_db, category, other_category):
    product = Product.objects.create(
        id=4,
        name="Test product 4",
        url="http://test-products.org/4",
        nutriscore="d",
        description="lorem ipsum",
        image_url="http://test-products.org/image.png",
        image_nutrition_url="http://test-products.org/image.png",
    )
    product.categories.add(category)
    product.categories.add(other_category)
    yield product


@pytest.fixture
def product_e_other_category(transactional_db, category, other_category):
    product = Product.objects.create(
        id=5,
        name="Test product 5",
        url="http://test-products.org/5",
        nutriscore="e",
        description="lorem ipsum",
        image_url="http://test-products.org/image.png",
        image_nutrition_url="http://test-products.org/image.png",
    )
    product.categories.add(category)
    product.categories.add(other_category)
    yield product


@pytest.fixture
def product_a(transactional_db, category):
    product = Product.objects.create(
        id=6,
        name="Test product 6",
        url="http://test-products.org/6",
        nutriscore="a",
        description="lorem ipsum",
        image_url="http://test-products.org/image.png",
        image_nutrition_url="http://test-products.org/image.png",
    )
    product.categories.add(category)
    yield product


@pytest.fixture
def product_b(transactional_db, category):
    product = Product.objects.create(
        id=7,
        name="Test product 7",
        url="http://test-products.org/7",
        nutriscore="b",
        description="lorem ipsum",
        image_url="http://test-products.org/image.png",
        image_nutrition_url="http://test-products.org/image.png",
    )
    product.categories.add(category)
    yield product


@pytest.fixture
def product_c(transactional_db, category):
    product = Product.objects.create(
        id=8,
        name="Test product 8",
        url="http://test-products.org/8",
        nutriscore="c",
        description="lorem ipsum",
        image_url="http://test-products.org/image.png",
        image_nutrition_url="http://test-products.org/image.png",
    )
    product.categories.add(category)
    yield product


@pytest.fixture
def product_d(transactional_db, category):
    product = Product.objects.create(
        id=9,
        name="Test product 9",
        url="http://test-products.org/9",
        nutriscore="d",
        description="lorem ipsum",
        image_url="http://test-products.org/image.png",
        image_nutrition_url="http://test-products.org/image.png",
    )
    product.categories.add(category)
    yield product


@pytest.fixture
def product_e(transactional_db, category):
    product = Product.objects.create(
        id=10,
        name="Test product 10",
        url="http://test-products.org/10",
        nutriscore="e",
        description="lorem ipsum",
        image_url="http://test-products.org/image.png",
        image_nutrition_url="http://test-products.org/image.png",
    )
    product.categories.add(category)
    yield product


@pytest.fixture
def first_favorite(user, product_a, product_b):
    favorite, _ = Favorite.objects.create_favorite(
        product=product_b, substitute=product_a, user=user
    )
    yield favorite


@pytest.fixture
def second_favorite(user, product_b, product_d):
    favorite, _ = Favorite.objects.create_favorite(
        product=product_d, substitute=product_b, user=user
    )
    yield favorite


@pytest.fixture
def third_favorite(user, product_c, product_e):
    favorite, _ = Favorite.objects.create_favorite(
        product=product_e, substitute=product_c, user=user
    )
    yield favorite


@pytest.fixture
def fourth_favorite(user, product_a_other_category, product_b_other_category):
    favorite, _ = Favorite.objects.create_favorite(
        product=product_b_other_category,
        substitute=product_a_other_category,
        user=user,
    )
    yield favorite


@pytest.fixture
def fifth_favorite(user, product_b_other_category, product_d_other_category):
    favorite, _ = Favorite.objects.create_favorite(
        product=product_d_other_category,
        substitute=product_b_other_category,
        user=user,
    )
    yield favorite


@pytest.fixture
def sixth_favorite(user, product_c_other_category, product_e_other_category):
    favorite, _ = Favorite.objects.create_favorite(
        product=product_e_other_category,
        substitute=product_c_other_category,
        user=user,
    )
    yield favorite


@pytest.fixture
def sixth_favorite(user, product_c_other_category, product_e_other_category):
    favorite, _ = Favorite.objects.create_favorite(
        product=product_e_other_category,
        substitute=product_c_other_category,
        user=user,
    )
    yield favorite


@pytest.fixture
def seventh_favorite(user, product_c, product_e_other_category):
    favorite, _ = Favorite.objects.create_favorite(
        product=product_e_other_category,
        substitute=product_c,
        user=user,
    )
    yield favorite


@pytest.fixture
def all_favorites(
    first_favorite,
    second_favorite,
    third_favorite,
    fourth_favorite,
    fifth_favorite,
    sixth_favorite,
    seventh_favorite,
):
    yield [
        first_favorite,
        second_favorite,
        third_favorite,
        fourth_favorite,
        fifth_favorite,
        sixth_favorite,
        seventh_favorite,
    ]
