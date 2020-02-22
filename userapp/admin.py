from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    def realname(self):
        return self.realname_state

    list_display = ['user_id','username','user_email',realname]  # 显示的字段
    fields = ['username','user_email','has_realname']
    list_per_page = 2   #分页，每页显示多少条数据

    realname.short_description = '实名状态'

admin.site.register(User,UserAdmin)
