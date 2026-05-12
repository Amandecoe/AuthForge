from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.db.models import Count, Max
from django.utils import timezone
from datetime import timedelta
from .models import Activity
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

class ProfilePageView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = "dashboard/profile.html"
    context_object_name = "profile"

    def get_object(self):
        return self.request

@login_required
def profile_data(request):
    profile = request.user.userprofile #access the UserProfile data of the user that requested the data through the one to one relationship UserProfile has with user

    data = {
        "Username" : request.user.username,
        "Email": request.user.email,
        "bio": profile.bio,
        "FullName": request.user.full_name,
        "Phone_Number": profile.phone_number,
        "Last_Login": request.user.last_login,
    }

    return JsonResponse(data)

class PasswordChangeView(PasswordChangeView):
    template_name = "registration/password_change_form.html"
    success_url = reverse_lazy("password_change_done")

@login_required
def account_status(request):
    activity = Activity.objects.filter(
        user = request.user,
        action = "login",
        )

    stats = activity.aggregate(
        login_count = Count("id"),
        last_login = Max("timestamp")
    )
