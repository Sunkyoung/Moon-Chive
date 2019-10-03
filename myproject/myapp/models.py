from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    body=models.TextField()

    def __str__(self):
        return self.title

class Board(models.Model):
    title = models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now_add=True)
    body=models.TextField()
    # Field()안에 default='' 쓰면 내용에 아무것도 안써도 null 에러 안남

    def __str__(self):
        return self.title

class Comment(models.Model):
    board = models.ForeignKey('myapp.Board', related_name='comments', on_delete=models.CASCADE)
    c_author = models.CharField(max_length=200, default="익명")
    c_content = models.TextField()
    c_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
