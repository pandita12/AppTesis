from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(label='Email', widget=forms.EmailInput)
	name = forms.CharField(label='Nombre', widget=forms.TextInput)
	first_name = forms.CharField(label='Apellido', widget=forms.TextInput)
	dni = forms.CharField(label='Dni', widget=forms.TextInput)
	direction = forms.CharField(label='Direccion', widget=forms.TextInput)
	phone = forms.CharField(label='Telefono', widget=forms.TextInput)
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
	gender = forms.ChoiceField(label='Sexo', widget=forms.Select)
	is_student = forms.BooleanField(label='Estudiante', widget=forms.CheckboxInput)
	is_teacher = forms.BooleanField(label='Profesor', widget=forms.CheckboxInput)
	is_moderator = forms.BooleanField(label='Moderador', widget=forms.CheckboxInput)

	class Meta:
		model = User
		fields = ['name', 'email', 'first_name', 'dni', 'direction', 'phone', 'password1', 'password2', 'gender', 'is_student', 'is_teacher', 'is_moderator']
		help_texts = {k: "" for k in fields}

