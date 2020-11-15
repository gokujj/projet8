import pytest
import requests

import tests.unit.apiclients.test_data as data

from apps.apiclients.clients import OpenfoodfactsClient
from apps.apiclients.validators import ProductValidator 
from apps.apiclients.normalizers import ProductNormalizer
from tests.unit.apiclients.test_data import VALID_PRODUCT


OPENFOODFACTS_SUCCESS_RESPONSE = {
    "page": 1,
    "page_size": 100,
    "count": 100,
    "products": [f"product-{i:03d}" for i in range(1, 101)],
}

OPENFOODFACTS_NOTHING_FOUND_RESPONSE = {
    "products": [],
    "count": 0,
    "page_size": 1000,
    "page": 1,
}


@pytest.fixture
def client():
    """Fixture créant une instance de OpenfoodfactsClient pour chaque test."""
    client = OpenfoodfactsClient()
    yield client


@pytest.fixture
def mock_get(mocker):
    """Fixture remplacant la fonction requests.get par une imitation."""

    mock_requests_get = mocker.patch('requests.get')
    mock_requests_get.return_value.json.return_value = (
        OPENFOODFACTS_SUCCESS_RESPONSE
    )
    yield mock_requests_get


@pytest.fixture
def mock_get_with_http_error(mocker):
    """Fixture remplacant la fonction requests.get par une imitation
    levant une requests.HTTPError via raise_for_status."""

    mock_requests_get = mocker.patch('requests.get')
    mock_requests_get.return_value.json.return_value = (
        OPENFOODFACTS_SUCCESS_RESPONSE
    )
    mock_requests_get.side_effect = requests.HTTPError(
        "Exception raised by mock_get_with_http_error"
    )
    yield mock_requests_get


@pytest.fixture
def mock_get_with_connection_error(mocker):
    """Fixture remplacant la fonction requests.get par une imitation
    levant une requests.ConnectionError."""

    mock_requests_get = mocker.patch('requests.get')
    mock_requests_get.side_effect = requests.ConnectionError(
        "Exception raised by mock_get_with_http_error"
    )
    yield mock_requests_get


@pytest.fixture
def mock_get_with_no_result(mocker):
    """Fixture remplacant la fonction requests.get par une imitation
    simulant un appel sans résultat à l'API."""

    mock_requests_get = mocker.patch('requests.get')
    mock_requests_get.return_value.json.return_value = (
        OPENFOODFACTS_NOTHING_FOUND_RESPONSE
    )
    yield mock_requests_get

@pytest.fixture
def validator():
    yield ProductValidator()

@pytest.fixture
def valid_products():
    yield data.get_valid_products()

@pytest.fixture
def valid_product():
    return VALID_PRODUCT

@pytest.fixture
def invalid_products():
    yield data.get_invalid_products()

@pytest.fixture
def invalid_with_one_valid_product():
    yield data.get_invalid_with_one_valid_product()

@pytest.fixture
def normalizer():
    return ProductNormalizer()