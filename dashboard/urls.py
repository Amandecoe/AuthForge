from django.urls import path
from .views import HomePageView, UserPageView, ProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("home/",HomePageView.as_view(), name = "home"),
    path("users/",UserPageView.as_view(), name = "users"),
    path ("profile/", ProfilePageView.as_view(), name = "profile")
]
