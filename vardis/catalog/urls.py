from django.urls import path
from .views import *

urlpatterns = [
    path('catalog/<slug:catalog_slug>', CategoryList.as_view(), name='catalog'),
    path('category/<slug:product_category_slug>', ProductList.as_view(), name='product_category'),
    path('product/<slug:product_slug>', ShowProduct.as_view(), name='product'),
]
