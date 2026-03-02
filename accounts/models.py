from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    is_verified = models.BooleanField(null = False, blank= False)
    is_2FA_enabled = models.BooleanField(blank = True)
    is_active = models.BooleanField()
    class rolechoices(models.TextChoices):
     ADMIN = 'Admin'
     USER = 'User'
    role = models.CharField(max_length=10, choices=rolechoices, default='user')

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
