from django import forms
from django.forms import DateField, CharField
from .models import ToDoNode

class ToDoFormCreate(forms.ModelForm):

    class Meta:
        model = ToDoNode
        fields = ['todo','done']
