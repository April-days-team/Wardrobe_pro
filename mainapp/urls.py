from django.urls import path
from mainapp.views import *
from . import views

app_name = 'mainapp'


urlpatterns = [
    path('login/',login_view,name='l'),  # 登录
    path('logout/',logout_view),    # 退出
    path('settings/',block_settings,name='s'),
    path('role/',role_view,name='r'),  # 角色管理
    path('source/',source_view,name='source'), # 资料展示

    path('manager/',manager_view,name='m'),  # 管理员信息
    path('edit_role/',views.EditRoleView.as_view()),
    path('regist/',regist_view,name='reg'),
    path('cooperation/',cooperation_view,name='coop'),  # 合作商信息
    path('',index_view,name='i')  # 首页

]















