from django.shortcuts import render,redirect
from django.http import Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .models import main,submission,mysubjects
from .forms import uploadForm,PostForm,subjectForm
from django.template.context_processors import csrf
from django.db.models import Count,Q
# from collection import Counter

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect("/index/")
    else:
        form=AuthenticationForm()
    # c={'form':form}
    # c= c.update(csrf(request))
    return render(request,'login.html', {'form': form})
def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('/')
def posted(request):
    if request.user.is_authenticated:
        name = request.user.username
    # choice=tuple([(i.subjectName,i.subjectName)for i in mysubjects.objects.all()])
    # print(choice)
    if request.method == 'POST' and 'postit' in request.POST:
        mainform = PostForm(request.POST,request.FILES)
        print(mainform)
        if mainform.is_valid():
            mainform.save()
            return redirect("/index/")
    else:
        mainform = PostForm( initial = {'assignedBy':name})
        # dummy(choice)
    if request.method == 'POST' and 'sub' in request.POST:
        subform = subjectForm(request.POST,request.FILES)
        # print(subform)
        print(subform)
        if subform.is_valid():
            subform.save()
            return HttpResponseRedirect(request.path_info)
    else:
        subform = subjectForm()


    if request.user.is_authenticated:
        return render(request,'post.html',{'mainform':mainform,'subform':subform})
    else:
        return redirect("/")

def index(request):
    # yea=main.objects.order_by('subjects').values('subjects').distinct()
    yea=mysubjects.objects.order_by('subjectName').values('subjectName').distinct()

    # print(yea)
    if request.user.is_authenticated:
        return render(request,'index.html',{'yea':yea})
    else:
        return redirect("/")
def deleteMyAssignment(request,assignmentName):
    x=main.objects.filter(assignmentName=assignmentName).values('subjects')
    path=x[0]['subjects']
    finalpath="/assignmentList/"+path+"/"
    main.objects.filter(assignmentName=assignmentName).delete()
    submission.objects.filter(assignmentName=assignmentName).delete()
    return redirect(finalpath)

    # return redirect("/assignmentList/django/")
def assignmentList(request,subjects):
    if request.user.is_authenticated:
        usn = request.user.username
    # letsTry=main.objects.raw('''SELECT * FROM MySubmissions_submission WHERE assignmentName=%s assignedBy=%s''',[usn]
    subject=main.objects.filter(subjects=subjects)
    if request.user.is_authenticated:
        return render(request,'assignments.html',{'subject':subject,'usn':usn})
    else:
        return redirect("/")
def uploadInfo(request,upload):
    # print(categorie)
    # usn = None
    if request.user.is_authenticated:
        usn = request.user.username
    letsTry=main.objects.filter(assignmentName=upload,assignedBy=usn).count()

    studentfile=submission.objects.raw('''SELECT * FROM MySubmissions_submission WHERE assignmentName=%s AND usn=%s''',[upload,usn])
    assignmentInfo=main.objects.filter(assignmentName=upload)
    # file=filest.objects.filter(categorie=categorie)
    file=submission.objects.raw('''SELECT * FROM MySubmissions_submission WHERE assignmentName=%s GROUP BY usn''',[upload])
    if request.method == 'POST' and 'b1' in request.POST:
        submission.objects.filter(assignmentName=upload).delete()
            # file=submission.objects.filter(assignmentName=upload)

        # return HttpResponseRedirect(request.path_info)
    # if request.method == 'POST' and 'b2' in request.POST:
        # submission.objects.filter(assignmentName=upload).delete()
        # file=submission.objects.filter(assignmentName=upload)

        return HttpResponseRedirect(request.path_info)
    if request.method == 'POST':
        form = uploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)

    else:
        form = uploadForm(auto_id=False, initial = {'assignmentName':upload,'usn':usn})
    if request.user.is_authenticated:
        return render(request,'fileupload.html',{'letsTry':letsTry,'file':file,'form':form,'assignmentInfo':assignmentInfo,'studentfile':studentfile})
    else:
        return redirect("/")
