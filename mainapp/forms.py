from django import forms
from guanliapp.models import SysManagerRole


# 角色验证表单
class RoleForm(forms.ModelForm):

    class Meta:
        model = SysManagerRole
        fields = ['username','code']
        error_messages = {
            'username':{
            'required':'角色名不能为空'
        },
            'code':{
                'required':'角色代码不能为空'
            }
        }


