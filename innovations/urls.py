from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_request, name='login'),
    path("logout_request", views.logout_request, name= "logout_request"),
    path('getInnovations', views.getInnovations, name='getInnovations'),
 


]