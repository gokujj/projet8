from django.urls import reverse
import pytest

pytestmark = pytest.mark.django_db(transaction=True)


def test_searchview_return_status_200_if_user_not_connected(client):
    response = client.get(reverse('products:search'))
    assert response.status_code == 200


def test_searchview_returns_status_200_if_user_connected(client, user):
    client.force_login(user)
    response = client.get(reverse('products:search'))
    assert response.status_code == 200


def test_searchview_returns_correct_template(client):
    response = client.get(reverse('products:search'))
    assert 'products/results.html' in response.template_name


def test_searchview_finds_three_substitutes(
    client, product_a, product_b, product_c, product_d, product_e
):
    response = client.get(
        reverse('products:search'), data={'search': product_d.name}
    )
    assert len(response.context_data['substitutes']) == 3
    assert product_a in response.context_data['substitutes']
    assert product_b in response.context_data['substitutes']
    assert product_c in response.context_data['substitutes']
    assert product_e not in response.context_data['substitutes']
    assert product_a == response.context_data['substitutes'][0]
    assert product_d == response.context_data['product']


def test_searchview_finds_no_substitutes(
    client, product_c, product_d, product_e
):
    response = client.get(
        reverse('products:search'), data={'search': product_c.name}
    )
    assert len(response.context_data['substitutes']) == 0
    assert product_d not in response.context_data['substitutes']
    assert product_e not in response.context_data['substitutes']
    assert product_c == response.context_data['product']


def test_productdetailview_returns_status_404_if_product_does_not_exist(
    client,
):
    response = client.get(reverse('products:details', kwargs={'pk': 1}))
    assert response.status_code == 404


def test_productdetailview_returns_status_200_if_product_exists(
    client, product_a
):
    response = client.get(reverse('products:details', kwargs={'pk': 6}))
    assert response.status_code == 200


def test_productdetailview_returns_correct_template(client):
    response = client.get(reverse('products:search'))
    assert 'products/results.html' in response.template_name