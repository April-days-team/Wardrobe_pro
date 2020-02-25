from django.urls import path
from mainapp.views import *
from . import views

app_name = 'mainapp'


urlpatterns = [
    path('login/',login_view,name='l'),  # 登录
    path('logout/',logout_view),    # 退出
    path('settings/',block_settings,name='s'),
    path('role/',role_view,name='r'),  # 角色管理

    path('edit_role/',views.EditRoleView.as_view()),

    path('index/',index_view,name='i')  # 首页
]















