import pytest

from apiclients import clients


class TestOpenfoodfactsClient:
    def test_openfoodfacts_client_class_exists(self):
        assert hasattr(clients, "OpenfoodfactsClient")

    def test_get_products_by_popularity_exists(self, client, mock_get):
        client.get_products_by_popularity()

    def test_get_products_by_popularity_returns_a_list_of_length_100(
        self, client, mock_get
    ):
        results = client.get_products_by_popularity()
        assert isinstance(results, list)
        assert len(results) == 100

    def test_get_products_by_popularity_calls_requests_get(
        self, client, mock_get
    ):
        results = client.get_products_by_popularity()
        mock_get.assert_called_once()

    def test_get_products_by_popularity_calls_get_with_correct_default_args(
        self, client, mock_get
    ):
        url = "https://fr.openfoodfacts.org/cgi/search.pl"
        params = {
            "action": "process",
            "json": True,
            "sort_by": "unique_scans_n",
            "page_size": 100,
            "page": 1
        }
        results = client.get_products_by_popularity()
        mock_get.assert_called_with(url, params=params)

    def test_get_products_by_popularity_calls_get_with_correct_args(
        self, client, mock_get
    ):
        url = "https://fr.openfoodfacts.org/cgi/search.pl"
        params = {
            "action": "process",
            "json": True,
            "sort_by": "unique_scans_n",
            "page_size": 500,
            "page": 2
        }
        results = client.get_products_by_popularity(page_size=500, number_of_pages=2)
        mock_get.assert_any_call(url, params=params)
        mock_get.assert_any_call(url, params={**params, "page": 1})


    def test_get_products_by_popularity_returns_list_with_correct_products(
        self, client, mock_get
    ):
        results = client.get_products_by_popularity()
        for i, result in enumerate(results, start=1):
            assert result == f"product-{i:03d}"

    def test_get_products_by_popularity_returns_empty_list_if_http_error(
        self, client, mock_get_with_http_error
    ):
        results = client.get_products_by_popularity()
        assert results == []

    def test_get_products_by_popularity_returns_empty_list_if_connection_error(
        self, client, mock_get_with_connection_error
    ):
        results = client.get_products_by_popularity()
        assert results == []

    def test_get_products_by_popularity_returns_empty_list_if_nothing_found(
        self, client, mock_get_with_no_result
    ):
        results = client.get_products_by_popularity()
        assert results == []

