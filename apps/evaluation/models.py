from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.consumer.models import User
from apps.lesson.models import Classroom, Professor
from apps.teacherbot.models import Config_bot
from django.utils import timezone
# Create your models here.

class Evaluation(models.Model):
    assignment_name = models.CharField(max_length=25)
    support_material = models.FileField(upload_to="material", max_length=100, null=True)
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()
    classroom_id = models.ForeignKey(Classroom, related_name='evaluation', null=False, blank=False, on_delete=models.CASCADE)

    def if_ending(self):
        return self.date_finish > timezone.now()


class Delivery(models.Model):

    GENDER_CHOICES = [
        ('D', _('Delivered')),
        ('U', _('Undelivered'))
    ]

    deliver_date = models.DateTimeField()
    task_upload = models.FileField(upload_to="taskupload/", max_length=100, null=True, blank=True)
    status_delivery = models.CharField(max_length=1, choices=GENDER_CHOICES, default='D') 
    status_notifications = models.BooleanField(max_length=1)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    evaluation_id = models.ForeignKey(Evaluation, null=False, blank=False, on_delete=models.CASCADE)
    ponderation = models.FloatField(null=True)

    def is_approved(self):
        return "approved" if self.ponderation >= self.config_delivery.min_aprobed and self.ponderation <= self.config_delivery.max_aprobed else "reprobate"

class Config_Delivery_Rest(models.Model):
    delivery = models.ForeignKey(Delivery, null=False, blank=False, on_delete=models.CASCADE,
     related_name= "config_delivery")
    min_aprobed = models.FloatField('reprobate')
    max_aprobed = models.FloatField('approved')


class Delivery_Rest(models.Model):
    config_delivery = models.ForeignKey(Config_Delivery_Rest, null=False, blank=False, on_delete=models.CASCADE)
    is_reprobate = models.BooleanField( 'ponderation reprobate', default=True)
    is_approved = models.BooleanField('ponderation approved', default=False) 