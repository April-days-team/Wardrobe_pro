# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MemberInfo(models.Model):
    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=50, blank=True, null=True)
    member_level = models.CharField(max_length=50, blank=True, null=True)
    member_score = models.CharField(max_length=50, blank=True, null=True)
    member_balance = models.CharField(max_length=50, blank=True, null=True)
    member_authority = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_info'


class MemberLevel(models.Model):
    member = models.ForeignKey(MemberInfo, models.DO_NOTHING, blank=True, null=True)
    member_name1 = models.CharField(max_length=50, blank=True, null=True)
    member_name2 = models.CharField(max_length=50, blank=True, null=True)
    member_name3 = models.CharField(max_length=50, blank=True, null=True)
    member_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_level'


class MemberScore(models.Model):
    member = models.ForeignKey(MemberInfo, models.DO_NOTHING, blank=True, null=True)
    member_score = models.CharField(max_length=70, blank=True, null=True)
    member_name = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_score'
