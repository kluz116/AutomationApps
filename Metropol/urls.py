from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_request, name='login'),
    path("logout_request", views.logout_request, name= "logout_request"),
    path('addCap', views.addCap, name='addCap'),
    path('pdfReport', views.pdfReport, name='pdfReport'),
    path('generateReport', views.generateReport, name='generateReport'),
    path('getCap',views.getCap,name='getCap'),
    path('updateCap/<int:id>/',views.updateCap,name='updateCap'),
    path('get_pdfreport',views.get_pdfreport,name='get_pdfreport'),

    path('Identity', views.Identity, name='Identity'),
    path('getIdentityDetails', views.getIdentityDetails, name='getIdentityDetails'),
    path('addNimble', views.addNimble, name='addNimble'),
    path('addBranch', views.addBranch, name='addBranch'),
    path('getBranches', views.getBranches, name='getBranches'),
    path('addBoucode', views.addBoucode,name='addBoucode')

]