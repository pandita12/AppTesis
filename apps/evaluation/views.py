from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.evaluation.models import Evaluation, Delivery
from .forms import CreateEvaluationForm
from django.views import View
from django.urls import reverse
from apps.lesson.models import Classroom
# Create your views here.

def asig_view(request):
	return render(request, 'evaluation/tasks.html')


class EvaluationView(View):
	def get(self,request, *args, **kwargs):
		context = {
			"form":CreateEvaluationForm
		}
		return render(request, 'evaluation/create-evaluation.html', context)
	def post(self,request, *args, **kwargs):
		form = CreateEvaluationForm(request.POST,request.FILES)
		if form.is_valid():
			evaluation = form.save(commit=False)
			evaluation.classroom_id = Classroom.objects.get(pk=self.kwargs.get('pk')
)
			evaluation.save()
			return redirect(reverse('lesson:classroom_index',kwargs={"pk":self.kwargs.get('pk')}))
		context = {
			"form":form
		}
		return render(request, 'evaluation/create-evaluation.html', context)

def evaluate_view(request, pk):
	deliverys = Delivery.objects.filter(evaluation_id__classroom_id__pk=pk)
	context = {
		"deliverys":deliverys
	}
	return render(request, 'evaluation/evaluate.html', context)

def result_evaluation_view(request):
	return render(request, 'evaluation/result_evaluacion.html')

def create_task_view(request):
	return render(request, 'evaluation/create-task.html')