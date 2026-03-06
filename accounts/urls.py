from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, LoginView, PasswordChangeView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name = "signup"),
    path("login/", LoginView.as_view(), name = "login" ),
    path("password_change/", PasswordChangeView.as_view(), name = "password_change"),
    path('reset/<uid64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name="password_reset_confirm")
]
