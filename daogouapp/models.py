# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DBoss(models.Model):
    d_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    dz_name = models.CharField(max_length=50)
    is_no = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_boss'


class DFans(models.Model):
    d = models.ForeignKey(DBoss, models.DO_NOTHING, blank=True, null=True)
    fans_id = models.IntegerField()
    fans_name = models.CharField(max_length=50)
    fans_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_fans'


class DMember(models.Model):
    d = models.ForeignKey(DBoss, models.DO_NOTHING, blank=True, null=True)
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    user_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_member'


class DOrderForm(models.Model):
    d_id = models.IntegerField()
    order_id = models.IntegerField(unique=True)
    d_data = models.TimeField()
    d_class = models.CharField(max_length=50)
    details = models.CharField(max_length=256)
    price = models.FloatField()
    tracking_number = models.CharField(max_length=100)
    z_state = models.IntegerField()
    f_state = models.IntegerField()
    f_jiaoyi = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_order_form'


class DPerformance(models.Model):
    d = models.ForeignKey(DBoss, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(DOrderForm, models.DO_NOTHING, blank=True, null=True)
    d_number = models.IntegerField()
    d_xiaoshou = models.FloatField()
    d_tuihuo = models.FloatField()
    d_tuihuolv = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'd_performance'
