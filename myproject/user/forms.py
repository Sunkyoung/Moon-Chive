import datetime
from django import forms
from django.forms import SelectDateWidget
from django.contrib.admin.helpers import ActionForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

#비밀번호 변경
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('student_id', 'major_type', 'major', 'firstname', 'lastname', 'username', 'email')

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('student_id', 'major_type', 'major', 'firstname', 'lastname', 'username', 'email')

class SetCertificationDateForm(ActionForm):
    certification_date = forms.DateField(
        widget=SelectDateWidget,
        initial=(datetime.date.today())
    )