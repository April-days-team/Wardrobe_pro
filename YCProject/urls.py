from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings



urlpatterns = [
    path('',include('mainapp.urls',namespace='y')),   # 主页
    path('',include('memberapp.urls',namespace='m')),  # 会员
    path('',include('daogouapp.urls',namespace='d')),  # 导购
    path('',include('userapp.urls',namespace='u'))  # 用户

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  # 静态资源的路径









