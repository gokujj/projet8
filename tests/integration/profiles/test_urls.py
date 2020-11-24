from django.urls import resolve

from profiles.views import UserProfileView


def test_root_url_resolves_to_userprofileview():
    view = resolve('/users/')
    assert view.func.view_class == UserProfileView