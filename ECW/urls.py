from django.urls import path
import ecw.views as views


urlpatterns = [

    path('', views.login_request, name='login'),
    path("logout_request_metropol", views.logout_request_metropol, name= "logout_request_metropol"),
    path('getIndex', views.getIndex, name='getIndex'),
]