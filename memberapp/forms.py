from django.forms import forms
from memberapp.models import MemberInfo



# 会员【消费者】表单认证
class MemberForm(forms.Form):

    class Meta:
        model = MemberInfo
        fields = ['member_name','member_level','member_score','member_balance']
        error_message = {
            'member_name':{
            'required':'会员名称不能为空'
            },
            'member_level':{
            'required':'会员等级不能为空'
            },
            'member_score':{
                'required':'会员积分不能为空'
            },
            'member_balance':{
                'required':'会员余额不能为空'
            }
        }
