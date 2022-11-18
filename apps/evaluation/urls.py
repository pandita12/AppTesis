from django.contrib import admin
from apps.evaluation.views import  asig_view, create_view, evaluate_view, result_evaluation_view, create_task_view
from django.urls import include, path

app_name = 'evaluation'

urlpatterns = [
   path('task/', asig_view, name="task"),
   path('create-task/', create_task_view, name="create-task"),
   path('create-evaluation/', create_view, name="create-evaluation"),
   path('check-evaluation/', evaluate_view, name="evaluate"),
   path('result-evaluativo/', result_evaluation_view, name="result_evaluacion"),
]
