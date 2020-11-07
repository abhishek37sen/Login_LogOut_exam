from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required(login_url='/accounts/login/')
def java_exams_views(request):
    return render(request,'javaexams.html')

@login_required(login_url='/accounts/login/')
def python_exams_views(request):
    return render(request,'pythonexams.html')

@login_required(login_url='/accounts/login/')
def aptitude_exams_views(request):
    return render(request,'aptitudeexams.html')