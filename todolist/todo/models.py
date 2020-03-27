from django import forms
from django.db import models
from datetime import date

class ToDoNode(models.Model):
    todo = models.CharField(max_length=100,blank=False)
    due_date = models.DateField(default=date.today)
    comment = models.TextField(max_length=300,default='')
    done = models.BooleanField(default=False)
