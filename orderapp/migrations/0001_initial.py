# Generated by Django 2.0.1 on 2020-02-22 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TAdress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=32, null=True)),
                ('user_phone', models.CharField(blank=True, max_length=32, null=True)),
                ('user_adress', models.CharField(blank=True, max_length=256, null=True)),
                ('adress_label', models.IntegerField(blank=True, null=True)),
                ('is_default', models.IntegerField(blank=True, null=True)),
                ('delete_adress', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_adress',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TOrder',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_pay', models.IntegerField(blank=True, null=True)),
                ('pay_time', models.DateTimeField(blank=True, null=True)),
                ('is_ship', models.IntegerField(blank=True, null=True)),
                ('ship_time', models.DateTimeField(blank=True, null=True)),
                ('is_receipt', models.IntegerField(blank=True, null=True)),
                ('receipt_time', models.DateTimeField(blank=True, null=True)),
                ('ship_number', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('updata_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TOrderdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_names', models.CharField(max_length=256)),
                ('goods_price', models.FloatField()),
                ('adress', models.CharField(max_length=256)),
                ('price', models.FloatField()),
                ('coupon', models.FloatField(blank=True, null=True)),
                ('total_price', models.FloatField()),
                ('freght_price', models.FloatField()),
                ('store_id', models.IntegerField(blank=True, null=True)),
                ('is_done', models.IntegerField()),
            ],
            options={
                'db_table': 't_orderdetails',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TShip',
            fields=[
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='orderapp.TOrder')),
                ('t_ship', models.CharField(blank=True, max_length=50, null=True)),
                ('ship_status', models.IntegerField(blank=True, null=True)),
                ('collect_time', models.DateTimeField(blank=True, null=True)),
                ('sign_for_status', models.IntegerField(blank=True, null=True)),
                ('sign_for_time', models.DateTimeField(blank=True, null=True)),
                ('well_recieve_status', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_ship',
                'managed': False,
            },
        ),
    ]
