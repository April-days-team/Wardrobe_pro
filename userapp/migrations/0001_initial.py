# Generated by Django 2.0.1 on 2020-02-23 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CouponsTypes',
            fields=[
                ('coupon_id', models.IntegerField(primary_key=True, serialize=False)),
                ('coupon_1', models.CharField(blank=True, max_length=50, null=True)),
                ('coupon_2', models.CharField(blank=True, max_length=50, null=True)),
                ('coupon_3', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'coupons_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('user_password', models.CharField(max_length=30)),
                ('user_email', models.CharField(max_length=50, verbose_name='邮箱')),
                ('user_balabce', models.CharField(max_length=100)),
                ('is_activate', models.SmallIntegerField(null=True)),
                ('user_images', models.CharField(blank=True, max_length=256, null=True)),
                ('user_level', models.IntegerField()),
                ('vip_datetime', models.CharField(blank=True, max_length=20, null=True)),
                ('lasttime', models.CharField(blank=True, max_length=20, null=True)),
                ('has_realname', models.IntegerField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserCollectStore',
            fields=[
                ('store_id', models.IntegerField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(blank=True, max_length=50, null=True)),
                ('store_news', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'user_collect_store',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserCoupon',
            fields=[
                ('coupon_types', models.IntegerField(primary_key=True, serialize=False)),
                ('coupan_nums', models.IntegerField(blank=True, null=True)),
                ('coupan_name', models.CharField(blank=True, max_length=70, null=True)),
            ],
            options={
                'db_table': 'user_coupon',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_message', models.CharField(blank=True, max_length=100, null=True)),
                ('cart_id', models.IntegerField()),
                ('user_message_time', models.DateTimeField()),
                ('cart_name', models.CharField(blank=True, max_length=50, null=True)),
                ('good_level', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'user_message',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_time', models.DateTimeField()),
                ('cart_name', models.CharField(blank=True, max_length=50, null=True)),
                ('cart_id', models.IntegerField()),
            ],
            options={
                'db_table': 'user_track',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserTransaction',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('details', models.CharField(blank=True, max_length=100, null=True)),
                ('number', models.IntegerField()),
                ('payment_types', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user_transaction',
                'managed': False,
            },
        ),
    ]
