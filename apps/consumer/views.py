from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect('consumer:base')
    else:
        form = RegisterForm()
    

    return render(response, 'account/register.html', {"form":form})





def home_index(request):
    return render(request, 'account/homepage.html')

def base_view(request):
    return render(request, 'base/base.html')

 
def login_view(request):
    return render(request, 'base/base.html')



def student_view(request):
    return render(request, 'base/base.html')


def teacher_view(request):
    return render(request, 'base/base.html')


def moderator_view(request):
    return render(request, 'base/base.html')