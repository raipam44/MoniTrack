# views.py
from datetime import timedelta
from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from .models import *
from django.contrib import messages


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
         return HttpResponseRedirect('/user')
    
    return render(request, 'home/home.html')


def log_in(request):
    
    
    if request.user.is_authenticated:
         return HttpResponseRedirect('/user')
    
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(f"Logging in {user}")
            login(request, user)

            error_message = create_session(request.user)

            if error_message:
                messages.error(request, error_message)
                print(f"Error creating session: {error_message}")
            else:
                print("Session created successfully")

            return redirect('/user')

    return render(request, 'registration/login.html')

def user(request):

    if request.user.is_authenticated:
        
        session = UserSession.objects.filter(user=request.user, logout_time__isnull=True).last()
        context = {
        
            'login_date': session.login_time if session else None,
        }
        return render(request, 'home/user.html', context)
    return redirect('/home')



def log_out(request):
    print(f"Signning out the {request.user}")
    if request.user.is_authenticated:
        update_session(request.user)  # Update the session record
        logout(request)
   

    return redirect('/home')



