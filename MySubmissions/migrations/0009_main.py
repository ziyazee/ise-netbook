# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-18 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySubmissions', '0008_auto_20180618_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.CharField(max_length=100)),
                ('assignmentName', models.CharField(max_length=100)),
                ('assignmentDescription', models.CharField(blank=True, max_length=2000)),
                ('assignmentFormat', models.CharField(blank=True, max_length=2000)),
                ('assignmentDate', models.CharField(max_length=50)),
                ('assignedBy', models.CharField(max_length=50)),
            ],
        ),
    ]
