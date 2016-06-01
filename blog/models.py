#coding=utf-8
from __future__ import unicode_literals
from django.utils import timezone
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
    def __unicode__(self):
         return self.name


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

class project(models.Model):
    name = models.CharField(max_length= 100)
    casej = models.TextField()
    notes = models.CharField(max_length =200)
    class Meta:
        db_table = "project"

class results(models.Model):
    name = models.CharField(max_length= 100)
    time = models.DateTimeField(auto_now=True)
    total = models.CharField(max_length= 10)
    ps = models.CharField(max_length= 10)
    fail = models.CharField(max_length= 10)
    result = models.TextField()
    class Meta:
        db_table = "results"