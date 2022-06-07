from django.contrib import admin

from apps.lesson.views import index_lesson
from django.urls import include, path

app_name = 'lesson'

urlpatterns = [
   path('index/', index_lesson),
]
