from django.core import management


def test_load_products_works_correctly(
    mock_client, mock_validator, mock_normalizer, mock_product_manager
):
    management.call_command('load_products')
    mock_product_manager.create_from_openfoodfacts.assert_called_with(
        mock_validator.filter.return_value
    )
    mock_validator.filter.assert_called_with(
        mock_client.get_products_by_popularity.return_value
    )
    mock_normalizer.normalize_all.assert_called_with(
        mock_validator.filter.return_value
    )
