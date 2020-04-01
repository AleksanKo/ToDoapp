from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

class ToDoNode(models.Model):
    todo = models.CharField(max_length=100,blank=False)
    #due_date = models.DateField(default=date.today())
    done = models.BooleanField(default=False)
    percents_done = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)],default=0)