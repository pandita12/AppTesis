from django.contrib import admin
from apps.evaluation.views import  asignament_view, EvaluationView, evaluate_view, SendtaskView, ObservationView, CorrectionView, delete, moderator_view, moderator_result
from django.urls import include, path
from . import views


app_name = 'evaluation'

urlpatterns = [
   
   #Urls Estudiante
   path('<pk>/asignament/', asignament_view, name="asignament"),
   path('<pk>/send-task/', SendtaskView.as_view(), name="send-task"),
   #path('result-evaluativo/', list_result, name="result-evaluation"),

   #Urls Profesor
   path('<pk>/create-evaluation/', EvaluationView.as_view(), name="create-evaluation"),
   path('<pk>/check-evaluation/', evaluate_view, name="evaluate"),
   path('<pk>/observation-evaluation/', ObservationView.as_view(), name="observation"),
   path('<pk>/correction-evaluation/', CorrectionView.as_view(), name="correction"),
   path('<pk>/delete/',views.delete, name="delete"),

   #Urls Moderator
   path('<pk>/moderator/', moderator_view, name="moderator"),
   path('<pk>/moderator-resultados/', moderator_result, name='moderator-result'),
]
