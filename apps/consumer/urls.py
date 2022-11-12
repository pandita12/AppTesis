from django.contrib import admin
from django.contrib.auth import views as auth_views
from apps.consumer.views import home_index, register, ProfileView, login_view, base_view, logout_view
from django.urls import include, path
from . import views

app_name = 'consumer'

urlpatterns = [
   path('', home_index, name='index'),
   path('login/', login_view, name='login'),
   path('logout/', logout_view, name='logout'),
   path('register/', register, name='register'),
   path('Inicio/', base_view, name='Inicio'),
   path('profile/', ProfileView.as_view(), name='profilepage'),



  ]
