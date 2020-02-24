from django.urls import path
from mainapp.views import *


urlpatterns = [
    path('/login/',login_view),  # 登录
    path('/logout/',logout_view),    # 退出

    path('/role/',role_view),  # 角色管理


    path('',index_view)  # 首页
]















