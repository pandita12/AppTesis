from django.db import models

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
    deliver_date = models.DateTimeField()
    status_notifications = models.BooleanField(max_length=1)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    evaluation_id = models.ForeignKey(Evaluation, null=False, blank=False, on_delete=models.CASCADE)

