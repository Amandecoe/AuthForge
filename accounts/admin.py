from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = [
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_2FA_enabled",
    ]


admin.site.register(CustomUser,CustomUserAdmin)
