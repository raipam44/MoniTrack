from django.urls import path, include
from . import views

# from .views import sign_up

urlpatterns = [

    # path("register", views.register_user, name="register_user"),
    path("", views.home, name="home"),
    path("sign-up", views.sign_up, name="sign_up"),
    path('home', views.home, name='home'),
    path('login', views.log_in, name='log_in'),
    path('user', views.user, name='user'),
    path('logout/', views.log_out, name = 'log_out')


]
