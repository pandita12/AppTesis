from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

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
                return redirect('consumer:Inicio')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('consumer:Inicio')
            elif user is not None and user.is_moderator:
                login(request, user)
                return redirect('consumer:Inicio')
            else:
                msg = ' Invalid credentials'
        else:
            msg = ' error validating form'


    return render(request, 'account/login.html', {'form': form, 'msg': msg})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, F" Sesión cerrada exitosamente")
    return redirect('/login/')



def home_index(request):
    return render(request, 'account/homepage.html')

@login_required
def base_view(request):
    return render(request, 'base/base.html')



class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'profile/profile.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)