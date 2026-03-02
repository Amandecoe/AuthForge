from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
        )

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if not first_name:
            raise forms.ValidationError("First Name is Required")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if not last_name:
            raise forms.ValidationError("Last Name is Required")
        return last_name
class CustomLoginView(AuthenticationForm):
    username = forms.EmailField(label = "Email", widget = forms.EmailInput(attrs = {
        "placeholder":"Enter Your Email"
    }))
