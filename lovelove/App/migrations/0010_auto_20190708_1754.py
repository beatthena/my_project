# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-07-08 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_auto_20190708_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_tuijian',
            name='tuijian_photo',
            field=models.CharField(default='/static/assets/img/demo/small-property-2.jpg', max_length=500, null=True),
        ),
    ]
