from django.contrib import admin
from django.urls import path

from .views import user_profile

app_name = 'profiles'

urlpatterns = [path('<int:user_id>/', user_profile, name='user_profile')]
