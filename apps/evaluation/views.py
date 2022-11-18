from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from apps.evaluation.models import Evaluation, Delivery
# Create your views here.

def asig_view(request):
	return render(request, 'evaluation/tasks.html')


def create_view(request):
    return render(request, 'evaluation/create-evaluation.html')


def evaluate_view(request):
	return render(request, 'evaluation/evaluate.html')

def result_evaluation_view(request):
	return render(request, 'evaluation/result_evaluacion.html')

def create_task_view(request):
	return render(request, 'evaluation/create-task.html')