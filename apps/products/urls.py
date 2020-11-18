from django.contrib import admin
from django.urls import path

from .views import SearchView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('substitutes/', SearchView.as_view(), name="search"),
    path('<int:pk>/', ProductDetailView.as_view(), name="details"),
]
