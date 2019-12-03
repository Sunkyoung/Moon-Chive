#from django.urls import path
# from . import views
# from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls import url, include
from . import views
import re
from django_registration.backends.activation.views import RegistrationView
from .forms import CustomAccountForm

app_name = 'accounts'
# urlpatterns = [
#     path('admin/'admin.site.urls),
#     path('',myproject.views.home, name='home'),
#     path('accounts/', include('accounts.url')
#     ]

urlpatterns = [
    # path('login',/accounts/login, name='login'),
    # url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    # url(r'^accounts/register/$',
    #     RegistrationView.as_view(
    #         form_class=CustomAccountForm
    #     ), name='django_registration_register'),
    # url(r'^accounts/', include('django_registration.backends.activation.urls')),
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^delete/$', views.delete_user, name='delete_user'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/(?P<num>[0-9]+)', views.login, name='login'),
    #path('login/', views.signin, name='login'),
    
]

# urlpatterns = [
    
#      path('signup/', views.signup, name='signup'),
#      path('login/', views.signin, name='login'),
#      path('logout/', views.logout_request, name='logout'),
#      path ('change_pw/', views.change_pw, name='change_pw'),
#      path('delete/', views.delete, name='delete'),
#      path('update/', views.update, name='update'),
# ]