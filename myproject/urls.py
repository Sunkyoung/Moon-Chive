"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  path
from accounts.views import RegistrationView
from accounts.forms import RegistrationForm

import myapp.views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

urlpatterns = [
    # path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name='home'),
    path('about/', myapp.views.about, name='about'),
    path('board/', myapp.views.board, name='board'),
    path('board/<int:board_id>/', myapp.views.board_detail, name='board_detail'),
    path('board/create/', myapp.views.board_create, name='create'),
    path('board/<int:board_id>/delete/', myapp.views.board_delete, name='delete'),
    path('board/<int:board_id>/update', myapp.views.board_update, name='update'),
    path('board/<int:board_id>/comment/<int:comment_id>/delete', myapp.views.comment_delete, name='comment_delete'),
    path('notice', myapp.views.notice, name='notice'),
    path('notice/<int:notice_id>/', myapp.views.notice_detail, name='detail'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/register/$',
        RegistrationView.as_view(
            form_class=RegistrationForm
        ), name='django_registration_register'),
    url(r'^accounts/', include('django_registration.one_step.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
