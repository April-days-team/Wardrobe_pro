# Generated by Django 2.0.1 on 2020-02-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlBoss',
            fields=[
                ('dl_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dl_name', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=50)),
                ('operation', models.IntegerField()),
            ],
            options={
                'db_table': 'gl_boss',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GlJurisdiction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qx_id', models.IntegerField()),
                ('qx_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'gl_jurisdiction',
                'managed': False,
            },
        ),
    ]