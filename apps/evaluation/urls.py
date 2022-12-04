from django.contrib import admin
from apps.evaluation.views import  asig_view, EvaluationView, evaluate_view, result_evaluation_view, create_task_view
from django.urls import include, path

app_name = 'evaluation'

urlpatterns = [
   
   #Urls Estudiante
   path('task/', asig_view, name="task"),
   path('create-task/', create_task_view, name="create-task"),
   path('result-evaluativo/', result_evaluation_view, name="result_evaluacion"),

   #Urls Profesor
   path('<pk>/create-evaluation/', EvaluationView.as_view(), name="create-evaluation"),
   path('<pk>/check-evaluation/', evaluate_view, name="evaluate"),
]
