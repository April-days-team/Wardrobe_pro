from django.urls import path

from memberapp import views
from memberapp.views import *

app_name = 'memberapp'




urlpatterns  =[
    path('buy/',buy_view,name='buy'),  # 消费者信息【会员】
    path('edit_member/',views.EditMemberView.as_view()), # 编辑会员角色
    # path('add_buy',add_member_view,name='add'),  # 新增
    path('del_buy',del_buy_view,name='del'),  #删除
]
