from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.consumer.models import User
from apps.lesson.models import Classroom, Professor
from apps.teacherbot.models import Config_bot
from django.utils import timezone
# Create your models here.

class Evaluation(models.Model):
    assignment_name = models.CharField(max_length=50)
    support_material = models.FileField(upload_to="material", max_length=100, null=True)
    date_start = models.DateTimeField()
    date_finish = models.DateTimeField()
    classroom_id = models.ForeignKey(Classroom, related_name='evaluation', null=False, blank=False, on_delete=models.CASCADE)

    def if_ending(self):
        return self.date_finish > timezone.now()

    def full_delivery(self):
        total = self.evaluation.count()
        delivery = self.classroom_id.enrollment.count() - self.evaluation.count() 
        return "%s / %s" % (total, delivery) 


class Delivery(models.Model):

    deliver_date = models.DateTimeField(default=timezone.now)
    evaluative_message = models.CharField(max_length=200, null=True, blank=True)
    title_task = models.CharField(max_length=100, null=True, blank=True)
    task_upload = models.FileField(upload_to="taskupload/", max_length=100, null=True, blank=True) 
    student = models.ForeignKey(User,related_name='delivery', null=False, blank=False, on_delete=models.CASCADE)
    evaluation = models.ForeignKey(Evaluation, related_name='evaluation', null=False, blank=False, on_delete=models.CASCADE)
    

    def is_approved(self):
        return "approved" if self.ponderation >= self.config_delivery.min_aprobed and self.ponderation <= self.config_delivery.max_aprobed else "reprobate"

    def has_ponderation(self):
        return self.ponderation.count()

class DeliveryPonderation(models.Model):
    delivery = models.OneToOneField(Delivery, related_name='ponderation', on_delete=models.CASCADE)
    ponderation = models.FloatField(null=True, blank=True)
    date_ponderation = models.DateTimeField(default=timezone.now)
 
class Config_Delivery_Rest(models.Model):
    delivery = models.ForeignKey(Delivery, null=False, blank=False, on_delete=models.CASCADE,
     related_name= "config_delivery")
    min_aprobed = models.FloatField('reprobate')
    max_aprobed = models.FloatField('approved')


class Observation(models.Model):
    delivery = models.OneToOneField(Delivery, related_name='observation_delivery', null=True, blank=False, on_delete=models.CASCADE)
    
    GENDER_CHOICES_OBSERVATION = [
        ('N',_('Still to deliver')),
        ('I',_('Incomplete content')),
    ]

    observation = models.CharField(max_length=1, choices=GENDER_CHOICES_OBSERVATION, default='N')
    claim = models.CharField(max_length=200, null=False)


class ModeratorClassroom(models.Model):
    classroom = models.ForeignKey(Classroom, related_name='moderator_classroom',null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='moderator_classroom',null=False, blank=False, on_delete=models.CASCADE)  