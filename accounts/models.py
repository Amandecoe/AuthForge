from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomeUser(AbstractUser):
    is_verified = models.BooleanField(null = False, blank= False)
    is_2FA_enabled = models.BooleanField(blank = True)
    is_active = models.BooleanField()
    ROLE_CHOICES = (
        ('admin''Admin'),
        ('user''User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

class email_verification_tokens(models.Model):
    user_id = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    
