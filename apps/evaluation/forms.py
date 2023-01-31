from django import forms
from django.forms import ModelForm, CharField, FileField, DateTimeField, CheckboxInput, ModelChoiceField, Select, ModelMultipleChoiceField, SelectMultiple, NumberInput
from .models import Evaluation, Observation, Delivery, DeliveryPonderation

class CreateEvaluationForm(ModelForm):
	assignment_name = CharField(max_length=100)
	note_comentary = CharField(max_length=500)
	support_material = FileField()
	date_start = DateTimeField()
	date_finish = DateTimeField()
	class Meta:
		model = Evaluation
		fields = ["assignment_name","note_comentary", "support_material", "date_start", "date_finish"]



class ObservationForm(ModelForm):

	GENDER_CHOICES = (
		('S','Still to deliver'),
		('I','Incomplete content'),
		)

	observation = forms.CharField(widget=forms.Select(choices=GENDER_CHOICES))
	claim = forms.CharField(
		widget = forms.Textarea(attrs={'rows':3})
		)
	class Meta:
		model = Observation
		fields = ["observation", "claim"]



class PonderationForm(ModelForm):

	ponderation = forms.NumberInput()

	class Meta:
		model = DeliveryPonderation
		fields = ["ponderation"]

class SendTaskForm(ModelForm):

	title_task = forms.CharField(max_length=100)
	task_upload = forms.FileField()

	class Meta:
		model = Delivery
		fields = ["title_task", "task_upload"]