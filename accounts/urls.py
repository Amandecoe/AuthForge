from django.urls import path
from .views import SignUpView, LoginView, PasswordChangeView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name = "signup"),
    path("login/", LoginView.as_view(), name = "login" ),
    path("password_change/", PasswordChangeView.as_view(), name = "password_change"),
]
