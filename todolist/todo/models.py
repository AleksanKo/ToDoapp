from django.db import models

class ToDoNode(models.Model):
    content = models.TextField()
