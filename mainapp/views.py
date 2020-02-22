from django.shortcuts import render, redirect
from django.urls import reverse

from common import md5_
from userapp.models import User


# 登录
def login_view(request):

    error = None

    # 分两种用户，一种是用户，一种是管理员[系统]
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':

        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        remember = request.POST.get('remember','')  #checkbox

        # 对密码进行加密处理
        password = md5_.hash_encode(password)  # 转成md5加密后的图文

        # 验证用户名和密码口令是否为空
        if not all((username,password)):
            error = f'用户名或密码不能为空'

        login_user = User.objects.filter(username=username,auth_string=password).first()

        # 登录成功后，验证该用户的身份
        if login_user:
            # 系统管理员
            role_ = login_user.role
            login_info = {
                '_id':login_user.id,
                'name':role_.username,
                'code':role_.code
            }
        else:
            login_user = User.objects.first(username=username,auth_string=password).first()
            if login_user:
                # 管理员(超级管理员，中级管理员，普通管理员，合作商管理员)
                role_ = login_user.role
                login_info = {
                    '_id':login_user.id,
                    'name':login_user.username,
                    'nick_name':login_user.nick_name
                }
            else:
                error = f'{username} 用户名或密码错误！'

        if not error:
        # 如果用户名和密码都没有错误,将当前登录用户的信息存入session中
            request.session['login_user'] = login_info
            return redirect(reverse('y:l'))

# 首页
def index_view(request):
    return render(request,'dashboard.html')

# 角色管理
def role_view(request):
    users = User.objects.all()
    return render(request,'role/list.html',locals())

