from django.urls import resolve

from pages.views import HomeView, LegalView


def test_url_resolves_to_homeview():
    view = resolve('/')
    assert view.func.view_class == HomeView


def test_url_resolves_to_legalview():
    view = resolve('/mentions-legales/')
    assert view.func.view_class == LegalView