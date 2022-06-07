from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_evaluation(request):
	return HttpResponse("Page Principal de evaluation")