import email
from django.utils.translation import gettext_lazy as _
from django.db.models import CharField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    GENDER_CHOICES = [
        ('F', _('Female')),
        ('M', _('Male'))
    ]
    #: First and last name do not cover name patterns around the globe
    name = models.CharField(blank=True, max_length=50)
    first_name = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, null=True, unique=True)
    direction = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    password = models.SlugField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='F')
    is_student = models.BooleanField('student status', default=True)
    is_teacher = models.BooleanField('teacher status', default=False)
    is_moderator = models.BooleanField('moderator status', default=False)
    email = models.EmailField(_(' email address'),max_length=254, unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


