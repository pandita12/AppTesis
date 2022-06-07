from django.contrib import admin

from apps.teacherbot.views import index_teacherbot
from django.urls import include, path

app_name = 'teacherbot'

urlpatterns = [
   path('index/', index_teacherbot),
]
