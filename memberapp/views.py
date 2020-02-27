from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from memberapp import forms
from memberapp.forms import MemberForm
from memberapp.models import MemberInfo




# 消费者信息【会员】
def buy_view(request):
    # 删除操作
    action = request.GET.get('action', '')
    if action == 'del':
        MemberInfo.objects.get(pk=request.GET.get('role.member_id')).delete()

    roles = MemberInfo.objects.all()
    return render(request,'memberapp/buy.html',locals())

# 编辑信息【会员】
class EditMemberView(View):
    def get(self, request):
        role_id = request.GET.get('role.member_id', '')
        if role_id:
            role = MemberInfo.objects.get(pk=role_id)
        return render(request, 'memberapp/member_editor_role.html', locals())

    def post(self, request):
        print(request.POST)
        role_id = request.POST.get('role.member_id', '')
        if role_id:
            form = MemberInfo(request.POST, instance=MemberInfo.objects.get(pk=role_id))
        else:
            form = MemberForm(request.POST)

        if form.is_valid():
            # 重定向到角色管理页面
            return redirect(reverse('m:buy'), locals())

# 新增买家信息[会员]
# def add_member_view(request):
#



# 删除买家信息
def del_buy_view(request):
    roles = MemberInfo.objects.all()
    action = request.GET.get('action','')
    if action == 'del':
        MemberInfo.objects.get(pk=request.GET.get('role_member_id')).delete()
        roles = MemberInfo.objects.all()
        return render(request,'memberapp/buy.html',locals())

















