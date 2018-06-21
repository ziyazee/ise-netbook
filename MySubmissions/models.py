# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
# from datetime import timedelta as tdelta
from django.utils.timezone import now
from django.utils import timezone
from django.db import models

# print("hye")
# Create your models here.
class mysubjects(models.Model):
    subjectName=models.CharField(max_length=100,unique=True)
class main(models.Model):
    subjects=models.CharField(max_length=100)
    assignmentName=models.CharField(max_length=100)
    assignmentDescription=models.CharField(max_length=2000,blank=True)
    assignmentFormat=models.CharField(max_length=2000,blank=True)
    assignmentDate=models.CharField(max_length=2000,blank=True)
    assignedBy=models.CharField(max_length=50)
class submission(models.Model):
    fileUpload=models.FileField()
    usn=models.CharField(max_length=100)
    uploadTime=models.DateTimeField(default=now, blank=True)
    assignmentName=models.CharField(max_length=100)
# choice=tuple([(i.subjectName,i.subjectName)for i in mysubjects.objects.all()])
# print(choice)
