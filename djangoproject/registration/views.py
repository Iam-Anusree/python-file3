from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid registration")
            return redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        mailid=request.POST['mailid']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif  User.objects.filter(email=mailid).exists():
                    messages.info(request, "email id taken")
                    return redirect('register')
            else:

                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=mailid)
                user.save()
                return redirect('login')

        else:
           print("password not match")
           messages.info(request,"password not match")
           return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
