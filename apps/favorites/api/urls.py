from django.urls import path
from .views import FavoriteListApiView, FavoriteApiView

app_name = 'favorites_api'

urlpatterns = [
    path('', FavoriteListApiView.as_view(), name="list"),
    path(
        '<int:pk>/',
        FavoriteApiView.as_view(),
        name="detail",
    ),
]
