from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from apps.evaluation.models import Evaluation, Delivery
# Create your views here.

def asig_view(request, pk):
	ueryevaluation = Evaluation.objects.get(pk=1)
	context = {
		"evaluation": ueryevaluation
	}

	return render(request, 'evaluation/tasks.html', context)


def create_view(request):
    return render(request, 'evaluation/create-evaluation.html')