from django.contrib import admin
from apps.consumer.views import home_index, register, StudentView, TeacherView, ModeratorView, login_view, base_view, logout_view
from django.urls import include, path
from . import views

app_name = 'consumer'

urlpatterns = [
   path('', home_index, name='index'),
   path('login/', login_view, name='login'),
   path('logout/', logout_view, name='logout'),
   path('register/', register, name='register'),
   path('base/', base_view, name='base'),
   path('studentpage/', StudentView.as_view()),
   path('teacherpage/', TeacherView.as_view()),
   path('moderatorpage/', ModeratorView.as_view()),
  ]
