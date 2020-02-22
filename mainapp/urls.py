from django.urls import path
from mainapp.views import *

app_name = 'mainapp'

urlpatterns = [
    path('login/',login_view,name='l'),  # 登录
    path('config/',index_view),   #  配置
    path('role/',role_view),  # 角色管理
]
