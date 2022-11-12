from django.db import models
from apps.lesson.models import Classroom, Matter, Professor
# Create your models here.

class Config_bot(models.Model):
    timefin = models.DateTimeField()
    professor_id = models.OneToOneField(Professor, null=False, blank=False, on_delete=models.CASCADE)
    matter_id = models.ForeignKey(Matter, null=False, blank=False, on_delete=models.CASCADE)
    classroom_id = models.ForeignKey(Classroom, null=False, blank=False, on_delete=models.CASCADE)
    