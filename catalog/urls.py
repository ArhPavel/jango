from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts

app_name = CatalogConfig.name

urlpatterns = [
    # Главная страница (Каталог)
    path('', home, name='index'),

    # Страница контактов
    path('contacts/', contacts, name='contacts'),
]