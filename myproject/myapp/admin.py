from django.contrib import admin

# Register your models here.
from .models import Notice, Board, Comment
from accounts.models import Account
class AccountAdmin(admin.ModelAdmin):
     list_display = ['id','username', 'firstname',  'lastname',  'email', 'student_id', 'major', 'major_type', 'permission','is_certificated', 'certification_date',]

# admin.site.register(Account, AccountAdmin)
admin.site.register(Notice)
admin.site.register(Board)
admin.site.register(Comment)
