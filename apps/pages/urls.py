from django.contrib import admin
from django.urls import path

from .views import HomeView, LegalView

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('mentions-legales/', LegalView.as_view(), name="legal"),
]