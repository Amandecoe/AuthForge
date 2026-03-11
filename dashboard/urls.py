from django.urls import path
from .views import HomePageView, UserPageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("home/",HomePageView.as_view(), name = "home"),
    path("users/",UserPageView.as_view(), name = "users" )
]
