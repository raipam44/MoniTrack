from django.contrib import admin
from .models import CustomUser, UserSession
# Register your models here.

class UserSessionInline(admin.TabularInline):  # Use TabularInline for a more compact display
    model = UserSession
    extra = 0  # Number of empty forms to display (0 to hide them if no sessions exist)

class CustomUserAdmin(admin.ModelAdmin):
    inlines = [UserSessionInline]



admin.site.register(CustomUser)
admin.site.register(UserSession)
