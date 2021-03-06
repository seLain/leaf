# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-03 06:39
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('storehouse', '0001_initial'),
        ('advertisement_mgmt', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('helpdesk', '0017_erppermisson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clerk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='advertisement_mgmt.Store')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('number', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('mission_type', models.TextField(choices=[('0', 'Unknown'), ('1', 'SpecificInventoryCheck')], default='Unknown')),
                ('status', models.TextField(choices=[('0', 'ToDo'), ('1', 'InProgress'), ('2', 'Done')], default='ToDo')),
                ('redo_count', models.IntegerField(default=0)),
                ('on_stock_count', models.FloatField(default=0)),
                ('storage_count', models.FloatField(default=0)),
                ('date', models.DateTimeField(default=datetime.datetime(1900, 1, 1, 0, 0))),
                ('goods', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='storehouse.Goods')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventorycheck.Clerk')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisement_mgmt.Store')),
                ('ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='helpdesk.Ticket')),
            ],
            options={
                'permissions': (('view_clerk_jobs', 'permission to check jobs assigned to clerks'),),
            },
        ),
    ]
