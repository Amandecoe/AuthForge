from .models import UserProfile
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import PasswordChangeForm
class ProfileEditing(ModelForm):
    class Meta:
        model = UserProfile
        fields = ("full_name","profile_picture","username","email","bio","phone_number" )

class ChangePassword(PasswordChangeForm):
    class Meta:
        model=UserProfile
