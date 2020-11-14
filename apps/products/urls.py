from django.contrib import admin
from django.urls import path

from .views import search

app_name = 'products'

urlpatterns = [path('substitutes/', search, name="search")]
