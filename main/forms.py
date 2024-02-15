#forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    student_number = forms.CharField(max_length=50, required=True)
    section = forms.ChoiceField(choices=[
        ('C1', 'C1'),
        ('C2', 'C2'),
        ('C3', 'C3'),
        ('C4', 'C4'),
        ('C5', 'C5'),
        ('C6', 'C6'),
        ('C7', 'C7'),
        ('C8', 'C8'),
    ], required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'password1',
                  'password2', 'student_number', 'section']  # Exclude the user field
