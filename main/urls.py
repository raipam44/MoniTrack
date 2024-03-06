from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

# from .views import sign_up

urlpatterns = [

  
    path("", views.home, name="home"),
    path("sign-up/", views.sign_up, name="sign_up"),
    path('home/', views.home, name='home'),
    path('login/', views.log_in, name='log_in'),
    path('user/', views.user, name='user'),
    path('logout/', auth_views.LogoutView.as_view(), name='log_out'),
    path('profile/', views.profile, name = 'profile'),
    path('feedback/', views.feedback, name='feedback')


]
