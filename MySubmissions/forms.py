from django import forms

from MySubmissions.views import *
from django.forms import ChoiceField
from .models import main,submission,mysubjects
import datetime
# from datetime import timedelta as tdelta
from django.utils.timezone import now
from django.utils import timezone
# def dummy(choice):
    # print("yessss",choice)
    # pass
class uploadForm(forms.ModelForm):
    class Meta:
        model=submission
        fields=('fileUpload','usn','uploadTime','assignmentName',)
        widgets = {
        'assignmentName': forms.HiddenInput(),
        'usn': forms.HiddenInput(),
        'uploadTime':forms.HiddenInput(),
        'fileUpload':forms.FileInput(attrs={'class': 'custom-file-input'})
        }
class subjectForm(forms.ModelForm):
    class Meta:
        model=mysubjects
        fields=('subjectName',)
class DateInput(forms.DateInput):
    input_type = 'date'
class PostForm(forms.ModelForm):
    # assignmentDate=forms.DateField()
    # assignedBy = forms.CharField(max_length=2000,
        # widget=forms.date )
    def __init__(self, *args, **kwargs):
        super(PostForm,self).__init__(*args, **kwargs)
        choice=tuple([(i.subjectName,i.subjectName)for i in mysubjects.objects.all()])
        self.fields['subjects'] =forms.ChoiceField(choices=choice)




    class Meta:
        # fdescription = forms.CharField(max_length=2000,
        # widget=forms.Textarea() )
        model = main
        # print("hye")
        # assignmentName=forms.CharField(max_length=100)
        # assignmentDescription=forms.CharField(max_length=2000,blank=True)
        # assignmentFormat=forms.CharField(max_length=2000,blank=True)
        # assignmentDate=forms.CharField(max_length=50)
        # assignedBy=forms.CharField(max_length=50)
        fields = ('subjects','assignmentName','assignmentDescription','assignmentFormat','assignmentDate','assignedBy',)
        widgets = {
            'assignedBy': forms.HiddenInput(),
            'assignmentDate': DateInput()
        }
