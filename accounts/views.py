from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CustomUserCreationForm, CustomLoginView
from .models import CustomUser, Activity
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import JsonResponse
# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"


class LoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = CustomLoginView
    success_url = reverse_lazy("home")


class PasswordChangeView(PasswordChangeView):
    template_name = "registration/password_change_form.html"
    success_url = reverse_lazy("password_change_done")

#dashboard viewer
class DashboardView(LoginRequiredMixin,ListView):
    model = Activity
    template_name = "dashboard/home.html"
    context_object_name = "activities"

    def get_queryset(self):
        return Activity.objects.order_by('-timestamp')[:10]

#an api for endpoint for the activites by users
def recent_activity_api(request):
    activities = Activity.objects.order_by('-timestamp')[:4]
    data = []
    for activity in activities:
        data.append({
            "action":activity.action,
            "user": str(activity.user) if activity.user else "Unknown",
            "time": activity.timestamp.strftime("%H:%M:%S"),
        })

    return JsonResponse({"activities": data})
