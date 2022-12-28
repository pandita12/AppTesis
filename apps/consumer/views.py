from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.http import HttpResponse
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .send_mail import SendMail
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
    return render(request, 'base/base_system.html')



class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'profile/profile.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            queryset = get_user_model().objects.all()
            if queryset.exists():
                for user in queryset:
                    subject = "Password Reset Requested"
                    email_template_name = "account/password_reset/password_reset_email.txt"
                    c = {
                    "email":user.email,
                    'domain':'0.0.0.0:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'swodorheranndez@gmail.com' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="account/password_reset/password_reset.html", context={"password_reset_form":password_reset_form})