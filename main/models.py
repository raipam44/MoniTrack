#models.py
from datetime import datetime, time
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render
from django.utils import timezone
from django.utils.timezone import now




 

def get_user_profile_pic_path(instance, filename):
    # Generate a unique filename with timestamp
    extension = filename.split('.')[-1]
    filename = f'{instance.username}_{now().strftime("%Y%m%d_%H%M%S")}.{extension}'
    return f'profile_pics/{instance.username}/{filename}'

class CustomUser(AbstractUser):
    student_number = models.CharField(unique=True, max_length=50)
    section = models.CharField(max_length=3)
    profile_pic = models.ImageField(upload_to=get_user_profile_pic_path, null=True, blank=True)
    
    def __str__(self) -> str:
          return f"{self.id} : {self.last_name} {self.first_name} ({self.section})"            
    

 

class UserSession(models.Model):
    
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = "session")
    login_time = models.DateTimeField(default=timezone.now)
    logout_time = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
 
    def __str__(self):
        return f"{self.user.last_name} ({self.user.section})" 
    


class UserRecord(models.Model):

        user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = "record")
        date = models.DateTimeField(default=timezone.now)


  
 
def create_session(user):
    
    
    print(f"Creating session for user {user}")
    UserSession.objects.create(user=user)
    
    section_time_mapping = {
        'C1': (time(13, 0), time(14, 0)),
        'C2': (time(14, 0), time(15, 0)),
        'C3': (time(13, 0), time(14, 30)),
        'C4': (time(13, 0), time(15, 0)),
        # Add similar mappings for other sections
    }

    current_time = datetime.now().time()
    section = user.section

    if section in section_time_mapping:
        start_time, end_time = section_time_mapping[section]
        if not (start_time <= current_time <= end_time):
            return f"Sorry, the {section} section is only available between {start_time} and {end_time}."

   
    return None
  
def update_session(user):
        print(f"Updating session for user {user}")
        session = UserSession.objects.filter(user=user, logout_time__isnull=True).last()
        if session:
            session.logout_time = timezone.now()
            session.duration = session.logout_time - session.login_time
            session.save()