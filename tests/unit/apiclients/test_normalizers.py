from copy import deepcopy

from apiclients import normalizers  

def test_unuseful_fields_are_removed(valid_product):
    valid_product = {**valid_product, "energy_100g": 500.0}
    normalizers.remove_unuseful_fields(valid_product)
    assert "energy_100g" not in valid_product

def test_letters_are_normalized_to_lowercase(valid_product):
    valid_product = deepcopy(valid_product)
    normalizers.transform_fields_into_lowercase_letters(valid_product)
    fields = {
        'product_name', 'categories', 'nutriscore_grade', 
        'generic_name', "image_url", "image_nutrition_url"
    }
    for field in fields:
        assert valid_product[field] == valid_product[field].lower()

def test_categories_are_transformed_to_list(valid_product):
    valid_product = deepcopy(valid_product)
    normalizers.transform_categories_into_list(valid_product)
    assert len(valid_product['categories']) == 3
    assert isinstance(valid_product['categories'], list)

def test_fields_are_renamed_correctly(valid_product):
    valid_product = deepcopy(valid_product)
    normalizers.transform_field_names(valid_product)
    assert "product_name" not in valid_product 
    assert "name" in valid_product 
    assert "nutriscore_grade" not in valid_product 
    assert "nutriscore" in valid_product 
    assert "generic_name" not in valid_product 
    assert "description" in valid_product
    assert "image_url" in valid_product
    assert "image_nutrition_url" in valid_product

def test_normalize_does_its_job_correctly(normalizer, valid_product):
    valid_product = {**valid_product, "energy_100g": 500.0}
    normalizer.normalize(valid_product)
    assert "energy_100g" not in valid_product
    assert valid_product['name'] == valid_product['name'].lower()
    assert len(valid_product['categories']) == 3
    assert "product_name" not in valid_product 
    assert "name" in valid_product 

def test_normalize_does_its_job_correctly(normalizer, valid_products):
    valid_products = deepcopy(valid_products)
    normalizer.normalize_all(valid_products)
    valid_product = valid_products[0]
    assert valid_product['name'] == valid_product['name'].lower()
    assert len(valid_product['categories']) == 3
    assert "product_name" not in valid_product 
    assert "name" in valid_product 