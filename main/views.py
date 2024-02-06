# views.py
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from .models import *


def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # print(request.POST)
            # print(form.errors)
            login(request, user)  # Redirect to a success page
            create_session(request.user) 
            return redirect('/home')
    else:
        form = CustomUserCreationForm()
    # print(form.errors)
    # print(request.POST)
    return render(request, 'registration/sign_up.html', {'form': form})


def home(request):
    
    if request.user.is_authenticated:
         return render(request, 'home/user.html')
    
    return render(request, 'home/home.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f"Logging in {user}")
            login(request, user)
            create_session(request.user)  # Create a session record
            return redirect('/home')
    return render(request, 'registration/login.html')

def user(request):

    if request.user.is_authenticated:
         return render(request, 'home/user.html')
    return redirect('/home')



def log_out(request):
    print(f"Signning out the {request.user}")
    if request.user.is_authenticated:
        update_session(request.user)  # Update the session record
        logout(request)
    return redirect('/home')

