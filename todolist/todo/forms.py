from django import forms
from django.forms import DateField, CharField
from .models import ToDoNode

class ToDoFormCreate(forms.ModelForm):
    todo = forms.CharField(label='')
    #percents = forms.IntegerField(label='')
    #due_date = forms.DateField(label='')
    class Meta:
        model = ToDoNode
        fields = ['todo',]
