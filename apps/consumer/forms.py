from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	
	class Meta:
		model = User
		fields = [ "name", "first_name", "dni", "direction", "phone", "email", "password1", "password2", "gender", "is_student", "is_moderator", "is_teacher","types_user" ]



class LoginForm(forms.Form):
	email = forms.EmailField(
		widget= forms.TextInput(
			attrs={

				"class": "form-control"

			}

		)

	)

	password = forms.CharField(
		widget= forms.PasswordInput(
			attrs={

				"class": "form-control"

			}

		)

	)