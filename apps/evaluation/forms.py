from django.forms import ModelForm, CharField, FileField, DateTimeField
from .models import Evaluation

class CreateEvaluationForm(ModelForm):
	assignment_name = CharField(max_length=25)
	support_material = FileField()
	date_start = DateTimeField()
	date_finish = DateTimeField()
	class Meta:
		model = Evaluation
		fields = ["assignment_name", "support_material", "date_start", "date_finish"]
