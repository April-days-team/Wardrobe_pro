# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from common import md5_


class SysManagerRole(models.Model): # 系统管理员角色
    username = models.CharField(unique=True, max_length=20)
    code = models.CharField(max_length=30, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'sys_manager_role'


class SysManagerUser(models.Model):   # 系统管理员
    username = models.CharField(unique=True, max_length=20)
    auth_string = models.CharField(max_length=32)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    role_id = models.IntegerField(blank=True, null=True)
    head = models.CharField(max_length=20, null=True)
    mail = models.CharField(max_length=20,null=True)
    code = models.CharField(max_length=30, blank=True, null=True)

    @property
    def role(self):   # 返回当前角色
        return SysManagerUser.objects.get(pk=self.role_id)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if len(self.auth_string) != 32:
            self.auth_string = md5_.hash_encode(self.auth_string)

        super(SysManagerUser, self).save()


    class Meta:
        managed = False
        db_table = 'sys_manager_user'


class SysRoleMenu(models.Model):  # 系统角色菜单
    username = models.CharField(max_length=20, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    ord = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=50, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'sys_role_menu'


class TransSysRoleMenu(models.Model):  # 系统角色和菜单的关系
    role_id = models.IntegerField(blank=True, null=True)
    menu_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_sys_role_menu'


class CooperationAdmin(models.Model):  # 合作商管理员
    username = models.CharField(max_length=30)
    auth_string = models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    sys_id = models.IntegerField(blank=True, null=True)
    head = models.CharField(max_length=20, null=True)
    mail = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cooperation_admin'


class SuperAdmin(models.Model):   # 超级管理员
    username = models.CharField(max_length=30)
    auth_string = models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    sys_id = models.IntegerField(blank=True, null=True)
    head = models.CharField(max_length=20, null=True)
    mail = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'super_admin'


class MiddleAdmin(models.Model):   # 中级管理员
    username = models.CharField(max_length=30)
    auth_string = models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    super_id = models.IntegerField(blank=True, null=True)
    head = models.CharField(max_length=20, null=True)
    mail = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'middle_admin'


class OrdinaryAdminRole(models.Model):  # 普通管理员
    username = models.CharField(max_length=30)
    auth_string = models.CharField(max_length=50,blank=True,null=True)
    code = models.CharField(max_length=30, blank=True, null=True)
    head = models.CharField(max_length=20, null=True)
    mail = models.CharField(max_length=20, null=True)


    class Meta:
        managed = False
        db_table = 'ordinary_admin_role'


class UserManager(models.Model):  # 用户管理员
    username = models.CharField(max_length=30)
    auth_string = models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    ordinary_id = models.IntegerField(blank=True, null=True)
    head = models.CharField(max_length=20, null=True)
    mail = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_manager'


class OrderManager(models.Model):  # 订单管理员
    username = models.CharField(max_length=30)
    auth_string = models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    ordinary_id = models.IntegerField(blank=True, null=True)
    head = models.CharField(max_length=20, null=True)
    mail = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_manager'


class MemberManager(models.Model):  # 会员管理员
    username = models.CharField(max_length=30)
    auth_string = models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    ordinary_id = models.IntegerField(blank=True, null=True)
    head = models.CharField(max_length=20, null=True)
    mail = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_manager'


class ProductManager(models.Model): # 商品管理员
    username = models.CharField(max_length=30)
    auth_string = models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    ordinary_id = models.IntegerField(blank=True, null=True)
    head = models.CharField(max_length=20, null=True)
    mail = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_manager'


class CartManager(models.Model):  # 购物车管理员
    username = models.CharField(max_length=30)
    auth_string = models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    ordinary_id = models.IntegerField(blank=True, null=True)
    head = models.CharField(max_length=20, null=True)
    mail = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart_manager'


class DaogouManager(models.Model):  # 导购管理员
    username = models.CharField(max_length=30)
    auth_string = models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    ordinary_id = models.IntegerField(blank=True, null=True)
    head = models.CharField(max_length=20, null=True)
    mail = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daogou_manager'


class ServerManager(models.Model):  # 服务管理员
    username = models.CharField(max_length=30)
    auth_string = models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(max_length=20, blank=True, null=True)
    ordinary_id = models.IntegerField(blank=True, null=True)
    head = models.CharField(max_length=20, null=True)
    mail = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_manager'
