from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_request, name='login'),
    path("logout_request_legal", views.logout_request_legal, name= "logout_request_legal"),
    path('getCustomers',views.getCustomers, name='getCustomers'),
    path('getBranchesLegal',views.getBranchesLegal, name='getBranchesLegal'),
    path('addBranchLegal', views.addBranchLegal, name='addBranchLegal'),
    path('addCustomerNimble', views.addCustomerNimble, name='addCustomerNimble'),
    path('getSecurityType', views.getSecurityType, name='getSecurityType'),
    path('addSecurityType', views.addSecurityType, name='addSecurityType'),
    path('addSecurityStatus', views.addSecurityStatus, name='addSecurityStatus'),
    path('getSecurityStatus', views.getSecurityStatus, name='getSecurityStatus'),
    path('addLandTitleType', views.addLandTitleType, name='addLandTitleType'),
    path('addContract', views.addContract, name='addContract'),
    path('getLandTitleType', views.getLandTitleType, name='getLandTitleType'),
    path('addSecurity', views.addSecurity, name='addSecurity'),
    path('getSecurity', views.getSecurity, name='getSecurity'),
    path('getContracts', views.getContracts, name='getContracts'),
    path('updateSecurity/<int:id>/', views.updateSecurity, name='updateSecurity'),
    path('updateCustomer/<int:id>/', views.updateCustomer, name='updateCustomer'),
    path('updateContract/<int:id>/', views.updateContract, name='updateContract'),
    path('security_detail/<int:id>/', views.security_detail, name='security_detail'),
    path('withdrawSecurity/<int:id>/', views.withdrawSecurity, name='withdrawSecurity'),
    path('uploadSecurity/<int:id>/', views.uploadSecurity, name='uploadSecurity'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('download_contract/<int:file_id>/', views.download_contract_file, name='download_contract_file'),
    path('sendForMortgage/<int:id>/', views.sendForMortgage, name='sendForMortgage'),
    path('sentForFurtherCharges/<int:id>/', views.sentForFurtherCharges, name='sentForFurtherCharges'),
    path('security_status', views.security_status, name='security_status'),
    path('landtitle', views.landtitle, name='landtitle'),
    path('addUsers', views.addUsers, name='addUsers'),
    path('getUsers', views.getUsers, name='getUsers'),
    path('addGroup', views.addGroup, name='addGroup'),
    path('change-password/', views.change_password, name='change_password'),
    










]