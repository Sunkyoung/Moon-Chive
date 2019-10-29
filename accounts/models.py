
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class AccountManager(BaseUserManager):
    use_in_migrations = True
    
    # def _create_user(self, username, password, **extra_fields):
    #     if not username:
    #         raise ValueError('The given username must be set')
    #     user = self.model(username=username, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    def create_user(self, username, email, firstname, lastname, student_id, major, major_type, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            lastname=lastname,
            student_id=student_id,
            major=major,
            major_type=major_type,
            password=password,
        )
        user.is_admin = False
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, firstname, lastname, student_id, major, major_type, password=None):
        user = self.create_user(
            email=email,
            username=username,
            firstname=firstname,
            lastname=lastname,
            student_id=student_id,
            major=major,
            major_type=major_type,
        )
        user.is_admin = True
        user.is_superuser = True
        # user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    TYPE_MAJOR=(
        ('주전공','문헌정보학과'),
        ('복수전공', '타전공')
    )

    TYPE_PERMISSIONS = (
        ('ADMIN', '관리자'),
        ('TINK', '팅커벨'),
        ('PETER', '일반'),
    )
    email = models.EmailField('이메일', max_length=254)
    username = models.CharField('닉네임', max_length=30, unique=True)
    firstname = models.CharField('성', max_length=30, blank=True)
    lastname = models.CharField('이름', max_length=30, blank=True)
    student_id = models.CharField('학번',max_length=7, unique=True)
    major = models.CharField('주전공',max_length=200)
    major_type = models.CharField('전공형태',max_length=4, choices=TYPE_MAJOR, default='주전공')
    permission = models.CharField('권한', max_length=2, choices=TYPE_PERMISSIONS, default='PETER')
    certification_date = models.DateField('인증일', default=None, null=True, blank=True)
    is_certificated = models.BooleanField('인증여부', default=False)
    is_admin = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'firstname', 'lastname', 'student_id', 'major', 'major_type']

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')
        swappable = 'AUTH_USER_MODEL'

    # def email_user(self, subject, message, from_email=None):
    #     """ Used for django-registration """
    #     send_mail(subject, message, from_email, [self.email])

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.firstname, self.lastname)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.lastname

    
