from django import forms
from django.db import models

from .models import Board, Comment
# from django.db.models.signals import post_saves
from django.dispatch import receiver
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
from ckeditor.widgets import CKEditorWidget

import datetime
from django.contrib.admin.helpers import ActionForm
from django.contrib.auth.forms import AuthenticationForm

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
            'pr_starttime' : TimePickerInput(attrs={'placeholder':'오전 09시 시작인 경우, 09:00'}).start_of('practice-time'),
            'pr_endtime' : TimePickerInput(attrs={'placeholder':'오후 03시 종료인 경우, 15:00'}).end_of('practice-time'),
            'pr_day' : forms.Textarea(attrs={'class': 'form-control','rows':1}),
            'pr_num' : forms.Textarea(attrs={'class': 'form-control','rows':1}),
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

