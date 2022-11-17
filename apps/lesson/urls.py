from django.contrib import admin

from apps.lesson.views import index_lesson, detail_lesson, classroom_index
from django.urls import include, path

app_name = 'lesson'

urlpatterns = [
   path('index/', index_lesson),
   path('<pk>/detail/', detail_lesson, name="detail"),
   path('<pk>/classroom/detail/',classroom_index, name="classroom_index"),
]
