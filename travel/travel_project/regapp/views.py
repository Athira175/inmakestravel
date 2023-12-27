from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=uname,password=pwd)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid register")
            return redirect('login')
    return render(request, "login.html")
def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        pwd=request.POST['password']
        cpwd=request.POST['password1']
        if pwd==cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username takes")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email takes")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=pwd,first_name=fname,last_name=lname,email=email)
                user.save();
                return redirect('login')
        else:
            print("pwd not matcing")
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")

# Create your views here.
