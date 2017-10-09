# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('erpadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('code', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('monthly_pay', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('picture', models.ImageField(blank=True, default='media/adv_images/None/no-img.jpg', null=True, upload_to='media/adv_images/')),
            ],
            options={
                'permissions': (('advertisement_mgmt', '可以新增廣告及查看當前廣告'),),
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('ss8_id', models.TextField(default='', null=True)),
                ('ss12_id', models.TextField(default='', null=True)),
                ('name', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='advertisement_mgmt.Store'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='erpadmin.Supplier'),
        ),
    ]
