import json

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from YCProject import settings
from mainapp.forms import RoleForm
from common import md5_
from guanliapp.models import *
from userapp.models import User


# 登录
def login_view(request):
    print('---',request.method)
    if request.method == 'GET':
        return render(request,'login.html')
    # 分两种用户，一种是系统管理员，一种是用户
    if request.method == 'POST':
        print(request.POST)

        error = None

        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        remember = request.POST.get('remember','')  #checkbox
        # 对密码进行加密处理
        password_ = md5_.hash_encode(password)  # 转成md5加密后的图文
        # 验证用户名和密码口令是否为空
        if not all((username,password)):
            error = f'用户名或口令不能为空!'
        login_user = SysManagerUser.objects.filter(username=username,auth_string=password_).first()
        print(login_user)


        # 登录成功后，验证该用户的身份
        if login_user:
            # 系统管理员
            role_ = login_user.role
            login_info = {
                '_id':login_user.id,
                'name':role_.username,
                'code':role_.code,
                'nike_name':role_.nick_name,
                'head':role_.head,
                'mail':role_.mail
            }
        else:
            login_user = User.objects.filter((Q(username=username) or Q(user_phone=username)) and Q(user_password=password)).first()
            if login_user:
                # 用户
                login_info = {
                    '_id':login_user.id,
                    'name':login_user.username,
                    'nick_name':login_user.nick_name,
                    'mail':login_user.mail,
                    'head':login_user.head
                }
            else:
                error = f'{username} 用户名或口令错误！'

        if not error:
        # 如果用户名和密码都没有错误,将当前登录用户的信息存入session中
            request.session['login_user'] = login_info
            return redirect(reverse('y:i'),locals())

    return render(request,'login.html',locals())

# 退出
def logout_view(request):
    del request.session['login_user']
    return redirect(reverse('y:l'))  # 重定向到登录页面


@csrf_exempt
def block_settings(request):
    block_default_size = request.POST.get('block_default_size', settings.DEFAULT_BLOCK_SIZE)
    friend_block_size = request.POST.get('friend_block_size', settings.FRIEND_BLOCK_SIZE)

    if request.method == 'POST':
        settings.DEFAULT_BLOCK_SIZE = int(block_default_size)
        settings.FRIEND_BLOCK_SIZE = int(friend_block_size)

    type_ = request.GET.get('type_', '')
    if type_ == 'ajax':
        return JsonResponse({
            'block_default_size': block_default_size,
            'friend_block_size': friend_block_size
        })

    return render(request, 'settings.html', locals())




# 首页
def index_view(request):
    return render(request,'dashboard.html')

# 删除
def role_del(request):
    action = request.GET.get('action','')
    if action == 'del':
        SysManagerRole.objects.get(pk=request.GET.get('role_id')).delete()

    roles = SysManagerRole.objects.all()
    return render(request,'role/list.html',locals())

# 编辑角色
class EditRoleView(View):
    def get(self,request):
        role_id = request.GET.get('role_id','')
        if role_id:
            role = SysManagerRole.objects.get(pk=role_id)
        return render(request,'role/edit.html',locals())

    def post(self,request):
        print(request.POST)
        role_id = request.POST.get('id','')
        if role_id:
            form = RoleForm(request.POST,instance=SysManagerRole.objects.get(pk=role_id))
        else:
            form = RoleForm(request.POST)

        if form.is_valid():
            form.save()
            # 重定向到角色管理页面
            return redirect('/role/')

        # form表单提交时错误的信息
        errors = json.loads(form.errors.as_json())
        return render(request,'role/edit.html',locals())

# 角色管理
def role_view(request):
    # 系统管理员
    users = SysManagerRole.objects.all()
    return render(request,'role/list.html',locals())

