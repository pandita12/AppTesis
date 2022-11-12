from django.contrib import admin
from apps.evaluation.views import  asig_view
from django.urls import include, path

app_name = 'evaluation'

urlpatterns = [
   path('<pk>/task/', asig_view, name="task"),
]
