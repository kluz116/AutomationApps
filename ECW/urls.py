from django.urls import path
import ecw.views as views


urlpatterns = [
    path('', views.login_request, name='login'),
    path("logout_request_metropol", views.logout_request_metropol, name= "logout_request_metropol"),
    path('getIndex', views.getIndex, name='getIndex'),
    path('addDeposit', views.addDeposit, name='addDeposit'),
    path('addAccountHolder', views.addAccountHolder, name='addAccountHolder'),
    path('getDeposits',views.getDeposits,name='getDeposits'),
    path('getAccountHolders',views.getAccountHolders,name='getAccountHolders'),

]