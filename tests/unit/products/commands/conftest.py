import pytest


@pytest.fixture
def mock_client(mocker):
    return mocker.patch('apiclients.clients.OpenfoodfactsClient')()

@pytest.fixture
def mock_validator(mocker):
    return mocker.patch('apiclients.validators.ProductValidator')()

@pytest.fixture
def mock_normalizer(mocker):
    return mocker.patch('apiclients.normalizers.ProductNormalizer')()

@pytest.fixture
def mock_product_manager(mocker):
    return mocker.patch('products.models.Product.objects')