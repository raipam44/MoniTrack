#models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    student_number = models.CharField(unique=True, max_length=50)
    section = models.CharField(max_length=50)


class UserSession(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    login_time = models.DateTimeField(default=timezone.now)
    logout_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    
    
def create_session(user):
        print(f"Creating session for user {user}")
        UserSession.objects.create(user=user)
        
def update_session(user):
        print(f"Updating session for user {user}")
        session = UserSession.objects.filter(user=user, logout_time__isnull=True).first()
        if session:
            session.logout_time = timezone.now()
            session.duration = session.logout_time - session.login_time
            session.save()