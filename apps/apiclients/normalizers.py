def remove_unuseful_fields(product):
    useful_fields = {
        "code",
        "product_name",
        "categories",
        "nutriscore_grade",
        "url",
        "generic_name",
        "image_nutrition_url",
        "image_url",
    }
    for field in product.keys() - useful_fields:
        del product[field]


def transform_fields_into_lowercase_letters(product):
    fields = {'product_name', 'categories', 'nutriscore_grade', 'generic_name'}
    for field in fields:
        product[field] = product[field].lower()


def transform_categories_into_list(product):
    product['categories'] = [
        category.strip() for category in product['categories'].split(',')
    ]


def transform_field_names(product):
    transformations = {
        "code": "id",
        "product_name": "name",
        "generic_name": "description",
        "nutriscore_grade": "nutriscore",
    }
    for old_field, new_field in transformations.items():
        product[new_field] = product[old_field]
        del product[old_field]


def transform_images_to_full_size(product):
    product["image_url"] = product["image_url"].replace("400.jpg", "full.jpg")
    product["image_nutrition_url"] = product["image_nutrition_url"].replace(
        "400.jpg", "full.jpg"
    )


def limit_length_of_product_names(product):
    product['name'] = product['name'][:255]


def limit_length_of_category_names(product):
    product['categories'] = [
        category_name[:255] for category_name in product['categories']
    ]


class ProductNormalizer:
    """Object used to standardize product dictionaries."""

    normalizers = [
        remove_unuseful_fields,
        transform_fields_into_lowercase_letters,
        transform_categories_into_list,
        transform_field_names,
        transform_images_to_full_size,
        limit_length_of_product_names,
        limit_length_of_category_names,
    ]

    def normalize(self, product):
        """Standardizes an individual product using the
        standardizers provided.
        """
        for normalizer in self.normalizers:
            normalizer(product)

    def normalize_all(self, products):
        """Standardize each product in the product list
        provided.
        """
        for product in products:
            self.normalize(product)
