from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from .models import Activity

@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    Activity.objects.create(
        user = user,
        action = "login",
        ip_address = request.META.get("REMOTE_ADDR")
    )


