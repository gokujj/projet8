def validate_fields_are_present_in_product(product):
    fields = {
        "code", "product_name", "categories", "nutriscore_grade",
        "url", "generic_name", "image_nutrition_url", "image_url"
    }
    if fields - product.keys():
        return False
    return True


def validate_fields_are_not_empty_in_product(product):
    fields = {
        "code", "product_name", "categories", "nutriscore_grade",
        "url", "generic_name", "image_nutrition_url", "image_url"
    }
    for field in fields:
        if isinstance(product[field], str) and not product[field].strip():
            return False
    return True


class ProductValidator:
    """Object responsible for validating products against rules
    in validators and keep only the valid ones.
    """

    validators = [
        validate_fields_are_present_in_product,
        validate_fields_are_not_empty_in_product
    ]

    def is_valid(self, product):
        """Returns True if the product passed as argument is valid.
        Args:
            product (dict): dictionary containing the data of a product
        Return:
            True if the product is valid.
        """
        for validator in self.validators:
            if not validator(product):
                return False
        return True

    def filter(self, products):
        """Eliminate invalid products from the past product list
        as an argument.
        Args:
            products (list): list of products to filter.
        Return:
            List of products considered valid.
        """
        filtered_products = []
        for product in products:
            if self.is_valid(product):
                filtered_products.append(product)
        return filtered_products
