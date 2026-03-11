from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from .models import UserProfile
# Create your views here.
User = get_user_model()
class HomePageView(TemplateView):
    template_name = "dashboard/home.html"

class UserPageView(ListView):
    model = UserProfile
    template_name = "dashboard/users.html"
    context_object_name = "users" #used to loop through the template

    def get_queryset(self): #orders the users with date joined
        return User.objects.all().order_by('-date_joined')
