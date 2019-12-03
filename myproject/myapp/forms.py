from django import forms
from django.db import models
# from django.contrib.auth.models import User
from .models import Board, Comment, Account
from django.db.models.signals import post_save
from django.dispatch import receiver
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from ckeditor.widgets import CKEditorWidget
# registration 
import datetime
from django.contrib.admin.helpers import ActionForm
from django.contrib.auth.forms import AuthenticationForm
# from django_registration.forms import RegistrationForm, RegistrationFormUniqueEmail
# from django_registration.forms import RegistrationForm
from django.forms import SelectDateWidget


class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ['title','pr_inst','pr_startdate','pr_enddate','pr_location',
        'pr_tranbus','pr_transub','pr_day','pr_starttime','pr_endtime','pr_num','body','pr_file']
        widgets={
            'title': forms.Textarea(attrs={'placeholder':'제목을 입력하세요','class':'form-control','rows':1}),
            'body': CKEditorWidget(),
            'pr_inst' : forms.Textarea(attrs={'class': 'form-control','rows' : 1}),
            'pr_startdate' : DatePickerInput(format='%Y-%m-%d').start_of('practice-date'),
            'pr_enddate' : DatePickerInput(format='%Y-%m-%d').end_of('practice-date'),
            'pr_location' : forms.Textarea(attrs={'class': 'form-control','rows':1}),
            'pr_tranbus' : forms.Textarea(attrs={'class': 'form-control','rows':1}),
            'pr_transub' : forms.Textarea(attrs={'class': 'form-control','rows':1}),
            'pr_starttime' : TimePickerInput(format='%I:%M %p').start_of('practice-time'),
            'pr_endtime' : TimePickerInput(format='%I:%M %p').end_of('practice-time'),
            'pr_day' : forms.Textarea(attrs={'class': 'form-control','rows':1}),
            'pr_num' : forms.Textarea(attrs={'class': 'form-control','rows':1}),
        }
        input_formats={
            'pr_starttime' : ['%I:%M %p'],
            'pr_endtime' : ['%I:%M %p'],
        }
        labels={
            'title' : '제목',
            'pr_inst' : '기관명',
            'pr_startdate' : '실습시작일',
            'pr_enddate' : '실습종료일',
            'pr_location' : '위치',
            'pr_tranbus' : '인근버스',
            'pr_transub' : '인근지하철',
            'pr_day' : '근무요일',
            'pr_starttime' : '근무시작시간',
            'pr_endtime' : '근무종료시간',
            'pr_num' : '실습인원',
            'body' : '내용',
            'pr_file' : '첨부파일',
        }
    def __init__(self, *args, **kwargs):
        super(BoardForm, self).__init__(*args, **kwargs)
        self.fields['pr_file'].required = False


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['c_content']
        widgets={
            'c_content' : forms.Textarea(attrs={'placeholder':'댓글을 입력하세요.','class':'form-control','rows':2})
        }
        labels={
            'c_content' : '내용',
        }

# # registration
# class SetCertificationDateForm(ActionForm):
#     certification_date = forms.DateField(
#         widget=SelectDateWidget,
#         initial=(datetime.date.today())
#     )
# # RegistrationFormUniqueEmail
# class CustomAccountForm(RegistrationForm):
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

#     error_messages = {
#         'email_mismatch': ('The two email fields didn\'t match.'),
#         'password_mismatch': ('The two password fields didn\'t match.'),
#     }

#     terms = forms.BooleanField(error_messages={'required': (u'You must agree to the terms to register')})
# # RegistrationFormUniqueEmail, 
#     def __init__( self, *args, **kwargs):
#         super(RegistrationForm, self).__init__(*args, **kwargs)
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
#         if Account.objects.filter(username=username).exists():
#             raise forms.ValidationError('이미 사용중인 닉네임입니다')
#         return username

    