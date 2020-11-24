from django.urls import reverse


def test_homeview_returns_status_code_200(client):
    response = client.get(reverse('pages:home'))
    assert response.status_code == 200


def test_homeview_returns_correct_template(client):
    response = client.get(reverse('pages:home'))
    assert 'pages/home.html' in response.template_name


def test_legalview_returns_status_code_200(client):
    response = client.get(reverse('pages:legal'))
    assert response.status_code == 200


def test_legalview_returns_correct_template(client):
    response = client.get(reverse('pages:legal'))
    assert 'pages/legal.html' in response.template_name