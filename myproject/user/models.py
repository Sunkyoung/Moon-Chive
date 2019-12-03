from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('아이디를 입력해주세요')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, password=None, **extra_fields):
        extra_fields.setdefault('permission', 'PETER')
        extra_fields.setdefault('is_certificated', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('permission', 'ADMIN')
        extra_fields.setdefault('is_certificated', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    TYPE_MAJOR=(
        ('주전공','주전공'),
        ('타전공', '복수전공')
    )

    TYPE_PERMISSIONS = (
        ('ADMIN', '관리자'),
        ('TINK', '팅커벨'),
        ('PETER', '일반'),
    )
    email = models.EmailField('이메일', max_length=254)
    username = models.CharField('아이디', max_length=30, unique=True)
    firstname = models.CharField('성', max_length=30)
    lastname = models.CharField('이름', max_length=30)
    student_id = models.CharField('학번',max_length=7, unique=True)
    major = models.CharField('주전공',max_length=200)
    major_type = models.CharField('문헌정보학 전공형태',max_length=4, choices=TYPE_MAJOR, default='주전공')
    permission = models.CharField('권한', max_length=2, choices=TYPE_PERMISSIONS, default='PETER')
    certification_date = models.DateField('인증일', default=None, null=True, blank=True)
    is_certificated = models.BooleanField('인증여부', default=False)
    is_staff = models.BooleanField('스태프 권한', default=False)
    is_active = models.BooleanField('사용중', default=True)
    date_joined = models.DateTimeField('가입일', default=timezone.now)

    objects = UserManager()
    
    USERNAME_FIELD = 'username'                   # 학번을 사용자의 식별자로 설정
    REQUIRED_FIELDS = ['student_id','email', 'firstname', 'lastname', 'major', 'major_type']                   # 필수입력값

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'

    def email_user(self, subject, message, from_email=None, **kwargs): # 이메일 발송 메소드
        send_mail(subject, message, from_email, [self.email], **kwargs)
