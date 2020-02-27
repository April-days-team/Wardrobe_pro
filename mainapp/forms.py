from django import forms
from guanliapp.models import SysManagerUser


# 角色验证表单
class RoleForm(forms.ModelForm):

    class Meta:
        model = SysManagerUser
        fields = ['username','code','auth_string','role_id']
        error_messages = {
            'username':{
            'required':'角色名不能为空'
        },
            'code':{
                'required':'角色代码不能为空'
            },
            'auth_string': {
                'required': '口令不能为空'
            },
            'role_id': {
                'required': '系统用户角色不能为空'
            }
        }


