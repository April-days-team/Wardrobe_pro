# Generated by Django 2.0.1 on 2020-02-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProClassify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('famili', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'pro_classify',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('pro_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('color', models.CharField(max_length=70)),
                ('size', models.CharField(max_length=70)),
                ('year', models.CharField(max_length=70)),
                ('price', models.FloatField()),
                ('pro_price', models.FloatField()),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'pro_tags',
                'managed': False,
            },
        ),
    ]
