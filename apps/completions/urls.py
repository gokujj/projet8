from django.urls import path

from .views import ProductsCompletionView

app_name = 'completions'

urlpatterns = [
    path('products/', ProductsCompletionView.as_view(), name='products')
]
