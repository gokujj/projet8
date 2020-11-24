from django.urls import reverse
import pytest

pytestmark = pytest.mark.django_db(transaction=True)


def test_userprofileview_returns_status_302_if_not_connected(client):
    response = client.get(reverse('profiles:user_profile'))
    assert response.status_code == 302


def test_userprofileview_redirects_to_homepage_if_not_connected(client):
    response = client.get(reverse('profiles:user_profile'))
    assert response['Location'] == reverse('account_login') + '?next=/users/'


def test_userprofileview_returns_status_200_if_connected(client, user):
    client.force_login(user)
    response = client.get(reverse('profiles:user_profile'))
    assert response.status_code == 200


def test_userprofileview_returns_user_profile_template_if_connected(
    client, user
):
    client.force_login(user)
    response = client.get(reverse('profiles:user_profile'))
    assert 'profiles/user_profile.html' in response.template_name
