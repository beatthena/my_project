# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-12 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_auto_20190711_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_villalist',
            name='bathroom_photo',
            field=models.CharField(default='/static/assets/img/icon/shawer.png', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user_villalist',
            name='bedroom_photo',
            field=models.CharField(default='/static/assets/img/icon/bed.png', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user_villalist',
            name='garage_photo',
            field=models.CharField(default='/static/assets/img/icon/cars.png', max_length=500, null=True),
        ),
    ]