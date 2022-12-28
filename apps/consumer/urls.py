from django.contrib import admin
from apps.consumer.views import home_index, register, ProfileView, login_view, base_view, logout_view
from django.urls import include, path
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from . import views

app_name = 'consumer'

urlpatterns = [
   path('', home_index, name='index'),
   path('login/', login_view, name='login'),
   path('logout/', logout_view, name='logout'),
   path('register/', register, name='register'),
   path('Inicio/', base_view, name='Inicio'),
   path('profile/', ProfileView.as_view(), name='profilepage'),


   #Resset password email
   
   path('reset_password/', views.password_reset_request, name='reset_password'),

   path('password_reset/done/', PasswordResetDoneView.as_view(template_name='account/password_reset/password_reset_done.html'), name='password_reset_done'),
   path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view
      (template_name="account/password_reset/password_reset_confirm.html",
         success_url=reverse_lazy("consumer:password_reset_complete")), 
      name='password_reset_confirm'),
   path('reset/done/', PasswordResetCompleteView.as_view
      (template_name='account/password_reset/password_reset_complete.html'), 
      name='password_reset_complete'), 

  ]
