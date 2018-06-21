# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import main,submission,mysubjects
@admin.register(main)
class  Ziya(admin.ModelAdmin):
    list_display=['subjects','assignmentName','assignmentDescription','assignmentFormat','assignmentDate','assignedBy']

@admin.register(submission)
class  Ziya(admin.ModelAdmin):
    list_display=['fileUpload','usn','uploadTime','assignmentName']

@admin.register(mysubjects)
class  Ziya(admin.ModelAdmin):
    list_display=['subjectName',]
