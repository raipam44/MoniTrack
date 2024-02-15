# middleware.py

from django.utils import timezone
from django.contrib.sessions.models import Session
from django.conf import settings

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Update the session timeout on every request
            request.session.set_expiry(settings.SESSION_COOKIE_AGE)
        return self.get_response(request)
