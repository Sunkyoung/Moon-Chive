from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from django.contrib import auth, messages
from django.contrib.auth.hashers import check_password # 비번 바꾸기

from myapp.models import Profile

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})             
            except User.DoesNotExist:
                user=User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
                email=request.POST["email"]
                profile=Profile(user=user,email=email)
                profile.save()
                auth.login(request, user)
                return redirtect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Password must match'})
    else:
        return render(request, 'accounts/signup.html')

def signin(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
           return (request, 'accounts/login.html', {'error':'Password must match'})
    else:
        return render(request, 'accounts/login.html')

def logout_request(request):
    if request.method=='POST':
        auth.logout(request)
        messages.info(request, "Logged out successfully!")
        return redirect('home')
    return render(request, "accounts/signup.html")

def change_pw(request):
    context= {}
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password,user.password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                auth.login(request,user)
                return redirect("home")
            else:
                context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
    else:
        context.update({'error':"현재 비밀번호가 일치하지 않습니다."})

    return render(request, "accounts/change_pw.html", context)
