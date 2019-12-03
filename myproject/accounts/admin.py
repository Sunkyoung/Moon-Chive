import datetime
  
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib import admin, messages
from .models import Account
from .forms import SetCertificationDateForm

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("패스워드가 동일하지 않습니다.")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('username', 'email', 'password')

    def clean_password(self):
        return self.initial["password"]

class AccountAdmin(BaseUserAdmin):
    #인증허가
    form = UserChangeForm
    add_form = UserCreationForm

    list_per_page = 10
    list_display = ['id','username', 'firstname',  'lastname',  'email', 'student_id', 'major', 'major_type', 'permission','is_certificated', 'certification_date',]
    list_editable = ['permission', ]
    list_filter = ['permission', ]
    search_fields = ['username',]

    ordering = ('student_id', 'permission', 'is_certificated')

    filter_horizontal = ()

    actions = ['set_certification_date','make_permission','delete_selected',]
    action_form = SetCertificationDateForm

    def set_certification_date(self, request, queryset):
        year = request.POST.get('certification_date_year')
        month = request.POST.get('certification_date_month')
        day = request.POST.get('certification_date_day')

        if year and month and day:
            date_str = '{0}-{1}-{2}'.format(year, month, day)
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

            for account in queryset:
                Account.objects.filter(id=account.id).update(is_certificated=True, certification_date=date)

            messages.success(request, '{0}명의 회원을 인증했습니다.'.format(len(queryset)))
        else:
            messages.error(request, '날짜가 선택되지 않았습니다.')

    set_certification_date.short_description = '선택된 유저를 해당 날짜 기준으로 인증합니다.'

    def make_permission(self, request, queryset):
        queryset.update(permission='TINK')
    make_permission.short_description = '선택된 유저의 권한을 변경합니다.'

    def delete_selected(self, request, queryset):
         queryset.delete()
    #     queryset = Account.objects
    delete_selected.short_description = '선택된 유저를 삭제합니다.'

admin.site.register(Account, AccountAdmin)
admin.site.unregister(Group)