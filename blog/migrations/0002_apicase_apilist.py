# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apicase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CaseName', models.CharField(max_length=50)),
                ('ApiUrl', models.URLField()),
                ('CaseMothed', models.CharField(max_length=20)),
                ('CaseData', models.TextField()),
                ('CaseCheck', models.CharField(max_length=100)),
                ('casenotes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Apilist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApiName', models.CharField(max_length=50)),
                ('ApiUrl', models.URLField()),
                ('ApiNotes', models.TextField()),
            ],
        ),
    ]