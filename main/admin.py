from django.contrib import admin
from .models import CustomUser, UserSession
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "section", "student_number")

    

class UserSessionAdmin(admin.ModelAdmin):
    list_display = ("user", "login_time", "logout_time", "duration")







admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserSession, UserSessionAdmin)

