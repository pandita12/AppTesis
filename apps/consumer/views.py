from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .forms import RegisterForm, LoginForm

# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST or None)
        if form.is_valid():
            form.save()

        return redirect('consumer:login')
    else:
        form = RegisterForm()
    

    return render(response, 'account/register.html', {"form":form})



def login_view(request):
    form = LoginForm(request.POST)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None and user.is_student:
                login(request, user)
                return redirect('consumer:studentpage')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('teacherpage')
            elif user is not None and user.is_moderator:
                login(request, user)
                return redirect('moderatorpage')
            else:
                msg = ' Invalid credentials'
        else:
            msg = ' error validating form'


    return render(request, 'account/login.html', {'form': form, 'msg': msg})




def home_index(request):
    return render(request, 'account/homepage.html')

def base_view(request):
    return render(request, 'base/base.html')


def student_view(request):
    return render(request, 'base/base.html')


def teacher_view(request):
    return render(request, 'base/base.html')


def moderator_view(request):
    return render(request, 'base/base.html')