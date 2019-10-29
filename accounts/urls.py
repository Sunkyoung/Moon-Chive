# from django.urls import path
# from . import views
# from django.contrib.auth import views as auth_views

from django.conf.urls import url, include
from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^delete/$', views.delete_user, name='delete_user'),
]

# urlpatterns = [
    
#     path('signup/', views.signup, name='signup'),
#     path('login/', views.signin, name='login'),
#     path('logout/', views.logout_request, name='logout'),
#     path ('change_pw/', views.change_pw, name='change_pw'),
#     path('delete/', views.delete, name='delete'),
#     path('update/', views.update, name='update')

    
# ]