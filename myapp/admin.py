from django.contrib import admin


# Register your models here.
from .models import Notice, Board, Comment

admin.site.register(Notice)
admin.site.register(Board)
admin.site.register(Comment)
