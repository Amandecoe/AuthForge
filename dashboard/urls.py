from django.urls import path
from .views import HomePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("home/",HomePageView.as_view(), name = "home"),
]
