from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, authenticate


def hello(request):
   return HttpResponse('hello')

def signup(request):
    if request.method == 'POST':
        print(request.POST)

        email = request.POST['email']
        name = request.POST['name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(password2)
        if password1 == password2:
            print('pass')
            User.objects.create_user(email=email, password=password1,name=name)
            user = authenticate(email=email, password=password1)
            login(request, user)
            return redirect('hello')

    return render(request, 'signup.html')

def userlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('products')
    return render(request,'login.html')


