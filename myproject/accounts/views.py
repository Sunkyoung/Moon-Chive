from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django_registration.backends.activation.views import RegistrationView as BaseRegistrationView
# from myapp.forms import RegistrationForm
from .models import Account
from .forms import CustomAccountForm


# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate

# from django.contrib import auth, messages
# from django.contrib.auth.hashers import check_password # 비번 바꾸기
# from django.contrib.auth.forms import UserChangeForm

# from myapp.models import Profile
from django.contrib.auth.decorators import login_required
# from .forms import CustomUserChangeForm

# # Create your views here.
# def signup(request):
#     if request.method == "POST":
#         if request.POST['password1']==request.POST['password2']:
#             try:
#                 user=User.objects.get(username=request.POST['username'])
#                 return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})             
#             except User.DoesNotExist:
#                 user=User.objects.create_user(request.POST['username'], password=request.POST['password1'],email=request.POST["email"],firstname=request.POST["first_name"])
            
#                 major=request.POST["major"]
#                 major_type=request.POST["major_type"]
#                 profile=Profile(user=user,email=email,major=major,major_type=major_type)
                
#                 auth.login(request, user)
#                 return redirect('home')
#         else:
#             return render(request, 'accounts/signup.html', {'error':'Password must match'})
#     else:
#         return render(request, 'accounts/signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=Account.authenticate(request, username=username, password=password)
        if user is not None:
            Account.login(request, user)
            return redirect('home')
        else:
           return render(request, 'accounts/login.html', {'error':'Password must match'})
    else:
        return render(request, 'accounts/login.html')

# def logout_request(request):
#     if request.method=='POST':
#         auth.logout(request)
#         messages.info(request, "Logged out successfully!")
#         return redirect('home')
#     return render(request, "accounts/signup.html")

# def change_pw(request):
#     context= {}
#     if request.method == "POST":
#         current_password = request.POST.get("origin_password")
#         user = request.user
#         if check_password(current_password,user.password):
#             new_password = request.POST.get("password1")
#             password_confirm = request.POST.get("password2")
#             if new_password == password_confirm:
#                 user.set_password(new_password)
#                 user.save()
#                 auth.login(request,user)
#                 return redirect("home")
#             else:
#                 context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
#     else:
#         context.update({'error':"현재 비밀번호가 일치하지 않습니다."})

#     return render(request, "accounts/change_pw.html", context)

# def delete(request):
#     if request.method == 'POST':
#         request.user.delete()
#         return redirect('posts:list')
#     return render(request, 'accounts/delete.html')

# def update(request):
#     if request.method == "POST":
#     	# updating
#         user_change_form = CustomUserChangeForm(data=request.POST, instance=request.user)
        
#         if user_change_form.is_valid() and profile_form.is_valid():
#             user = user_change_form.save()
        
#     else:
#         # editting
#         user_change_form = CustomUserChangeForm(instance=request.user)

#         context = {
#             'user_change_form': user_change_form,
#         }
        
#         return render(request, 'update.html', context)

class RegistrationView(BaseRegistrationView):
    form_class = CustomAccountForm

    def register(self, form):
        new_user = BaseRegistrationView.register(self, form)
        acc = Account()
        acc.username = form.cleaned_data['username']
        acc.user = new_user
        acc.status = 'created'
        acc.save()

@login_required
def profile(request):
    try:
        acc = Account.objects.get(user=request.user)
    except:
        acc = None

    context = {
        'user': request.user,
        'account': acc
    }

    return render(request, 'accounts/profile.html', context)

@login_required
def delete_user(request):
    user = Account.objects.get(student_id=request.user.student_id)
    user.save()
    return redirect('/')

# class RegistrationView(BaseRegistrationView):
#     template_name = 'django_registration/registration_form.html
#     form_class = CustomAccountForm
  
#     def register(self, form):
#         new_user = BaseRegistrationView.register(self, form)
#         acc = Account()
#         acc.username = form.cleaned_data['username']
#         acc.user = new_user
#         # acc.status = 'created'
#         acc.save()

# class CreateUserView(CreateView): # generic view중에 CreateView를 상속받는다.
#     template_name = 'registration/signup.html' 
#     form_class =  CustomAccountForm # 푸슨 폼 사용? >> 내장 회원가입 폼을 커스터마지징 한 것을 사용하는 경우
#     # form_class = UserCreationForm >> 내장 회원가입 폼 사용하는 경우
#     success_url = reverse_lazy('create_user_done') # 성공하면 어디로?

# class RegisteredView(TemplateView): # generic view중에 TemplateView를 상속받는다.
#     template_name = 'registration/signup_done.html'
        