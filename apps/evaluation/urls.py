from django.contrib import admin

from apps.evaluation.views import index_evaluation
from django.urls import include, path

app_name = 'evaluation'

urlpatterns = [
   path('index/', index_evaluation),
]
