from django import forms
from .models import Board, Comment

class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ['title','body']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['c_content']
        labels={
            'c_content' : '내용',
        }