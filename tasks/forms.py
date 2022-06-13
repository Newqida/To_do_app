from attr import field
from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):

    class Meta:
        title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
        model = Task
        fields = '__all__'