from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method=="POST":
        if request.POST['password']==request.POST['passwordagain']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request, 'register.html', {'error': "Username already Has been taken"})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['passwordagain'])
                return render(request, 'register.html')
        else:
            return render(request,'register.html',{'error':"Password don't match"})
    else:
        return render(request, 'register.html')



def login(request):
    if request.method == "POST":
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return render(request,'home.html',{'message':"User Login..."})
        else:
            return render(request,'login.html',{'error':"invalid login id..."})
    else:
        return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return render(request,'home.html',{'message':"User Logout...."})