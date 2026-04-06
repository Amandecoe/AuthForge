from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms
class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(label = "full_name", max_length=255)
    email = forms.EmailField(label = "email")
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password1',
            'password2',
        ) + ("full_name",)
class CustomLoginView(AuthenticationForm):
    username = forms.EmailField(label = "Email", widget = forms.EmailInput(attrs = {
        "placeholder":"Enter Your Email"
    }))
