from django.db import models
from apps.consumer.models import User
from django.utils import timezone

# Create your models here.

class Matter(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    name_m = models.CharField(max_length=30)
    typeofmatter = models.CharField(max_length=12)

    def __str__(self):
        return self.name_m.capitalize()


class Professor(models.Model):
    users = models.OneToOneField(User, null=False, blank=False, related_name="professor", on_delete=models.CASCADE)
    department = models.CharField(max_length=12)


    def __str__(self):
        return self.users.fullname()
    
class Classroom(models.Model):
    matter_id = models.ForeignKey(Matter, null=False, blank=False, on_delete=models.CASCADE)
    professor_id = models.ForeignKey(Professor,related_name="classroom", null=False, blank=False, on_delete=models.CASCADE)
    classperiod = models.DateTimeField(default=False)
    stardate = models.DateTimeField()
    finaldate = models.DateTimeField()
    section = models.CharField(max_length=5)

    def __str__(self):
        return "('%s') %s" % (self.section.capitalize(), self.matter_id.name_m.capitalize())

    def endings_evaluation(self):
        return self.evaluation.filter(date_finish__lte=timezone.now())
    def pendings_evaluation(self):
        return self.evaluation.filter(date_finish__gte=timezone.now())

class Students(models.Model):
    users = models.OneToOneField(User, null=False, blank=False, related_name="student", on_delete=models.CASCADE)
    matter_id = models.ForeignKey(Matter, null=False, blank=False, on_delete=models.CASCADE)
    classroom_id = models.ForeignKey(Classroom, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.users.fullname()

class Enrollment(models.Model):
    classroom = models.ForeignKey(Classroom, null=False, blank=False, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, null=False, related_name="enrollment", blank=False, on_delete=models.CASCADE)
    registration_date = models.DateTimeField()
    status = models.BooleanField(max_length=1)
    semester_period = models.CharField(max_length=6, null=True)

    def __str__(self):
        return "('%s') %s" % (self.student.users.fullname(), self.classroom.matter_id.name_m.capitalize())