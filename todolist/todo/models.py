from django.db import models
from django.contrib.auth.models import User

class ToDoNode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    todo = models.CharField(max_length=100,blank=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.todo