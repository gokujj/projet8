from django.urls import reverse
import pytest

pytestmark = pytest.mark.django_db(transaction=True)


def test_favoritelistview_returns_status_code_200_if_connected(client, user):
    client.force_login(user)
    response = client.get(reverse('favorites:list'))
    assert response.status_code == 200


def test_favoritelistview_returns_correct_template_if_connected(client, user):
    client.force_login(user)
    response = client.get(reverse('favorites:list'))
    assert 'favorites/list.html' in response.template_name


def test_favoritelistview_returns_status_code_302_if_not_connected(client):
    response = client.get(reverse('favorites:list'))
    assert response.status_code == 302


def test_favoritelistview_redirects_to_login_if_not_connected(client):
    response = client.get(reverse('favorites:list'))
    assert (
        response['Location']
        == f"{reverse('account_login')}?next={reverse('favorites:list')}"
    )


def test_favoritelistapiview_returns_status_code_302_if_not_connected(client):
    response = client.post(reverse('favorites_api:list'))
    assert response.status_code == 302


def test_favoritelistapiview_returns_status_code_404_if_invalid_data(
    client, user, product_a
):
    client.force_login(user)
    response = client.post(
        reverse('favorites_api:list'),
        data={'product': product_a.id, 'substitute': 11},
    )
    assert response.status_code == 404


def test_favoritelistapiview_returns_status_code_201_if_favorite_created(
    client, user, product_a, product_b
):

    client.force_login(user)
    response = client.post(
        reverse('favorites_api:list'),
        data={'product': product_b.id, 'substitute': product_a.id},
    )
    assert response.status_code == 201


def test_favoritelistapiview_returns_status_code_200_if_favorite_already_exists(
    client, user, product_a, product_b
):

    client.force_login(user)
    client.post(
        reverse('favorites_api:list'),
        data={'product': product_b.id, 'substitute': product_a.id},
    )
    # second creation
    response = client.post(
        reverse('favorites_api:list'),
        data={'product': product_b.id, 'substitute': product_a.id},
    )
    assert response.status_code == 200


def test_favoritelistapiview_returns_json_response_if_connected_and_valid_data(
    client, user, product_a, product_b
):
    client.force_login(user)
    response = client.post(
        reverse('favorites_api:list'),
        data={'product': product_b.id, 'substitute': product_a.id},
    )
    assert response['Content-Type'] == 'application/json'


def test_favoritelistapiview_returns_not_allowed_if_requested_with_get(
    client, user
):
    client.force_login(user)
    response = client.get(reverse('favorites_api:list'))
    assert response.status_code == 405


def test_favoriteapiview_returns_status_302_if_not_connected(
    client, first_favorite
):
    response = client.delete(
        reverse('favorites_api:detail', kwargs={'pk': first_favorite.id})
    )
    assert response.status_code == 302


def test_favoriteapiview_redirects_to_login_if_not_connected(
    client, first_favorite
):
    url = reverse('favorites_api:detail', kwargs={'pk': first_favorite.id})
    response = client.delete(url)
    assert response['Location'] == f"{reverse('account_login')}?next={url}"


def test_favoriteapiview_returns_404_if_favorite_does_not_exist(client, user):
    client.force_login(user)
    url = reverse('favorites_api:detail', kwargs={'pk': 7777})
    response = client.delete(url)
    assert response.status_code == 404


def test_favoriteapiview_returns_not_allowed_if_requested_with_get(
    client, user
):
    client.force_login(user)
    url = reverse('favorites_api:detail', kwargs={'pk': 1})
    response = client.get(url)
    assert response.status_code == 405


def test_favoriteapiview_returns_not_allowed_if_requested_with_post(
    client, user
):
    client.force_login(user)
    url = reverse('favorites_api:detail', kwargs={'pk': 1})
    response = client.post(url)
    assert response.status_code == 405


def test_favoriteapiview_returns_returns_not_allowed_if_requested_with_post():
    pass


def test_favoriteapiview_returns_status_204_if_favorite_deleted():
    pass