# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TAdress(models.Model):
    order = models.ForeignKey('TShip', models.DO_NOTHING, blank=True, null=True)
    t_o_order = models.ForeignKey('TOrder', models.DO_NOTHING, blank=True, null=True)
    user_name = models.CharField(max_length=32, blank=True, null=True)
    user_phone = models.CharField(max_length=32, blank=True, null=True)
    user_adress = models.CharField(max_length=256, blank=True, null=True)
    adress_label = models.IntegerField(blank=True, null=True)
    is_default = models.IntegerField(blank=True, null=True)
    delete_adress = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_adress'


class TOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    is_pay = models.IntegerField(blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    is_ship = models.IntegerField(blank=True, null=True)
    ship_time = models.DateTimeField(blank=True, null=True)
    is_receipt = models.IntegerField(blank=True, null=True)
    receipt_time = models.DateTimeField(blank=True, null=True)
    ship_number = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    updata_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_order'


class TOrderdetails(models.Model):
    order = models.ForeignKey(TOrder, models.DO_NOTHING, blank=True, null=True)
    goods_names = models.CharField(max_length=256)
    goods_price = models.FloatField()
    adress = models.CharField(max_length=256)
    price = models.FloatField()
    coupon = models.FloatField(blank=True, null=True)
    total_price = models.FloatField()
    freght_price = models.FloatField()
    store_id = models.IntegerField(blank=True, null=True)
    is_done = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_orderdetails'


class TShip(models.Model):
    order = models.ForeignKey(TOrder, models.DO_NOTHING, primary_key=True)
    t_ship = models.CharField(max_length=50, blank=True, null=True)
    ship_status = models.IntegerField(blank=True, null=True)
    collect_time = models.DateTimeField(blank=True, null=True)
    sign_for_status = models.IntegerField(blank=True, null=True)
    sign_for_time = models.DateTimeField(blank=True, null=True)
    well_recieve_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_ship'

