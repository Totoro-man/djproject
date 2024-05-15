from django.urls import path

from catalog.apps import MyShopConfig
from catalog.views import index, contacts, product_info, catalog

app_name = MyShopConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product_info/', product_info, name='product_info'),
    path('catalog/', catalog, name='catalog'),
]