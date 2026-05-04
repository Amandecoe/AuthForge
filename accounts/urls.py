from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, LoginView, PasswordChangeView, recent_activity_api

urlpatterns = [
    path("signup/", SignUpView.as_view(), name = "signup"),
    path("login/", LoginView.as_view(), name = "login" ),
    path("password_change/", PasswordChangeView.as_view(), name = "password_change"),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path ("api/activity/", recent_activity_api, name="activity_api")
]
