import datetime
from django.contrib import admin, messages
from .models import User
from .forms import SetCertificationDateForm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'student_id', 'username', 'firstname', 'lastname',  'email',  'major', 'major_type', 'permission','is_certificated', 'certification_date', 'joined_at', 'last_login_at', 'is_superuser', 'is_active')
    list_editable = ('permission',)
    search_fields = ('username',)
    list_filter=('permission',)
    ordering = ('student_id', 'permission', 'is_certificated')
    exclude = ('password',)                           # 사용자 상세 정보에서 비밀번호 필드를 노출하지 않음

    def joined_at(self, obj):
        return obj.date_joined.strftime("%Y-%m-%d")

    def last_login_at(self, obj):
        if not obj.last_login:
            return ''
        return obj.last_login.strftime("%Y-%m-%d %H:%M")

    joined_at.admin_order_field = '-date_joined'      # 가장 최근에 가입한 사람부터 리스팅
    joined_at.short_description = '가입일'
    last_login_at.admin_order_field = 'last_login_at'
    last_login_at.short_description = '최근로그인'

    actions = ('set_certification_date','make_permission','delete_selected',)
    action_form = SetCertificationDateForm

    def set_certification_date(self, request, queryset):
        year = request.POST.get('certification_date_year')
        month = request.POST.get('certification_date_month')
        day = request.POST.get('certification_date_day')

        if year and month and day:
            date_str = '{0}-{1}-{2}'.format(year, month, day)
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

            for user in queryset:
                User.objects.filter(id=user.id).update(is_certificated=True, certification_date=date)

            messages.success(request, '{0}명의 회원을 인증했습니다.'.format(len(queryset)))
        else:
            messages.error(request, '날짜가 선택되지 않았습니다.')

    set_certification_date.short_description = '선택된 유저를 해당 날짜 기준으로 인증합니다.'

    def make_permission(self, request, queryset):
        queryset.update(permission='TINK')
    make_permission.short_description = '선택된 유저의 권한을 변경합니다.'

    def delete_selected(self, request, queryset):
         queryset.delete()
    delete_selected.short_description = '선택된 유저를 삭제합니다.'
