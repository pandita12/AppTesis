from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_lesson(request):
	return HttpResponse("Page Principal de lesson")

def detail_lesson(request, pk):
	ueryclassroom = Classroom.object.get(pk)
	context = {
		"classroom": ueryclassroom
	}
	return HttpResponse("Page Principal de lesson", context)