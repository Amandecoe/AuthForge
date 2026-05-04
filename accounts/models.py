from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    is_2FA_enabled = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class RoleChoices(models.TextChoices):
        ADMIN = "Admin", "Admin"
        USER = "User", "User"

    role = models.CharField(
        max_length=10,
        choices=RoleChoices.choices,
        default=RoleChoices.USER
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
class email_verification_tokens(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True) #runs once when token is created
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(blank=False)

class password_reset_tokens(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(blank=False)

#stores user activites in the system
class Activity(models.Model):
    ACTION_CHOICES =[
        ("login", "Login"),
        ("logout", "Logout"),
        ("signup", "Signup"),
        ("password_change", "Password Change"),
        ("login_failed", "Login Failed"),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address=models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.action}"
