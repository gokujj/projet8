from django.urls import resolve

from favorites.views import FavoriteListView
from favorites.api.views import FavoriteListApiView, FavoriteApiView


def test_url_resolves_to_favoritelistview():
    view = resolve('/favorites/')
    assert view.func.view_class == FavoriteListView


def test_url_resolves_to_favoritelistapiview():
    view = resolve('/api/favorites/')
    assert view.func.view_class == FavoriteListApiView


def test_url_resolves_to_favoriteapiview():
    view = resolve('/api/favorites/1/')
    assert view.func.view_class == FavoriteApiView