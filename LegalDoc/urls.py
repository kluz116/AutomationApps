from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_request, name='login'),
    path("logout_request", views.logout_request, name= "logout_request"),
    path('getCustomers',views.getCustomers, name='getCustomers'),
    path('getBranches',views.getBranches, name='getBranches'),
    path('addBranch', views.addBranch, name='addBranch'),
    path('addCustomer', views.addCustomer, name='addCustomer'),
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
    path('sendForMortgage/<int:id>/', views.sendForMortgage, name='sendForMortgage'),
    path('sentForFurtherCharges/<int:id>/', views.sentForFurtherCharges, name='sentForFurtherCharges'),
    path('security_status', views.security_status, name='security_status'),
    path('landtitle', views.landtitle, name='landtitle'),






]