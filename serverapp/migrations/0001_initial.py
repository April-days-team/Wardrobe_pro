# Generated by Django 2.0.1 on 2020-02-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServAppearance',
            fields=[
                ('user_id', models.CharField(max_length=70)),
                ('servic_id', models.AutoField(primary_key=True, serialize=False)),
                ('service_id', models.IntegerField(blank=True, null=True)),
                ('style', models.CharField(max_length=70)),
                ('user_size', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'serv_appearance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='NAME', max_length=50)),
                ('service_time', models.TimeField()),
                ('clerk', models.CharField(max_length=20)),
                ('server', models.CharField(blank=True, db_column='SERVER', max_length=20, null=True)),
            ],
            options={
                'db_table': 'service',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServShoppingCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.IntegerField(blank=True, null=True)),
                ('city', models.CharField(max_length=70)),
                ('clerk_id', models.CharField(max_length=70)),
                ('clerk_name', models.CharField(max_length=70)),
                ('clerk_img', models.CharField(max_length=255)),
                ('clerk_sex', models.CharField(max_length=70)),
                ('slogen', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'serv_shopping_company',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServStoreQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.IntegerField(blank=True, null=True)),
                ('serv_name', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'serv_store_query',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServWardrobe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'serv_wardrobe',
                'managed': False,
            },
        ),
    ]
