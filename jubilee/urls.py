from django.urls import path
from . import views

urlpatterns = [

    path('postTransactionsDebit', views.postTransactionsDebit, name='postTransactionsDebit'),
    path('postTransactionsCredit', views.postTransactionsCredit, name='postTransactionsCredit'),
    path('addTransactions', views.addTransactions, name='addTransactions'),
    path('getTransactions', views.getTransactions, name='getTransactions'),
    path('GetAccountCustomer', views.GetAccountCustomer, name='GetAccountCustomer'),



]
