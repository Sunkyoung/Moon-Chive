import datetime
from django import forms
from django.contrib.admin.helpers import ActionForm
from django.contrib.auth.forms import AuthenticationForm
from django_registration.forms import RegistrationForm, RegistrationFormUniqueEmail
from .models import Account
from django.forms import SelectDateWidget
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

# class SetCertificationDateForm(ActionForm):
#     certification_date = forms.DateField(
#         widget=SelectDateWidget,
#         initial=(datetime.date.today())
#     )
    


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'email', 'first_name','last_name']

# class RegistrationForm(RegistrationFormUniqueEmail):
#     error_messages = {
#         'email_mismatch': ('The two email fields didn\'t match.'),
#         'password_mismatch': ('The two password fields didn\'t match.'),
#     }

#     terms = forms.BooleanField(error_messages={'required': (u'You must agree to the terms to register')})

#     def __init__(self, *args, **kwargs):
#         super(RegistrationFormUniqueEmail, self).__init__(*args, **kwargs)
#         if 'username' in self.fields:
#             self.fields['username'].widget.attrs.update({'placeholder':(u'사용할 닉네임을 입력하세요(로그인 시 사용될 아이디)'), 'autofocus': ''})    
#         if 'email' in self.fields:
#             self.fields['email'].widget.attrs.update({'placeholder': (u'이메일을 입력하세요')})
#         if 'password1' in self.fields:
#             self.fields['password1'].widget.attrs.update({'placeholder': (u'비밀번호를 입력하세요')})
#         if 'password2' in self.fields:
#             self.fields['password2'].widget.attrs.update({'placeholder': (u'비밀번호를 한 번 더 입력하세요')})

#     def clean_password2(self):
#         # Passwords must match
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError(
#                 self.error_messages['password_mismatch'],
#                 code='password_mismatch',
#             )
#         return password2

#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if User.objects.filter(username=username).exists():
#             raise forms.ValidationError('이미 사용중인 닉네임입니다')
#         return username

#     class Meta:
#         model = Account
#         fields = ['student_id', 'major', 'major_type', 'username', 'password1', 'password2', 'firstname', 'lastname', 'email' ]
#         widgets = {
#             'student_id' : forms.TextInput(attrs={'placeholder':'제목을 입력하세요'}),
#             'major' : forms.TextInput(attrs={'placeholder':'ex) 문헌정보학'}), 
#             'firstname' : forms.TextInput(attrs={'placeholder':'ex) 이'}),
#             'lastname' : forms.TextInput(attrs={'placeholder':'ex) 화연'}), 
#         }
#         labels={
#             'student_id' : '학번',
#             'major' : '주전공', 
#             'major_type' : '문헌정보학 전공 형태',
#             'username' : '닉네임', 
#             'password1' : '비밀번호' , 
#             'password2' : '비밀번호 확인', 
#             'firstname' : '성', 
#             'lastname' : '이름', 
#             'email' : '이메일'
#         }

# registration
class SetCertificationDateForm(ActionForm):
    certification_date = forms.DateField(
        widget=SelectDateWidget,
        initial=(datetime.date.today())
    )
# RegistrationFormUniqueEmail
class CustomAccountForm(RegistrationForm):
    class Meta:
        model = Account
        fields = ['student_id', 'major', 'major_type', 'username', 'password1', 'password2', 'firstname', 'lastname', 'email' ]
        widgets = {
            'student_id' : forms.TextInput(attrs={'placeholder':'제목을 입력하세요'}),
            'major' : forms.TextInput(attrs={'placeholder':'ex) 문헌정보학'}), 
            'firstname' : forms.TextInput(attrs={'placeholder':'ex) 이'}),
            'lastname' : forms.TextInput(attrs={'placeholder':'ex) 화연'}), 
        }
        labels={
            'student_id' : '학번',
            'major' : '주전공', 
            'major_type' : '문헌정보학 전공 형태',
            'username' : '닉네임', 
            'password1' : '비밀번호' , 
            'password2' : '비밀번호 확인', 
            'firstname' : '성', 
            'lastname' : '이름', 
            'email' : '이메일'
        }

    error_messages = {
        'email_mismatch': ('The two email fields didn\'t match.'),
        'password_mismatch': ('The two password fields didn\'t match.'),
    }

    terms = forms.BooleanField(error_messages={'required': (u'You must agree to the terms to register')})
    # RegistrationFormUniqueEmail, 
    def __init__( self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        if 'username' in self.fields:
            self.fields['username'].widget.attrs.update({'placeholder':(u'사용할 닉네임을 입력하세요(로그인 시 사용될 아이디)'), 'autofocus': ''})    
        if 'email' in self.fields:
            self.fields['email'].widget.attrs.update({'placeholder': (u'이메일을 입력하세요')})
        if 'password1' in self.fields:
            self.fields['password1'].widget.attrs.update({'placeholder': (u'비밀번호를 입력하세요')})
        if 'password2' in self.fields:
            self.fields['password2'].widget.attrs.update({'placeholder': (u'비밀번호를 한 번 더 입력하세요')})

    def clean_password2(self):
        # Passwords must match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def clean_username(self):
        username = self.cleaned_data['username']
        if Account.objects.filter(username=username).exists():
            raise forms.ValidationError('이미 사용중인 닉네임입니다')
        return username

    