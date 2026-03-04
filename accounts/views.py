from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, CustomLoginView, PasswordChangeView
from .models import CustomUser
from django.contrib.auth.views import LoginView
# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class LoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = CustomLoginView

class PasswordChange(PasswordChangeView):
    form_class = PasswordChangeView
    template_name = "password_change_form.html"
    success_url = reverse_lazy("password_change_done")
