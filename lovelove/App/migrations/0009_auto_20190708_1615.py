# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-08 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_auto_20190708_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_tuijian',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
