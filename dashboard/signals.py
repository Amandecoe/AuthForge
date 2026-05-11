from .models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save)
def create_profile(sender, request, user, **kwargs):
    UserProfile.objects.create(
        user = user,
        action = "signup"
    )
