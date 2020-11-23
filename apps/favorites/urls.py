from django.contrib import admin
from django.urls import path

from .views import FavoriteListView

app_name = 'favorites'

urlpatterns = [
    path('', FavoriteListView.as_view(), name="list"),
]
