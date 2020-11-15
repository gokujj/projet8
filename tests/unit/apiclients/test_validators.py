def test_valid_products_are_kept_by_product_validator(
    validator, valid_products
):
    filtered_products = validator.filter(valid_products)
    assert len(filtered_products) == len(valid_products)


def test_invalid_products_are_removed_by_product_validator(
    validator, invalid_products
):
    filtered_products = validator.filter(invalid_products)
    assert len(filtered_products) == 0


def test_only_invalid_products_are_removed_by_product_validator(
    validator, invalid_with_one_valid_product
):
    filtered_products = validator.filter(invalid_with_one_valid_product)
    assert len(filtered_products) == 1