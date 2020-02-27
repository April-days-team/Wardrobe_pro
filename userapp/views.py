from django.shortcuts import render
from userapp.models import User


# 系统用户界面
def user_view(request):
    roles = User.objects.all()
    return render(request,'userapp/user.html',locals())