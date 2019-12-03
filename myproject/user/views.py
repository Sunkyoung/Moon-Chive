from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import CreateView
from user.forms import UserRegistrationForm, CustomUserChangeForm
from django.contrib import messages
from django.contrib.auth import views
from django.contrib.auth.forms import UserChangeForm
from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
 
@login_required
def delete(request):
    if request.method == "POST":
        pw_del=request.POST["pw_del"]
        user=request.user
        if check_password(pw_del, user.password):
            user.delete()
            return redirect('/')
    return render(request, 'user/delete.html')

class MyPasswordChangeView(PasswordChangeView):
    success_url=reverse_lazy('profile')
    template_name='user/password_change_form.html'
    success_url = '/user/mypage'

    def form_valid(self, form):
        messages.info(self.request, '암호 변경을 완료했습니다.')
        return super().form_valid(form)

class UserRegistrationView(CreateView):
    template_name = 'user/signup_form.html'
    model = get_user_model()
    form_class = UserRegistrationForm
    success_url = '/'

class UserLoginView(LoginView):           # 로그인
    template_name = 'user/login_form.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)

# 마이페이지
@login_required
def mypage(request):
    conn_user = request.user
    context = {
        'student_id' : conn_user.student_id , 
        'major_type' : conn_user.major_type, 
        'major' : conn_user.major, 
        'firstname' : conn_user.firstname, 
        'lastname' : conn_user.lastname, 
        'username' : conn_user.username, 
        'email' : conn_user.email,
    }
    return render(request, 'user/mypage.html', context=context)

def update(request): # 사용자 수정
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('user:mypage', request.user.username)
    else:
	    form = CustomUserChangeForm(instance = request.user)
	    return render(request, 'user/update.html', {'form':form})
