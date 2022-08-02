from django.contrib import admin
from apps.consumer.views import home_index, register, student_view, teacher_view, moderator_view, login_view, base_view
from django.urls import include, path
from . import views

app_name = 'consumer'

urlpatterns = [
   path('', home_index, name='index'),
   path('login/', login_view, name='login'),
   path('register/', register, name='register'),
   path('base/', base_view, name='base'),
   path('studentpage/', student_view, name='studentpage'),
   path('teacherpage/', teacher_view, name='teacherpage'),
   path('moderatorpage/', moderator_view, name='moderatorpage'),
  ]
