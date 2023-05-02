from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def login_user(request,*args,**kwargs): 
    logout(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password) # returns None if user is not found

        if user is not None:
            login(request,user)
            return redirect(f'/user/{username}/1')
        
        if user is None:
            messages.error(request,('Invalid Credentials'))
            return redirect('/login')
        
    if request.method == 'GET':
        return render(request,'auth_system/login.html')

def logout_user(request,*args,**kwargs):
    logout(request)
    messages.success(request,('You have been logged out'))
    return redirect('/login')

def register_user(request,*args,**kwargs):
    logout(request)
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,('You have registered'))
            return redirect('/login')
        else:
            messages.error(request,('Invalid Credentials'))
            return redirect('/register')
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request,'auth_system/register.html',{'form':form})