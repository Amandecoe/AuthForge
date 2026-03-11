from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
from .models import UserProfile
# Create your views here.
User = get_user_model()
class HomePageView(TemplateView):
    template_name = "dashboard/home.html"

class UserPageView(DetailView):
    model = UserProfile
    template_name = "dashboard/home.html"
