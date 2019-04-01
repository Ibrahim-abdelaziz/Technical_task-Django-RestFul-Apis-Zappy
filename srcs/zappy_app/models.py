from django.db import models
from datetime import date
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=200)
    message = models.TextField(max_length=250)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.name

