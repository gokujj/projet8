from django.contrib import admin
from django.urls import path

from .views import UserProfileView

app_name = 'profiles'

urlpatterns = [path('', UserProfileView.as_view(), name='user_profile')]
