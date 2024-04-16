from django.urls import path

from catalog.views import index, contacts, right_way

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('right_way/', right_way),
]