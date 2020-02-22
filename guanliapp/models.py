# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class GlBoss(models.Model):
    dl_id = models.IntegerField(primary_key=True)
    dl_name = models.IntegerField()
    phone = models.IntegerField()
    email = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50)
    operation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gl_boss'


class GlJurisdiction(models.Model):
    dl = models.ForeignKey(GlBoss, models.DO_NOTHING, blank=True, null=True)
    qx_id = models.IntegerField()
    qx_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'gl_jurisdiction'
