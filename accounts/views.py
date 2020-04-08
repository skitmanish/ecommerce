
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from cart.models import Cart

from address.models import Add
def signup(request):
    if request.method=="POST":
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'User already exist'})

            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])


                cart=Cart(user=request.POST['username'],cartitem=[[0]])
                add=Add(uname=request.POST['username'])
                add.save()
                cart.save()
                return redirect('home')

        else:
             return render(request,'accounts/signup.html',{'error':'Password does not match'})


    else:

         return render(request,'accounts/signup.html')

def login(request):
        if request.method=="POST":
            user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                auth.login(request,user)

                return redirect('home')
            else:
                return render(request,'accounts/login.html',{'error':'Password or Username does not match'})
        else:
            return render(request,'accounts/login.html',)
def logout(request):
    if request.method=="POST":
        auth.logout(request)
        return redirect('home')
