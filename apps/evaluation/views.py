from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.evaluation.models import Evaluation, Delivery, Observation, DeliveryPonderation
from .forms import CreateEvaluationForm, ObservationForm, PonderationForm, SendTaskForm
from django.views import View
from django.views.generic import DeleteView, ListView
from django.urls import reverse
from apps.lesson.models import Classroom
from django.urls import reverse_lazy
# Create your views here.

def asignament_view(request, pk):
	evaluations = Evaluation.objects.filter(classroom_id=pk)
	deliverys_pending = Delivery.objects.filter(evaluation__classroom_id__pk=pk, ponderation__isnull=True,student=request.user.pk)
	deliverys_complete = Delivery.objects.filter(evaluation__classroom_id__pk=pk,ponderation__isnull=False,student=request.user.pk)	
	context = {
		"deliverys_pending":deliverys_pending,
	    "deliverys_complete":deliverys_complete,
	    "evaluations":evaluations
	}

	return render(request, 'evaluation/asignament/assignament.html', context)


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


def delete(request, pk):
	deliverys = Delivery.objects.get(id=pk)
	context = {
		"deliverys":deliverys
	}
	deliverys.delete()
	return render(request, 'base/base_system.html', context)



def evaluate_view(request, pk):
	deliverys_pending = Delivery.objects.filter(evaluation_id__classroom_id__pk=pk, ponderation__isnull=True)
	deliverys_complete = Delivery.objects.filter(evaluation_id__classroom_id__pk=pk,ponderation__isnull=False)
	context = {
		"deliverys_pending":deliverys_pending,
	    "deliverys_complete":deliverys_complete
	}
	return render(request, 'evaluation/check-resultado/check-resultado.html', context)


class SendtaskView(View):
	def get(self,request, *args, **kwargs):
		context = {
			"form":SendTaskForm
		}
		return render(request, 'evaluation/send-task/send-task.html', context)
	def post(self,request, *args, **kwargs):
		form = SendTaskForm(request.POST,request.FILES)
		if form.is_valid():
			deliverys = form.save(commit=False)
			deliverys.student = request.user
			deliverys.evaluation = Evaluation.objects.get(pk=self.kwargs.get('pk')
)
			deliverys.save()
			return redirect(reverse('lesson:detail',kwargs={"pk":self.kwargs.get('pk')}))
		context = {
			"form":form
		}
		return render(request, 'evaluation/send-task/send-task.html', context)



class ObservationView(View):
	def get(self,request, *args, **kwargs):
		context = {
			"form":ObservationForm
		}
		return render(request, 'evaluation/observation-teacher/observation.html', context)
	def post(self,request, *args, **kwargs):
		form = ObservationForm(request.POST,request.FILES)
		if form.is_valid():
			observation = form.save(commit=False)
			observation.delivery = Delivery.objects.get(pk=self.kwargs.get('pk')
)
			observation.save()
			return redirect(reverse('lesson:classroom_index',kwargs={"pk":self.kwargs.get('pk')}))
		context = {
			"form":form
		}
		return render(request, 'evaluation/observation-teacher/observation.html', context)



class CorrectionView(View):
	def get(self,request, *args, **kwargs):
		context = {
			"form":PonderationForm
		}
		return render(request, 'evaluation/correction-teacher/correction.html', context)
	def post(self,request, *args, **kwargs):
		form = PonderationForm(request.POST,request.FILES)
		if form.is_valid():
			ponderation = form.save(commit=False)
			ponderation.delivery = Delivery.objects.get(pk=self.kwargs.get('pk')
)
			ponderation.save()
			return redirect(reverse('lesson:classroom_index',kwargs={"pk":self.kwargs.get('pk')}))
		context = {
			"form":form
		}
		return render(request, 'evaluation/correction-teacher/correction.html', context)