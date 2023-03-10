import datetime

from django.db import models
from django.utils import timezone

class Article(models.Model):

    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    date_reg = models.DateTimeField('date reqister')
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name

class Chief(models.Model):

    full_name = models.CharField(max_length=200)
    def __str__(self):
        return self.full_name