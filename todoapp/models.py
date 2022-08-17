from datetime import date
from importlib.resources import contents
from django.db import models
from django.utils import timezone


class TodoListItem(models.Model):
    added_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200, default='text')

# Create your models here.
