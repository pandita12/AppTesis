from django.contrib import admin
from apps.evaluation.views import  asig_view, create_view
from django.urls import include, path

app_name = 'evaluation'

urlpatterns = [
   path('<pk>/task/', asig_view, name="task"),
   path('create-evaluation/', create_view, name="create-evaluation"),
]
