from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, LoginView, PasswordChangeView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name = "signup"),
    path("login/", LoginView.as_view(), name = "login" ),
    path("password_change/", PasswordChangeView.as_view(), name = "password_change"),
]
