# api/urls.py
from django.urls import path
from .views import ItemList
from . import views

urlpatterns = [
    path('paymentinstruction/', views.item_list, name='item_list'),
    path('paymentinstruction/', ItemList.as_view(), name='item-list'),
]