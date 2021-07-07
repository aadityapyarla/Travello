from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.``
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists():
                messages.info(request, "Your username and email already exists!")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Your username already taken!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Your email already exists!")
                return redirect('register')
            else: 
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
        else:
            messages.info(request,  "Your passwords don't match!")
            return redirect('register')
        auth.login(request, user)
        return redirect('/')
    else:
        
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = str(request.POST['username'])
        password = str(request.POST['password'])
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else: 
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')