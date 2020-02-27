from django.urls import path

from daogouapp.views import *

app_name = 'daogouapp'

urlpatterns = [
    path('sale/',sale_view,name='sale'), # 商家
    path('add_sale/',add_sale_view,name='add') # 增加商家
]