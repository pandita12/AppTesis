from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import * 
from .forms import UserRegisterForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def home_index(request):
	return render(request, 'account/homepage.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            messages.success(request, f'Usuario {name} creado')
            return redirect('base/base.html')
    else:
        form = UserRegisterForm()

    context = { 'form' : form }
    return render(request, 'account/register.html')







def student_view(request):
    return render(request, 'base/base.html')


def teacher_view(request):
    return render(request, 'base/base.html')


def moderator_view(request):
    return render(request, 'base/base.html')