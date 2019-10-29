from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import Board, Comment
from django.db.models.signals import post_save
from django.dispatch import receiver

class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ['title','body','pr_inst','pr_startdate','pr_enddate','pr_location',
        'pr_tranbus','pr_transub','pr_day','pr_starttime','pr_endtime','pr_num','pr_file']
        widgets={
            'title': forms.Textarea(attrs={'placeholder':'제목을 입력하세요','class':'form-control','rows':1}),
            'body': forms.Textarea(attrs={'placeholder':'내용을 입력하세요.','class':'form-control','rows':20}),
            'pr_inst' : forms.Textarea(attrs={'class': 'form-control'}),
            'pr_location' : forms.Textarea(attrs={'class': 'form-control'}),
            'pr_tranbus' : forms.Textarea(attrs={'class': 'form-control'}),
            'pr_transub' : forms.Textarea(attrs={'class': 'form-control'}),
            'pr_day' : forms.Textarea(attrs={'class': 'form-control'}),
            'pr_num' : forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels={
            'title' : '제목',
            'body' : '내용',
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

