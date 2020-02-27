from django.urls import path

from userapp.views import user_view

app_name = 'userapp'

urlpatterns = [
    path('user/',user_view,name='ua')  # 用户
]