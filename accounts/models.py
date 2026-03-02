from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomeUser(AbstractUser):
    is_verified = models.BooleanField(null = False, blank= False)
    is_2FA_enabled = models.BooleanField(blank = True)
    is_active = models.BooleanField()
    ROLE_CHOICES = (
        ('admin''Admin'),
        ()
    )
    role = models.
