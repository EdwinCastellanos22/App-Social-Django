
from re import template
from unicodedata import name
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='inicio'),
    path('', welcome, name='inicio'),
    path('register/', register, name='registro'),
    path('login/', LoginView.as_view(template_name= 'login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= 'login.html'), name='logout'),
    path('profile/', perfil, name='perfil'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('reset', reset_Password, name='reset password')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header= 'Page Social'
