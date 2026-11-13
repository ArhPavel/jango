from django.urls import path
from .views import category_list, category_products, product_detail

app_name = 'catalog'

urlpatterns = [
    path('', category_list, name='category_list'),
    path('category/<int:pk>/', category_products, name='category_products'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
]