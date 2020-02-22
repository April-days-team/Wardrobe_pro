# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ProClassify(models.Model):
    pro = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
    category = models.CharField(max_length=50)
    famili = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pro_classify'


class ProTags(models.Model):
    pro = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
    promotion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_tags'


class Products(models.Model):
    pro_id = models.CharField(primary_key=True, max_length=70)
    name = models.CharField(max_length=70)
    color = models.CharField(max_length=70)
    size = models.CharField(max_length=70)
    year = models.CharField(max_length=70)
    price = models.FloatField()
    pro_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'products'




