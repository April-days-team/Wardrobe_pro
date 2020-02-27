# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CouponsTypes(models.Model):
    coupon_id = models.IntegerField(primary_key=True)
    coupon_1 = models.CharField(max_length=50, blank=True, null=True)
    coupon_2 = models.CharField(max_length=50, blank=True, null=True)
    coupon_3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupons_types'

class User(models.Model):

    user_id = models.AutoField(primary_key=True,verbose_name='用户ID')
    username = models.CharField(max_length=50,verbose_name='用户名')
    auth_string = models.CharField(max_length=30)
    user_email = models.CharField(max_length=50,verbose_name='邮箱')
    user_balabce = models.CharField(max_length=100)
    is_activate = models.SmallIntegerField(null=True)
    user_images = models.CharField(max_length=256, blank=True, null=True)
    user_level = models.IntegerField()
    vip_datetime = models.CharField(max_length=20, blank=True, null=True)
    lasttime = models.CharField(max_length=20, blank=True, null=True)
    has_realname = models.IntegerField()
    user_phone = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'user'

class UserCollectStore(models.Model):
    store_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    store_name = models.CharField(max_length=50, blank=True, null=True)
    store_news = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_collect_store'


class UserCoupon(models.Model):
    coupon_types = models.IntegerField(primary_key=True)
    coupon = models.ForeignKey(CouponsTypes, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    coupan_nums = models.IntegerField(blank=True, null=True)
    coupan_name = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_coupon'




class UserMessage(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    user_message = models.CharField(max_length=100, blank=True, null=True)
    cart_id = models.IntegerField()
    user_message_time = models.DateTimeField()
    cart_name = models.CharField(max_length=50, blank=True, null=True)
    good_level = models.CharField(max_length=50, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'user_message'


class UserTrack(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    skill_time = models.DateTimeField()
    cart_name = models.CharField(max_length=50, blank=True, null=True)
    cart_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_track'


class UserTransaction(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(blank=True, null=True)
    details = models.CharField(max_length=100, blank=True, null=True)
    number = models.IntegerField()
    payment_types = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user_transaction'
