from .models import UserProfile
from django import forms
from django.forms import ModelForm

class ProfileEditing(ModelForm):
    class Meta:
        model = UserProfile
        fields = ("full_name","profile_picture","username","email","bio","phone_number" )

class ChangePassword()
