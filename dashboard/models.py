from django.db import models
from django.conf import settings
from accounts.models import CustomUser
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    profile_picture = models.ImageField(null=True, blank=True)
    bio = models.TextField(max_length=200, default = "User Here")
    phone_number = models.PositiveSmallIntegerField(blank=True , default = +251)
    last_seen = models.DateTimeField(blank=True, null=True)

class AccountsActivity(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    action = models.CharField(max_length=50)
    class Meta:
        db_table = "accounts_activity"
        managed = False
