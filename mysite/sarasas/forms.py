from .models import Task
from django import forms
from django.contrib.auth.models import User

class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

class UserUzsakymasCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'tbd']
        widgets = {'tbd': DateTimeInput()}