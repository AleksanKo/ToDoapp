from django import forms
from django.forms import DateField, CharField
from .models import ToDoNode, Person

class ToDoFormCreate(forms.ModelForm):

    class Meta:
        model = ToDoNode
        fields = ['todo']

class PersonCreate(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name','second_name']