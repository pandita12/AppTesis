from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from apps.lesson.models import Classroom

# Create your views here.

def index_lesson(request):
	return HttpResponse("Page Principal de lesson")

@login_required
def detail_lesson(request, pk):
	ueryclassroom = Classroom.objects.get(pk=1)
	context = {
		"classroom": ueryclassroom
	}

	return render(request, 'home/home.html', context)




#def materia_view(request):
    #return render(request, 'home/home.html')