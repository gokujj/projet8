from django.contrib import admin
from django.urls import path

from .views import user_favorites

app_name = 'favorites'

urlpatterns = [path('<int:user_id>/', user_favorites, name="user_favorites")]
