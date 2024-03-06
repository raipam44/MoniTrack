from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_out
from .models import update_session_signal


@receiver(user_logged_out)
def update_session_on_logout(sender, user, request, **kwargs):
    print(f"Signning out the {request.user}")
    update_session_signal(user)
    