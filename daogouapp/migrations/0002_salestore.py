# Generated by Django 2.0.1 on 2020-02-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daogouapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleStore',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=50)),
                ('store_num', models.IntegerField()),
                ('create_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'sale_store',
                'managed': False,
            },
        ),
    ]
