from django import forms
from django.db import models
from datetime import date

class ToDoNode(models.Model):
    todo = models.CharField(max_length=200,blank=False)
    #due_date = models.DateField(default=date.today)

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
