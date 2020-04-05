from django import forms
from django.forms import DateField, CharField
from .models import ToDoNode

class ToDoFormCreate(forms.ModelForm):
    todo = forms.CharField(label='',)
    class Meta:
        model = ToDoNode
        fields = ['todo',]
