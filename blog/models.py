from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Mysites(models.Model):
    title = models.CharField(max_length = 100)
    url = models.URLField()
    author = models.CharField(max_length = 100)

class apilist(models.Model):
    name = models.CharField(max_length = 50)
    url = models.URLField()
    notes = models.TextField()
    class Meta:
        db_table = "apilist"

class apicase(models.Model):
    apiname = models.CharField(max_length = 50)
    apiurl = models.URLField()
    mothed = models.CharField(max_length = 20)
    data = models.TextField()
    check = models.CharField(max_length = 100)
    notes = models.TextField()
    name = models.CharField(max_length = 50)
    class Meta:
        db_table = "apicase"