from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from apps.lesson.models import Classroom, Professor, Matter
from apps.consumer.models import User

# Create your views here.

def index_lesson(request):
	return HttpResponse("Page Principal de lesson")

@login_required
def detail_lesson(request, pk):
	
	return render(request, 'home/home.html',)


@login_required
def classroom_index(request, pk):
	classroom = Classroom.objects.get(pk=1)
	context = { 
		"classroom": classroom  

	}

	return render(request, 'teacher/classroom/class_index.html', context)

 
