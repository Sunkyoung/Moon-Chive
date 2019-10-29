from django.db import models
from accounts.models import Account
from ckeditor.fields import RichTextField
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
    body=RichTextField()
    # hit = 
    pr_inst = models.CharField(default='도서관',max_length=20)
    pr_startdate = models.DateField(default='2019-07-01')
    pr_enddate = models.DateField(default='2019-08-31')
    pr_location = models.TextField(default='서울시')
    pr_tranbus = models.CharField(max_length=100, blank=True)
    pr_transub = models.CharField(max_length=100, blank=True)
    pr_day = models.TextField(default='월, 화, 수, 목, 금')
    pr_starttime = models.TimeField(default='09:00')
    pr_endtime = models.TimeField(default='18:00')
    pr_num = models.CharField(default='1명',max_length=20)
    pr_file = models.FileField(null=True)
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

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     TYPE_MAJOR=(
#         ('주전공','문헌정보학과'),
#         ('복수전공', '타전공')
#         )

#      TYPE_PERMISSIONS = (
#         ('ADMIN', '관리자'),
#         ('TINK', '팅커벨'),
#         ('PETER', '일반'),
#     )
#     email = models.EmailField(max_length=254)
#     student_id = models.CharField(max_length=7)
#     major = models.CharField(max_length=200)
#     major_type = models.CharField(max_length=4,choices=TYPE_MAJOR,default='주전공')
#     permission = models.CharField('권한', max_length=2, choices=TYPE_PERMISSIONS, default='PETER')
#     certification_date = models.DateField('인증일', default=None, null=True, blank=True)
#     is_certificated = models.BooleanField('인증여부', default=False)
    
class Category(models.Model):
    name=models.CharField('카테고리 이름', max_length=20)

