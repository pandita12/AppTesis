from django.contrib import admin
from apps.evaluation.views import  asignament_view, EvaluationView, evaluate_view, result_evaluation_view, send_task_view
from django.urls import include, path

app_name = 'evaluation'

urlpatterns = [
   
   #Urls Estudiante
   path('asignament/', asignament_view, name="asignament"),
   path('send-task/', send_task_view, name="send-task"),
   path('result-evaluativo/', result_evaluation_view, name="result_evaluacion"),

   #Urls Profesor
   path('<pk>/create-evaluation/', EvaluationView.as_view(), name="create-evaluation"),
   path('<pk>/check-evaluation/', evaluate_view, name="evaluate"),
]
